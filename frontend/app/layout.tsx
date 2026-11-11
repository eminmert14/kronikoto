import "./globals.css";
import Link from "next/link";
import type { ReactNode } from "react";
import ThemeToggle from "@/components/ThemeToggle";

export const metadata = {
  title: "KronikOto — Araç tavsiye, Euro NCAP güvenlik ve kronik arıza rehberi",
  description: "Kriterlerine uyan araçları bul, Euro NCAP / IIHS güvenlik puanlarını, motor/şanzıman kronik arızalarını ve masrafları gör.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="tr">
      <body>
        <header className="header">
          <div className="header-brand-row" style={{ display: "flex", alignItems: "baseline", gap: 14 }}>
            <Link href="/" className="logo">Kronik<span>Oto</span></Link>
            <span className="tagline">Almadan önce bil.</span>
          </div>

          <nav className="header-nav" style={{ display: "flex", gap: 10, alignItems: "flex-start", flexWrap: "wrap" }}>
            <Link
              href="/"
              className="nav-link-search"
              style={{
                fontWeight: 600,
                fontSize: "0.92rem",
                color: "var(--text-secondary)",
                background: "var(--card-alt)",
                border: "1px solid var(--border)",
                padding: "7px 12px",
                borderRadius: "8px",
                textAlign: "center",
              }}
            >
              🔍 Araç Ara
            </Link>
            <Link
              href="/compare"
              className="nav-link-compare"
              style={{
                fontWeight: 700,
                fontSize: "0.92rem",
                color: "var(--accent)",
                background: "var(--accent-light)",
                border: "1px solid var(--border)",
                padding: "7px 14px",
                borderRadius: "8px",
                textAlign: "center",
              }}
            >
              ⚖️ Araç Karşılaştır
            </Link>
            <div className="nav-ekspertiz-group" style={{ display: "flex", flexDirection: "column", gap: 6, alignItems: "stretch" }}>
              <Link
                href="/ekspertiz"
                style={{
                  fontWeight: 700,
                  fontSize: "0.92rem",
                  background: "var(--accent)",
                  color: "#ffffff",
                  padding: "7px 16px",
                  borderRadius: "8px",
                  boxShadow: "0 2px 8px rgba(234, 88, 12, 0.28)",
                  textAlign: "center",
                }}
              >
                🛡️ Ekspertiz Danışmanı
              </Link>
              <ThemeToggle />
            </div>
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
