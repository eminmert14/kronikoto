"use client";
import React from "react";
import { SafetyRatingsData } from "@/lib/ncapSafety";

interface NcapSafetyCardProps {
  safety: SafetyRatingsData;
}

export default function NcapSafetyCard({ safety }: NcapSafetyCardProps) {
  const { euro_ncap, iihs, nhtsa } = safety;

  const starsArray = [1, 2, 3, 4, 5];

  const metrics = [
    { label: "Yetişkin Yolcu", pct: euro_ncap.adult_occupant, icon: "🧑" },
    { label: "Çocuk Yolcu", pct: euro_ncap.child_occupant, icon: "🧒" },
    { label: "Yaya & Bisiklet", pct: euro_ncap.vulnerable_road_users, icon: "🚶" },
    { label: "Güvenlik Asist.", pct: euro_ncap.safety_assist, icon: "🛡️" },
  ];

  return (
    <div
      className="card ncap-card"
      style={{
        padding: "14px 18px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        gap: 10,
        minWidth: 270,
        maxWidth: 340,
        border: "1px solid var(--border)",
      }}
    >
      {/* Üst Başlık: Euro NCAP Yıldızları + Test Yılı */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 8,
          borderBottom: "1px solid var(--border)",
          paddingBottom: 8,
        }}
      >
        <div>
          <div
            style={{
              fontSize: "0.73rem",
              fontWeight: 800,
              textTransform: "uppercase",
              letterSpacing: "0.4px",
              color: "var(--muted)",
            }}
          >
            🛡️ Euro NCAP · IIHS · NHTSA
          </div>
          <div style={{ display: "flex", alignItems: "center", gap: 6, marginTop: 2 }}>
            <span
              style={{
                fontSize: "1.05rem",
                letterSpacing: "1px",
                color: "var(--accent)",
                fontWeight: 900,
              }}
            >
              {starsArray
                .map((s) => (s <= euro_ncap.stars ? "★" : "☆"))
                .join("")}
            </span>
            <span
              style={{
                fontSize: "0.85rem",
                fontWeight: 800,
                color: "var(--text)",
              }}
            >
              {euro_ncap.stars}/5 Yıldız
            </span>
          </div>
        </div>

        <span
          style={{
            fontSize: "0.72rem",
            fontWeight: 800,
            padding: "3px 8px",
            borderRadius: 6,
            background: "var(--accent-light)",
            color: "var(--accent)",
            border: "1px solid var(--border)",
            whiteSpace: "nowrap",
          }}
        >
          Test: {euro_ncap.test_year}
        </span>
      </div>

      {/* Orta Kısım: 4 Euro NCAP Kategori Yüzdesi (2x2 Grid + İlerleme Çubukları) */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: "8px 12px",
        }}
      >
        {metrics.map((m, idx) => (
          <div key={idx}>
            <div
              style={{
                display: "flex",
                justifyContent: "space-between",
                fontSize: "0.74rem",
                fontWeight: 700,
                color: "var(--text-secondary)",
                marginBottom: 3,
              }}
            >
              <span>
                {m.icon} {m.label}
              </span>
              <span style={{ color: "var(--accent)", fontWeight: 800 }}>%{m.pct}</span>
            </div>
            <div
              style={{
                width: "100%",
                height: 6,
                background: "var(--card-alt)",
                borderRadius: 999,
                overflow: "hidden",
                border: "1px solid var(--border)",
              }}
            >
              <div
                style={{
                  width: `${Math.min(100, Math.max(0, m.pct))}%`,
                  height: "100%",
                  background: "var(--accent)",
                  borderRadius: 999,
                }}
              />
            </div>
          </div>
        ))}
      </div>

      {/* Alt Kısım: IIHS ve NHTSA Rozetleri */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 6,
          flexWrap: "wrap",
          borderTop: "1px solid var(--border)",
          paddingTop: 8,
          fontSize: "0.73rem",
        }}
      >
        <span
          style={{
            background: "var(--card-alt)",
            color: "var(--text-secondary)",
            border: "1px solid var(--border)",
            padding: "2px 7px",
            borderRadius: 5,
            fontWeight: 700,
          }}
          title={`IIHS Ön Çarpışma: ${iihs.small_overlap_front} | Yan: ${iihs.side_impact}`}
        >
          🏅 IIHS: <strong style={{ color: "var(--text)" }}>{iihs.award}</strong>
        </span>

        <span
          style={{
            background: "var(--card-alt)",
            color: "var(--text-secondary)",
            border: "1px solid var(--border)",
            padding: "2px 7px",
            borderRadius: 5,
            fontWeight: 700,
          }}
          title={`NHTSA Devrilme Riski: ${nhtsa.rollover_risk}`}
        >
          🇺🇸 NHTSA: <strong style={{ color: "var(--accent)" }}>{nhtsa.overall_stars}★</strong>
        </span>
      </div>
    </div>
  );
}
