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

// Türkçe karakter normalizasyonu
function normalizeTr(s: string): string {
  const map: Record<string, string> = {
    ç: "c", ğ: "g", ı: "i", ö: "o", ş: "s", ü: "u",
    Ç: "c", Ğ: "g", İ: "i", I: "i", Ö: "o", Ş: "s", Ü: "u",
  };
  return s
    .split("")
    .map((ch) => map[ch] ?? ch)
    .join("")
    .toLowerCase()
    .trim();
}

// Levenshtein mesafesi (yazım hatası tahmini için)
function levenshtein(a: string, b: string): number {
  const m = a.length;
  const n = b.length;
  const dp: number[][] = Array.from({ length: m + 1 }, () => Array(n + 1).fill(0));
  for (let i = 0; i <= m; i++) dp[i][0] = i;
  for (let j = 0; j <= n; j++) dp[0][j] = j;
  for (let i = 1; i <= m; i++) {
    for (let j = 1; j <= n; j++) {
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      dp[i][j] = Math.min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost);
    }
  }
  return dp[m][n];
}

// Bilinen popüler fonetik yazım yanlışları -> Önerilen doğrular
const PHONETIC_SUGGESTIONS: Record<string, string[]> = {
  "civik": ["Honda Civic"],
  "sivik": ["Honda Civic"],
  "civi": ["Honda Civic"],
  "sity": ["Honda City"],
  "siti": ["Honda City"],
  "ford kuma": ["Ford Puma", "Ford Kuga"],
  "kuma": ["Ford Puma", "Ford Kuga"],
  "kuga": ["Ford Puma"],
  "puna": ["Ford Puma"],
  "megan": ["Renault Megane"],
  "pasat": ["Volkswagen Passat"],
  "korola": ["Toyota Corolla"],
  "korolla": ["Toyota Corolla"],
  "corola": ["Toyota Corolla"],
  "fokus": ["Ford Focus"],
  "foküs": ["Ford Focus"],
  "egeya": ["Fiat Egea"],
  "dastır": ["Dacia Duster"],
  "tuson": ["Hyundai Tucson"],
  "tukson": ["Hyundai Tucson"],
  "kaşkai": ["Renault Kadjar", "Renault Austral"],
  "qashqai": ["Renault Kadjar", "Renault Austral"],
  "oktavya": ["Skoda Octavia"],
  "oktavia": ["Skoda Octavia"],
  "süperb": ["Skoda Superb"],
  "superp": ["Skoda Superb"],
  "pejo": ["Peugeot 3008", "Peugeot 208", "Peugeot 301"],
  "pöjo": ["Peugeot 3008", "Peugeot 208"],
  "reno": ["Renault Megane", "Renault Clio"],
  "vosvogen": ["Volkswagen Passat", "Volkswagen Golf"],
  "hundai": ["Hyundai i20", "Hyundai Tucson"],
  "sportaj": ["Kia Sportage"],
  "kliyo": ["Renault Clio"],
  "klio": ["Renault Clio"],
  "talyant": ["Renault Taliant"],
  "kacar": ["Renault Kadjar"],
};

const POPULAR_COMPARISONS = [
  {
    title: "Fiat Egea vs Renault Megane",
    subtitle: "Türkiye'nin en çok satan iki C-Sedan modeli karşı karşıya",
    c1: "Egea Sedan",
    c2: "Megane 4 Sedan",
    badge: "En Popüler",
  },
  {
    title: "VW Golf vs Ford Focus",
    subtitle: "Alman konforu ve yol tutuş efsanesinin düellosu",
    c1: "Golf 7",
    c2: "Focus 4",
    badge: "Sürüş & Konfor",
  },
  {
    title: "Honda Civic vs Toyota Corolla",
    subtitle: "Japon sorunsuzluğu, atmosferik/turbo motor ve ikinci el kıyaslaması",
    c1: "Civic FC5",
    c2: "Corolla E210",
    badge: "Japon Düellosu",
  },
  {
    title: "Peugeot 3008 vs Hyundai Tucson",
    subtitle: "C-SUV segmentinin en gözde iki aile aracının kapışması",
    c1: "3008",
    c2: "Tucson",
    badge: "SUV Karşılaştırma",
  },
  {
    title: "VW Passat vs Skoda Superb",
    subtitle: "D-Segment makam ve geniş aile konforunda zirve yarışı",
    c1: "Passat B8",
    c2: "Superb",
    badge: "D-Segment Zirvesi",
  },
  {
    title: "Renault Clio vs Hyundai i20",
    subtitle: "Şehir içi pratiklik, yakıt ekonomisi ve kronik sağlamlık",
    c1: "Clio 5",
    c2: "i20",
    badge: "Şehir İçi B-HB",
  },
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
  const [allCatalog, setAllCatalog] = useState<SearchResult[]>([]);
  const [error, setError] = useState("");
  const [isMobileDrawerOpen, setIsMobileDrawerOpen] = useState(false);

  // Katalog verisini arka planda çek (Öne Çıkan En Yüksek Puanlı 3 Araç + "Bunu mu demek istediniz?" tahmin motoru için)
  useEffect(() => {
    api<SearchResult[]>("/vehicles/search")
      .then((data) => setAllCatalog(data))
      .catch(() => {});
  }, []);

  // Puanı en yüksek 3 araba ("Öne Çıkan / Güvenilir Araçlar")
  const topFeaturedCars = useMemo(() => {
    if (!allCatalog.length) return [];
    return [...allCatalog]
      .sort((a, b) => (b.comfort_score ?? 0) - (a.comfort_score ?? 0))
      .slice(0, 3);
  }, [allCatalog]);

  // "Bunu mu demek istediniz?" akıllı tahmin hesaplayıcı
  const didYouMeanSuggestions = useMemo(() => {
    const raw = searchQuery.trim();
    if (raw.length < 2) return [];
    const qNorm = normalizeTr(raw);

    // Eğer tam eşleşme varsa öneriye gerek yok
    const hasExactSubstring = allCatalog.some((c) => {
      const full = normalizeTr(`${c.brand} ${c.name}`);
      return full.includes(qNorm);
    });

    const suggestions = new Set<string>();

    // 1. Özel fonetik sözlük kontrolü ("civik", "sity", "ford kuma" vb.)
    if (PHONETIC_SUGGESTIONS[qNorm]) {
      PHONETIC_SUGGESTIONS[qNorm].forEach((s) => suggestions.add(s));
    }
    for (const token of qNorm.split(/\s+/)) {
      if (PHONETIC_SUGGESTIONS[token]) {
        PHONETIC_SUGGESTIONS[token].forEach((s) => suggestions.add(s));
      }
    }

    // 2. Katalogdaki marka ve modeller üzerinde Levenshtein benzerlik taraması
    if (!hasExactSubstring && allCatalog.length > 0) {
      const qTokens = qNorm.split(/\s+/);
      const scored: { label: string; dist: number }[] = [];

      for (const car of allCatalog) {
        const bNorm = normalizeTr(car.brand);
        const mNorm = normalizeTr(car.name);
        const mFirstWord = mNorm.split(/\s+/)[0];
        const candidates = [mFirstWord, bNorm, `${bNorm} ${mFirstWord}`];

        for (const cand of candidates) {
          for (const qt of [qNorm, ...qTokens]) {
            if (qt.length < 3) continue;
            const d = levenshtein(qt, cand);
            const maxAllowed = qt.length <= 4 ? 1 : 2;
            if (d > 0 && d <= maxAllowed) {
              scored.push({ label: `${car.brand} ${car.name}`, dist: d });
            }
          }
        }
      }

      scored
        .sort((a, b) => a.dist - b.dist)
        .slice(0, 3)
        .forEach((item) => suggestions.add(item.label));
    }

    return Array.from(suggestions).slice(0, 3);
  }, [searchQuery, allCatalog]);

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

  // Son açılan aramanın anahtarı (Aynı filtrelerle tekrar "Araçları Listele"ye basınca kapanması için)
  const [lastExecutedKey, setLastExecutedKey] = useState<string | null>(null);

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
    setLastExecutedKey(null);
  };

  async function executeSearch(overrideQuery?: string) {
    setError("");
    const qToUse = overrideQuery !== undefined ? overrideQuery : searchQuery;

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
    if (qToUse.trim()) queryParams.q = qToUse.trim();
    if (yearMin) queryParams.year_min = yearMin;
    if (yearMax) queryParams.year_max = yearMax;

    const currentKey = JSON.stringify(queryParams);

    try {
      const data = await api<SearchResult[]>("/vehicles/search", queryParams);
      setResults(data);
      setLastExecutedKey(currentKey);
      setIsMobileDrawerOpen(false);
    } catch (err: any) {
      setError(err?.message || "Bir hata oluştu.");
      setResults(null);
    }
  }

  // Kullanıcı İsteği 1: "Araçları Listele"ye basınca açılsın, bir daha basınca kapansın (Toggle)
  const handleToggleList = (e: React.FormEvent) => {
    e.preventDefault();
    const queryParams: Record<string, string> = { ...f };
    if (searchQuery.trim()) queryParams.q = searchQuery.trim();
    if (yearMin) queryParams.year_min = yearMin;
    if (yearMax) queryParams.year_max = yearMax;
    const currentKey = JSON.stringify(queryParams);

    // Eğer liste zaten açıksa ve filtreler değişmediyse listeyi kapat
    if (results !== null && lastExecutedKey === currentKey) {
      setResults(null);
      setLastExecutedKey(null);
      return;
    }

    executeSearch();
  };

  // Önerilen kelimeye ("Bunu mu demek istediniz?") tıklanınca otomatik arama yap
  const applySuggestion = (suggestedText: string) => {
    // Eğer "Ford Kuga" gibi katalogda Puma karşılığı olan bir öneriyse veya doğrudan modelse
    const queryForApi = suggestedText.toLowerCase().includes("kuga") ? "Ford Puma" : suggestedText;
    setSearchQuery(suggestedText);
    executeSearch(queryForApi);
  };

  const isListOpenWithSameFilters = useMemo(() => {
    if (results === null) return false;
    const queryParams: Record<string, string> = { ...f };
    if (searchQuery.trim()) queryParams.q = searchQuery.trim();
    if (yearMin) queryParams.year_min = yearMin;
    if (yearMax) queryParams.year_max = yearMax;
    return lastExecutedKey === JSON.stringify(queryParams);
  }, [results, lastExecutedKey, f, searchQuery, yearMin, yearMax]);

  // Filtreleme formu (En üstte serbest Marka/Model Arama kutusu + Akıllı Tahmin Önerisi)
  const FilterInputs = (
    <>
      <div style={{ gridColumn: "1 / -1", marginBottom: 4 }}>
        <label style={{ fontSize: "0.95rem", fontWeight: 700, color: "var(--text)" }}>
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
              border: "2px solid var(--border)",
              borderRadius: "10px",
              marginTop: 4,
            }}
          />
        </label>

        {/* Bunu mu demek istediniz? (Akıllı Tahmin Kutusu) */}
        {didYouMeanSuggestions.length > 0 && (
          <div
            style={{
              marginTop: 8,
              padding: "8px 12px",
              background: "var(--accent-light)",
              border: "1px solid var(--border)",
              borderRadius: "8px",
              display: "flex",
              alignItems: "center",
              flexWrap: "wrap",
              gap: 8,
              fontSize: "0.88rem",
            }}
          >
            <span style={{ color: "var(--muted)", fontWeight: 600 }}>
              💡 Bunu mu demek istediniz:
            </span>
            {didYouMeanSuggestions.map((sug) => (
              <button
                key={sug}
                type="button"
                onClick={() => applySuggestion(sug)}
                style={{
                  background: "var(--accent)",
                  color: "#ffffff",
                  border: "none",
                  borderRadius: "999px",
                  padding: "4px 12px",
                  fontSize: "0.82rem",
                  fontWeight: 700,
                  cursor: "pointer",
                }}
              >
                {sug} ↗
              </button>
            ))}
          </div>
        )}
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
        <h1 style={{ fontSize: "1.9rem", marginBottom: 6, color: "var(--text)" }}>
          Hangi aracı almalı? Önce kronik arızalarını ve konforunu gör.
        </h1>
        <p className="muted" style={{ margin: 0, fontSize: "0.95rem" }}>
          Türkiye pazarındaki 50 popüler aracın motor & şanzıman kronik arızaları, gerçekçi konfor göstergesi ve güncel ilan filtreleri.
        </p>
      </div>

      {/* Masaüstü Filtre Formu */}
      <form className="filters card desktop-filters" onSubmit={handleToggleList}>
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
          <button
            type="submit"
            style={{
              height: "44px",
              minWidth: "155px",
              fontWeight: 700,
              background: isListOpenWithSameFilters ? "#475569" : "var(--accent)",
            }}
          >
            {isListOpenWithSameFilters ? "Listeyi Kapat ▲" : "Araçları Listele ▼"}
          </button>
          <Link
            href="/compare"
            className="nav-link-compare"
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
              background: "var(--accent)",
              color: "#ffffff",
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

            <div className="bottom-sheet-body">{FilterInputs}</div>

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
                  onClick={() => {
                    if (isListOpenWithSameFilters) {
                      setResults(null);
                      setLastExecutedKey(null);
                      setIsMobileDrawerOpen(false);
                    } else {
                      executeSearch();
                    }
                  }}
                  style={{
                    flex: 2,
                    background: "var(--accent)",
                    color: "#ffffff",
                    height: "44px",
                    fontWeight: 800,
                  }}
                >
                  {isListOpenWithSameFilters ? "Listeyi Kapat" : "Araçları Listele"}
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

      {/* Sonuç Yok Uyarısı */}
      {results !== null && results.length === 0 && (
        <div className="card muted" style={{ textAlign: "center", padding: "2.5rem 1rem", marginBottom: 24 }}>
          <div style={{ fontSize: "2rem", marginBottom: 8 }}>🚗💨</div>
          <strong style={{ color: "var(--text)" }}>Belirtilen kriterlere uygun araç bulunamadı.</strong>
          <p className="small" style={{ margin: "6px 0 0" }}>
            Lütfen arama kelimenizi veya filtrelerinizi genişleterek tekrar deneyin.
          </p>
        </div>
      )}

      {/* AÇILIR/KAPANIR ARAÇ LİSTESİ (Araçları Listele'ye basıldığında açılır, tekrar basınca kapanır) */}
      {results !== null && results.length > 0 && (
        <div style={{ marginBottom: 36 }}>
          <div
            style={{
              display: "flex",
              justifyContent: "space-between",
              alignItems: "center",
              marginBottom: 14,
              flexWrap: "wrap",
              gap: 10,
            }}
          >
            <strong style={{ fontSize: "1.1rem", color: "var(--text)" }}>
              📋 Listelenen Araçlar ({results.length} Model)
            </strong>
            <button
              type="button"
              onClick={() => {
                setResults(null);
                setLastExecutedKey(null);
              }}
              style={{
                background: "transparent",
                color: "var(--muted)",
                border: "1px solid var(--border)",
                padding: "6px 14px",
                fontSize: "0.85rem",
                fontWeight: 700,
              }}
            >
              ✕ Listeyi Kapat
            </button>
          </div>

          <div className="grid">
            {results.map((r) => {
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
                    gap: 10,
                    border: "1px solid var(--border)",
                    textAlign: "center",
                    padding: "20px 20px 16px 20px",
                    transition: "transform 0.15s, box-shadow 0.15s",
                  }}
                >
                  {/* Üst Başlık: Marka Model - Puan + Kasa Tipi · Yıl */}
                  <div>
                    <div style={{ fontSize: "1.15rem", fontWeight: 800, color: "var(--text)" }}>
                      {r.brand} {r.name}{" "}
                      {r.comfort_score !== null && (
                        <span style={{ fontWeight: 700, color: "var(--accent)" }}>
                          - {r.comfort_score.toFixed(1)}/10
                        </span>
                      )}
                    </div>
                    <div className="muted small" style={{ marginTop: 4 }}>
                      {BODY_TYPE_LABEL[r.body_type] ?? r.body_type} · {r.year_start}–
                      {r.year_end ?? "devam"}
                    </div>
                  </div>

                  {/* Orta Kısım: Puana Göre Doluluk Oranlı Mavi Yarım Daire + Marka Logosu */}
                  <div style={{ margin: "4px auto" }}>
                    <ScoreGauge
                      score={r.comfort_score ?? 7.5}
                      brand={r.brand}
                      size="md"
                      showScoreText={false}
                    />
                  </div>

                  {/* Alt Çizgi: Sol tarafta X motor/şanzıman, Sağ tarafta İncele & İlanlar -> */}
                  <div
                    className="row"
                    style={{
                      borderTop: "1px solid var(--border)",
                      paddingTop: 12,
                      marginTop: 4,
                    }}
                  >
                    <span className="small muted">
                      {r.variants_count > 0
                        ? `${r.variants_count} motor/şanzıman`
                        : "Motor verisi hazırlanıyor"}
                    </span>
                    <span style={{ color: "var(--accent)", fontSize: "0.88rem", fontWeight: 800 }}>
                      İncele & İlanlar →
                    </span>
                  </div>
                </Link>
              );
            })}
          </div>
        </div>
      )}

      {/* ANA GİRİŞ EKRANI VİTRİNİ: 1. Öne Çıkan / Güvenilir Araçlar (Ekranı 3'e Bölen En Yüksek Puanlı 3 Araba) */}
      <section style={{ marginTop: 12, marginBottom: 36 }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 14, flexWrap: "wrap", gap: 8 }}>
          <div>
            <h2 style={{ fontSize: "1.4rem", fontWeight: 800, margin: 0, color: "var(--text)" }}>
              🏆 Öne Çıkan / Güvenilir Araçlar
            </h2>
            <p className="muted small" style={{ margin: "2px 0 0 0" }}>
              Konfor, yalıtım ve uzun ömürlülük puanı en yüksek 3 model — motor ve kronik arıza analizi için araca tıklayın.
            </p>
          </div>
        </div>

        <div className="featured-3-grid">
          {topFeaturedCars.map((car) => (
            <Link
              key={car.id}
              href={`/model/${car.id}`}
              className="card"
              style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
                gap: 10,
                border: "1px solid var(--border)",
                textAlign: "center",
                padding: "20px 20px 16px 20px",
                transition: "transform 0.15s, box-shadow 0.15s",
              }}
            >
              {/* Üst Başlık: Marka Model - Puan + Kasa Tipi · Yıl */}
              <div>
                <div style={{ fontSize: "1.18rem", fontWeight: 800, color: "var(--text)" }}>
                  {car.brand} {car.name}{" "}
                  {car.comfort_score !== null && (
                    <span style={{ fontWeight: 700, color: "var(--accent)" }}>
                      - {car.comfort_score.toFixed(1)}/10
                    </span>
                  )}
                </div>
                <div className="muted small" style={{ marginTop: 4 }}>
                  {BODY_TYPE_LABEL[car.body_type] ?? car.body_type} · {car.year_start}–
                  {car.year_end ?? "devam"}
                </div>
              </div>

              {/* Orta Kısım: Puana Göre Doluluk Oranlı Mavi Yarım Daire + Marka Logosu */}
              <div style={{ margin: "4px auto" }}>
                <ScoreGauge
                  score={car.comfort_score ?? 8.0}
                  brand={car.brand}
                  size="md"
                  showScoreText={false}
                />
              </div>

              {/* Alt Çizgi: Sol tarafta X motor/şanzıman, Sağ tarafta İncele & İlanlar -> */}
              <div
                className="row"
                style={{
                  borderTop: "1px solid var(--border)",
                  paddingTop: 12,
                  marginTop: 4,
                }}
              >
                <span className="small muted">
                  {car.variants_count > 0
                    ? `${car.variants_count} motor/şanzıman`
                    : "Motor verisi hazırlanıyor"}
                </span>
                <span style={{ color: "var(--accent)", fontSize: "0.88rem", fontWeight: 800 }}>
                  İncele & İlanlar →
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* ANA GİRİŞ EKRANI VİTRİNİ: 2. Popüler Karşılaştırmalar */}
      <section style={{ marginBottom: 24 }}>
        <div style={{ marginBottom: 14 }}>
          <h2 style={{ fontSize: "1.4rem", fontWeight: 800, margin: 0, color: "var(--text)" }}>
            ⚔️ Popüler Karşılaştırmalar
          </h2>
          <p className="muted small" style={{ margin: "2px 0 0 0" }}>
            Türkiye pazarında en çok arada kalınan rakipler — tek tıkla yan yana teknik veri, donanım ve konfor kıyaslamasını açın.
          </p>
        </div>

        <div className="featured-3-grid">
          {POPULAR_COMPARISONS.map((item, idx) => (
            <Link
              key={idx}
              href={`/compare?c1=${encodeURIComponent(item.c1)}&c2=${encodeURIComponent(item.c2)}`}
              className="card"
              style={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "space-between",
                gap: 10,
                border: "1px solid var(--border)",
                transition: "transform 0.15s ease, border-color 0.15s ease",
              }}
            >
              <div>
                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 8 }}>
                  <span
                    style={{
                      fontSize: "0.75rem",
                      fontWeight: 800,
                      padding: "3px 10px",
                      borderRadius: "999px",
                      background: "var(--accent-light)",
                      color: "var(--accent)",
                    }}
                  >
                    ⚖️ {item.badge}
                  </span>
                  <span style={{ fontSize: "0.8rem", fontWeight: 700, color: "var(--muted)" }}>
                    VS
                  </span>
                </div>
                <strong style={{ fontSize: "1.12rem", display: "block", color: "var(--text)", marginBottom: 4 }}>
                  {item.title}
                </strong>
                <p className="muted small" style={{ margin: 0, lineHeight: 1.4 }}>
                  {item.subtitle}
                </p>
              </div>

              <div
                style={{
                  borderTop: "1px solid var(--border)",
                  paddingTop: 10,
                  display: "flex",
                  justifyContent: "space-between",
                  alignItems: "center",
                }}
              >
                <span className="small muted">Teknik & Kronik Kıyaslama</span>
                <span style={{ color: "var(--accent)", fontWeight: 800, fontSize: "0.88rem" }}>
                  Karşılaştırmayı Aç →
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>
    </>
  );
}
