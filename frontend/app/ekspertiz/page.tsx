"use client";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { useState, useEffect, useMemo, Suspense } from "react";
import { api, formatThousand, parseThousand } from "@/lib/api";
import { getModelExpertProfile } from "@/lib/expertAdvisorData";

interface VariantItem {
  id: string;
  engine_label: string;
  transmission_type: string;
  fuel_type: string;
  power_hp: number;
}

interface ModelItem {
  id: string;
  name: string;
  body_type: string;
  year_start: number;
  year_end: number | null;
  variants: VariantItem[];
}

interface BrandTreeItem {
  brand_id: string;
  brand_name: string;
  models: ModelItem[];
}

function EkspertizContent() {
  const searchParams = useSearchParams();
  const initBrand = searchParams.get("brand") || "";
  const initModel = searchParams.get("model") || "";

  const [tree, setTree] = useState<BrandTreeItem[]>([]);
  const [loading, setLoading] = useState(true);

  // Form alanları
  const [selectedBrand, setSelectedBrand] = useState(initBrand);
  const [selectedModel, setSelectedModel] = useState(initModel);
  const [year, setYear] = useState("2018");
  const [kmDisplay, setKmDisplay] = useState("95.000");
  const [km, setKm] = useState("95000");
  const [transmission, setTransmission] = useState("otomatik");
  const [fuelType, setFuelType] = useState("dizel");
  const [priceDisplay, setPriceDisplay] = useState("950.000");
  const [listingUrl, setListingUrl] = useState("");

  // Rapor üretildi mi?
  const [reportGenerated, setReportGenerated] = useState(false);
  const [checkedItems, setCheckedItems] = useState<Record<string, boolean>>({});

  useEffect(() => {
    api<BrandTreeItem[]>("/comparison-tree")
      .then((data) => {
        setTree(data);
        setLoading(false);

        // Parametre ile geldiyse otomatik eşleştir
        if (initBrand) {
          setSelectedBrand(initBrand);
          if (initModel) {
            setSelectedModel(initModel);
            setReportGenerated(true);
          }
        }
      })
      .catch(() => setLoading(false));
  }, [initBrand, initModel]);

  const availableModels = useMemo(() => {
    const b = tree.find((x) => x.brand_name.toLowerCase() === selectedBrand.toLowerCase());
    return b?.models || [];
  }, [tree, selectedBrand]);

  const handleKmChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const raw = parseThousand(e.target.value);
    const fmt = formatThousand(e.target.value);
    setKmDisplay(fmt);
    setKm(raw);
  };

  const handlePriceChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const fmt = formatThousand(e.target.value);
    setPriceDisplay(fmt);
  };

  const handleGenerateReport = (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedBrand || !selectedModel) {
      alert("Lütfen marka ve model seçiniz.");
      return;
    }
    setReportGenerated(true);
  };

  const toggleCheck = (id: string) => {
    setCheckedItems((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  // Modele ve Şanzımana Özel Uzman Profili
  const expertProfile = useMemo(() => {
    return getModelExpertProfile(selectedModel || "Genel Model", selectedBrand || "Genel Marka", transmission);
  }, [selectedModel, selectedBrand, transmission]);

  // Sayısal Değerler
  const kmNum = parseInt(km, 10) || 95000;
  const yearNum = parseInt(year, 10) || 2018;
  const age = 2026 - yearNum;

  // Modele Özel Gerçekçi Kilometre Analizi (Sadece düz 100k kuralı yok, motor karakterine göre!)
  const kmThresholds = expertProfile.kmThresholds;
  let kmStatus = {
    title: "Düşük & İdeal Kilometre",
    color: "#16a34a",
    bg: "#f0fdf4",
    text: `${expertProfile.title} için bu kilometre seviyesi motor ömrü açısından oldukça güvenlidir. Temel sıvı bakımları ve filtre kontrolleri yeterlidir.`,
  };

  if (kmNum >= kmThresholds.heavyMaintenanceAt) {
    kmStatus = {
      title: "Ağır Bakım Eşiğinde",
      color: "#dc2626",
      bg: "#fef2f2",
      text: `DİKKAT: ${expertProfile.title} için ${kmThresholds.chainOrBeltName} periyodu (${kmThresholds.chainOrBeltInterval}) bu kilometre aralığında dolmaktadır. Yetkili servis faturası kontrol edilmeli, yapılmadıysa acil masraf olarak hesaplanmalıdır.`,
    };
  } else if (kmNum >= kmThresholds.lowRiskUpTo) {
    kmStatus = {
      title: "Orta Kilometre (Olağan Aşınma)",
      color: "#d97706",
      bg: "#fffbeb",
      text: `${expertProfile.title} bu kilometrede olağan aşınma periyodundadır. ${expertProfile.engineKeyCheck}`,
    };
  }

  // Dinamik Skor Hesaplama (Modelin temel sağlamlık puanı baz alınır)
  let score = expertProfile.reliabilityScoreBase;
  if (kmNum > kmThresholds.heavyMaintenanceAt) score -= 12;
  else if (kmNum > kmThresholds.lowRiskUpTo) score -= 6;
  if (age > 10) score -= 8;
  else if (age > 6) score -= 4;
  if (transmission === "otomatik" && !expertProfile.title.includes("Toyota")) score -= 3;
  score = Math.max(45, Math.min(98, score));

  return (
    <div style={{ maxWidth: 1040, margin: "0 auto" }}>
      <div style={{ marginBottom: 20 }}>
        <Link href="/" className="muted small" style={{ fontWeight: 600 }}>
          ← Ana Sayfaya Dön
        </Link>
        <h1 style={{ fontSize: "2rem", margin: "6px 0 2px 0", color: "var(--text)", fontWeight: 800 }}>
          🛡️ İlan Analiz & Ekspertiz Danışmanı
        </h1>
        <p className="muted small" style={{ margin: 0 }}>
          Seçtiğiniz modelin <strong>gerçek kronik arızalarına</strong>, <strong>şanzıman tipine</strong> ve <strong>motor ömrüne</strong> göre optimize edilmiş ekspertiz satın alma karnesi:
        </p>
      </div>

      {/* GİRİŞ FORMU */}
      <div className="card" style={{ border: "2px solid var(--border)", marginBottom: 24 }}>
        <h3 style={{ margin: "0 0 14px 0", fontSize: "1.15rem", color: "var(--text)" }}>
          🚗 İncelemek İstediğiniz Aracın Bilgileri
        </h3>

        <form onSubmit={handleGenerateReport} style={{ display: "grid", gap: 14 }}>
          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 14 }}>
            {/* Marka */}
            <label>
              Marka:
              <select
                value={selectedBrand}
                onChange={(e) => {
                  setSelectedBrand(e.target.value);
                  setSelectedModel("");
                }}
                required
              >
                <option value="">-- Marka Seçin --</option>
                {tree.map((b) => (
                  <option key={b.brand_id} value={b.brand_name}>
                    {b.brand_name}
                  </option>
                ))}
              </select>
            </label>

            {/* Model */}
            <label>
              Model:
              <select
                value={selectedModel}
                disabled={!selectedBrand}
                onChange={(e) => setSelectedModel(e.target.value)}
                required
              >
                <option value="">{!selectedBrand ? "Önce Marka Seçin" : "-- Model Seçin --"}</option>
                {availableModels.map((m) => (
                  <option key={m.id} value={m.name}>
                    {m.name} ({m.year_start}–{m.year_end ?? "devam"})
                  </option>
                ))}
              </select>
            </label>

            {/* Model Yılı */}
            <label>
              Model Üretim Yılı:
              <input
                type="number"
                min="1990"
                max="2026"
                value={year}
                onChange={(e) => setYear(e.target.value)}
                required
              />
            </label>

            {/* Kilometre */}
            <label>
              Araç Kilometresi (KM):
              <input
                type="text"
                placeholder="Örn: 95.000"
                value={kmDisplay}
                onChange={handleKmChange}
                required
              />
            </label>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: 14 }}>
            {/* Şanzıman */}
            <label>
              Şanzıman Türü:
              <select value={transmission} onChange={(e) => setTransmission(e.target.value)}>
                <option value="otomatik">Otomatik (EDC / DSG / EAT / CVT vb.)</option>
                <option value="manuel">Manuel</option>
              </select>
            </label>

            {/* Yakıt */}
            <label>
              Yakıt Türü:
              <select value={fuelType} onChange={(e) => setFuelType(e.target.value)}>
                <option value="benzin">Benzin</option>
                <option value="dizel">Dizel</option>
                <option value="hibrit">Hibrit</option>
                <option value="lpg">LPG & Benzin</option>
                <option value="elektrik">Elektrik</option>
              </select>
            </label>

            {/* İlan Fiyatı */}
            <label>
              İlan Fiyatı (TL):
              <input
                type="text"
                placeholder="Örn: 850.000"
                value={priceDisplay}
                onChange={handlePriceChange}
              />
            </label>

            {/* İlan Linki (Opsiyonel) */}
            <label>
              İlan Linki (Sahibinden / Arabam):
              <input
                type="text"
                placeholder="https://... (Opsiyonel)"
                value={listingUrl}
                onChange={(e) => setListingUrl(e.target.value)}
              />
            </label>
          </div>

          <button
            type="submit"
            className="btn"
            style={{
              padding: "12px 28px",
              fontSize: "1.05rem",
              fontWeight: 800,
              justifySelf: "start",
              boxShadow: "0 4px 14px rgba(37, 99, 235, 0.25)",
              cursor: "pointer",
            }}
          >
            📋 Ekspertiz ve Satın Alma Raporu Oluştur →
          </button>
        </form>
      </div>

      {/* RAPOR SONUÇ BÖLÜMÜ */}
      {reportGenerated && (
        <div className="stack" style={{ gap: 20 }}>
          {/* 1. ÖZET GÜVEN KARTI */}
          <div
            className="card"
            style={{
              border: "2px solid var(--accent)",
              borderRadius: 14,
              padding: "20px 24px",
            }}
          >
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: 14 }}>
              <div>
                <span className="small muted" style={{ fontWeight: 700, textTransform: "uppercase" }}>
                  Ekspertiz Satın Alma Karnesi
                </span>
                <h2 style={{ fontSize: "1.6rem", margin: "4px 0", color: "var(--text)" }}>
                  {expertProfile.title} ({year})
                </h2>
                <div style={{ color: "var(--text-secondary)", fontSize: "0.95rem" }}>
                  {Number(kmNum).toLocaleString("tr-TR")} KM · {transmission.toUpperCase()} · {fuelType.toUpperCase()}
                  {priceDisplay && ` · ${priceDisplay} TL İlan Fiyatı`}
                </div>
              </div>

              <div style={{ textAlign: "right" }}>
                <div style={{ fontSize: "0.85rem", color: "var(--muted)", fontWeight: 700 }}>
                  Satın Alma Güven Skoru
                </div>
                <div style={{ fontSize: "2.4rem", fontWeight: 900, color: score >= 80 ? "#16a34a" : score >= 65 ? "#d97706" : "#dc2626", lineHeight: 1.1 }}>
                  {score}<span style={{ fontSize: "1.2rem", color: "var(--muted)" }}>/100</span>
                </div>
                <span
                  style={{
                    display: "inline-block",
                    marginTop: 4,
                    fontSize: "0.8rem",
                    fontWeight: 700,
                    color: score >= 80 ? "#166534" : "#92400e",
                    background: score >= 80 ? "#dcfce7" : "#fef3c7",
                    padding: "2px 8px",
                    borderRadius: 6,
                  }}
                >
                  {score >= 80 ? "✓ Alınabilir Seviyede" : "⚠️ Titiz Kontrol Şart"}
                </span>
              </div>
            </div>

            {/* Modelin Kritik Motor & Şanzıman Özeti */}
            <div style={{ marginTop: 16, paddingTop: 14, borderTop: "1px solid var(--border)", display: "grid", gap: 6, fontSize: "0.9rem" }}>
              <div>
                <strong style={{ color: "var(--text)" }}>🔧 Motor Değerlendirmesi: </strong>
                <span style={{ color: "var(--text-secondary)" }}>{expertProfile.engineKeyCheck}</span>
              </div>
              <div>
                <strong style={{ color: "var(--text)" }}>⚙️ Şanzıman Değerlendirmesi: </strong>
                <span style={{ color: "var(--text-secondary)" }}>{expertProfile.gearboxKeyCheck}</span>
              </div>
            </div>
          </div>

          {/* 2. MODELE ÖZEL KİLOMETRE VE AĞIR BAKIM ALARMI */}
          <div
            className="card"
            style={{
              border: `1px solid ${kmStatus.color}`,
              borderLeft: `6px solid ${kmStatus.color}`,
            }}
          >
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 6 }}>
              <strong style={{ fontSize: "1.1rem", color: kmStatus.color }}>
                ⚠️ Kilometre Analizi: {kmStatus.title}
              </strong>
            </div>
            <p style={{ margin: 0, color: "var(--text)", fontSize: "0.95rem", lineHeight: 1.5 }}>
              {kmStatus.text}
            </p>
          </div>

          {/* 3. İNTERAKTİF VE ŞİKAYETVAR ODAKLI EKSPERTİZ KONTROL LİSTESİ */}
          <div className="card" style={{ border: "1px solid var(--border)" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12, flexWrap: "wrap", gap: 8 }}>
              <div>
                <h3 style={{ margin: 0, fontSize: "1.2rem", color: "var(--text)" }}>
                  📝 {expertProfile.title} Modeline Özel Ekspertiz Kontrol Maddeleri
                </h3>
                <p className="muted small" style={{ margin: "2px 0 0" }}>
                  Ekspertiz istasyonundayken bu maddeleri ustaya özellikle baktırın ve telefonunuzdan onaylayın:
                </p>
              </div>
              <button
                type="button"
                onClick={() => window.print()}
                style={{
                  fontSize: "0.85rem",
                  padding: "6px 14px",
                  borderRadius: 6,
                  background: "var(--card-alt)",
                  color: "var(--text)",
                  border: "1px solid var(--border)",
                  cursor: "pointer",
                  fontWeight: 600,
                }}
              >
                🖨️ Listeyi Yazdır / PDF
              </button>
            </div>

            <div style={{ display: "grid", gap: 12 }}>
              {expertProfile.modelSpecificChecks.map((item) => {
                const isChecked = !!checkedItems[item.id];
                return (
                  <div
                    key={item.id}
                    onClick={() => toggleCheck(item.id)}
                    style={{
                      display: "flex",
                      alignItems: "flex-start",
                      gap: 12,
                      padding: "14px",
                      borderRadius: 10,
                      border: isChecked ? "1px solid #16a34a" : "1px solid var(--border)",
                      background: "var(--card-alt)",
                      cursor: "pointer",
                      transition: "all 0.15s",
                    }}
                  >
                    <input
                      type="checkbox"
                      checked={isChecked}
                      onChange={() => toggleCheck(item.id)}
                      style={{ marginTop: 4, width: 18, height: 18, cursor: "pointer" }}
                    />
                    <div style={{ flex: 1 }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
                        <strong style={{ color: isChecked ? "#22c55e" : "var(--text)", textDecoration: isChecked ? "line-through" : "none" }}>
                          {item.title}
                        </strong>
                        <span className="small muted" style={{ fontSize: "0.75rem", background: "var(--card)", border: "1px solid var(--border)", padding: "1px 6px", borderRadius: 4 }}>
                          {item.category}
                        </span>
                        {item.critical && (
                          <span style={{ fontSize: "0.7rem", color: "#ffffff", fontWeight: 700, background: "#dc2626", padding: "1px 6px", borderRadius: 4 }}>
                            KRİTİK
                          </span>
                        )}
                      </div>
                      <p style={{ margin: "4px 0 0", fontSize: "0.88rem", color: "var(--text-secondary)", lineHeight: 1.4 }}>
                        {item.desc}
                      </p>
                      {item.sikayetvarIssue && (
                        <div style={{ marginTop: 6, fontSize: "0.78rem", color: "#ea580c", background: "#fff7ed", padding: "3px 8px", borderRadius: 4, display: "inline-block", fontWeight: 600 }}>
                          💬 Şikayetvar Bildirimi: &quot;{item.sikayetvarIssue}&quot;
                        </div>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* 4. MODELE ÖZEL PAZARLIK TAVSİYESİ */}
          <div className="card" style={{ border: "1px solid var(--border)" }}>
            <h3 style={{ margin: "0 0 10px 0", fontSize: "1.1rem", color: "#16a34a" }}>
              🤝 Modele Özel Ekspertiz Pazarlık Tavsiyesi
            </h3>
            <p className="small" style={{ color: "var(--text-secondary)", lineHeight: 1.5, margin: "0 0 10px 0" }}>
              {expertProfile.negotiationSuggestion.notes}
            </p>
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 12 }}>
              <div
                style={{
                  background: "#f0fdf4",
                  border: "1px solid #bbf7d0",
                  padding: "12px 16px",
                  borderRadius: 8,
                }}
              >
                <div style={{ fontSize: "0.8rem", color: "#166534", fontWeight: 600 }}>Normal Aşınma Durumunda İndirim Talebi:</div>
                <div style={{ fontSize: "1.3rem", fontWeight: 800, color: "#15803d", marginTop: 2 }}>
                  {expertProfile.negotiationSuggestion.normalRange}
                </div>
              </div>
              <div
                style={{
                  background: "#fef2f2",
                  border: "1px solid #fecaca",
                  padding: "12px 16px",
                  borderRadius: 8,
                }}
              >
                <div style={{ fontSize: "0.8rem", color: "#991b1b", fontWeight: 600 }}>Kritik Arıza / Eksik Ağır Bakımda İndirim Talebi:</div>
                <div style={{ fontSize: "1.3rem", fontWeight: 800, color: "#b91c1c", marginTop: 2 }}>
                  {expertProfile.negotiationSuggestion.criticalDefectRange}
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default function EkspertizPage() {
  return (
    <Suspense fallback={<p className="muted" style={{ padding: 20 }}>Sayfa yükleniyor…</p>}>
      <EkspertizContent />
    </Suspense>
  );
}
