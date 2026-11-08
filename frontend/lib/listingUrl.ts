/**
 * Sahibinden ve Arabam.com için kullanıcının aktif filtrelerini
 * platformun gerçek ve garantili arama URL'lerine dönüştüren yardımcı fonksiyonlar.
 *
 * Sahibinden'de rastgele kategori slug'ları veya /otomobil direkt GET istekleri
 * "Aradığınız sayfaya ulaşılamadı" (404) hatası verebildiğinden,
 * garantili arama endpoint'i olan "kelime-ile-arama" kullanılır.
 */

export interface FilterParams {
  year_min?: string | number | null;
  year_max?: string | number | null;
  budget_max?: string | number | null;
  km_min?: string | number | null;
  km_max?: string | number | null;
  fuel_type?: string | null;
  transmission_type?: string | null;
  body_type?: string | null;
  brand?: string | null;
  model?: string | null;
}

/**
 * Sahibinden.com için asla 404 vermeyen, kelime ve filtre bazlı arama linki üretir.
 */
export function buildSahibindenUrl(searchTerm: string, filters?: FilterParams): string {
  const baseUrl = "https://www.sahibinden.com/kelime-ile-arama";

  // Temiz arama kelimeleri
  const parts: string[] = [searchTerm.trim().replace(/-/g, " ")];

  if (filters) {
    if (filters.year_min && filters.year_max && filters.year_min === filters.year_max) {
      parts.push(String(filters.year_min));
    } else if (filters.year_min) {
      parts.push(String(filters.year_min));
    }

    if (filters.fuel_type) {
      const f = filters.fuel_type.toLowerCase();
      if (f === "benzin") parts.push("Benzin");
      else if (f === "dizel") parts.push("Dizel");
      else if (f === "hibrit") parts.push("Hibrit");
      else if (f === "lpg") parts.push("LPG");
      else if (f === "elektrik") parts.push("Elektrik");
    }

    if (filters.transmission_type) {
      const t = filters.transmission_type.toLowerCase();
      if (t === "manuel") parts.push("Manuel");
      else if (t === "otomatik" || t === "cvt" || t === "dct") parts.push("Otomatik");
    }
  }

  const queryText = parts.filter(Boolean).join(" ");
  const qs = new URLSearchParams();
  qs.set("query_text", queryText);

  return `${baseUrl}?${qs.toString()}`;
}

/**
 * Arabam.com için garantili arama ve filtre linki üretir.
 */
export function buildArabamUrl(searchTerm: string, filters?: FilterParams): string {
  const baseUrl = "https://www.arabam.com/ikinci-el";
  const qs = new URLSearchParams();

  const cleanSearch = searchTerm.trim().replace(/-/g, " ");
  qs.set("searchText", cleanSearch);

  if (filters) {
    if (filters.year_min) {
      qs.set("minYear", String(filters.year_min));
    }
    if (filters.year_max) {
      qs.set("maxYear", String(filters.year_max));
    }

    if (filters.budget_max) {
      qs.set("minPrice", "0");
      qs.set("maxPrice", String(filters.budget_max));
    }

    if (filters.km_min) {
      qs.set("minKm", String(filters.km_min));
    }
    if (filters.km_max) {
      qs.set("maxKm", String(filters.km_max));
    }
  }

  return `${baseUrl}?${qs.toString()}`;
}
