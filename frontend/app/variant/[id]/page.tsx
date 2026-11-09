"use client";
import Link from "next/link";
import { useParams, useSearchParams } from "next/navigation";
import { useEffect, useState, useMemo, Suspense } from "react";
import {
  api,
  CATEGORY_LABEL,
  SEVERITY_LABEL,
  FUEL_TYPE_LABEL,
  tl,
  VariantFaultsResponse,
  UserCommentItem,
} from "@/lib/api";
import { buildSahibindenUrl, buildArabamUrl, FilterParams } from "@/lib/listingUrl";
import ScoreGauge from "@/components/ScoreGauge";

const km = (n: number | null) => (n ? n.toLocaleString("tr-TR") : "?");

function VariantContent() {
  const { id } = useParams<{ id: string }>();
  const searchParams = useSearchParams();

  const [r, setR] = useState<VariantFaultsResponse | null>(null);
  const [tab, setTab] = useState<"faults" | "packages" | "software" | "comments">("faults");
  const [error, setError] = useState("");

  // Yorum Ekleme Form State
  const [comments, setComments] = useState<UserCommentItem[]>([]);
  const [authorName, setAuthorName] = useState("");
  const [ownershipStatus, setOwnershipStatus] = useState("Sahibiyim");
  const [mileageKm, setMileageKm] = useState("");
  const [rating, setRating] = useState(5);
  const [recommend, setRecommend] = useState(true);
  const [commentBody, setCommentBody] = useState("");
  const [commentSubmitting, setCommentSubmitting] = useState(false);
  const [commentSuccess, setCommentSuccess] = useState(false);

  const filterQueryString = searchParams.toString();

  useEffect(() => {
    api<VariantFaultsResponse>(`/variants/${id}/faults`)
      .then((data) => {
        setR(data);
        if (data.user_comments) {
          setComments(data.user_comments);
        }
      })
      .catch((e) => setError(String(e)));
  }, [id]);

  // URL filtreleri + varyantın kendi motor/şanzıman bilgisi
  const combinedFilters: FilterParams = useMemo(() => {
    return {
      year_min: searchParams.get("year_min"),
      year_max: searchParams.get("year_max"),
      budget_max: searchParams.get("budget_max"),
      km_min: searchParams.get("km_min"),
      km_max: searchParams.get("km_max"),
      fuel_type: searchParams.get("fuel_type") || (r?.variant.fuel_type ?? null),
      transmission_type: searchParams.get("transmission_type") || (r?.variant.transmission_type ?? null),
      body_type: searchParams.get("body_type"),
    };
  }, [searchParams, r]);

  // Üye olmadan doğrudan yorum gönderme
  const handleCommentSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!commentBody.trim()) return;

    setCommentSubmitting(true);
    setCommentSuccess(false);

    try {
      const newComment = await api<UserCommentItem>(
        `/variants/${id}/comments`,
        undefined,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            author_name: authorName.trim() || "Anonim Sürücü",
            ownership_status: ownershipStatus,
            mileage_km: mileageKm ? parseInt(mileageKm.replace(/\D/g, ""), 10) : null,
            rating,
            recommend,
            body: commentBody.trim(),
          }),
        }
      );

      setComments((prev) => [newComment, ...prev]);
      setCommentBody("");
      setAuthorName("");
      setMileageKm("");
      setCommentSuccess(true);
      setTimeout(() => setCommentSuccess(false), 4000);
    } catch (err: any) {
      alert("Yorum eklenirken hata: " + err?.message);
    } finally {
      setCommentSubmitting(false);
    }
  };

  if (error) return <div className="card">{error}</div>;
  if (!r) return <p className="muted" style={{ padding: 20 }}>Yükleniyor…</p>;

  const v = r.variant;
  const trimPackages = r.trim_packages || [];
  const media = r.media_specs;

  // Sahibinden ve Arabam linklerini hatasız arama parametreleriyle oluştur
  const searchKeyword = `${v.brand} ${v.model}`;
  const sahibindenUrl = buildSahibindenUrl(searchKeyword, combinedFilters);
  const arabamUrl = buildArabamUrl(searchKeyword, combinedFilters);

  // Aktif filtre etiketleri
  const activeBadges: string[] = [];
  if (combinedFilters.year_min || combinedFilters.year_max) {
    activeBadges.push(`Yıl: ${combinedFilters.year_min ?? ""}–${combinedFilters.year_max ?? ""}`);
  }
  if (combinedFilters.budget_max) {
    activeBadges.push(`Bütçe: ${Number(combinedFilters.budget_max).toLocaleString("tr-TR")} TL`);
  }
  if (combinedFilters.km_min || combinedFilters.km_max) {
    activeBadges.push(`KM: ${combinedFilters.km_min ?? "0"}–${combinedFilters.km_max ?? "Maks"}`);
  }
  if (combinedFilters.fuel_type) {
    activeBadges.push(`Yakıt: ${FUEL_TYPE_LABEL[combinedFilters.fuel_type] ?? combinedFilters.fuel_type}`);
  }
  if (combinedFilters.transmission_type) {
    activeBadges.push(`Vites: ${combinedFilters.transmission_type.toUpperCase()}`);
  }

  return (
    <>
      <Link
        href={filterQueryString ? `/model/${v.model_id}?${filterQueryString}` : `/model/${v.model_id}`}
        className="muted"
        style={{ fontWeight: 600 }}
      >
        ← {v.brand} {v.model} Modeline Dön
      </Link>

      {/* Başlık ve Hız Göstergesi */}
      <div className="row" style={{ marginTop: 14, alignItems: "center" }}>
        <div>
          <h1 style={{ margin: "4px 0", fontSize: "2rem", color: "var(--text)" }}>
            {v.brand} {v.model} – {v.engine}
          </h1>
          <div className="muted small" style={{ fontSize: "0.95rem" }}>
            Şanzıman: <strong style={{ color: "var(--text)" }}>{v.transmission}</strong> · Üretim: {v.year_start}–{v.year_end ?? "devam"}
            {v.used_price_tl ? ` · Tahmini Piyasa: ~${tl(v.used_price_tl)}` : ""}
          </div>
        </div>

        {/* Mavi Doluluk Oranlı & Marka Logolu Konfor Göstergesi */}
        {v.comfort_score !== null && (
          <div className="card" style={{ padding: "12px 20px" }}>
            <ScoreGauge
              score={v.comfort_score}
              brand={v.brand}
              size="md"
              label="Konfor & Yalıtım Puanı"
              showTicks={true}
            />
          </div>
        )}
      </div>

      {/* 2 SÜTUNLU DÜZEN (Sol %35 Model Analizi, Sağ %65 Detaylar) */}
      <div className="split-layout">
        
        {/* SOL SÜTUN: Karakteristik Analizi + Avantaj / Dezavantajlar (Fotoğraf kaldırıldı) */}
        <div className="stack">
          {/* Model Karakteristik Analizi (Performans, Yakıt, Yol Tutuşu, İç Hacim, Kalite, Yalıtım) */}
          {media?.characteristics && (
            <div className="card">
              <h3 style={{ margin: "0 0 14px 0", fontSize: "1.1rem", borderBottom: "1px solid var(--border)", paddingBottom: 8 }}>
                📊 Araç Karakteristik Analizi
              </h3>
              
              <div style={{ display: "grid", gap: 10, fontSize: "0.85rem" }}>
                <div>
                  <strong style={{ color: "var(--text-secondary)" }}>⚡ Motor Performansı:</strong>
                  <div style={{ color: "var(--text)", marginTop: 2, fontWeight: 500 }}>
                    {media.characteristics.motor_performansi}
                  </div>
                </div>

                <div>
                  <strong style={{ color: "var(--text-secondary)" }}>⛽ Yakıt Tüketimi:</strong>
                  <div style={{ color: "var(--text)", marginTop: 2, fontWeight: 500 }}>
                    {media.characteristics.yakit_tuketimi}
                  </div>
                </div>

                <div>
                  <strong style={{ color: "var(--text-secondary)" }}>🎯 Yol Tutuşu & Şasi:</strong>
                  <div style={{ color: "var(--text)", marginTop: 2, fontWeight: 500 }}>
                    {media.characteristics.yol_tutusu}
                  </div>
                </div>

                <div>
                  <strong style={{ color: "var(--text-secondary)" }}>🛋️ İç Hacim & Yaşam Alanı:</strong>
                  <div style={{ color: "var(--text)", marginTop: 2, fontWeight: 500 }}>
                    {media.characteristics.ic_hacim}
                  </div>
                </div>

                <div>
                  <strong style={{ color: "var(--text-secondary)" }}>✨ İç Malzeme Kalitesi:</strong>
                  <div style={{ color: "var(--text)", marginTop: 2, fontWeight: 500 }}>
                    {media.characteristics.malzeme_kalitesi}
                  </div>
                </div>

                <div>
                  <strong style={{ color: "var(--text-secondary)" }}>🔇 Kabin & Yol Yalıtımı:</strong>
                  <div style={{ color: "var(--text)", marginTop: 2, fontWeight: 500 }}>
                    {media.characteristics.yalitim}
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Model Avantajları & Dezavantajları */}
          <div className="card">
            <h3 style={{ margin: "0 0 10px 0", fontSize: "1.05rem", color: "#16a34a" }}>
              👍 Modelin Güçlü Yönleri (Artıları)
            </h3>
            <ul className="small" style={{ margin: 0, paddingLeft: 18, color: "var(--text-secondary)", display: "grid", gap: 6 }}>
              {media?.advantages?.map((adv, idx) => (
                <li key={idx}>{adv}</li>
              ))}
            </ul>

            <h3 style={{ margin: "16px 0 10px 0", fontSize: "1.05rem", color: "#ea580c" }}>
              👎 Dikkat Edilmesi Gerekenler (Eksileri)
            </h3>
            <ul className="small" style={{ margin: 0, paddingLeft: 18, color: "var(--text-secondary)", display: "grid", gap: 6 }}>
              {media?.disadvantages?.map((dis, idx) => (
                <li key={idx}>{dis}</li>
              ))}
            </ul>
          </div>
        </div>

        {/* SAĞ SÜTUN: Arıza Özeti, Sekmeler (Arızalar, Donanım Paketleri, Yazılım, Yorumlar) */}
        <div>
          {/* Arıza Masraf Özeti */}
          <div className="card row" style={{ marginBottom: 16 }}>
            <div style={{ display: "flex", gap: 8, flexWrap: "wrap", alignItems: "center" }}>
              {Object.entries(r.fault_summary.counts).map(([s, c]) => (
                <span key={s} style={{ display: "inline-flex", alignItems: "center", gap: 4 }}>
                  <span className={`badge ${s}`}>{SEVERITY_LABEL[s] ?? s}</span>
                  <strong>{c}</strong>
                </span>
              ))}
            </div>
            <span className="muted small">
              Olası Toplam Masraf: <strong>{tl(r.fault_summary.expected_cost_range_tl[0])}</strong> –{" "}
              <strong>{tl(r.fault_summary.expected_cost_range_tl[1])}</strong>
            </span>
          </div>

          {/* Sekme Butonları (4 Sekme) */}
          <div className="tabs">
            <button
              className={`tab ${tab === "faults" ? "active" : ""}`}
              onClick={() => setTab("faults")}
            >
              Kronik Arızalar & Şikayetler ({r.faults.length})
            </button>
            <button
              className={`tab ${tab === "packages" ? "active" : ""}`}
              onClick={() => setTab("packages")}
            >
              Donanım Paketleri ({trimPackages.length})
            </button>
            <button
              className={`tab ${tab === "software" ? "active" : ""}`}
              onClick={() => setTab("software")}
            >
              Yazılım / Stage ({r.software_mods.length})
            </button>
            <button
              className={`tab ${tab === "comments" ? "active" : ""}`}
              onClick={() => setTab("comments")}
            >
              💬 Kullanıcı Yorumları ({comments.length})
            </button>
          </div>

          {/* TAB 1: ARIZALAR & ŞİKAYETVAR */}
          {tab === "faults" && (
            <div className="stack">
              {r.faults.length === 0 && (
                <p className="muted card">Bu kombinasyon için henüz onaylanmış arıza kaydı bulunmamaktadır.</p>
              )}
              {r.faults.map((f) => {
                const hasSikayetvar = f.sources?.some((s) => s.toLowerCase().includes("sikayetvar"));

                return (
                  <div key={f.id} className="card">
                    <div className="row">
                      <strong style={{ fontSize: "1.05rem" }}>{f.title}</strong>
                      <span>
                        {hasSikayetvar && (
                          <span className="badge source-sikayet" title="Şikayetvar.com kullanıcı kayıtlı">
                            Şikayetvar Doğrulamalı
                          </span>
                        )}{" "}
                        {!f.verified && (
                          <span className="badge draft" title="Kaynak doğrulaması yapılmadı">
                            Taslak
                          </span>
                        )}{" "}
                        <span className="badge cat">{CATEGORY_LABEL[f.category] ?? f.category}</span>{" "}
                        <span className={`badge ${f.severity}`}>{SEVERITY_LABEL[f.severity] ?? f.severity}</span>
                      </span>
                    </div>

                    <p style={{ margin: "8px 0", color: "var(--text-secondary)" }}>{f.description}</p>

                    <div className="muted small">
                      Oluşum Aralığı: <strong>{km(f.occurrence_km[0])}–{km(f.occurrence_km[1])} km</strong> · Ortalama Masraf:{" "}
                      <strong style={{ color: "var(--text)" }}>{tl(f.avg_repair_cost_tl)}</strong>
                      {f.max_repair_cost_tl ? ` (maks. ${tl(f.max_repair_cost_tl)})` : ""}
                      {f.report_count ? ` · ~${f.report_count} kullanıcı bildirimi` : ""}
                    </div>

                    {f.checklist.length > 0 && (
                      <div style={{ marginTop: 10, background: "var(--card-alt)", border: "1px solid var(--border)", padding: 10, borderRadius: 8 }}>
                        <div className="small">
                          <strong>🔍 Ekspertizde & Satın Alırken Özellikle Bakılacaklar:</strong>
                        </div>
                        <ul className="small" style={{ color: "var(--text-secondary)" }}>
                          {f.checklist.map((c, i) => (
                            <li key={i}>{c}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {f.sources && f.sources.length > 0 && (
                      <div className="muted small" style={{ marginTop: 10 }}>
                        <strong>Doğrulama Kaynakları:</strong>{" "}
                        {f.sources
                          .map((s) =>
                            s
                              .replace("youtube:", "▶ YouTube (Usta/Kanal): ")
                              .replace("forum:", "💬 Forum/Kulüp: ")
                              .replace("sikayetvar:", "🌐 Şikayetvar.com: ")
                              .replace("tuv:", "📋 TÜV/Muayene Raporu: ")
                          )
                          .join(" · ")}
                      </div>
                    )}
                  </div>
                );
              })}
            </div>
          )}

          {/* TAB 2: DONANIM PAKETLERİ (DÜŞÜK / ORTA / PREMİUM) */}
          {tab === "packages" && (
            <div className="stack">
              {trimPackages.length === 0 && (
                <p className="muted card">Bu araç için donanım paket detayları hazırlanıyor.</p>
              )}
              <div className="grid">
                {trimPackages.map((tp, idx) => {
                  const isPremium = tp.level === "premium";
                  const isOrta = tp.level === "orta";

                  return (
                    <div
                      key={tp.id || idx}
                      className="card"
                      style={{
                        border: isPremium
                          ? "2px solid #ea580c"
                          : isOrta
                          ? "2px solid #2563eb"
                          : "1px solid var(--border)",
                      }}
                    >
                      <div className="row" style={{ marginBottom: 8 }}>
                        <strong style={{ fontSize: "1.1rem" }}>{tp.name}</strong>
                        {isPremium ? (
                          <span className="badge yuksek">Premium / En Dolu</span>
                        ) : isOrta ? (
                          <span className="badge orta">Orta / Konfor</span>
                        ) : (
                          <span className="badge dusuk">Giriş / Ekonomik</span>
                        )}
                      </div>

                      {tp.summary && (
                        <p className="muted small" style={{ margin: "4px 0 12px" }}>
                          {tp.summary}
                        </p>
                      )}

                      <div style={{ marginTop: 8 }}>
                        <div className="small" style={{ fontWeight: 600, marginBottom: 6 }}>
                          Paket Standart Özellikleri:
                        </div>
                        <div>
                          {tp.features?.map((feat, fIdx) => (
                            <span key={fIdx} className="feature-chip">
                              ✓ {feat}
                            </span>
                          ))}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Kullanıcı isteği: modelin yılına göre değişiklikler uyarısı */}
              <p style={{ fontSize: "0.8rem", color: "var(--muted)", marginTop: 14, fontWeight: 500 }}>
                * Modelin yılına göre değişiklikler olabilir.
              </p>
            </div>
          )}

          {/* TAB 3: YAZILIM / STAGE & MULTİMEDYA */}
          {tab === "software" && (
            <div className="stack">
              {r.software_mods.length === 0 && (
                <p className="muted card">Bu motor/şanzıman için henüz yazılım (stage) kaydı girilmedi.</p>
              )}
              {r.software_mods.map((s) => (
                <div key={s.id} className="card">
                  <div className="row">
                    <strong>{s.mod_type.toUpperCase()} Yazılım Uygulaması</strong>
                    <span>
                      {!s.verified && <span className="badge draft">Taslak</span>}{" "}
                      {s.is_recommended === true && <span className="badge dusuk">Önerilir / Güvenli</span>}
                      {s.is_recommended === false && <span className="badge kritik">Kesinlikle Önerilmez</span>}
                      {s.is_recommended === null && <span className="badge orta">Koşullu / Dikkat Gerekir</span>}
                    </span>
                  </div>

                  <div className="small" style={{ marginTop: 8 }}>
                    <strong>Güç Değişimi:</strong> {s.hp[0]} HP → <strong>{s.hp[1]} HP</strong> ·{" "}
                    <strong>Tork:</strong> {s.nm[0]} Nm → <strong>{s.nm[1]} Nm</strong>
                    {s.approx_cost_tl ? ` · Tahmini Maliyet: ~${tl(s.approx_cost_tl)}` : ""}
                  </div>

                  {s.risk_note && (
                    <p
                      className="small"
                      style={{
                        marginTop: 8,
                        background: "#fef3c7",
                        color: "#92400e",
                        borderLeft: "4px solid #f59e0b",
                        padding: 10,
                        borderRadius: 6,
                      }}
                    >
                      ⚠️ <strong>Risk & Şanzıman/Motor Tavsiyesi:</strong> {s.risk_note}
                    </p>
                  )}
                </div>
              ))}
            </div>
          )}

          {/* TAB 4: ÜYELİKSİZ DOĞRUDAN KULLANICI YORUMLARI & FORMU */}
          {tab === "comments" && (
            <div className="stack">
              {/* 1. Mevcut Kullanıcı Yorumları Listesi (Önce Yorumlar Gösterilir) */}
              <div className="stack">
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 4 }}>
                  <h3 style={{ margin: 0, fontSize: "1.1rem", color: "#0f172a" }}>
                    💬 Kullanıcı & Sürücü Deneyimleri ({comments.length})
                  </h3>
                  <span className="small muted">sikayetvar.com & Gerçek Araç Sahipleri</span>
                </div>

                {comments.length === 0 && (
                  <p className="muted card">Henüz kullanıcı yorumu yapılmamış. İlk yorumu aşağıdaki formdan siz yapabilirsiniz!</p>
                )}
                {comments.map((c) => (
                  <div key={c.id} className="card" style={{ background: "#ffffff", border: "1px solid #e2e8f0" }}>
                    <div className="row">
                      <div>
                        <strong>{c.author_name}</strong>
                        {c.ownership_status && (
                          <span className="muted small" style={{ marginLeft: 8 }}>
                            ({c.ownership_status})
                          </span>
                        )}
                        {c.mileage_km && (
                          <span className="muted small" style={{ marginLeft: 8 }}>
                            · {c.mileage_km.toLocaleString("tr-TR")} km
                          </span>
                        )}
                      </div>
                      <div className="small">
                        {"⭐".repeat(c.rating || 5)} ·{" "}
                        <span style={{ color: c.recommend ? "#16a34a" : "#dc2626", fontWeight: 700 }}>
                          {c.recommend ? "Tavsiye Ediyor 👍" : "Tavsiye Etmiyor 👎"}
                        </span>
                      </div>
                    </div>
                    <p style={{ margin: "8px 0 0", color: "var(--text-secondary)", lineHeight: 1.5 }}>{c.body}</p>
                    <div className="muted small" style={{ marginTop: 6, fontSize: "0.75rem" }}>
                      Tarih: {c.created_at}
                    </div>
                  </div>
                ))}
              </div>

              {/* 2. Yorum Ekleme Formu (Kullanıcı İsteği: Yorumların Altında) */}
              <div className="card" style={{ background: "#ffffff", border: "2px solid #e2e8f0", marginTop: 16 }}>
                <h3 style={{ margin: "0 0 8px 0", fontSize: "1.1rem", color: "#0f172a" }}>
                  ✍️ Deneyiminizi Paylaşın (Üyelik Gerekmez)
                </h3>
                <p className="muted small" style={{ margin: "0 0 16px 0" }}>
                  Bu aracı kullandıysanız, arıza veya memnuniyet durumunuzu diğer alıcılarla paylaşabilirsiniz.
                </p>

                {commentSuccess && (
                  <div style={{ background: "#dcfce7", color: "#166534", padding: "10px 14px", borderRadius: 8, marginBottom: 14, fontSize: "0.9rem" }}>
                    ✓ Yorumunuz başarıyla yayınlandı! Katkınız için teşekkürler.
                  </div>
                )}

                <form onSubmit={handleCommentSubmit} style={{ display: "grid", gap: 12 }}>
                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
                    <label>
                      Adınız veya Takma Ad
                      <input
                        type="text"
                        placeholder="Örn: Ahmet Y. (Opsiyonel)"
                        value={authorName}
                        onChange={(e) => setAuthorName(e.target.value)}
                      />
                    </label>

                    <label>
                      Sahiplik Durumunuz
                      <select value={ownershipStatus} onChange={(e) => setOwnershipStatus(e.target.value)}>
                        <option value="Sahibiyim">Halen Sahibiyim</option>
                        <option value="Eski Sahibiyim">Eski Sahibiyim</option>
                        <option value="Test Ettim">Test Ettim / Uzun Dönem Kullandım</option>
                      </select>
                    </label>
                  </div>

                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 12 }}>
                    <label>
                      Araç Kilometresi
                      <input
                        type="text"
                        placeholder="Örn: 125.000"
                        value={mileageKm}
                        onChange={(e) => setMileageKm(e.target.value)}
                      />
                    </label>

                    <label>
                      Memnuniyet Puanı
                      <select value={rating} onChange={(e) => setRating(parseInt(e.target.value, 10))}>
                        <option value="5">⭐⭐⭐⭐⭐ (5/5 Mükemmel)</option>
                        <option value="4">⭐⭐⭐⭐ (4/5 İyi)</option>
                        <option value="3">⭐⭐⭐ (3/5 Orta)</option>
                        <option value="2">⭐⭐ (2/5 Zayıf)</option>
                        <option value="1">⭐ (1/5 Kötü)</option>
                      </select>
                    </label>

                    <label>
                      Tavsiye Eder misiniz?
                      <select value={recommend ? "evet" : "hayir"} onChange={(e) => setRecommend(e.target.value === "evet")}>
                        <option value="evet">👍 Evet, Öneririm</option>
                        <option value="hayir">👎 Hayır, Önermem</option>
                      </select>
                    </label>
                  </div>

                  <label>
                    Yorumunuz ve Tecrübeleriniz
                    <textarea
                      rows={3}
                      placeholder="Aracın motor performansı, yakıt tüketimi, yaşadığınız kronik sorunlar veya servisteki tecrübelerinizi yazabilirsiniz..."
                      value={commentBody}
                      onChange={(e) => setCommentBody(e.target.value)}
                      required
                      style={{ resize: "vertical" }}
                    />
                  </label>

                  <button
                    type="submit"
                    className="btn"
                    disabled={commentSubmitting}
                    style={{ justifySelf: "start", padding: "10px 24px" }}
                  >
                    {commentSubmitting ? "Yayınlanıyor..." : "Yorumu Gönder & Yayınla"}
                  </button>
                </form>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* GÜNCEL PİYASA İLANLARI (EN ALTA TAŞINDI) */}
      <div className="card" style={{ marginTop: 32, background: "#ffffff", border: "2px solid #e2e8f0" }}>
        <div style={{ fontWeight: 800, marginBottom: 6, fontSize: "1.15rem", color: "#0f172a" }}>
          🚗 Güncel Canlı İlanlar: {v.brand} {v.model} İlanlarını Nerede İncelemek İstersiniz?
        </div>
        <p className="muted small" style={{ margin: "0 0 14px 0" }}>
          Uygulamada seçtiğiniz tüm filtreler (yıl, bütçe, km, yakıt türü) aktarılmıştır. Tıkladığınızda doğrudan filtreli canlı ilanlar açılır:
        </p>

        {activeBadges.length > 0 && (
          <div style={{ display: "flex", gap: 6, flexWrap: "wrap", marginBottom: 16 }}>
            <span className="small muted" style={{ alignSelf: "center", fontWeight: 600 }}>
              İlana Taşınan Kriterler:
            </span>
            {activeBadges.map((badge, idx) => (
              <span
                key={idx}
                style={{
                  background: "#eff6ff",
                  color: "#1d4ed8",
                  border: "1px solid #bfdbfe",
                  borderRadius: "6px",
                  padding: "3px 9px",
                  fontSize: "0.8rem",
                  fontWeight: 600,
                }}
              >
                ✓ {badge}
              </span>
            ))}
          </div>
        )}

        <div style={{ display: "flex", gap: 14, flexWrap: "wrap" }}>
          <a
            href={sahibindenUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="listing-btn sahibinden"
          >
            Sahibinden.com&apos;da İlanları Filtrele ↗
          </a>
          <a
            href={arabamUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="listing-btn arabam"
          >
            Arabam.com&apos;da İlanları Filtrele ↗
          </a>
        </div>
      </div>
    </>
  );
}

export default function VariantPage() {
  return (
    <Suspense fallback={<p className="muted" style={{ padding: 20 }}>Sayfa yükleniyor...</p>}>
      <VariantContent />
    </Suspense>
  );
}
