"use client";
import React, { useEffect, useState } from "react";

interface ScoreGaugeProps {
  score: number; // 0 ile 10 arasında
  brand?: string;
  label?: string;
  size?: "sm" | "md" | "lg";
  showTicks?: boolean;
  showScoreText?: boolean;
}

const MERCEDES_STAR_DATA_URI =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#2563eb"><path d="M12 1C5.925 1 1 5.925 1 12s4.925 11 11 11 11-4.925 11-11S18.075 1 12 1zm0 1.65c4.777 0 8.716 3.588 9.28 8.215L13.72 12.8l-1.72-9.66-1.72 9.66-7.56-1.935C3.284 6.238 7.223 2.65 12 2.65zm-9.29 9.765L10.35 14.5l-5.735 5.39A9.317 9.317 0 0 1 2.71 12.415zm18.58 0a9.317 9.317 0 0 1-1.905 7.475L13.65 14.5l7.64-2.085zM12 15.65l6.23 5.29a9.298 9.298 0 0 1-12.46 0L12 15.65z"/></svg>`
  );

const CUPRA_LOGO_DATA_URI =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#2563eb"><path d="M12 2L3 7.5l3.6 6.2L12 10.5l5.4 3.2L21 7.5 12 2zm0 10.2l-4.5 2.7L12 22l4.5-7.1-4.5-2.7z"/></svg>`
  );

const CHERY_LOGO_DATA_URI =
  "data:image/svg+xml;utf8," +
  encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.2"><ellipse cx="12" cy="12" rx="10" ry="6.5"/><path d="M6.5 15.5L12 7.5l5.5 8" stroke-linecap="round" stroke-linejoin="round"/></svg>`
  );

const BRAND_LOGO_URLS: Record<string, string> = {
  skoda: "https://cdn.simpleicons.org/skoda/2563eb",
  volkswagen: "https://cdn.simpleicons.org/volkswagen/2563eb",
  toyota: "https://cdn.simpleicons.org/toyota/2563eb",
  honda: "https://cdn.simpleicons.org/honda/2563eb",
  peugeot: "https://cdn.simpleicons.org/peugeot/2563eb",
  renault: "https://cdn.simpleicons.org/renault/2563eb",
  fiat: "https://cdn.simpleicons.org/fiat/2563eb",
  ford: "https://cdn.simpleicons.org/ford/2563eb",
  hyundai: "https://cdn.simpleicons.org/hyundai/2563eb",
  kia: "https://cdn.simpleicons.org/kia/2563eb",
  opel: "https://cdn.simpleicons.org/opel/2563eb",
  dacia: "https://cdn.simpleicons.org/dacia/2563eb",
  audi: "https://cdn.simpleicons.org/audi/2563eb",
  bmw: "https://cdn.simpleicons.org/bmw/2563eb",
  "mercedes-benz": MERCEDES_STAR_DATA_URI,
  mercedes: MERCEDES_STAR_DATA_URI,
  nissan: "https://cdn.simpleicons.org/nissan/2563eb",
  seat: "https://cdn.simpleicons.org/seat/2563eb",
  citroen: "https://cdn.simpleicons.org/citroen/2563eb",
  volvo: "https://cdn.simpleicons.org/volvo/2563eb",
  cupra: CUPRA_LOGO_DATA_URI,
  chery: CHERY_LOGO_DATA_URI,
};

export function BrandLogoBadge({ brand, size = "md" }: { brand?: string; size?: "sm" | "md" | "lg" }) {
  const b = (brand || "").toLowerCase();
  const src = BRAND_LOGO_URLS[b];
  const boxSize = size === "sm" ? 38 : size === "lg" ? 50 : 44;
  const imgSize = size === "sm" ? 21 : size === "lg" ? 28 : 24;

  return (
    <div
      style={{
        width: boxSize,
        height: boxSize,
        borderRadius: "50%",
        border: "2px solid var(--border)",
        background: "var(--card-alt)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxShadow: "0 2px 6px rgba(0,0,0,0.08)",
      }}
    >
      {src ? (
        <img
          src={src}
          alt={brand || "Marka"}
          style={{ width: imgSize, height: imgSize, objectFit: "contain" }}
          onError={(e) => {
            (e.target as HTMLElement).style.display = "none";
          }}
        />
      ) : (
        <span style={{ fontWeight: 800, fontSize: "0.82rem", color: "var(--accent)" }}>
          {brand ? brand.slice(0, 2).toUpperCase() : "🚗"}
        </span>
      )}
    </div>
  );
}

export default function ScoreGauge({
  score,
  brand,
  label = "",
  size = "md",
  showScoreText = true,
}: ScoreGaugeProps) {
  const [animatedScore, setAnimatedScore] = useState(0);
  const clamped = Math.max(0, Math.min(10, score));

  useEffect(() => {
    const timer = setTimeout(() => {
      setAnimatedScore(clamped);
    }, 80);
    return () => clearTimeout(timer);
  }, [clamped]);

  let statusText = "Orta / Dengeli";
  if (clamped >= 8) {
    statusText = "Yüksek / Konforlu";
  } else if (clamped < 5) {
    statusText = "Sert / Düşük Yalıtım";
  }

  const dimensions = {
    sm: { width: 150, height: 84, stroke: 13, fontSize: "1.05rem", subSize: "0.72rem" },
    md: { width: 170, height: 95, stroke: 14, fontSize: "1.25rem", subSize: "0.78rem" },
    lg: { width: 200, height: 110, stroke: 16, fontSize: "1.45rem", subSize: "0.85rem" },
  }[size];

  const cx = 100;
  const cy = 80;
  const r = 64;
  const arcLength = Math.PI * r;
  const fillLength = (animatedScore / 10) * arcLength;

  return (
    <div
      style={{
        display: "inline-flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        userSelect: "none",
      }}
    >
      {/* Mavi Doluluk Oranlı Yarım Daire + Ortasında Marka Logosu */}
      <div style={{ position: "relative", width: dimensions.width, height: dimensions.height }}>
        <svg
          viewBox="0 0 200 95"
          width={dimensions.width}
          height={dimensions.height}
          style={{ display: "block", overflow: "visible" }}
        >
          {/* Gri/Koyu Arka Plan Yayı */}
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke="var(--border)"
            strokeWidth={dimensions.stroke}
            strokeLinecap="round"
          />

          {/* Puana Göre Doluluk Oranlı Mavi Yay */}
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke="var(--accent)"
            strokeWidth={dimensions.stroke}
            strokeDasharray={`${fillLength} ${arcLength}`}
            strokeDashoffset={0}
            strokeLinecap="round"
            style={{
              transition: "stroke-dasharray 0.7s cubic-bezier(0.34, 1.3, 0.64, 1)",
            }}
          />
        </svg>

        {/* Yayın Ortasında Marka Logosu */}
        <div
          style={{
            position: "absolute",
            left: "50%",
            bottom: "4px",
            transform: "translateX(-50%)",
          }}
        >
          <BrandLogoBadge brand={brand} size={size} />
        </div>
      </div>

      {/* Puan Metni (Kart başlığında zaten yazıyorsa showScoreText=false ile gizlenebilir) */}
      {showScoreText && (
        <div
          style={{
            marginTop: 4,
            textAlign: "center",
            lineHeight: 1.2,
            display: "flex",
            alignItems: "baseline",
            justifyContent: "center",
          }}
        >
          <span
            style={{
              fontSize: dimensions.fontSize,
              fontWeight: 800,
              color: "var(--accent)",
              letterSpacing: "-0.5px",
            }}
          >
            {score.toFixed(1)}
          </span>
          <span style={{ fontSize: dimensions.subSize, color: "var(--muted)", fontWeight: 700, marginLeft: 2 }}>
            /10
          </span>
        </div>
      )}

      {label && (
        <div style={{ marginTop: 3, textAlign: "center" }}>
          <div style={{ fontSize: dimensions.subSize, color: "var(--muted)", fontWeight: 600 }}>
            {label}
          </div>
          <div
            style={{
              fontSize: dimensions.subSize,
              fontWeight: 700,
              color: "var(--accent)",
              marginTop: 1,
            }}
          >
            ● {statusText}
          </div>
        </div>
      )}
    </div>
  );
}
