"use client";
import Link from "next/link";
import { useParams, useSearchParams } from "next/navigation";
import { useEffect, useState, useMemo, Suspense } from "react";
import {
  api,
  BODY_TYPE_LABEL,
  FUEL_TYPE_LABEL,
  tl,
  TrimPackage,
  ListingUrls,
} from "@/lib/api";
import { buildSahibindenUrl, buildArabamUrl, FilterParams } from "@/lib/listingUrl";
import { getSingleCarPhoto } from "@/lib/singleCarPhotos";
import ScoreGauge from "@/components/ScoreGauge";

type Variant = {
  id: string;
  engine: string;
  fuel_type: string;
  transmission: string;
  year_start: number;
  year_end: number | null;
  used_price_tl: number | null;
};

type ModelDetailResponse = {
  id: string;
  brand: string;
  name: string;
  body_type: string;
  year_start: number;
  year_end: number | null;
  comfort_score: number | null;
  variants: Variant[];
  trim_packages: TrimPackage[];
  listing_urls: ListingUrls;
};

function ModelDetailContent() {
  const { id } = useParams<{ id: string }>();
  const searchParams = useSearchParams();

  const [model, setModel] = useState<ModelDetailResponse | null>(null);
  const [error, setError] = useState("");

  const currentFilters: FilterParams = useMemo(() => {
    return {
      year_min: searchParams.get("year_min"),
      year_max: searchParams.get("year_max"),
      budget_max: searchParams.get("budget_max"),
      km_min: searchParams.get("km_min"),
      km_max: searchParams.get("km_max"),
      fuel_type: searchParams.get("fuel_type"),
      transmission_type: searchParams.get("transmission_type"),
      body_type: searchParams.get("body_type"),
    };
  }, [searchParams]);

  const filterQueryString = searchParams.toString();

  useEffect(() => {
    api<ModelDetailResponse>(`/models/${id}`)
      .then(setModel)
      .catch((e) => setError(String(e)));
  }, [id]);

  if (error) return <div className="card">{error}</div>;
  if (!model) return <p className="muted" style={{ padding: 20 }}>Yükleniyor…</p>;

  // Sahibinden ve Arabam arama URL'leri (asla 404 vermez)
  const searchKeyword = `${model.brand} ${model.name}`;
  const sahibindenUrl = buildSahibindenUrl(searchKeyword, currentFilters);
  const arabamUrl = buildArabamUrl(searchKeyword, currentFilters);
  const carPhoto = getSingleCarPhoto(model.name, model.brand);

  // Aktif filtreler
  const activeBadges: string[] = [];
  if (currentFilters.year_min || currentFilters.year_max) {
    activeBadges.push(`Yıl: ${currentFilters.year_min ?? ""}–${currentFilters.year_max ?? ""}`);
  }
  if (currentFilters.budget_max) {
    activeBadges.push(`Maks: ${Number(currentFilters.budget_max).toLocaleString("tr-TR")} TL`);
  }
  if (currentFilters.km_min || currentFilters.km_max) {
    activeBadges.push(`KM: ${currentFilters.km_min ?? "0"}–${currentFilters.km_max ?? "Maks"}`);
  }
  if (currentFilters.fuel_type) {
    activeBadges.push(FUEL_TYPE_LABEL[currentFilters.fuel_type] ?? currentFilters.fuel_type);
  }
  if (currentFilters.transmission_type) {
    activeBadges.push(currentFilters.transmission_type.toUpperCase());
  }

  return (
    <>
      <Link href={filterQueryString ? `/?${filterQueryString}` : "/"} className="muted" style={{ fontWeight: 600 }}>
        ← Filtrelere dön
      </Link>

      <div className="row" style={{ marginTop: 14, alignItems: "center" }}>
        <div>
          <h1 style={{ margin: "4px 0", fontSize: "2rem", color: "var(--text)" }}>
            {model.brand} {model.name}
          </h1>
          <p className="muted" style={{ margin: 0, fontSize: "0.95rem" }}>
            {BODY_TYPE_LABEL[model.body_type] ?? model.body_type} · {model.year_start}–
            {model.year_end ?? "devam"}
          </p>
        </div>

        {/* Mavi Doluluk Oranlı & Marka Logolu Konfor Göstergesi */}
        {model.comfort_score !== null && (
          <div className="card" style={{ padding: "12px 20px" }}>
            <ScoreGauge
              score={model.comfort_score}
              brand={model.brand}
              size="md"
              label="Model Konfor Puanı"
              showTicks={true}
            />
          </div>
        )}
      </div>

      {/* MODEL RESMİ TEK FOTOĞRAF KARTI */}
      <div className="card" style={{ marginTop: 20, border: "1px solid var(--border)", overflow: "hidden", padding: 0 }}>
        <div style={{ display: "grid", gridTemplateColumns: "minmax(280px, 380px) 1fr", gap: 0, alignItems: "stretch" }}>
          <div style={{ background: "#ffffff", borderRight: "1px solid var(--border)", position: "relative", minHeight: 220, display: "flex", alignItems: "center", justifyContent: "center", padding: 12 }}>
            {carPhoto.photoUrl ? (
              <img
                src={carPhoto.photoUrl}
                alt={`${model.brand} ${model.name}`}
                style={{ width: "100%", height: "100%", maxHeight: 240, objectFit: "contain", display: "block" }}
                loading="eager"
                onError={(e) => {
                  const parent = (e.target as HTMLElement).parentElement;
                  if (parent) {
                    parent.innerHTML = `
                      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;text-align:center;color:#64748b;">
                        <span style="font-size:3rem;margin-bottom:8px;">🚗</span>
                        <span style="font-weight:600;font-size:0.95rem;color:#334155;">${model.brand} ${model.name}</span>
                        <a href="${carPhoto.googleSearchUrl}" target="_blank" rel="noopener noreferrer" style="margin-top:10px;font-size:0.8rem;color:#2563eb;text-decoration:none;font-weight:600;">Google'da Fotoğrafları Gör ↗</a>
                      </div>
                    `;
                  }
                }}
              />
            ) : (
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: 24, textAlign: "center", color: "#64748b" }}>
                <span style={{ fontSize: "3rem", marginBottom: 8 }}>🚗</span>
                <span style={{ fontWeight: 600, fontSize: "0.95rem", color: "#334155" }}>{model.brand} {model.name}</span>
                <a href={carPhoto.googleSearchUrl} target="_blank" rel="noopener noreferrer" style={{ marginTop: 10, fontSize: "0.8rem", color: "#2563eb", textDecoration: "none", fontWeight: 600 }}>Google'da Fotoğrafları Gör ↗</a>
              </div>
            )}
          </div>

          <div style={{ padding: "20px 24px", display: "flex", flexDirection: "column", justifyContent: "space-between", gap: 14 }}>
            <div>
              <div style={{ display: "flex", gap: 8, alignItems: "center", marginBottom: 6 }}>
                <span className="badge" style={{ background: "var(--accent-light)", color: "var(--accent)" }}>
                  {BODY_TYPE_LABEL[model.body_type] ?? model.body_type}
                </span>
                <span className="badge" style={{ background: "var(--card-alt)", color: "var(--text-secondary)", border: "1px solid var(--border)" }}>
                  {model.year_start}–{model.year_end ?? "devam"}
                </span>
              </div>
              <h3 style={{ fontSize: "1.4rem", margin: 0, color: "var(--text)" }}>
                {model.brand} {model.name}
              </h3>
              <p className="small muted" style={{ margin: "6px 0 0", lineHeight: 1.5 }}>
                Bu model için motor & şanzıman kronik arızaları, donanım paketleri ve canlı ekspertiz kontrol noktaları aşağıda derlenmiştir.
              </p>
            </div>

            <div style={{ display: "flex", gap: 10, flexWrap: "wrap", alignItems: "center" }}>
              <Link
                href={`/ekspertiz?brand=${encodeURIComponent(model.brand)}&model=${encodeURIComponent(model.name)}`}
                style={{
                  fontSize: "0.85rem",
                  fontWeight: 700,
                  color: "#166534",
                  background: "#f0fdf4",
                  border: "1px solid #bbf7d0",
                  padding: "8px 14px",
                  borderRadius: 8,
                  textDecoration: "none",
                }}
              >
                🛡️ Ekspertiz Karnesi Çıkar ↗
              </Link>
              <a
                href={carPhoto.sikayetvarSearchUrl}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  fontSize: "0.85rem",
                  fontWeight: 700,
                  color: "#ea580c",
                  background: "#fff7ed",
                  border: "1px solid #fed7aa",
                  padding: "8px 14px",
                  borderRadius: 8,
                  textDecoration: "none",
                }}
              >
                📢 Şikayetvar İncelemeleri ↗
              </a>
              <a
                href={carPhoto.googleSearchUrl}
                target="_blank"
                rel="noopener noreferrer"
                style={{
                  fontSize: "0.85rem",
                  fontWeight: 700,
                  color: "#2563eb",
                  background: "#eff6ff",
                  border: "1px solid #bfdbfe",
                  padding: "8px 14px",
                  borderRadius: 8,
                  textDecoration: "none",
                }}
              >
                🔍 Google Görseller ↗
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* Donanım Paketleri Özeti */}
      {model.trim_packages && model.trim_packages.length > 0 && (
        <div style={{ marginTop: 24 }}>
          <h2 style={{ fontSize: "1.3rem" }}>Donanım Paketleri & Öne Çıkan Özellikler</h2>
          <div className="grid">
            {model.trim_packages.map((tp, idx) => {
              const levelBadge =
                tp.level === "premium" ? (
                  <span className="badge yuksek">Premium / En Dolu</span>
                ) : tp.level === "orta" ? (
                  <span className="badge orta">Orta / Konfor</span>
                ) : (
                  <span className="badge dusuk">Giriş / Ekonomik</span>
                );

              return (
                <div key={tp.id || idx} className="card">
                  <div className="row" style={{ marginBottom: 6 }}>
                    <strong style={{ fontSize: "1.05rem" }}>{tp.name}</strong>
                    {levelBadge}
                  </div>
                  {tp.summary && <p className="muted small" style={{ margin: "4px 0 10px" }}>{tp.summary}</p>}
                  <div>
                    {tp.features?.map((feat, fIdx) => (
                      <span key={fIdx} className="feature-chip">
                        ✓ {feat}
                      </span>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>

          {/* Model yılına göre değişiklikler uyarısı */}
          <p style={{ fontSize: "0.8rem", color: "var(--muted)", marginTop: 14, fontWeight: 500 }}>
            * Modelin yılına göre değişiklikler olabilir.
          </p>
        </div>
      )}

      {/* Motor & Şanzıman Seçenekleri */}
      <h2 style={{ marginTop: 32, fontSize: "1.3rem" }}>Motor ve Şanzıman Seçenekleri</h2>
      <p className="muted small" style={{ marginTop: -8, marginBottom: 12 }}>
        Kronik arızaları, fotoğraflı analizleri, usta notlarını ve yazılım/tuning durumunu görmek için kombinasyon seçin:
      </p>

      <div className="stack">
        {model.variants.map((v) => {
          const variantUrl = filterQueryString
            ? `/variant/${v.id}?${filterQueryString}`
            : `/variant/${v.id}`;

          return (
            <Link
              key={v.id}
              href={variantUrl}
              className="card row"
              style={{
                transition: "transform 0.15s, box-shadow 0.15s",
                border: "1px solid var(--border)",
              }}
            >
              <div>
                <strong style={{ fontSize: "1.05rem", color: "var(--text)" }}>{v.engine}</strong> + {v.transmission}
                <div className="muted small" style={{ marginTop: 4 }}>
                  {FUEL_TYPE_LABEL[v.fuel_type] ?? v.fuel_type} · {v.year_start}–
                  {v.year_end ?? "devam"}
                  {v.used_price_tl ? ` · ~${tl(v.used_price_tl)}` : ""}
                </div>
              </div>
              <div style={{ color: "var(--accent)", fontWeight: 700, fontSize: "0.95rem" }}>
                Arızaları ve Özellikleri Gör →
              </div>
            </Link>
          );
        })}
      </div>

      {/* GÜNCEL PİYASA İLANLARI (EN ALTA TAŞINDI) */}
      <div className="card" style={{ marginTop: 36, border: "2px solid var(--border)" }}>
        <div style={{ fontWeight: 800, marginBottom: 6, fontSize: "1.15rem", color: "var(--text)" }}>
          🚗 Güncel Canlı İlanlar: {model.brand} {model.name} İlanlarını Nerede İncelemek İstersiniz?
        </div>
        <p className="muted small" style={{ marginBottom: 12 }}>
          Bu model için belirlediğiniz tüm filtreler (yıl, bütçe, km, yakıt) seçtiğiniz platformda otomatik filtrelenecektir:
        </p>

        {activeBadges.length > 0 && (
          <div style={{ display: "flex", gap: 6, flexWrap: "wrap", marginBottom: 14 }}>
            <span className="small muted" style={{ alignSelf: "center", fontWeight: 600 }}>Uygulanan Filtreler:</span>
            {activeBadges.map((badge, idx) => (
              <span
                key={idx}
                style={{
                  background: "#eff6ff",
                  color: "#1d4ed8",
                  border: "1px solid #bfdbfe",
                  borderRadius: "6px",
                  padding: "3px 8px",
                  fontSize: "0.8rem",
                  fontWeight: 600,
                }}
              >
                ✓ {badge}
              </span>
            ))}
          </div>
        )}

        <div style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
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

export default function ModelPage() {
  return (
    <Suspense fallback={<p className="muted" style={{ padding: 20 }}>Sayfa yükleniyor...</p>}>
      <ModelDetailContent />
    </Suspense>
  );
}
