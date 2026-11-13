"use client";

import { useEffect, useState, useCallback } from "react";
import Link from "next/link";
import { BODY_TYPE_LABEL, FUEL_TYPE_LABEL } from "@/lib/api";

const API_BASE =
  typeof window === "undefined"
    ? ""
    : (process.env.NEXT_PUBLIC_API_URL ?? "");

const TOKEN_KEY = "kronikoto_admin_token";

interface AdminOverview {
  counts: {
    brands: number;
    models: number;
    variants: number;
    faults: number;
    comments: number;
  };
  body_types: Record<string, number>;
  fuel_types: Record<string, number>;
  recent_comments: Array<{
    id: string;
    variant_id: string;
    author_name: string;
    ownership_status: string | null;
    mileage_km: number | null;
    rating: number;
    recommend: boolean;
    body: string;
    created_at: string | null;
  }>;
}

interface AdminVariantItem {
  id: string;
  engine_label: string;
  fuel_type: string;
  transmission_label: string;
  year_start: number;
  year_end: number | null;
  used_price_tl: number | null;
  is_active: boolean;
}

interface AdminModelItem {
  id: string;
  brand: string;
  name: string;
  body_type: string;
  year_start: number;
  year_end: number | null;
  comfort_score: number;
  is_active: boolean;
  variants: AdminVariantItem[];
}

export default function AdminPage() {
  const [token, setToken] = useState<string | null>(null);
  const [password, setPassword] = useState("");
  const [showPass, setShowPass] = useState(false);
  const [loginError, setLoginError] = useState("");
  const [loading, setLoading] = useState(false);

  const [tab, setTab] = useState<"overview" | "models" | "faults">("overview");
  const [toast, setToast] = useState<{ type: "ok" | "err"; msg: string } | null>(null);

  const [overview, setOverview] = useState<AdminOverview | null>(null);
  const [models, setModels] = useState<AdminModelItem[]>([]);
  const [searchQ, setSearchQ] = useState("");
  const [expandedModel, setExpandedModel] = useState<string | null>(null);

  // Inline edits
  const [comfortEdits, setComfortEdits] = useState<Record<string, string>>({});
  const [priceEdits, setPriceEdits] = useState<Record<string, string>>({});

  // Fault create form
  const [faultModelId, setFaultModelId] = useState("");
  const [faultTitle, setFaultTitle] = useState("");
  const [faultDesc, setFaultDesc] = useState("");
  const [faultCat, setFaultCat] = useState("mekanik");
  const [faultAvgCost, setFaultAvgCost] = useState("15000");
  const [faultMaxCost, setFaultMaxCost] = useState("30000");
  const [faultSeverity, setFaultSeverity] = useState("");
  const [faultKmStart, setFaultKmStart] = useState("60000");
  const [faultKmEnd, setFaultKmEnd] = useState("140000");
  const [faultCheck, setFaultCheck] = useState("");

  const notify = (type: "ok" | "err", msg: string) => {
    setToast({ type, msg });
    setTimeout(() => setToast(null), 4000);
  };

  const adminFetch = useCallback(
    async <T,>(path: string, init?: RequestInit): Promise<T> => {
      const res = await fetch(`${API_BASE}/api/v1${path}`, {
        ...init,
        headers: {
          "Content-Type": "application/json",
          ...(token ? { Authorization: `Bearer ${token}` } : {}),
          ...(init?.headers ?? {}),
        },
      });
      if (res.status === 401) {
        localStorage.removeItem(TOKEN_KEY);
        setToken(null);
        throw new Error("Oturum süresi doldu veya yetkisiz erişim.");
      }
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || `İstek hatası (${res.status})`);
      }
      return res.json();
    },
    [token]
  );

  const loadData = useCallback(async () => {
    if (!token) return;
    setLoading(true);
    try {
      const [ov, ms] = await Promise.all([
        adminFetch<AdminOverview>("/admin/overview"),
        adminFetch<AdminModelItem[]>("/admin/models"),
      ]);
      setOverview(ov);
      setModels(ms);
      if (!faultModelId && ms.length > 0) setFaultModelId(ms[0].id);
    } catch (e: unknown) {
      notify("err", e instanceof Error ? e.message : "Veri yüklenemedi");
    } finally {
      setLoading(false);
    }
  }, [token, adminFetch, faultModelId]);

  useEffect(() => {
    const saved = localStorage.getItem(TOKEN_KEY);
    if (saved) setToken(saved);
  }, []);

  useEffect(() => {
    if (token) loadData();
  }, [token, loadData]);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoginError("");
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/api/v1/admin/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password }),
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({}));
        throw new Error(err.detail || "Hatalı şifre");
      }
      const data = await res.json();
      localStorage.setItem(TOKEN_KEY, data.token);
      setToken(data.token);
      setPassword("");
    } catch (e: unknown) {
      setLoginError(e instanceof Error ? e.message : "Giriş başarısız");
    } finally {
      setLoading(false);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem(TOKEN_KEY);
    setToken(null);
    setOverview(null);
    setModels([]);
  };

  const saveModelComfort = async (m: AdminModelItem) => {
    const raw = comfortEdits[m.id] ?? String(m.comfort_score);
    const val = parseFloat(raw);
    if (isNaN(val) || val < 1 || val > 10) {
      notify("err", "Konfor puanı 1.0 ile 10.0 arasında olmalıdır.");
      return;
    }
    try {
      await adminFetch(`/admin/models/${m.id}`, {
        method: "PATCH",
        body: JSON.stringify({ comfort_score: val }),
      });
      setModels((prev) =>
        prev.map((item) => (item.id === m.id ? { ...item, comfort_score: val } : item))
      );
      notify("ok", `${m.brand} ${m.name} konfor puanı ${val} olarak güncellendi.`);
    } catch (e: unknown) {
      notify("err", e instanceof Error ? e.message : "Güncelleme başarısız");
    }
  };

  const saveVariantPrice = async (v: AdminVariantItem) => {
    const raw = priceEdits[v.id] ?? String(v.used_price_tl ?? "");
    const val = parseFloat(raw);
    if (isNaN(val) || val < 0) {
      notify("err", "Geçerli bir TL fiyatı girin.");
      return;
    }
    try {
      await adminFetch(`/admin/variants/${v.id}`, {
        method: "PATCH",
        body: JSON.stringify({ used_price_tl: val }),
      });
      setModels((prev) =>
        prev.map((m) => ({
          ...m,
          variants: m.variants.map((vr) =>
            vr.id === v.id ? { ...vr, used_price_tl: val } : vr
          ),
        }))
      );
      notify("ok", `${v.engine_label} fiyatı ${val.toLocaleString("tr-TR")} TL olarak kaydedildi.`);
    } catch (e: unknown) {
      notify("err", e instanceof Error ? e.message : "Fiyat güncellenemedi");
    }
  };

  const deleteComment = async (id: string) => {
    try {
      await adminFetch(`/admin/comments/${id}`, { method: "DELETE" });
      setOverview((prev) =>
        prev
          ? {
              ...prev,
              counts: { ...prev.counts, comments: Math.max(0, prev.counts.comments - 1) },
              recent_comments: prev.recent_comments.filter((c) => c.id !== id),
            }
          : prev
      );
      notify("ok", "Yorum silindi.");
    } catch (e: unknown) {
      notify("err", e instanceof Error ? e.message : "Silinemedi");
    }
  };

  const createFault = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await adminFetch("/admin/faults", {
        method: "POST",
        body: JSON.stringify({
          model_id: faultModelId,
          title: faultTitle,
          description: faultDesc,
          category: faultCat,
          avg_repair_cost_tl: parseFloat(faultAvgCost) || 10000,
          max_repair_cost_tl: parseFloat(faultMaxCost) || 20000,
          severity_override: faultSeverity || null,
          occurrence_km_start: faultKmStart ? parseInt(faultKmStart, 10) : null,
          occurrence_km_end: faultKmEnd ? parseInt(faultKmEnd, 10) : null,
          checklist: faultCheck.trim() ? [faultCheck.trim()] : [],
        }),
      });
      notify("ok", "Yeni kronik arıza kaydı eklendi.");
      setFaultTitle("");
      setFaultDesc("");
      setFaultCheck("");
      loadData();
    } catch (e: unknown) {
      notify("err", e instanceof Error ? e.message : "Arıza eklenemedi");
    }
  };

  const filteredModels = models.filter((m) => {
    const q = searchQ.trim().toLowerCase();
    if (!q) return true;
    return `${m.brand} ${m.name}`.toLowerCase().includes(q);
  });

  if (!token) {
    return (
      <div className="min-h-screen bg-[#16181c] text-zinc-100 flex items-center justify-center p-4">
        <div className="w-full max-w-md rounded-2xl bg-[#1f2228] border border-zinc-800 p-6 sm:p-8 shadow-2xl">
          <div className="flex items-center justify-between mb-6">
            <div>
              <span className="inline-block text-xs font-semibold uppercase tracking-wider text-orange-400 mb-1">
                KronikOto Yönetim
              </span>
              <h1 className="text-2xl font-bold text-white">Yönetici Girişi</h1>
            </div>
            <Link
              href="/"
              className="text-xs text-zinc-400 hover:text-orange-400 transition"
            >
              ← Siteye Dön
            </Link>
          </div>

          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label className="block text-xs font-medium text-zinc-400 mb-1.5">
                Yönetici Şifresi
              </label>
              <div className="relative">
                <input
                  type={showPass ? "text" : "password"}
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Şifrenizi girin..."
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-4 py-3 pr-16 text-sm text-white focus:outline-none focus:border-orange-500"
                  required
                />
                <button
                  type="button"
                  onClick={() => setShowPass((v) => !v)}
                  className="absolute right-3 top-1/2 -translate-y-1/2 text-xs text-zinc-400 hover:text-white"
                >
                  {showPass ? "Gizle" : "Göster"}
                </button>
              </div>
            </div>

            {loginError && (
              <p className="text-xs text-red-400 bg-red-500/10 border border-red-500/30 rounded-lg px-3 py-2">
                {loginError}
              </p>
            )}

            <button
              type="submit"
              disabled={loading}
              className="w-full rounded-xl bg-orange-500 hover:bg-orange-400 disabled:opacity-60 text-zinc-950 font-semibold py-3 text-sm transition cursor-pointer"
            >
              {loading ? "Kontrol ediliyor..." : "Panele Giriş Yap"}
            </button>
          </form>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-[#16181c] text-zinc-100">
      {/* Header */}
      <header className="sticky top-0 z-30 bg-[#1f2228]/95 backdrop-blur border-b border-zinc-800">
        <div className="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <Link href="/" className="text-lg font-extrabold tracking-tight text-white">
              Kronik<span className="text-orange-400">Oto</span>
            </Link>
            <span className="text-xs px-2.5 py-0.5 rounded-full bg-orange-500/15 text-orange-400 border border-orange-500/30 font-medium">
              Admin Paneli
            </span>
          </div>

          <div className="flex items-center gap-2">
            <Link
              href="/"
              className="text-xs px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-zinc-700 text-zinc-200 transition"
            >
              Siteyi Aç
            </Link>
            <button
              onClick={handleLogout}
              className="text-xs px-3 py-1.5 rounded-lg bg-red-500/15 hover:bg-red-500/25 text-red-300 border border-red-500/30 transition cursor-pointer"
            >
              Çıkış Yap
            </button>
          </div>
        </div>
      </header>

      {/* Toast */}
      {toast && (
        <div className="fixed bottom-4 right-4 z-50 max-w-sm rounded-xl px-4 py-3 text-sm font-medium shadow-xl border backdrop-blur bg-[#1f2228]/95 border-orange-500/40 text-white">
          <span className={toast.type === "ok" ? "text-emerald-400 mr-2" : "text-red-400 mr-2"}>
            {toast.type === "ok" ? "✓" : "✕"}
          </span>
          {toast.msg}
        </div>
      )}

      <main className="max-w-6xl mx-auto px-4 py-6 space-y-6">
        {/* Tabs */}
        <div className="flex flex-wrap gap-2">
          {[
            { id: "overview", label: "Genel Bakış & Yorumlar" },
            { id: "models", label: `Fiyat & Puan Yönetimi (${models.length})` },
            { id: "faults", label: "+ Kronik Arıza Ekle" },
          ].map((t) => (
            <button
              key={t.id}
              onClick={() => setTab(t.id as typeof tab)}
              className={`px-4 py-2 rounded-xl text-sm font-medium transition cursor-pointer ${
                tab === t.id
                  ? "bg-orange-500 text-zinc-950 font-semibold"
                  : "bg-[#1f2228] text-zinc-300 border border-zinc-800 hover:border-zinc-700"
              }`}
            >
              {t.label}
            </button>
          ))}
        </div>

        {/* Tab 1: Overview */}
        {tab === "overview" && overview && (
          <div className="space-y-6">
            <div className="grid grid-cols-2 sm:grid-cols-5 gap-3">
              {[
                { label: "Marka", val: overview.counts.brands },
                { label: "Model", val: overview.counts.models },
                { label: "Varyant", val: overview.counts.variants },
                { label: "Kronik Arıza", val: overview.counts.faults },
                { label: "Kullanıcı Yorumu", val: overview.counts.comments },
              ].map((kpi) => (
                <div
                  key={kpi.label}
                  className="rounded-2xl bg-[#1f2228] border border-zinc-800 p-4"
                >
                  <div className="text-xs text-zinc-400">{kpi.label}</div>
                  <div className="text-2xl font-bold text-orange-400 mt-1">{kpi.val}</div>
                </div>
              ))}
            </div>

            <div className="grid md:grid-cols-2 gap-4">
              <div className="rounded-2xl bg-[#1f2228] border border-zinc-800 p-5">
                <h2 className="text-sm font-semibold text-white mb-3">Kasa Tipi Dağılımı</h2>
                <div className="flex flex-wrap gap-2">
                  {Object.entries(overview.body_types).map(([k, v]) => (
                    <span
                      key={k}
                      className="text-xs px-3 py-1.5 rounded-lg bg-[#16181c] border border-zinc-800 text-zinc-200"
                    >
                      {BODY_TYPE_LABEL[k] ?? k}: <strong className="text-orange-400">{v}</strong>
                    </span>
                  ))}
                </div>
              </div>

              <div className="rounded-2xl bg-[#1f2228] border border-zinc-800 p-5">
                <h2 className="text-sm font-semibold text-white mb-3">Yakıt Tipi Dağılımı (Varyant)</h2>
                <div className="flex flex-wrap gap-2">
                  {Object.entries(overview.fuel_types).map(([k, v]) => (
                    <span
                      key={k}
                      className="text-xs px-3 py-1.5 rounded-lg bg-[#16181c] border border-zinc-800 text-zinc-200"
                    >
                      {FUEL_TYPE_LABEL[k] ?? k}: <strong className="text-orange-400">{v}</strong>
                    </span>
                  ))}
                </div>
              </div>
            </div>

            <div className="rounded-2xl bg-[#1f2228] border border-zinc-800 p-5">
              <h2 className="text-sm font-semibold text-white mb-3">
                Son Kullanıcı Yorumları (Moderasyon)
              </h2>
              {overview.recent_comments.length === 0 ? (
                <p className="text-xs text-zinc-400">Henüz veritabanına kayıtlı ziyaretçi yorumu yok.</p>
              ) : (
                <div className="space-y-3">
                  {overview.recent_comments.map((c) => (
                    <div
                      key={c.id}
                      className="rounded-xl bg-[#16181c] border border-zinc-800 p-3.5 flex flex-col sm:flex-row sm:items-center justify-between gap-3"
                    >
                      <div className="space-y-1">
                        <div className="flex flex-wrap items-center gap-2 text-xs">
                          <span className="font-semibold text-white">{c.author_name}</span>
                          <span className="text-orange-400">{"★".repeat(c.rating)}</span>
                          {c.ownership_status && (
                            <span className="text-zinc-400">· {c.ownership_status}</span>
                          )}
                        </div>
                        <p className="text-xs text-zinc-300">{c.body}</p>
                      </div>
                      <button
                        onClick={() => deleteComment(c.id)}
                        className="shrink-0 text-xs px-3 py-1.5 rounded-lg bg-red-500/15 hover:bg-red-500/25 text-red-300 border border-red-500/30 cursor-pointer"
                      >
                        Sil
                      </button>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>
        )}

        {/* Tab 2: Models & Prices */}
        {tab === "models" && (
          <div className="space-y-4">
            <input
              type="text"
              value={searchQ}
              onChange={(e) => setSearchQ(e.target.value)}
              placeholder="Marka veya model ara (ör: Passat, Togg, Golf 8)..."
              className="w-full rounded-xl bg-[#1f2228] border border-zinc-800 px-4 py-3 text-sm text-white focus:outline-none focus:border-orange-500"
            />

            <div className="space-y-3">
              {filteredModels.map((m) => {
                const isOpen = expandedModel === m.id;
                return (
                  <div
                    key={m.id}
                    className="rounded-2xl bg-[#1f2228] border border-zinc-800 overflow-hidden"
                  >
                    <div className="p-4 flex flex-wrap items-center justify-between gap-3">
                      <button
                        type="button"
                        onClick={() => setExpandedModel(isOpen ? null : m.id)}
                        className="text-left flex items-center gap-3 cursor-pointer"
                      >
                        <span className="text-orange-400 text-xs font-mono">
                          {isOpen ? "▼" : "▶"}
                        </span>
                        <div>
                          <div className="font-semibold text-white text-sm">
                            {m.brand} {m.name}
                          </div>
                          <div className="text-xs text-zinc-400">
                            {BODY_TYPE_LABEL[m.body_type] ?? m.body_type} · {m.year_start}–
                            {m.year_end ?? "devam"} · {m.variants.length} varyant
                          </div>
                        </div>
                      </button>

                      <div className="flex items-center gap-2">
                        <span className="text-xs text-zinc-400">Konfor:</span>
                        <input
                          type="number"
                          step="0.1"
                          min="1"
                          max="10"
                          value={comfortEdits[m.id] ?? String(m.comfort_score)}
                          onChange={(e) =>
                            setComfortEdits((prev) => ({ ...prev, [m.id]: e.target.value }))
                          }
                          className="w-16 rounded-lg bg-[#16181c] border border-zinc-700 px-2 py-1 text-xs text-white text-center"
                        />
                        <button
                          onClick={() => saveModelComfort(m)}
                          className="text-xs px-3 py-1.5 rounded-lg bg-orange-500 hover:bg-orange-400 text-zinc-950 font-semibold cursor-pointer"
                        >
                          Kaydet
                        </button>
                      </div>
                    </div>

                    {isOpen && (
                      <div className="border-t border-zinc-800 bg-[#16181c]/60 p-4 space-y-2.5">
                        {m.variants.map((v) => (
                          <div
                            key={v.id}
                            className="flex flex-wrap items-center justify-between gap-3 rounded-xl bg-[#1f2228] border border-zinc-800 px-3.5 py-2.5"
                          >
                            <div>
                              <div className="text-xs font-semibold text-white">
                                {v.engine_label} · {v.transmission_label}
                              </div>
                              <div className="text-[11px] text-zinc-400">
                                {FUEL_TYPE_LABEL[v.fuel_type] ?? v.fuel_type} · {v.year_start}–
                                {v.year_end ?? "devam"}
                              </div>
                            </div>

                            <div className="flex items-center gap-2">
                              <input
                                type="number"
                                step="10000"
                                value={priceEdits[v.id] ?? String(v.used_price_tl ?? "")}
                                onChange={(e) =>
                                  setPriceEdits((prev) => ({ ...prev, [v.id]: e.target.value }))
                                }
                                placeholder="TL"
                                className="w-28 rounded-lg bg-[#16181c] border border-zinc-700 px-2.5 py-1 text-xs text-white text-right"
                              />
                              <span className="text-xs text-zinc-400">TL</span>
                              <button
                                onClick={() => saveVariantPrice(v)}
                                className="text-xs px-3 py-1.5 rounded-lg bg-zinc-800 hover:bg-orange-500 hover:text-zinc-950 text-zinc-200 font-medium transition cursor-pointer"
                              >
                                Fiyat Güncelle
                              </button>
                            </div>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          </div>
        )}

        {/* Tab 3: Add Fault */}
        {tab === "faults" && (
          <form
            onSubmit={createFault}
            className="rounded-2xl bg-[#1f2228] border border-zinc-800 p-6 space-y-4 max-w-2xl"
          >
            <h2 className="text-base font-semibold text-white">Yeni Kronik Arıza Kaydı Ekle</h2>

            <div>
              <label className="block text-xs text-zinc-400 mb-1">Araç Modeli</label>
              <select
                value={faultModelId}
                onChange={(e) => setFaultModelId(e.target.value)}
                className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2.5 text-sm text-white"
              >
                {models.map((m) => (
                  <option key={m.id} value={m.id}>
                    {m.brand} {m.name}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label className="block text-xs text-zinc-400 mb-1">Arıza Başlığı</label>
              <input
                type="text"
                value={faultTitle}
                onChange={(e) => setFaultTitle(e.target.value)}
                placeholder="Örn: DSG Mekatronik Basınç Kaybı"
                className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2.5 text-sm text-white"
                required
              />
            </div>

            <div>
              <label className="block text-xs text-zinc-400 mb-1">Detaylı Açıklama</label>
              <textarea
                rows={3}
                value={faultDesc}
                onChange={(e) => setFaultDesc(e.target.value)}
                placeholder="Belirtileri ve kullanıcı şikayetlerini yazın..."
                className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2.5 text-sm text-white"
                required
              />
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
              <div>
                <label className="block text-xs text-zinc-400 mb-1">Kategori</label>
                <select
                  value={faultCat}
                  onChange={(e) => setFaultCat(e.target.value)}
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2 text-sm text-white"
                >
                  <option value="mekanik">Mekanik</option>
                  <option value="elektronik">Elektronik</option>
                  <option value="yazilim_multimedya">Yazılım / Multimedya</option>
                  <option value="konfor">Konfor / Trim</option>
                  <option value="guvenlik">Güvenlik</option>
                </select>
              </div>
              <div>
                <label className="block text-xs text-zinc-400 mb-1">Ort. Masraf (TL)</label>
                <input
                  type="number"
                  value={faultAvgCost}
                  onChange={(e) => setFaultAvgCost(e.target.value)}
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2 text-sm text-white"
                />
              </div>
              <div>
                <label className="block text-xs text-zinc-400 mb-1">Max Masraf (TL)</label>
                <input
                  type="number"
                  value={faultMaxCost}
                  onChange={(e) => setFaultMaxCost(e.target.value)}
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2 text-sm text-white"
                />
              </div>
            </div>

            <div className="grid grid-cols-3 gap-3">
              <div>
                <label className="block text-xs text-zinc-400 mb-1">Şiddet</label>
                <select
                  value={faultSeverity}
                  onChange={(e) => setFaultSeverity(e.target.value)}
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2 text-sm text-white"
                >
                  <option value="">Otomatik (Masrafa Göre)</option>
                  <option value="dusuk">Düşük</option>
                  <option value="orta">Orta</option>
                  <option value="yuksek">Yüksek</option>
                  <option value="cok_yuksek">Çok Yüksek</option>
                </select>
              </div>
              <div>
                <label className="block text-xs text-zinc-400 mb-1">Başlangıç Km</label>
                <input
                  type="number"
                  value={faultKmStart}
                  onChange={(e) => setFaultKmStart(e.target.value)}
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2 text-sm text-white"
                />
              </div>
              <div>
                <label className="block text-xs text-zinc-400 mb-1">Bitiş Km</label>
                <input
                  type="number"
                  value={faultKmEnd}
                  onChange={(e) => setFaultKmEnd(e.target.value)}
                  className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2 text-sm text-white"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs text-zinc-400 mb-1">Ekspertiz Kontrol Maddesi (Opsiyonel)</label>
              <input
                type="text"
                value={faultCheck}
                onChange={(e) => setFaultCheck(e.target.value)}
                placeholder="Örn: Soğuk marşta zincir sesi kontrol edilmeli"
                className="w-full rounded-xl bg-[#16181c] border border-zinc-700 px-3 py-2.5 text-sm text-white"
              />
            </div>

            <button
              type="submit"
              className="rounded-xl bg-orange-500 hover:bg-orange-400 text-zinc-950 font-semibold px-6 py-2.5 text-sm transition cursor-pointer"
            >
              Arızayı Veritabanına Kaydet
            </button>
          </form>
        )}
      </main>
    </div>
  );
}
