import uuid
import difflib
from urllib.parse import quote_plus
from pydantic import BaseModel, Field

from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, desc, func
from sqlalchemy.orm import Session, joinedload

from . import models as m
from .config import settings
from .database import engine, get_db, SessionLocal
from .models import Base, UserComment
from .scoring import SEVERITY_ORDER, fault_severity
from .car_media_specs import get_variant_media_specs
from .car_model_reviews import get_model_sikayetvar_reviews
from .full_50_data import ALL_MODELS
from .seed import run as seed_run
from .ncap_safety import get_model_safety_ratings, fetch_nhtsa_live_api

def _tr_sort_key(s: str) -> str:
    """Türkçe karakterleri doğru alfabetik sıraya sokan anahtar fonksiyonu."""
    tr_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return s.translate(tr_map).lower()


# Yaygın Türkçe fonetik yazım hataları / alternatif isimler sözlüğü
TYPO_ALIASES: dict[str, list[str]] = {
    "civik": ["Honda Civic FC5"],
    "sivik": ["Honda Civic FC5"],
    "civi": ["Honda Civic FC5"],
    "sity": ["Honda City"],
    "siti": ["Honda City"],
    "kuma": ["Ford Puma", "Ford Kuga"],
    "kuga": ["Ford Kuga"],
    "puna": ["Ford Puma"],
    "megan": ["Renault Megane 4 Sedan", "Renault Megane 3"],
    "megane": ["Renault Megane 4 Sedan", "Renault Megane 3"],
    "fluens": ["Renault Fluence"],
    "fluan": ["Renault Fluence"],
    "fiyorino": ["Fiat Fiorino Combi"],
    "fiorino": ["Fiat Fiorino Combi"],
    "pasat": ["Volkswagen Passat B8", "Volkswagen Passat B7"],
    "cetta": ["Volkswagen Jetta"],
    "taygo": ["Volkswagen Taigo"],
    "korola": ["Toyota Corolla E210", "Toyota Corolla E180"],
    "korolla": ["Toyota Corolla E210", "Toyota Corolla E180"],
    "corola": ["Toyota Corolla E210", "Toyota Corolla E180"],
    "oris": ["Toyota Auris"],
    "fokus": ["Ford Focus 4", "Ford Focus 3"],
    "foküs": ["Ford Focus 4", "Ford Focus 3"],
    "kurye": ["Ford Tourneo Courier"],
    "kuriyer": ["Ford Tourneo Courier"],
    "courier": ["Ford Tourneo Courier"],
    "egeya": ["Fiat Egea Sedan", "Fiat Egea Cross"],
    "ega": ["Fiat Egea Sedan", "Fiat Egea Cross"],
    "dastır": ["Dacia Duster"],
    "duster": ["Dacia Duster"],
    "tuson": ["Hyundai Tucson"],
    "tukson": ["Hyundai Tucson"],
    "aksent": ["Hyundai Accent Blue"],
    "accent": ["Hyundai Accent Blue"],
    "kaşkai": ["Nissan Qashqai"],
    "kaskai": ["Nissan Qashqai"],
    "qashqai": ["Nissan Qashqai"],
    "nisan": ["Nissan Qashqai", "Nissan Juke", "Nissan Micra", "Nissan X-Trail"],
    "cuk": ["Nissan Juke"],
    "mikra": ["Nissan Micra"],
    "xtrail": ["Nissan X-Trail"],
    "oktavya": ["Skoda Octavia"],
    "oktavia": ["Skoda Octavia"],
    "süperb": ["Skoda Superb"],
    "superp": ["Skoda Superb"],
    "kamyk": ["Skoda Kamiq"],
    "kamik": ["Skoda Kamiq"],
    "karok": ["Skoda Karoq"],
    "kodyak": ["Skoda Kodiaq"],
    "kodiyak": ["Skoda Kodiaq"],
    "skala": ["Skoda Scala"],
    "fabya": ["Skoda Fabia"],
    "insignya": ["Opel Insignia"],
    "insignia": ["Opel Insignia"],
    "pejo": ["Peugeot 3008", "Peugeot 2008", "Peugeot 408", "Peugeot 508", "Peugeot 308", "Peugeot 208", "Peugeot Rifter", "Peugeot 301"],
    "pöjo": ["Peugeot 3008", "Peugeot 2008", "Peugeot 408", "Peugeot 508", "Peugeot 308", "Peugeot 208", "Peugeot Rifter", "Peugeot 301"],
    "riftır": ["Peugeot Rifter"],
    "reno": ["Renault Megane 4 Sedan", "Renault Fluence", "Renault Clio 5", "Renault Captur", "Renault Kadjar", "Renault Austral", "Renault Taliant", "Renault Symbol"],
    "sembol": ["Renault Symbol"],
    "simbol": ["Renault Symbol"],
    "vosvogen": ["Volkswagen Passat B8", "Volkswagen Jetta", "Volkswagen Golf 7", "Volkswagen Polo", "Volkswagen Taigo", "Volkswagen Tiguan", "Volkswagen T-Roc", "Volkswagen Caddy"],
    "vw": ["Volkswagen Passat B8", "Volkswagen Jetta", "Volkswagen Golf 7", "Volkswagen Polo", "Volkswagen Taigo", "Volkswagen Tiguan", "Volkswagen T-Roc", "Volkswagen Caddy"],
    "hundai": ["Hyundai i20", "Hyundai i30", "Hyundai Accent Blue", "Hyundai Elantra", "Hyundai Tucson", "Hyundai Kona", "Hyundai Bayon"],
    "hyndai": ["Hyundai i20", "Hyundai i30", "Hyundai Accent Blue", "Hyundai Elantra", "Hyundai Tucson", "Hyundai Kona", "Hyundai Bayon"],
    "sportaj": ["Kia Sportage"],
    "siid": ["Kia Ceed", "Kia XCeed"],
    "sid": ["Kia Ceed", "Kia XCeed"],
    "iksceed": ["Kia XCeed"],
    "pikanto": ["Kia Picanto"],
    "kliyo": ["Renault Clio 5", "Renault Clio 4"],
    "klio": ["Renault Clio 5", "Renault Clio 4"],
    "talyant": ["Renault Taliant"],
    "kacar": ["Renault Kadjar"],
    "mersedes": ["Mercedes-Benz C Serisi", "Mercedes-Benz E Serisi", "Mercedes-Benz A Serisi", "Mercedes-Benz CLA", "Mercedes-Benz GLA", "Mercedes-Benz GLC"],
    "mercedes": ["Mercedes-Benz C Serisi", "Mercedes-Benz E Serisi", "Mercedes-Benz A Serisi", "Mercedes-Benz CLA", "Mercedes-Benz GLA", "Mercedes-Benz GLC"],
    "merco": ["Mercedes-Benz C Serisi", "Mercedes-Benz E Serisi", "Mercedes-Benz A Serisi", "Mercedes-Benz CLA", "Mercedes-Benz GLA", "Mercedes-Benz GLC"],
    "c180": ["Mercedes-Benz C Serisi"],
    "c200": ["Mercedes-Benz C Serisi"],
    "e180": ["Mercedes-Benz E Serisi"],
    "e200": ["Mercedes-Benz E Serisi"],
    "a180": ["Mercedes-Benz A Serisi"],
    "bemve": ["BMW 3 Serisi", "BMW 5 Serisi", "BMW 1 Serisi", "BMW X1", "BMW X3"],
    "bmv": ["BMW 3 Serisi", "BMW 5 Serisi", "BMW 1 Serisi", "BMW X1", "BMW X3"],
    "320i": ["BMW 3 Serisi"],
    "320d": ["BMW 3 Serisi"],
    "520i": ["BMW 5 Serisi"],
    "520d": ["BMW 5 Serisi"],
    "118i": ["BMW 1 Serisi"],
    "116d": ["BMW 1 Serisi"],
    "avdi": ["Audi A3 Sedan", "Audi A4 Sedan", "Audi A6 Sedan", "Audi Q2", "Audi Q3"],
    "sitren": ["Citroen C5 Aircross", "Citroen C4 X", "Citroen C3 Aircross", "Citroen C-Elysee"],
    "sitroen": ["Citroen C5 Aircross", "Citroen C4 X", "Citroen C3 Aircross", "Citroen C-Elysee"],
    "elise": ["Citroen C-Elysee"],
    "elysee": ["Citroen C-Elysee"],
    "kupra": ["Cupra Formentor"],
    "şeri": ["Chery Tiggo 7 Pro", "Chery Tiggo 8 Pro"],
    "seri": ["Chery Tiggo 7 Pro", "Chery Tiggo 8 Pro"],
    "tiggo": ["Chery Tiggo 7 Pro", "Chery Tiggo 8 Pro"],
    "stepvay": ["Dacia Sandero Stepway"],
    "stepway": ["Dacia Sandero Stepway"],
    "coger": ["Dacia Jogger"],
    "ateka": ["Seat Ateca"],
}


def _fuzzy_match_model(search_term: str, brand_name: str, model_name: str) -> bool:
    """Kullanıcının yazdığı metinle marka/model arasında hem alt dize hem de bulanık (fuzzy) eşleşme yapar."""
    q_norm = _tr_sort_key(search_term.strip())
    b_norm = _tr_sort_key(brand_name)
    m_norm = _tr_sort_key(model_name)
    full_norm = f"{b_norm} {m_norm}"

    # 1. Doğrudan alt dize eşleşmesi
    if q_norm in full_norm or q_norm in b_norm or q_norm in m_norm:
        return True

    # 2. Bilinen yazım hatası / fonetik sözlük kontrolü
    q_tokens = q_norm.split()
    for tok in [q_norm] + q_tokens:
        if tok in TYPO_ALIASES:
            for target in TYPO_ALIASES[tok]:
                t_norm = _tr_sort_key(target)
                if t_norm in full_norm or full_norm in t_norm:
                    return True

    # 3. Kelime bazlı benzerlik (Levenshtein / SequenceMatcher) kontrolü
    model_tokens = full_norm.split()
    matched_tokens = 0
    for qt in q_tokens:
        if len(qt) < 3:
            if qt in full_norm:
                matched_tokens += 1
            continue
        best_ratio = max(
            (difflib.SequenceMatcher(None, qt, mt).ratio() for mt in model_tokens),
            default=0.0,
        )
        # C/K, S/C, Y/I gibi Türkçe okunuş dönüşümüyle ekstra kontrol
        qt_phonetic = qt.replace("k", "c").replace("s", "c").replace("y", "i").replace("v", "w")
        best_phonetic = max(
            (
                difflib.SequenceMatcher(
                    None,
                    qt_phonetic,
                    mt.replace("k", "c").replace("s", "c").replace("y", "i").replace("v", "w"),
                ).ratio()
                for mt in model_tokens
            ),
            default=0.0,
        )
        if max(best_ratio, best_phonetic) >= 0.72:
            matched_tokens += 1

    return len(q_tokens) > 0 and matched_tokens == len(q_tokens)

app = FastAPI(title="KronikOto API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in settings.cors_origins.split(",")],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def _startup():
    Base.metadata.create_all(engine)
    with SessionLocal() as db:
        current_count = db.scalar(select(func.count(m.CarModel.id))) or 0
        if current_count < len(ALL_MODELS):
            seed_run(reset=True)


# ---------- yardımcılar ----------
def _fault_applies(f: m.FaultReport, v: m.Variant) -> bool:
    """Dolu olan kapsam alanlarının hepsi varyantla eşleşmeli; hepsi boşsa geçersiz."""
    scope = [(f.engine_id, v.engine_id), (f.transmission_id, v.transmission_id), (f.model_id, v.model_id)]
    if all(a is None for a, _ in scope):
        return False
    return all(a is None or a == b for a, b in scope)


def _fault_out(f: m.FaultReport) -> dict:
    scope = "model" if f.model_id else "motor" if f.engine_id else "sanziman"
    return {
        "id": str(f.id), "title": f.title, "description": f.description,
        "category": f.category, "severity": fault_severity(f), "scope": scope,
        "avg_repair_cost_tl": float(f.avg_repair_cost_tl),
        "max_repair_cost_tl": float(f.max_repair_cost_tl) if f.max_repair_cost_tl else None,
        "occurrence_km": [f.occurrence_km_start, f.occurrence_km_end],
        "report_count": f.report_count, "sources": f.sources, "checklist": f.checklist,
        "verified": f.verified,
    }


def _variant_out(v: m.Variant) -> dict:
    return {
        "id": str(v.id), "engine": v.engine.label, "fuel_type": v.engine.fuel_type,
        "power_hp": v.engine.power_hp, "transmission": v.transmission.label,
        "transmission_type": v.transmission.type,
        "year_start": v.year_start, "year_end": v.year_end, "trim_level": v.trim_level,
        "used_price_tl": float(v.used_price_tl) if v.used_price_tl else None,
    }





# ---------- endpoint'ler ----------
@app.get("/api/v1/comparison-tree")
def get_comparison_tree(db: Session = Depends(get_db)):
    """Karşılaştırma modülü için hiyerarşik Marka -> Model -> Varyant & Donanım ağacı."""
    brands_rows = db.scalars(select(m.Brand).where(m.Brand.is_active).order_by(m.Brand.name)).all()

    models_rows = db.scalars(
        select(m.CarModel)
        .where(m.CarModel.is_active)
        .options(
            joinedload(m.CarModel.variants).joinedload(m.Variant.engine),
            joinedload(m.CarModel.variants).joinedload(m.Variant.transmission),
            joinedload(m.CarModel.trim_packages),
        )
        .order_by(m.CarModel.name)
    ).unique().all()

    tree = []
    for b in brands_rows:
        b_models = [mo for mo in models_rows if mo.brand_id == b.id]
        if not b_models:
            continue

        model_list = []
        for mo in b_models:
            variants_list = []
            for v in mo.variants:
                if not v.is_active:
                    continue
                # Motor teknik verileri & 0-100 / son hız hesapları
                hp = v.engine.power_hp or 100
                torque = v.engine.torque_nm or 200
                fuel = v.engine.fuel_type
                t_type = "Otomatik" if v.transmission.type in ["otomatik", "dct", "cvt"] else "Manuel"

                # Gerçekçi 0-100 ve son hız hesabı
                if hp >= 180:
                    acc = round(7.4 + (200 - hp) * 0.02, 1)
                    top_speed = 225
                elif hp >= 130:
                    acc = round(9.0 + (150 - hp) * 0.04, 1)
                    top_speed = 210
                elif hp >= 100:
                    acc = round(10.5 + (120 - hp) * 0.05, 1)
                    top_speed = 195
                else:
                    acc = round(12.2 + (95 - hp) * 0.06, 1)
                    top_speed = 180

                # Ortalama tüketim tahmini
                if fuel == "dizel":
                    consumption = "4.2 - 5.0 lt"
                elif fuel == "hibrit":
                    consumption = "3.8 - 4.5 lt"
                elif fuel == "lpg":
                    consumption = "7.0 - 8.5 lt (LPG)"
                elif hp > 140:
                    consumption = "7.2 - 8.8 lt"
                else:
                    consumption = "5.8 - 6.8 lt"

                # Çekiş
                drivetrain = "Dört Tekerlekten Çekiş (AWD / 4x4)" if "4x4" in mo.name.lower() or "duster" in mo.name.lower() and fuel == "dizel" else "Önden Çekiş (FWD)"

                # Segment
                segment_label = "B-Segment (Küçük Şehir)" if mo.body_type == "hatchback" and "clio" in mo.name.lower() or "polo" in mo.name.lower() or "corsa" in mo.name.lower() or "i20" in mo.name.lower() else "D-Segment (Geniş / Makam)" if "passat" in mo.name.lower() or "superb" in mo.name.lower() or "insignia" in mo.name.lower() or "508" in mo.name.lower() else "C-Segment (Aile / Kompakt)"

                variants_list.append({
                    "id": str(v.id),
                    "engine_label": v.engine.label,
                    "transmission_label": v.transmission.label,
                    "transmission_type": t_type,
                    "fuel_type": v.engine.fuel_type,
                    "power_hp": hp,
                    "torque_nm": torque,
                    "acceleration_0_100": f"{acc} sn",
                    "top_speed": f"{top_speed} km/s",
                    "drivetrain": drivetrain,
                    "avg_consumption": consumption,
                    "segment": segment_label,
                    "year_start": v.year_start,
                    "year_end": v.year_end,
                    "used_price_tl": float(v.used_price_tl) if v.used_price_tl else None,
                })

            trims_list = [
                {
                    "name": tp.name,
                    "level": tp.level,
                    "features": tp.features,
                }
                for tp in mo.trim_packages
            ]

            model_list.append({
                "id": str(mo.id),
                "name": mo.name,
                "body_type": mo.body_type,
                "year_start": mo.year_start,
                "year_end": mo.year_end,
                "comfort_score": mo.comfort_score,
                "safety_ratings": get_model_safety_ratings(b.name, mo.name),
                "sahibinden_slug": mo.sahibinden_slug,
                "arabam_slug": mo.arabam_slug,
                "variants": variants_list,
                "trim_packages": trims_list,
            })

        tree.append({
            "brand_id": str(b.id),
            "brand_name": b.name,
            "models": model_list,
        })

    return tree


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}


@app.get("/api/v1/brands")
def brands(db: Session = Depends(get_db)):
    rows = db.scalars(select(m.Brand).where(m.Brand.is_active).order_by(m.Brand.name)).all()
    return [{"id": str(b.id), "name": b.name} for b in rows]


@app.get("/api/v1/vehicles/search")
def search(
    q: str | None = Query(None, description="Marka veya model arama metni"),
    body_type: str | None = None,
    year_min: int | None = None,
    year_max: int | None = None,
    fuel_type: str | None = None,
    transmission_type: str | None = None,
    budget_max: float | None = Query(None, description="İkinci el fiyatı (TL); fiyatı bilinmeyen varyantlar elenmez"),
    km_min: int | None = Query(None, description="Rezerve: ilan verisi entegrasyonuna kadar uygulanmaz"),
    km_max: int | None = Query(None, description="Rezerve: ilan verisi entegrasyonuna kadar uygulanmaz"),
    exclude_brands: str | None = Query(None, description="Virgülle ayrılmış marka adları"),
    exclude_models: str | None = Query(None, description="Virgülle ayrılmış model adları"),
    db: Session = Depends(get_db),
):
    # Üretim yılı saçma/hatalı giriş kontrolü
    if year_min is not None:
        if year_min < 1970 or year_min > 2026:
            raise HTTPException(400, "Geçersiz üretim yılı! Min yıl 1970 ile 2026 arasında olmalıdır.")
    if year_max is not None:
        if year_max < 1970 or year_max > 2026:
            raise HTTPException(400, "Geçersiz üretim yılı! Maks yıl 1970 ile 2026 arasında olmalıdır.")
    if year_min is not None and year_max is not None:
        if year_min > year_max:
            raise HTTPException(400, "Minimum üretim yılı, maksimum üretim yılından büyük olamaz.")

    excl_b = {x.strip().lower() for x in (exclude_brands or "").split(",") if x.strip()}
    excl_m = {x.strip().lower() for x in (exclude_models or "").split(",") if x.strip()}

    query_sel = select(m.CarModel).options(
        joinedload(m.CarModel.brand),
        joinedload(m.CarModel.variants).joinedload(m.Variant.engine),
        joinedload(m.CarModel.variants).joinedload(m.Variant.transmission),
    ).where(m.CarModel.is_active)
    if body_type:
        query_sel = query_sel.where(m.CarModel.body_type == body_type)
    models_ = db.scalars(query_sel).unique().all()

    search_term = q.strip().lower() if q and q.strip() else None

    out = []
    for mo in models_:
        if mo.brand.name.lower() in excl_b or mo.name.lower() in excl_m:
            continue

        # Marka veya model serbest metin + akıllı tahmin (fuzzy) araması
        if search_term:
            if not _fuzzy_match_model(search_term, mo.brand.name, mo.name):
                continue

        vs = [v for v in mo.variants if v.is_active]
        if year_min:
            vs = [v for v in vs if (v.year_end or 9999) >= year_min]
        if year_max:
            vs = [v for v in vs if v.year_start <= year_max]
        if fuel_type:
            vs = [v for v in vs if v.engine.fuel_type == fuel_type]
        if transmission_type:
            t_type = transmission_type.lower()
            if t_type == "otomatik":
                vs = [v for v in vs if v.transmission.type in ["otomatik", "dct", "cvt"]]
            elif t_type == "manuel":
                vs = [v for v in vs if v.transmission.type == "manuel"]
            else:
                vs = [v for v in vs if v.transmission.type == transmission_type]
        if budget_max:
            vs = [v for v in vs if v.used_price_tl is None or float(v.used_price_tl) <= budget_max]
        
        has_variant_filter = any([fuel_type, transmission_type, budget_max, year_min, year_max])
        if has_variant_filter and not vs:
            continue
        if year_min and not vs and (mo.year_end or 9999) < year_min:
            continue
        if year_max and not vs and mo.year_start > year_max:
            continue

        # Şanzıman türlerini sadece Manuel ve Otomatik olarak normalize et
        clean_transmissions = set()
        for v in vs:
            if v.transmission.type in ["otomatik", "dct", "cvt"]:
                clean_transmissions.add("otomatik")
            else:
                clean_transmissions.add("manuel")

        # Fiyat / Performans & Puan Endeksi için varyant verileri
        prices = [float(v.used_price_tl) for v in vs if v.used_price_tl]
        hps = [v.engine.power_hp for v in vs if v.engine and v.engine.power_hp]
        min_price_tl = min(prices) if prices else None
        avg_hp = round(sum(hps) / len(hps)) if hps else 110
        comfort = mo.comfort_score or 7.5
        price_m = max(0.4, (min_price_tl or 1200000) / 1_000_000)
        value_index = round(((comfort * 1.4) + (avg_hp / 45.0)) / price_m, 2)

        clean_search_query = quote_plus(f"{mo.brand.name} {mo.name}")
        out.append({
            "id": str(mo.id),
            "brand": mo.brand.name,
            "name": mo.name,
            "body_type": mo.body_type,
            "year_start": mo.year_start,
            "year_end": mo.year_end,
            "comfort_score": mo.comfort_score,
            "min_price_tl": min_price_tl,
            "avg_hp": avg_hp,
            "value_index": value_index,
            "variants_count": len(vs),
            "fuel_types": sorted({v.engine.fuel_type for v in vs}),
            "transmission_types": sorted(clean_transmissions),
            "listing_urls": {
                "sahibinden": f"https://www.sahibinden.com/kelime-ile-arama?query_text={clean_search_query}",
                "arabam": f"https://www.arabam.com/ikinci-el?searchText={clean_search_query}",
            },
        })

    # Kullanıcı isteği: Önce alfabetik Marka, sonra alfabetik Model (A'dan Z'ye)
    out.sort(key=lambda r: (_tr_sort_key(r["brand"]), _tr_sort_key(r["name"])))
    return out


@app.get("/api/v1/models/{model_id}")
def model_detail(model_id: uuid.UUID, db: Session = Depends(get_db)):
    mo = db.scalars(
        select(m.CarModel).where(m.CarModel.id == model_id).options(
            joinedload(m.CarModel.brand),
            joinedload(m.CarModel.variants).joinedload(m.Variant.engine),
            joinedload(m.CarModel.variants).joinedload(m.Variant.transmission),
            joinedload(m.CarModel.trim_packages),
        )
    ).unique().one_or_none()
    if not mo:
        raise HTTPException(404, "Model bulunamadı")
    return {
        "id": str(mo.id),
        "brand": mo.brand.name,
        "name": mo.name,
        "body_type": mo.body_type,
        "year_start": mo.year_start,
        "year_end": mo.year_end,
        "comfort_score": mo.comfort_score,
        "safety_ratings": get_model_safety_ratings(mo.brand.name, mo.name),
        "variants": [_variant_out(v) for v in mo.variants if v.is_active],
        "trim_packages": [
            {
                "id": str(tp.id),
                "name": tp.name,
                "level": tp.level,
                "summary": tp.summary,
                "features": tp.features,
            }
            for tp in mo.trim_packages
        ],
        "listing_urls": {
            "sahibinden": f"https://www.sahibinden.com/kelime-ile-arama?query_text={quote_plus(f'{mo.brand.name} {mo.name}')}",
            "arabam": f"https://www.arabam.com/ikinci-el?searchText={quote_plus(f'{mo.brand.name} {mo.name}')}",
        },
    }


@app.get("/api/v1/models/{model_id}/ncap-live")
def model_ncap_live(model_id: uuid.UUID, db: Session = Depends(get_db)):
    """Model için Euro NCAP, IIHS ve NHTSA Resmi API (api.nhtsa.gov) entegrasyon verisini döndürür."""
    mo = db.scalars(
        select(m.CarModel).where(m.CarModel.id == model_id).options(joinedload(m.CarModel.brand))
    ).one_or_none()
    if not mo:
        raise HTTPException(404, "Model bulunamadı")
    return {
        "brand": mo.brand.name,
        "model": mo.name,
        "safety_ratings": get_model_safety_ratings(mo.brand.name, mo.name),
        "nhtsa_api_check": fetch_nhtsa_live_api(mo.brand.name, mo.name, mo.year_start or 2021),
    }


class CommentCreate(BaseModel):
    author_name: str | None = Field(default="Anonim Sürücü")
    ownership_status: str | None = Field(default="Sahibiyim")
    mileage_km: int | None = None
    rating: int = Field(default=5, ge=1, le=5)
    recommend: bool = True
    body: str = Field(..., min_length=3)


@app.get("/api/v1/variants/{variant_id}/comments")
def get_variant_comments(variant_id: uuid.UUID, db: Session = Depends(get_db)):
    rows = db.scalars(
        select(UserComment)
        .where(UserComment.variant_id == variant_id)
        .order_by(desc(UserComment.created_at))
    ).all()
    return [
        {
            "id": str(c.id),
            "author_name": c.author_name,
            "ownership_status": c.ownership_status,
            "mileage_km": c.mileage_km,
            "rating": c.rating,
            "recommend": c.recommend,
            "body": c.body,
            "created_at": c.created_at.strftime("%d.%m.%Y") if c.created_at else "Yeni",
        }
        for c in rows
    ]


@app.post("/api/v1/variants/{variant_id}/comments")
def add_variant_comment(
    variant_id: uuid.UUID,
    payload: CommentCreate,
    db: Session = Depends(get_db),
):
    v = db.scalars(select(m.Variant).where(m.Variant.id == variant_id)).first()
    if not v:
        raise HTTPException(404, "Varyant bulunamadı")

    c = UserComment(
        variant_id=variant_id,
        author_name=payload.author_name or "Anonim Sürücü",
        ownership_status=payload.ownership_status or "Sahibiyim",
        mileage_km=payload.mileage_km,
        rating=payload.rating,
        recommend=payload.recommend,
        body=payload.body,
    )
    db.add(c)
    db.commit()
    db.refresh(c)
    return {
        "id": str(c.id),
        "author_name": c.author_name,
        "ownership_status": c.ownership_status,
        "mileage_km": c.mileage_km,
        "rating": c.rating,
        "recommend": c.recommend,
        "body": c.body,
        "created_at": "Şimdi",
    }


@app.get("/api/v1/variants/{variant_id}/faults")
def variant_faults(variant_id: uuid.UUID, db: Session = Depends(get_db)):
    v = db.scalars(
        select(m.Variant).where(m.Variant.id == variant_id).options(
            joinedload(m.Variant.model).joinedload(m.CarModel.brand),
            joinedload(m.Variant.model).joinedload(m.CarModel.trim_packages),
            joinedload(m.Variant.engine),
            joinedload(m.Variant.transmission),
        )
    ).unique().one_or_none()
    if not v:
        raise HTTPException(404, "Varyant bulunamadı")

    faults = [f for f in db.scalars(select(m.FaultReport)).all() if _fault_applies(f, v)]
    faults.sort(key=lambda f: (-SEVERITY_ORDER.index(fault_severity(f)), -float(f.avg_repair_cost_tl)))
    counts = {s: 0 for s in SEVERITY_ORDER}
    for f in faults:
        counts[fault_severity(f)] += 1

    mods = db.scalars(
        select(m.SoftwareMod).where(
            m.SoftwareMod.engine_id == v.engine_id,
            (m.SoftwareMod.transmission_id.is_(None)) | (m.SoftwareMod.transmission_id == v.transmission_id),
        ).options(joinedload(m.SoftwareMod.comments))
    ).unique().all()

    # Kullanıcı yorumları
    comments = db.scalars(
        select(UserComment)
        .where(UserComment.variant_id == variant_id)
        .order_by(desc(UserComment.created_at))
    ).all()

    # Eğer henüz yorum yoksa kullanıcı deneyimini zenginleştirmek için 2 adet gerçekçi kullanıcı yorumu
    comment_list = [
        {
            "id": str(c.id),
            "author_name": c.author_name,
            "ownership_status": c.ownership_status,
            "mileage_km": c.mileage_km,
            "rating": c.rating,
            "recommend": c.recommend,
            "body": c.body,
            "created_at": c.created_at.strftime("%d.%m.%Y") if c.created_at else "Yeni",
        }
        for c in comments
    ]

    # sikayetvar.com kaynaklı gerçekçi kullanıcı ve arıza yorumları
    sikayetvar_reviews = get_model_sikayetvar_reviews(v.model.name, v.model.brand.name)
    all_reviews = comment_list + sikayetvar_reviews

    # Medya ve Analiz Karakteristiği (Performans, Yakıt, Yol Tutuşu, İç Hacim, Kalite, Yalıtım)
    media_specs = get_variant_media_specs(
        brand=v.model.brand.name,
        model_name=v.model.name,
        fuel_type=v.engine.fuel_type,
        body_type=v.model.body_type,
        hp=v.engine.power_hp,
    )

    clean_var_query = quote_plus(f"{v.model.brand.name} {v.model.name}")

    return {
        "variant": {
            **_variant_out(v),
            "brand": v.model.brand.name,
            "model": v.model.name,
            "model_id": str(v.model_id),
            "comfort_score": v.model.comfort_score,
            "body_type": v.model.body_type,
        },
        "safety_ratings": get_model_safety_ratings(v.model.brand.name, v.model.name),
        "media_specs": media_specs,
        "trim_packages": [
            {
                "id": str(tp.id),
                "name": tp.name,
                "level": tp.level,
                "summary": tp.summary,
                "features": tp.features,
            }
            for tp in v.model.trim_packages
        ],
        "listing_urls": {
            "sahibinden": f"https://www.sahibinden.com/kelime-ile-arama?query_text={clean_var_query}",
            "arabam": f"https://www.arabam.com/ikinci-el?searchText={clean_var_query}",
        },
        "fault_summary": {
            "counts": counts,
            "expected_cost_range_tl": [
                sum(float(f.avg_repair_cost_tl) for f in faults),
                sum(float(f.max_repair_cost_tl or f.avg_repair_cost_tl) for f in faults),
            ],
        },
        "faults": [_fault_out(f) for f in faults],
        "user_comments": all_reviews,
        "software_mods": [{
            "id": str(s.id), "mod_type": s.mod_type, "is_recommended": s.is_recommended,
            "hp": [s.hp_before, s.hp_after], "nm": [s.nm_before, s.nm_after],
            "risk_note": s.risk_note, "approx_cost_tl": float(s.approx_cost_tl) if s.approx_cost_tl else None,
            "verified": s.verified,
            "comments": [
                {"author": c.author_name, "body": c.body, "km_at_mod": c.km_at_mod, "outcome": c.outcome}
                for c in s.comments if c.status == "approved"
            ],
        } for s in mods],
    }
