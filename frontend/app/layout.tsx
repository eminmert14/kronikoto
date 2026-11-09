import "./globals.css";
import Link from "next/link";
import type { ReactNode } from "react";
import ThemeToggle from "@/components/ThemeToggle";

export const metadata = {
  title: "KronikOto — Araç tavsiye ve kronik arıza rehberi",
  description: "Kriterlerine uyan araçları bul, motor/şanzıman bazında kronik arızaları ve masrafları gör.",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="tr">
      <body>
        <header className="header" style={{ justifyContent: "space-between", alignItems: "center" }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 14 }}>
            <Link href="/" className="logo">Kronik<span>Oto</span></Link>
            <span className="tagline">Almadan önce bil.</span>
          </div>

          <nav style={{ display: "flex", gap: 12, alignItems: "flex-start", flexWrap: "wrap" }}>
            <Link
              href="/"
              className="nav-link-search"
              style={{
                fontWeight: 600,
                fontSize: "0.95rem",
                color: "var(--text-secondary)",
                padding: "7px 12px",
                borderRadius: "6px",
              }}
            >
              🔍 Araç Ara
            </Link>
            <Link
              href="/compare"
              className="nav-link-compare"
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
            <div style={{ display: "flex", flexDirection: "column", gap: 6, alignItems: "stretch" }}>
              <Link
                href="/ekspertiz"
                style={{
                  fontWeight: 700,
                  fontSize: "0.95rem",
                  background: "var(--accent)",
                  color: "#ffffff",
                  padding: "7px 16px",
                  borderRadius: "8px",
                  boxShadow: "0 2px 8px rgba(37, 99, 235, 0.25)",
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
