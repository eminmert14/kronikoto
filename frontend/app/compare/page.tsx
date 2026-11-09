"use client";
import Link from "next/link";
import { useState, useEffect, Suspense } from "react";
import { useSearchParams } from "next/navigation";
import { api } from "@/lib/api";
import { buildSahibindenUrl, buildArabamUrl } from "@/lib/listingUrl";
import ScoreGauge from "@/components/ScoreGauge";

interface VariantItem {
  id: string;
  engine_label: string;
  transmission_label: string;
  transmission_type: string;
  fuel_type: string;
  power_hp: number;
  torque_nm: number;
  acceleration_0_100: string;
  top_speed: string;
  drivetrain: string;
  avg_consumption: string;
  segment: string;
  year_start: number;
  year_end: number | null;
  used_price_tl: number | null;
}

interface TrimItem {
  name: string;
  level: string;
  features: string[];
}

interface ModelItem {
  id: string;
  name: string;
  body_type: string;
  year_start: number;
  year_end: number | null;
  comfort_score: number | null;
  sahibinden_slug?: string | null;
  arabam_slug?: string | null;
  variants: VariantItem[];
  trim_packages: TrimItem[];
}

interface BrandTreeItem {
  brand_id: string;
  brand_name: string;
  models: ModelItem[];
}

interface CarSelection {
  brandName: string;
  modelId: string;
  variantId: string;
  trimName: string;
}

function ComparePageContent() {
  const searchParams = useSearchParams();
  const [tree, setTree] = useState<BrandTreeItem[]>([]);
  const [loading, setLoading] = useState(true);

  // 3 Araç Seçimi (Kullanıcı isteği: en başta varsayılan araç seçili gelmez, boş başlar)
  const [car1, setCar1] = useState<CarSelection>({ brandName: "", modelId: "", variantId: "", trimName: "" });
  const [car2, setCar2] = useState<CarSelection>({ brandName: "", modelId: "", variantId: "", trimName: "" });
  const [car3, setCar3] = useState<CarSelection>({ brandName: "", modelId: "", variantId: "", trimName: "" });

  const [comparedCars, setComparedCars] = useState<any[] | null>(null);

  useEffect(() => {
    api<BrandTreeItem[]>("/comparison-tree")
      .then((data) => {
        setTree(data);
        setLoading(false);
      })
      .catch(() => setLoading(false));
  }, []);

  // Seçilen araç verisini hiyerarşik ağaçtan çözümleyen yardımcı
  const resolveCarDataFromTree = (dataTree: BrandTreeItem[], sel: CarSelection) => {
    if (!sel.brandName || !sel.modelId) return null;
    const brand = dataTree.find((b) => b.brand_name === sel.brandName);
    if (!brand) return null;
    const model = brand.models.find((m) => m.id === sel.modelId);
    if (!model) return null;
    const variant = model.variants.find((v) => v.id === sel.variantId) || model.variants[0];
    const trim = model.trim_packages.find((t) => t.name === sel.trimName) || model.trim_packages[0];

    const searchKeyword = `${brand.brand_name} ${model.name}`;
    const sahibindenUrl = buildSahibindenUrl(searchKeyword);
    const arabamUrl = buildArabamUrl(searchKeyword);

    return {
      brandName: brand.brand_name,
      modelName: model.name,
      bodyType: model.body_type,
      comfortScore: model.comfort_score,
      variant,
      trim,
      sahibindenUrl,
      arabamUrl,
    };
  };

  // Ana sayfadaki "Popüler Karşılaştırmalar" bağlantısından gelen c1 ve c2 parametrelerini otomatik yükle
  useEffect(() => {
    if (!tree.length) return;
    const q1 = searchParams.get("c1");
    const q2 = searchParams.get("c2");
    if (!q1 || !q2) return;

    const findCarByQuery = (queryStr: string): CarSelection | null => {
      const qLower = queryStr.toLowerCase();
      for (const b of tree) {
        for (const m of b.models) {
          const full = `${b.brand_name} ${m.name}`.toLowerCase();
          if (full.includes(qLower) || m.name.toLowerCase().includes(qLower)) {
            return {
              brandName: b.brand_name,
              modelId: m.id,
              variantId: m.variants[0]?.id || "",
              trimName: m.trim_packages[0]?.name || "",
            };
          }
        }
      }
      return null;
    };

    const sel1 = findCarByQuery(q1);
    const sel2 = findCarByQuery(q2);
    if (sel1 && sel2) {
      setCar1(sel1);
      setCar2(sel2);
      const resolved1 = resolveCarDataFromTree(tree, sel1);
      const resolved2 = resolveCarDataFromTree(tree, sel2);
      if (resolved1 && resolved2) {
        setComparedCars([resolved1, resolved2]);
      }
    }
  }, [tree, searchParams]);

  // Seçilen araç verisini hiyerarşik ağaçtan çözümleyen yardımcı
  const resolveCarData = (sel: CarSelection) => resolveCarDataFromTree(tree, sel);

  const handleCompare = () => {
    const list = [resolveCarData(car1), resolveCarData(car2), resolveCarData(car3)].filter(Boolean);
    if (list.length < 2) {
      alert("Lütfen karşılaştırma için en az 2 araç (1. Araç ve 2. Araç) seçiniz.");
      return;
    }
    setComparedCars(list);
  };

  // Araç seçim kutucuğu bileşeni (Mobil uyumlu, placeholder'lı)
  const renderCarSelector = (
    title: string,
    isOptional: boolean,
    car: CarSelection,
    setCar: React.Dispatch<React.SetStateAction<CarSelection>>
  ) => {
    const selectedBrand = tree.find((b) => b.brand_name === car.brandName);
    const availableModels = selectedBrand?.models || [];
    const selectedModel = availableModels.find((m) => m.id === car.modelId);
    const availableVariants = selectedModel?.variants || [];
    const availableTrims = selectedModel?.trim_packages || [];

    return (
      <div
        className="card"
        style={{
          flex: "1 1 280px",
          minWidth: "260px",
          background: "#ffffff",
          boxShadow: "0 2px 8px rgba(0,0,0,0.04)",
          border: car.modelId ? "2px solid #3b82f6" : "1px solid #e2e8f0",
          borderRadius: "12px",
          transition: "border-color 0.2s",
        }}
      >
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
          <strong style={{ fontSize: "1.05rem", color: "#0f172a" }}>🚗 {title}</strong>
          {isOptional ? (
            <span className="small muted" style={{ fontSize: "0.75rem", background: "#f1f5f9", padding: "2px 6px", borderRadius: 4 }}>
              Opsiyonel
            </span>
          ) : (
            <span style={{ fontSize: "0.75rem", color: car.modelId ? "#16a34a" : "#ea580c", fontWeight: 700 }}>
              {car.modelId ? "✓ Seçildi" : "* Zorunlu"}
            </span>
          )}
        </div>

        <div style={{ display: "grid", gap: 12 }}>
          {/* 1. Marka */}
          <div>
            <label style={{ fontSize: "0.8rem", fontWeight: 700, color: "#475569", display: "block", marginBottom: 4 }}>
              Marka:
            </label>
            <select
              style={{ width: "100%", padding: "8px 10px", borderRadius: 8, border: "1px solid #cbd5e1" }}
              value={car.brandName}
              onChange={(e) => {
                const bName = e.target.value;
                setCar({ brandName: bName, modelId: "", variantId: "", trimName: "" });
              }}
            >
              <option value="">{isOptional ? "Araç Eklenmedi (Boş)" : "Marka Seçin..."}</option>
              {tree.map((b) => (
                <option key={b.brand_id} value={b.brand_name}>
                  {b.brand_name}
                </option>
              ))}
            </select>
          </div>

          {/* 2. Model */}
          <div>
            <label style={{ fontSize: "0.8rem", fontWeight: 700, color: "#475569", display: "block", marginBottom: 4 }}>
              Model:
            </label>
            <select
              disabled={!car.brandName}
              style={{
                width: "100%",
                padding: "8px 10px",
                borderRadius: 8,
                border: "1px solid #cbd5e1",
                background: !car.brandName ? "#f8fafc" : "#ffffff",
              }}
              value={car.modelId}
              onChange={(e) => {
                const mId = e.target.value;
                const mObj = availableModels.find((m) => m.id === mId);
                setCar((prev) => ({
                  ...prev,
                  modelId: mId,
                  variantId: mObj?.variants[0]?.id || "",
                  trimName: mObj?.trim_packages[0]?.name || "",
                }));
              }}
            >
              <option value="">{!car.brandName ? "Önce Marka Seçin" : "Model Seçin..."}</option>
              {availableModels.map((m) => (
                <option key={m.id} value={m.id}>
                  {m.name} ({m.year_start}–{m.year_end ?? "devam"})
                </option>
              ))}
            </select>
          </div>

          {/* 3. Motor & Şanzıman */}
          <div>
            <label style={{ fontSize: "0.8rem", fontWeight: 700, color: "#475569", display: "block", marginBottom: 4 }}>
              Motor & Şanzıman:
            </label>
            <select
              disabled={!car.modelId}
              style={{
                width: "100%",
                padding: "8px 10px",
                borderRadius: 8,
                border: "1px solid #cbd5e1",
                background: !car.modelId ? "#f8fafc" : "#ffffff",
              }}
              value={car.variantId}
              onChange={(e) => setCar((prev) => ({ ...prev, variantId: e.target.value }))}
            >
              {!car.modelId ? (
                <option value="">Önce Model Seçin</option>
              ) : (
                availableVariants.map((v) => (
                  <option key={v.id} value={v.id}>
                    {v.engine_label} · {v.transmission_type.toUpperCase()} ({v.power_hp} HP)
                  </option>
                ))
              )}
            </select>
          </div>

          {/* 4. Donanım Paketi */}
          <div>
            <label style={{ fontSize: "0.8rem", fontWeight: 700, color: "#475569", display: "block", marginBottom: 4 }}>
              Donanım Paketi (Opsiyonel):
            </label>
            <select
              disabled={!car.modelId}
              style={{
                width: "100%",
                padding: "8px 10px",
                borderRadius: 8,
                border: "1px solid #cbd5e1",
                background: !car.modelId ? "#f8fafc" : "#ffffff",
              }}
              value={car.trimName}
              onChange={(e) => setCar((prev) => ({ ...prev, trimName: e.target.value }))}
            >
              {!car.modelId ? (
                <option value="">Önce Model Seçin</option>
              ) : (
                availableTrims.map((t, idx) => (
                  <option key={idx} value={t.name}>
                    {t.name} ({t.level === "premium" ? "En Dolu" : t.level === "orta" ? "Orta Paket" : "Giriş"})
                  </option>
                ))
              )}
            </select>
          </div>
        </div>
      </div>
    );
  };

  return (
    <>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 20, flexWrap: "wrap", gap: 12 }}>
        <div>
          <Link href="/" className="muted small" style={{ fontWeight: 600 }}>
            ← Ana Sayfaya & Filtrelere Dön
          </Link>
          <h1 style={{ fontSize: "1.85rem", margin: "6px 0 2px 0", color: "#0f172a", fontWeight: 800 }}>
            ⚖️ Araç Karşılaştırma Modülü
          </h1>
          <p className="muted small" style={{ margin: 0 }}>
            Türkiye pazarındaki araçları motor gücü, tork, 0-100 hızlanması, yakıt tüketimi, donanımları ve konforuyla yan yana kıyaslayın.
          </p>
        </div>
      </div>

      {loading ? (
        <p className="muted card" style={{ padding: 20 }}>Araç veritabanı yükleniyor…</p>
      ) : (
        <>
          {/* 3 Araç Seçim Kartı */}
          <div style={{ display: "flex", gap: 14, flexWrap: "wrap", marginBottom: 18 }}>
            {renderCarSelector("1. Araç", false, car1, setCar1)}
            {renderCarSelector("2. Araç", false, car2, setCar2)}
            {renderCarSelector("3. Araç", true, car3, setCar3)}
          </div>

          <div style={{ textAlign: "center", marginBottom: 28 }}>
            <button
              type="button"
              className="btn"
              onClick={handleCompare}
              style={{
                padding: "12px 34px",
                fontSize: "1.05rem",
                borderRadius: "10px",
                fontWeight: 800,
                boxShadow: "0 4px 14px rgba(37, 99, 235, 0.25)",
                cursor: "pointer",
              }}
            >
              🚀 Araçları Yan Yana Karşılaştır
            </button>
          </div>

          {/* Henüz Karşılaştırma Yapılmadıysa Bilgi Kartı */}
          {(!comparedCars || comparedCars.length < 2) && (
            <div
              className="card"
              style={{
                textAlign: "center",
                padding: "3rem 1.5rem",
                background: "#ffffff",
                borderRadius: "16px",
                border: "1px dashed #cbd5e1",
              }}
            >
              <div style={{ fontSize: "2.5rem", marginBottom: 10 }}>⚖️🚘</div>
              <h3 style={{ fontSize: "1.25rem", fontWeight: 800, color: "#0f172a", margin: "0 0 8px 0" }}>
                Karşılaştırmak İstediğiniz Araçları Seçin
              </h3>
              <p style={{ color: "#64748b", maxWidth: 500, margin: "0 auto", fontSize: "0.95rem", lineHeight: 1.5 }}>
                Yukarıdaki kutulardan en az 2 aracı (1. Araç ve 2. Araç) belirleyip ardından <strong>&apos;Araçları Yan Yana Karşılaştır&apos;</strong> butonuna basınız. İsterseniz 3. aracı da dahil edebilirsiniz.
              </p>
            </div>
          )}

          {/* Yan Yana Karşılaştırma Tablosu (Mobil Kaydırma ve Sabit Başlık Uyumlu) */}
          {comparedCars && comparedCars.length >= 2 && (
            <div
              className="card"
              style={{
                padding: 0,
                overflowX: "auto",
                border: "2px solid #e2e8f0",
                borderRadius: 14,
                boxShadow: "0 4px 12px rgba(0,0,0,0.04)",
                WebkitOverflowScrolling: "touch",
              }}
            >
              <table
                style={{
                  width: "100%",
                  minWidth: "620px",
                  borderCollapse: "collapse",
                  textAlign: "left",
                  fontSize: "0.95rem",
                }}
              >
                <thead>
                  <tr style={{ background: "#f8fafc", borderBottom: "2px solid #e2e8f0" }}>
                    <th
                      style={{
                        padding: "16px 20px",
                        width: "26%",
                        color: "#475569",
                        fontWeight: 800,
                        position: "sticky",
                        left: 0,
                        background: "#f8fafc",
                        zIndex: 2,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Kriterler
                    </th>
                    {comparedCars.map((c, i) => (
                      <th key={i} style={{ padding: "16px 20px", width: `${74 / comparedCars.length}%` }}>
                        <div style={{ fontSize: "1.15rem", fontWeight: 800, color: "#0f172a" }}>
                          {c.brandName} {c.modelName}
                        </div>
                        <div style={{ color: "var(--accent)", fontSize: "0.85rem", fontWeight: 700, marginTop: 2 }}>
                          {c.trim?.name || "Standart Paket"}
                        </div>
                      </th>
                    ))}
                  </tr>
                </thead>
                <tbody>
                  {/* Satır 1: Konfor & Yalıtım Göstergesi */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Konfor & Yalıtım Puanı
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        {c.comfortScore !== null ? (
                          <div style={{ display: "inline-block" }}>
                            <ScoreGauge score={c.comfortScore} size="sm" showTicks={false} label="" />
                          </div>
                        ) : (
                          "Hesaplanıyor"
                        )}
                      </td>
                    ))}
                  </tr>

                  {/* Satır 2: Segment & Kasa */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9", background: "#fafafa" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#fafafa",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Segment & Kasa Tipi
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px", fontWeight: 600 }}>
                        {c.variant?.segment || "C-Segment"} ({c.bodyType?.toUpperCase()})
                      </td>
                    ))}
                  </tr>

                  {/* Satır 3: Model Yılı */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Model Üretim Yılı
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        {c.variant?.year_start}–{c.variant?.year_end ?? "Günümüz"}
                      </td>
                    ))}
                  </tr>

                  {/* Satır 4: Motor & Güç */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9", background: "#fafafa" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#fafafa",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Motor & Güç (HP)
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        <strong>{c.variant?.power_hp} HP</strong>
                        <div className="muted small">{c.variant?.engine_label}</div>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 5: Maksimum Tork */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Maksimum Tork (Nm)
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        <strong style={{ color: "#0f172a" }}>{c.variant?.torque_nm} Nm</strong>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 6: 0-100 Hızlanma */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9", background: "#fafafa" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#fafafa",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      0-100 km/s Hızlanma
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        <span style={{ fontWeight: 800, color: "#2563eb" }}>
                          {c.variant?.acceleration_0_100 || "9.5 sn"}
                        </span>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 7: Maksimum Hız */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Maksimum Hız
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        {c.variant?.top_speed || "195 km/s"}
                      </td>
                    ))}
                  </tr>

                  {/* Satır 8: Çekiş Sistemi */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9", background: "#fafafa" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#fafafa",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Çekiş Sistemi
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px", fontWeight: 600 }}>
                        {c.variant?.drivetrain || "Önden Çekiş"}
                      </td>
                    ))}
                  </tr>

                  {/* Satır 9: Şanzıman Tipi */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Şanzıman Türü
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        <span className="badge" style={{ textTransform: "capitalize" }}>
                          {c.variant?.transmission_type === "otomatik" ? "Otomatik" : "Manuel"}
                        </span>
                        <div className="muted small" style={{ marginTop: 2 }}>
                          {c.variant?.transmission_label}
                        </div>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 10: Yakıt Türü */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9", background: "#fafafa" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#fafafa",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Yakıt Türü
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px", textTransform: "capitalize", fontWeight: 600 }}>
                        {c.variant?.fuel_type}
                      </td>
                    ))}
                  </tr>

                  {/* Satır 11: Ortalama Yakıt Tüketimi */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Ortalama Tüketim
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        <strong style={{ color: "#16a34a" }}>
                          {c.variant?.avg_consumption || "5.2 lt / 100 km"}
                        </strong>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 12: Seçilen Donanım Paketi */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9", background: "#fafafa" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#fafafa",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Donanım Seviyesi
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px" }}>
                        <strong>{c.trim?.name || "Standart"}</strong>
                        <div className="muted small">
                          {c.trim?.level === "premium" ? "En Üst Paket" : c.trim?.level === "orta" ? "Orta Paket" : "Giriş Paketi"}
                        </div>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 13: Donanım Özellikleri */}
                  <tr style={{ borderBottom: "1px solid #f1f5f9" }}>
                    <td
                      style={{
                        padding: "14px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#ffffff",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Öne Çıkan Özellikler
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "14px 20px", verticalAlign: "top" }}>
                        <div style={{ display: "flex", flexWrap: "wrap", gap: 4 }}>
                          {(c.trim?.features || ["Klima", "Bluetooth", "Yokuş Kalkış"]).map((f: string, fi: number) => (
                            <span
                              key={fi}
                              style={{
                                background: "#f1f5f9",
                                color: "#334155",
                                padding: "2px 8px",
                                borderRadius: "4px",
                                fontSize: "0.8rem",
                                fontWeight: 500,
                              }}
                            >
                              ✓ {f}
                            </span>
                          ))}
                        </div>
                      </td>
                    ))}
                  </tr>

                  {/* Satır 14: Canlı İlan Arama Linkleri (Asla 404 vermez) */}
                  <tr style={{ background: "#f8fafc" }}>
                    <td
                      style={{
                        padding: "18px 20px",
                        fontWeight: 700,
                        color: "#334155",
                        position: "sticky",
                        left: 0,
                        background: "#f8fafc",
                        zIndex: 1,
                        boxShadow: "2px 0 4px rgba(0,0,0,0.03)",
                      }}
                    >
                      Canlı Piyasa İlanları
                    </td>
                    {comparedCars.map((c, i) => (
                      <td key={i} style={{ padding: "18px 20px" }}>
                        <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                          <a
                            href={c.sahibindenUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="listing-btn sahibinden"
                            style={{ padding: "8px 12px", fontSize: "0.85rem" }}
                          >
                            Sahibinden.com ↗
                          </a>
                          <a
                            href={c.arabamUrl}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="listing-btn arabam"
                            style={{ padding: "8px 12px", fontSize: "0.85rem" }}
                          >
                            Arabam.com ↗
                          </a>
                        </div>
                      </td>
                    ))}
                  </tr>
                </tbody>
              </table>
            </div>
          )}
        </>
      )}
    </>
  );
}

export default function ComparePage() {
  return (
    <Suspense fallback={<p className="muted card" style={{ padding: 20 }}>Karşılaştırma modülü yükleniyor…</p>}>
      <ComparePageContent />
    </Suspense>
  );
}
