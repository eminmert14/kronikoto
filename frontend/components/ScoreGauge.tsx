"use client";
import React, { useEffect, useState } from "react";

interface ScoreGaugeProps {
  score: number; // 0 ile 10 arasında
  label?: string;
  size?: "sm" | "md" | "lg";
  showTicks?: boolean;
}

export default function ScoreGauge({
  score,
  label = "Konfor & Yalıtım",
  size = "md",
  showTicks = true,
}: ScoreGaugeProps) {
  const [animatedScore, setAnimatedScore] = useState(0);

  // 0 - 10 sınırlandırması
  const clamped = Math.max(0, Math.min(10, score));

  useEffect(() => {
    const timer = setTimeout(() => {
      setAnimatedScore(clamped);
    }, 100);
    return () => clearTimeout(timer);
  }, [clamped]);

  // Renk belirleme: 0-5 Kırmızı, 5-8 Sarı, 8-10 Yeşil
  let scoreColor = "#dc2626"; // Kırmızı
  let statusText = "Düşük";
  if (clamped >= 8) {
    scoreColor = "#16a34a"; // Yeşil
    statusText = "Yüksek / Konforlu";
  } else if (clamped >= 5) {
    scoreColor = "#d97706"; // Sarı
    statusText = "Orta / Dengeli";
  } else {
    scoreColor = "#dc2626"; // Kırmızı
    statusText = "Sert / Düşük Yalıtım";
  }

  const dimensions = {
    sm: { width: 110, height: 60, stroke: 8, fontSize: "1.1rem", subSize: "0.7rem", gap: 10 },
    md: { width: 160, height: 85, stroke: 12, fontSize: "1.5rem", subSize: "0.75rem", gap: 14 },
    lg: { width: 210, height: 110, stroke: 16, fontSize: "2rem", subSize: "0.85rem", gap: 18 },
  }[size];

  // SVG Yarı Çember (Merkez: 100, 75, Yarıçap: 60)
  const cx = 100;
  const cy = 75;
  const r = 60;

  // Ark uzunluğu = PI * r
  const arcLength = Math.PI * r;

  // Segment oranları:
  // 0 - 5 = %50 (Kırmızı)
  // 5 - 8 = %30 (Sarı)
  // 8 - 10 = %20 (Yeşil)
  const redLength = arcLength * 0.5;
  const yellowLength = arcLength * 0.3;
  const greenLength = arcLength * 0.2;

  // İbre Açı Hesabı: 0 puan = -180deg (sol), 5 puan = -90deg (tepe), 10 puan = 0deg (sağ)
  const angleDeg = -180 + (animatedScore / 10) * 180;
  const angleRad = (angleDeg * Math.PI) / 180;

  // İbre Ucu Koordinatları (Yay sınırını aşmayacak uzunlukta)
  const needleLength = r - 12;
  const tipX = cx + needleLength * Math.cos(angleRad);
  const tipY = cy + needleLength * Math.sin(angleRad);

  // İbre tabanı
  const baseWidth = size === "sm" ? 3.5 : 5;
  const baseAngle1 = angleRad + Math.PI / 2;
  const baseAngle2 = angleRad - Math.PI / 2;
  const p1X = cx + baseWidth * Math.cos(baseAngle1);
  const p1Y = cy + baseWidth * Math.sin(baseAngle1);
  const p2X = cx + baseWidth * Math.cos(baseAngle2);
  const p2Y = cy + baseWidth * Math.sin(baseAngle2);

  return (
    <div
      style={{
        display: "inline-flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        userSelect: "none",
        padding: "4px 0",
      }}
    >
      {/* Kadran SVG Bölümü */}
      <div style={{ position: "relative", width: dimensions.width, height: dimensions.height }}>
        <svg
          viewBox="0 0 200 90"
          width={dimensions.width}
          height={dimensions.height}
          style={{ overflow: "visible", display: "block" }}
        >
          {/* Arka plan sönük yay */}
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke="#e2e8f0"
            strokeWidth={dimensions.stroke}
            strokeLinecap="round"
          />

          {/* 1. Segment: 0 - 5 Kırmızı (%50) */}
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke="#dc2626"
            strokeWidth={dimensions.stroke}
            strokeDasharray={`${redLength} ${arcLength}`}
            strokeDashoffset={0}
            strokeLinecap="round"
            opacity="0.95"
          />

          {/* 2. Segment: 5 - 8 Sarı (%30) */}
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke="#eab308"
            strokeWidth={dimensions.stroke}
            strokeDasharray={`${yellowLength} ${arcLength}`}
            strokeDashoffset={-redLength}
            opacity="0.95"
          />

          {/* 3. Segment: 8 - 10 Yeşil (%20) */}
          <path
            d={`M ${cx - r} ${cy} A ${r} ${r} 0 0 1 ${cx + r} ${cy}`}
            fill="none"
            stroke="#16a34a"
            strokeWidth={dimensions.stroke}
            strokeDasharray={`${greenLength} ${arcLength}`}
            strokeDashoffset={-(redLength + yellowLength)}
            strokeLinecap="round"
            opacity="0.95"
          />

          {/* Çentikler (0, 5, 8, 10) */}
          {showTicks && (
            <g fontSize="9" fill="#64748b" textAnchor="middle" fontWeight="bold">
              <text x={cx - r - 2} y={cy + 13}>0</text>
              <text x={cx} y={cy - r - 6}>5</text>
              <text x={cx + r * 0.62} y={cy - r * 0.68}>8</text>
              <text x={cx + r + 4} y={cy + 13}>10</text>
            </g>
          )}

          {/* İbre */}
          <polygon
            points={`${p1X.toFixed(1)},${p1Y.toFixed(1)} ${tipX.toFixed(1)},${tipY.toFixed(1)} ${p2X.toFixed(1)},${p2Y.toFixed(1)}`}
            fill="var(--text)"
            style={{
              transition: "all 0.8s cubic-bezier(0.34, 1.3, 0.64, 1)",
            }}
          />

          {/* İbre Göbeği (Merkez Pim) */}
          <circle cx={cx} cy={cy} r={size === "sm" ? 4 : 5.5} fill="var(--text)" />
          <circle cx={cx} cy={cy} r={size === "sm" ? 1.8 : 2.5} fill={scoreColor} />
        </svg>
      </div>

      {/* Rakam Göbeğin ve İbrenin TAMAMEN ALTINDA (Geniş boşlukla ayrılmış, çakışma sıfır) */}
      <div
        style={{
          marginTop: dimensions.gap,
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
            color: scoreColor,
            letterSpacing: "-0.5px",
          }}
        >
          {score.toFixed(1)}
        </span>
        <span style={{ fontSize: dimensions.subSize, color: "#64748b", fontWeight: 700, marginLeft: 3 }}>
          /10
        </span>
      </div>

      {label && (
        <div style={{ marginTop: 4, textAlign: "center" }}>
          <div style={{ fontSize: dimensions.subSize, color: "#64748b", fontWeight: 600 }}>
            {label}
          </div>
          <div
            style={{
              fontSize: dimensions.subSize,
              fontWeight: 700,
              color: scoreColor,
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
