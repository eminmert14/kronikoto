import "./globals.css";
import Link from "next/link";
import type { ReactNode } from "react";

export const metadata = {
  title: "KronikOto — Araç tavsiye ve kronik arıza rehberi",
  description: "Kriterlerine uyan araçları bul, motor/şanzıman bazında kronik arızaları ve masrafları gör.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="tr">
      <body>
        <header className="header" style={{ justifyContent: "space-between" }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 14 }}>
            <Link href="/" className="logo">Kronik<span>Oto</span></Link>
            <span className="tagline">Almadan önce bil.</span>
          </div>

          <nav style={{ display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" }}>
            <Link
              href="/"
              style={{
                fontWeight: 600,
                fontSize: "0.95rem",
                color: "#334155",
                padding: "6px 12px",
                borderRadius: "6px",
              }}
            >
              🔍 Araç Ara
            </Link>
            <Link
              href="/compare"
              style={{
                fontWeight: 600,
                fontSize: "0.95rem",
                color: "#1d4ed8",
                background: "#eff6ff",
                border: "1px solid #bfdbfe",
                padding: "7px 14px",
                borderRadius: "8px",
              }}
            >
              ⚖️ Araç Karşılaştır
            </Link>
            <Link
              href="/ekspertiz"
              style={{
                fontWeight: 700,
                fontSize: "0.95rem",
                background: "#16a34a",
                color: "#ffffff",
                padding: "7px 16px",
                borderRadius: "8px",
                boxShadow: "0 2px 8px rgba(22, 163, 74, 0.25)",
              }}
            >
              🛡️ Ekspertiz Danışmanı
            </Link>
          </nav>
        </header>
        <main className="container">{children}</main>
        <footer className="footer">
          Veriler bilgilendirme amaçlıdır; satın almadan önce mutlaka ekspertiz yaptırın.
        </footer>
      </body>
    </html>
  );
}
