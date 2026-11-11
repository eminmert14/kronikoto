"use client";
import { useEffect, useState } from "react";

export default function ThemeToggle() {
  const [dark, setDark] = useState(false);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const saved = localStorage.getItem("kronikoto_theme");
    if (saved === "dark") {
      setDark(true);
      document.documentElement.setAttribute("data-theme", "dark");
    } else {
      setDark(false);
      document.documentElement.removeAttribute("data-theme");
    }
  }, []);

  const toggleTheme = () => {
    const next = !dark;
    setDark(next);
    if (next) {
      document.documentElement.setAttribute("data-theme", "dark");
      localStorage.setItem("kronikoto_theme", "dark");
    } else {
      document.documentElement.removeAttribute("data-theme");
      localStorage.setItem("kronikoto_theme", "light");
    }
  };

  if (!mounted) {
    return (
      <div style={{ height: "30px", width: "100%" }} />
    );
  }

  return (
    <button
      type="button"
      onClick={toggleTheme}
      title={dark ? "Açık Moda Geç" : "Karanlık Moda Geç"}
      style={{
        display: "inline-flex",
        alignItems: "center",
        justifyContent: "center",
        gap: "6px",
        width: "100%",
        padding: "5px 12px",
        fontSize: "0.78rem",
        fontWeight: 700,
        borderRadius: "7px",
        border: "1px solid var(--border)",
        background: "var(--card-alt)",
        color: "var(--text)",
        cursor: "pointer",
        transition: "all 0.2s ease",
        boxShadow: "0 1px 3px rgba(0,0,0,0.06)",
      }}
    >
      <span>{dark ? "☀️ Açık Mod" : "🌙 Karanlık Mod"}</span>
    </button>
  );
}
