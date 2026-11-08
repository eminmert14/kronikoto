"use client";
import Link from "next/link";
import { useState, useMemo, useEffect } from "react";
import {
  api,
  BODY_TYPE_LABEL,
  formatThousand,
  parseThousand,
  SearchResult,
} from "@/lib/api";
import ScoreGauge from "@/components/ScoreGauge";

const BODY_OPTIONS: [string, string][] = [
  ["sedan", "Sedan"],
  ["hatchback", "Hatchback"],
  ["suv", "Arazi / SUV"],
  ["station", "Station Wagon"],
  ["coupe", "Coupe"],
  ["kombi", "Ticari / Kombi"],
];

const FUEL_OPTIONS: [string, string][] = [
  ["benzin", "Benzin"],
  ["dizel", "Dizel"],
  ["hibrit", "Hibrit"],
  ["lpg", "LPG"],
  ["elektrik", "Elektrik"],
];

const TRANS_OPTIONS: [string, string][] = [
  ["manuel", "Manuel"],
  ["otomatik", "Otomatik"],
];

export default function Home() {
  const [f, setF] = useState<Record<string, string>>({});
  const [searchQuery, setSearchQuery] = useState("");
  const [yearMin, setYearMin] = useState("");
  const [yearMax, setYearMax] = useState("");
  const [budgetDisplay, setBudgetDisplay] = useState("");
  const [kmMinDisplay, setKmMinDisplay] = useState("");
  const [kmMaxDisplay, setKmMaxDisplay] = useState("");

  const [results, setResults] = useState<SearchResult[] | null>(null);
  const [error, setError] = useState("");
  const [isMobileDrawerOpen, setIsMobileDrawerOpen] = useState(false);

  // Kullanıcı isteği: Sayfa ilk açıldığında araçlar otomatik listelenmez.
  // "Araçları Listele" butonuna basınca Alfabetik (A-Z) listelenir.

  // Aktif filtre sayısı hesabı
  const activeFilterCount = useMemo(() => {
    let count = 0;
    if (searchQuery.trim()) count++;
    if (f.body_type) count++;
    if (yearMin || yearMax) count++;
    if (f.budget_max) count++;
    if (f.km_min || f.km_max) count++;
    if (f.fuel_type) count++;
    if (f.transmission_type) count++;
    return count;
  }, [searchQuery, f, yearMin, yearMax]);

  // URL query parametre string'i üret
  const filterQueryString = useMemo(() => {
    const qs = new URLSearchParams();
    if (searchQuery.trim()) qs.set("q", searchQuery.trim());
    if (f.body_type) qs.set("body_type", f.body_type);
    if (yearMin) qs.set("year_min", yearMin);
    if (yearMax) qs.set("year_max", yearMax);
    if (f.budget_max) qs.set("budget_max", f.budget_max);
    if (f.km_min) qs.set("km_min", f.km_min);
    if (f.km_max) qs.set("km_max", f.km_max);
    if (f.fuel_type) qs.set("fuel_type", f.fuel_type);
    if (f.transmission_type) qs.set("transmission_type", f.transmission_type);
    return qs.toString();
  }, [searchQuery, f, yearMin, yearMax]);

  const setSelect = (k: string) => (e: React.ChangeEvent<HTMLSelectElement>) => {
    setF((prev) => ({ ...prev, [k]: e.target.value }));
  };

  const handleBudgetChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const raw = parseThousand(e.target.value);
    const formatted = formatThousand(e.target.value);
    setBudgetDisplay(formatted);
    setF((prev) => ({ ...prev, budget_max: raw }));
  };

  const handleKmMinChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const raw = parseThousand(e.target.value);
    const formatted = formatThousand(e.target.value);
    setKmMinDisplay(formatted);
    setF((prev) => ({ ...prev, km_min: raw }));
  };

  const handleKmMaxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const raw = parseThousand(e.target.value);
    const formatted = formatThousand(e.target.value);
    setKmMaxDisplay(formatted);
    setF((prev) => ({ ...prev, km_max: raw }));
  };

  const handleYearMinChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value.replace(/\D/g, "");
    setYearMin(val);
  };

  const handleYearMaxChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value.replace(/\D/g, "");
    setYearMax(val);
  };

  const resetFilters = () => {
    setF({});
    setSearchQuery("");
    setYearMin("");
    setYearMax("");
    setBudgetDisplay("");
    setKmMinDisplay("");
    setKmMaxDisplay("");
    setError("");
    setResults(null);
  };

  async function executeSearch() {
    setError("");

    // Üretim yılı kontrolleri
    const yMinNum = yearMin ? parseInt(yearMin, 10) : null;
    const yMaxNum = yearMax ? parseInt(yearMax, 10) : null;

    if (yMinNum !== null && (yMinNum < 1970 || yMinNum > 2026)) {
      setError("Geçersiz üretim yılı! Minimum yıl 1970 ile 2026 arasında olmalıdır.");
      setResults(null);
      return;
    }

    if (yMaxNum !== null && (yMaxNum < 1970 || yMaxNum > 2026)) {
      setError("Geçersiz üretim yılı! Maksimum yıl 1970 ile 2026 arasında olmalıdır.");
      setResults(null);
      return;
    }

    if (yMinNum !== null && yMaxNum !== null && yMinNum > yMaxNum) {
      setError("Minimum üretim yılı, maksimum üretim yılından büyük olamaz.");
      setResults(null);
      return;
    }

    const queryParams: Record<string, string> = { ...f };
    if (searchQuery.trim()) queryParams.q = searchQuery.trim();
    if (yearMin) queryParams.year_min = yearMin;
    if (yearMax) queryParams.year_max = yearMax;

    try {
      const data = await api<SearchResult[]>("/vehicles/search", queryParams);
      setResults(data);
      setIsMobileDrawerOpen(false);
    } catch (err: any) {
      setError(err?.message || "Bir hata oluştu.");
      setResults(null);
    }
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    executeSearch();
  };

  // Filtreleme formu (En üstte serbest Marka/Model Arama kutusu)
  const FilterInputs = (
    <>
      <div style={{ gridColumn: "1 / -1", marginBottom: 4 }}>
        <label style={{ fontSize: "0.95rem", fontWeight: 700, color: "#0f172a" }}>
          🔍 Marka veya Model Ara
          <input
            type="text"
            placeholder="Örn: Megane, Passat, Corolla, Egea, Focus, Civic..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              width: "100%",
              padding: "11px 14px",
              fontSize: "1rem",
              border: "2px solid #cbd5e1",
              borderRadius: "10px",
              marginTop: 4,
            }}
          />
        </label>
      </div>

      <label>
        Kasa Tipi
        <select value={f.body_type ?? ""} onChange={setSelect("body_type")}>
          <option value="">Hepsi</option>
          {BODY_OPTIONS.map(([val, label]) => (
            <option key={val} value={val}>
              {label}
            </option>
          ))}
        </select>
      </label>

      <label>
        Üretim Yılı
        <div className="input-range-group">
          <input
            type="text"
            inputMode="numeric"
            placeholder="Min"
            maxLength={4}
            value={yearMin}
            onChange={handleYearMinChange}
          />
          <input
            type="text"
            inputMode="numeric"
            placeholder="Maks"
            maxLength={4}
            value={yearMax}
            onChange={handleYearMaxChange}
          />
        </div>
      </label>

      <label>
        Bütçe (Maks. TL)
        <input
          type="text"
          inputMode="numeric"
          placeholder="1.000.000"
          value={budgetDisplay}
          onChange={handleBudgetChange}
        />
      </label>

      <label>
        Kilometre
        <div className="input-range-group">
          <input
            type="text"
            inputMode="numeric"
            placeholder="Min"
            value={kmMinDisplay}
            onChange={handleKmMinChange}
          />
          <input
            type="text"
            inputMode="numeric"
            placeholder="Maks"
            value={kmMaxDisplay}
            onChange={handleKmMaxChange}
          />
        </div>
      </label>

      <label>
        Yakıt
        <select value={f.fuel_type ?? ""} onChange={setSelect("fuel_type")}>
          <option value="">Hepsi</option>
          {FUEL_OPTIONS.map(([val, label]) => (
            <option key={val} value={val}>
              {label}
            </option>
          ))}
        </select>
      </label>

      {/* Şanzıman: Sadece Manuel ve Otomatik */}
      <label>
        Şanzıman
        <select
          value={f.transmission_type ?? ""}
          onChange={setSelect("transmission_type")}
        >
          <option value="">Hepsi</option>
          {TRANS_OPTIONS.map(([val, label]) => (
            <option key={val} value={val}>
              {label}
            </option>
          ))}
        </select>
      </label>
    </>
  );

  return (
    <>
      <div style={{ marginBottom: 20 }}>
        <h1 style={{ fontSize: "1.9rem", marginBottom: 6, color: "#0f172a" }}>
          Hangi aracı almalı? Önce kronik arızalarını ve konforunu gör.
        </h1>
        <p className="muted" style={{ margin: 0, fontSize: "0.95rem" }}>
          Türkiye pazarındaki 50 popüler aracın motor & şanzıman kronik arızaları, gerçekçi konfor göstergesi ve güncel ilan filtreleri.
        </p>
      </div>

      {/* Masaüstü Filtre Formu */}
      <form className="filters card desktop-filters" onSubmit={handleSubmit}>
        {FilterInputs}
        <div style={{ display: "flex", gap: 8, alignSelf: "end" }}>
          {activeFilterCount > 0 && (
            <button
              type="button"
              onClick={resetFilters}
              style={{
                background: "transparent",
                color: "var(--muted)",
                border: "1px solid var(--border)",
                height: "44px",
                padding: "0 14px",
              }}
            >
              Temizle
            </button>
          )}
          <button type="submit" style={{ height: "44px", minWidth: "130px", fontWeight: 700 }}>
            Araçları Listele
          </button>
          <Link
            href="/compare"
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              height: "44px",
              padding: "0 14px",
              background: "#eff6ff",
              color: "#1d4ed8",
              border: "1px solid #bfdbfe",
              borderRadius: "8px",
              fontWeight: 700,
              fontSize: "0.9rem",
              whiteSpace: "nowrap",
            }}
          >
            ⚖️ Karşılaştır
          </Link>
          <Link
            href="/ekspertiz"
            style={{
              display: "inline-flex",
              alignItems: "center",
              justifyContent: "center",
              height: "44px",
              padding: "0 14px",
              background: "#f0fdf4",
              color: "#166534",
              border: "1px solid #bbf7d0",
              borderRadius: "8px",
              fontWeight: 700,
              fontSize: "0.9rem",
              whiteSpace: "nowrap",
            }}
          >
            🛡️ Ekspertiz Danışmanı
          </Link>
        </div>
      </form>

      {/* Mobil Sticky Filtre Açma Çubuğu */}
      <div className="mobile-filter-bar">
        <button
          type="button"
          className="mobile-filter-trigger"
          onClick={() => setIsMobileDrawerOpen(true)}
        >
          <span>🔍 Filtreleri Aç</span>
          {activeFilterCount > 0 && (
            <span
              style={{
                background: "#ffffff",
                color: "#1d4ed8",
                fontSize: "0.8rem",
                padding: "2px 8px",
                borderRadius: "999px",
                fontWeight: 800,
              }}
            >
              {activeFilterCount}
            </span>
          )}
        </button>
      </div>

      {/* Mobil Filtre Çekmecesi (Bottom Sheet) */}
      {isMobileDrawerOpen && (
        <div
          className="bottom-sheet-backdrop"
          onClick={(e) => {
            if (e.target === e.currentTarget) setIsMobileDrawerOpen(false);
          }}
        >
          <div className="bottom-sheet-content">
            <div className="bottom-sheet-header">
              <div>
                <div className="bottom-sheet-drag-handle" />
                <strong style={{ fontSize: "1.1rem" }}>Araç Filtreleri</strong>
              </div>
              <button
                type="button"
                onClick={() => setIsMobileDrawerOpen(false)}
                style={{
                  background: "transparent",
                  border: "none",
                  color: "var(--muted)",
                  fontSize: "1.4rem",
                  cursor: "pointer",
                  padding: "4px 8px",
                }}
              >
                ✕
              </button>
            </div>

            <div className="bottom-sheet-body">
              {FilterInputs}
            </div>

            <div className="bottom-sheet-footer" style={{ flexDirection: "column", gap: 8 }}>
              <div style={{ display: "flex", gap: 10, width: "100%" }}>
                <button
                  type="button"
                  onClick={resetFilters}
                  style={{
                    flex: 1,
                    background: "transparent",
                    border: "1px solid var(--border)",
                    color: "var(--text)",
                    height: "44px",
                  }}
                >
                  Temizle
                </button>
                <button
                  type="button"
                  onClick={executeSearch}
                  style={{
                    flex: 2,
                    background: "var(--accent)",
                    color: "#ffffff",
                    height: "44px",
                    fontWeight: 800,
                  }}
                >
                  Filtreleri Uygula
                </button>
              </div>
              <Link
                href="/compare"
                style={{
                  width: "100%",
                  height: "42px",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  background: "#eff6ff",
                  color: "#1d4ed8",
                  border: "1px solid #bfdbfe",
                  borderRadius: "8px",
                  fontWeight: 700,
                  fontSize: "0.95rem",
                }}
              >
                ⚖️ Araç Karşılaştırma Modülüne Git
              </Link>
            </div>
          </div>
        </div>
      )}

      {/* Hata Mesajı */}
      {error && (
        <div
          className="card"
          style={{
            borderLeft: "4px solid #ef4444",
            background: "#fef2f2",
            color: "#991b1b",
            marginBottom: 20,
          }}
        >
          <strong>Hata:</strong> {error}
        </div>
      )}

      {/* Sayfa İlk Açılışı: Araç Listeleme Çağrısı */}
      {results === null && !error && (
        <div
          className="card"
          style={{
            textAlign: "center",
            padding: "3.5rem 1.5rem",
            background: "#ffffff",
            borderRadius: "16px",
            border: "1px dashed #cbd5e1",
            marginTop: 12,
            boxShadow: "0 2px 8px rgba(0,0,0,0.03)",
          }}
        >
          <div style={{ fontSize: "2.6rem", marginBottom: 12 }}>🚗🔍</div>
          <h3 style={{ fontSize: "1.35rem", fontWeight: 800, color: "#0f172a", margin: "0 0 8px 0" }}>
            Araçları İncelemek İçin Başlayın
          </h3>
          <p style={{ color: "#64748b", maxWidth: 540, margin: "0 auto 24px auto", lineHeight: 1.5, fontSize: "0.95rem" }}>
            Yukarıdaki filtreleri (kasa tipi, bütçe, km, üretim yılı, yakıt, şanzıman) belirleyebilir veya doğrudan alfabetik sırayla tüm araçları listeleyebilirsiniz.
          </p>
          <button
            type="button"
            className="btn"
            onClick={executeSearch}
            style={{
              padding: "12px 32px",
              fontSize: "1.05rem",
              fontWeight: 700,
              boxShadow: "0 4px 14px rgba(37, 99, 235, 0.25)",
              cursor: "pointer",
            }}
          >
            📋 Araçları Listele (A-Z)
          </button>
        </div>
      )}

      {/* Sonuç Yok Uyarısı */}
      {results !== null && results.length === 0 && (
        <div className="card muted" style={{ textAlign: "center", padding: "3rem 1rem", background: "#ffffff" }}>
          <div style={{ fontSize: "2rem", marginBottom: 8 }}>🚗💨</div>
          <strong style={{ color: "#0f172a" }}>Belirtilen kriterlere uygun araç bulunamadı.</strong>
          <p className="small" style={{ margin: "6px 0 0" }}>
            Lütfen arama kelimenizi veya filtrelerinizi genişleterek tekrar deneyin.
          </p>
        </div>
      )}

      {/* Araç Kartları Izgarası */}
      <div className="grid">
        {results?.map((r) => {
          const detailUrl = filterQueryString
            ? `/model/${r.id}?${filterQueryString}`
            : `/model/${r.id}`;

          return (
            <Link
              key={r.id}
              href={detailUrl}
              className="card"
              style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
                gap: 12,
                transition: "transform 0.15s, box-shadow 0.15s",
                background: "#ffffff",
              }}
            >
              <div className="row" style={{ alignItems: "flex-start" }}>
                <div>
                  <strong style={{ fontSize: "1.15rem", display: "block", color: "#0f172a" }}>
                    {r.brand} {r.name}
                  </strong>
                  <div className="muted small" style={{ marginTop: 2 }}>
                    {BODY_TYPE_LABEL[r.body_type] ?? r.body_type} · {r.year_start}–
                    {r.year_end ?? "devam"}
                  </div>
                </div>

                {/* Düzeltilmiş Hız Göstergesi (Rakam ibrenin altında, çakışma yok) */}
                {r.comfort_score !== null && (
                  <ScoreGauge
                    score={r.comfort_score}
                    size="sm"
                    label=""
                    showTicks={false}
                  />
                )}
              </div>

              <div className="row" style={{ borderTop: "1px solid #f1f5f9", paddingTop: 10 }}>
                <span className="small muted">
                  {r.variants_count > 0
                    ? `${r.variants_count} motor/şanzıman`
                    : "Motor verisi hazırlanıyor"}
                </span>
                <span style={{ color: "var(--accent)", fontSize: "0.85rem", fontWeight: 700 }}>
                  İncele & İlanlar →
                </span>
              </div>
            </Link>
          );
        })}
      </div>
    </>
  );
}
