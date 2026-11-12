import { SafetyRatingsData } from "./ncapSafety";

const API = typeof window === "undefined"
  ? (process.env.INTERNAL_API_URL ?? "https://kronikoto.onrender.com")
  : (process.env.NEXT_PUBLIC_API_URL ?? "");

export async function api<T>(
  path: string,
  params?: Record<string, string | undefined>,
  init?: RequestInit
): Promise<T> {
  const qs = new URLSearchParams();
  Object.entries(params ?? {}).forEach(([k, v]) => v && qs.set(k, v));
  const res = await fetch(`${API}/api/v1${path}${qs.size ? `?${qs}` : ""}`, init);
  if (!res.ok) {
    let errorDetail = `API hatası: ${res.status}`;
    try {
      const errJson = await res.json();
      if (errJson && errJson.detail) {
        errorDetail = errJson.detail;
      }
    } catch {}
    throw new Error(errorDetail);
  }
  return res.json();
}

export const BODY_TYPE_LABEL: Record<string, string> = {
  sedan: "Sedan",
  hatchback: "Hatchback",
  suv: "Arazi / SUV",
  station: "Station Wagon",
  coupe: "Coupe",
  kombi: "Ticari / Kombi",
};

export const FUEL_TYPE_LABEL: Record<string, string> = {
  benzin: "Benzin",
  dizel: "Dizel",
  hibrit: "Hibrit",
  lpg: "LPG",
  elektrik: "Elektrik",
};

export const TRANSMISSION_TYPE_LABEL: Record<string, string> = {
  manuel: "Manuel",
  otomatik: "Otomatik",
  dct: "Otomatik",
  cvt: "Otomatik",
};

export const SEVERITY_LABEL: Record<string, string> = {
  dusuk: "Düşük (0 - 10.000 TL)",
  orta: "Orta (10.000 - 30.000 TL)",
  yuksek: "Yüksek (30.000 - 80.000 TL)",
  cok_yuksek: "Çok Yüksek (80.000 TL+)",
  kritik: "Çok Yüksek (80.000 TL+)",
};

export const CATEGORY_LABEL: Record<string, string> = {
  mekanik: "Mekanik",
  elektronik: "Elektronik",
  guvenlik: "Güvenlik",
  konfor: "Konfor",
  yazilim_multimedya: "Yazılım / Multimedya",
};

export interface TrimPackage {
  id?: string;
  name: string;
  level: "dusuk" | "orta" | "premium" | string;
  summary?: string;
  features: string[];
}

export interface ListingUrls {
  sahibinden?: string | null;
  arabam?: string | null;
}

export interface SearchResult {
  id: string;
  brand: string;
  name: string;
  body_type: string;
  year_start: number;
  year_end: number | null;
  comfort_score: number | null;
  min_price_tl?: number | null;
  avg_hp?: number | null;
  value_index?: number | null;
  variants_count: number;
  fuel_types: string[];
  transmission_types: string[];
  listing_urls?: ListingUrls;
}

export interface VariantDetail {
  id: string;
  brand: string;
  model: string;
  model_id: string;
  engine: string;
  fuel_type: string;
  power_hp: number;
  transmission: string;
  transmission_type: string;
  year_start: number;
  year_end: number | null;
  trim_level: string | null;
  used_price_tl: number | null;
  comfort_score: number | null;
  body_type?: string;
}

export interface Fault {
  id: string;
  title: string;
  description: string;
  category: string;
  severity: string;
  scope: string;
  avg_repair_cost_tl: number;
  max_repair_cost_tl: number | null;
  occurrence_km: [number, number];
  report_count: number;
  sources: string[];
  checklist: string[];
  verified: boolean;
}

export interface MediaSpecs {
  characteristics: {
    motor_performansi: string;
    motor_performansi_seviye?: string;
    yakit_tuketimi: string;
    yakit_tuketimi_seviye?: string;
    yol_tutusu: string;
    ic_hacim: string;
    malzeme_kalitesi: string;
    yalitim: string;
  };
  advantages: string[];
  disadvantages: string[];
}

export interface UserCommentItem {
  id: string;
  author_name: string;
  ownership_status?: string | null;
  mileage_km?: number | null;
  rating: number;
  recommend: boolean;
  body: string;
  created_at: string;
}

export interface VariantFaultsResponse {
  variant: VariantDetail;
  safety_ratings?: SafetyRatingsData;
  media_specs: MediaSpecs;
  trim_packages: TrimPackage[];
  listing_urls: ListingUrls;
  fault_summary: {
    counts: Record<string, number>;
    expected_cost_range_tl: [number, number];
  };
  faults: Fault[];
  user_comments: UserCommentItem[];
  software_mods: Array<{
    id: string;
    mod_type: string;
    is_recommended: boolean | null;
    hp: [number, number];
    nm: [number, number];
    risk_note: string | null;
    approx_cost_tl: number | null;
    verified: boolean;
    comments: Array<{
      author: string;
      body: string;
      km_at_mod: number;
      outcome: string;
    }>;
  }>;
}

export const tl = (n: number) => `${Math.round(n).toLocaleString("tr-TR")} TL`;

export const formatThousand = (val: string): string => {
  const digits = val.replace(/\D/g, "");
  if (!digits) return "";
  return Number(digits).toLocaleString("tr-TR");
};

export const parseThousand = (val: string): string => {
  return val.replace(/\D/g, "");
};
