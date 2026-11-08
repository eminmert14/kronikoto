"""KronikOto - Veritabanı Tohumlama (Seed Script - 50 Model Tam Kapsam)

Kullanım:
    python -m app.seed [--reset]
"""
import sys
from sqlalchemy import select

from .database import SessionLocal, engine
from . import models as m
from .models import Base
from .full_50_data import (
    BRANDS,
    ALL_MODELS,
    ENGINES,
    TRANSMISSIONS,
    ALL_VARIANTS,
    DETAILED_FAULTS,
    DETAILED_SOFTWARE_MODS,
)
from .trim_catalog import ALL_TRIM_PACKAGES


def run(reset: bool = False):
    if reset:
        print("Tablolar sıfırlanıyor (DROP ALL)...")
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    db = SessionLocal()
    try:
        existing_brand = db.scalars(select(m.Brand)).first()
        if existing_brand:
            print("Veri zaten mevcut. Sıfırdan yüklemek için: python -m app.seed --reset")
            return

        print("1. Markalar ekleniyor...")
        brand_map = {}
        for name, country in BRANDS:
            brand_obj = m.Brand(name=name, country=country)
            db.add(brand_obj)
            brand_map[name] = brand_obj
        db.flush()

        print("2. 50 Model ve Donanım Paketleri ekleniyor...")
        car_map = {}
        trim_package_count = 0
        for item in ALL_MODELS:
            brand_name, model_name, body, y_start, y_end = item[0], item[1], item[2], item[3], item[4]
            comfort_score = item[5] if len(item) > 5 else 7.0
            s_slug = item[6] if len(item) > 6 else None
            a_slug = item[7] if len(item) > 7 else None

            car_obj = m.CarModel(
                brand_id=brand_map[brand_name].id,
                name=model_name,
                body_type=body,
                year_start=y_start,
                year_end=y_end,
                comfort_score=comfort_score,
                sahibinden_slug=s_slug,
                arabam_slug=a_slug,
                tags=["populer", "turkiye_pazari"],
            )
            db.add(car_obj)
            car_map[(brand_name, model_name)] = car_obj
        db.flush()

        # Donanım paketlerini ekle (Resmi katalogdan)
        for (b_name, m_name), c_obj in car_map.items():
            trims = ALL_TRIM_PACKAGES.get((b_name, m_name))
            if not trims:
                # Markaya göre doğru resmi paket fallback
                if b_name == "Volkswagen":
                    trims = [
                        {"name": "Impression", "level": "dusuk", "summary": "Başlangıç Donanımı", "features": ["LED Farlar", "Manuel Klima", "Dokunmatik Multimedya", "Hız Sınırlayıcı"]},
                        {"name": "Life / Business", "level": "orta", "summary": "Orta Konfor Donanımı", "features": ["Dijital Klima", "App-Connect CarPlay", "Alaşım Jantlar", "Ön-Arka Park Sensörü"]},
                        {"name": "Elegance / R-Line", "level": "premium", "summary": "En Dolu Donanım", "features": ["Açılır Cam Tavan / Sunroof", "IQ.Light LED Matrix Farlar", "Hayalet Ekran", "Koltuk Isıtma"]},
                    ]
                elif b_name == "Fiat":
                    trims = [
                        {"name": "Easy", "level": "dusuk", "summary": "Ekonomik Donanım", "features": ["Manuel Klima", "Elektrikli Camlar", "Bluetooth", "Yokuş Kalkış Desteği"]},
                        {"name": "Urban", "level": "orta", "summary": "Aile ve Konfor Paketi", "features": ["Alaşım Jantlar", "Dokunmatik Tablet Ekran & CarPlay", "Otomatik Klima", "Park Sensörü"]},
                        {"name": "Lounge", "level": "premium", "summary": "Full Teknoloji Paketi", "features": ["Hayalet Ekran Kadran", "Geri Görüş Kamerası", "Anahtarsız Giriş & Çalıştırma", "17\" Elmas Kesim Jantlar"]},
                    ]
                elif b_name == "Ford":
                    trims = [
                        {"name": "Trend X", "level": "dusuk", "summary": "Giriş Seviyesi", "features": ["16\" Alaşım Jant", "Manuel Klima", "Hız Sabitleyici", "Deri Direksiyon"]},
                        {"name": "Titanium", "level": "orta", "summary": "Konfor Paketi", "features": ["SYNC Dokunmatik Ekran", "Çift Bölgeli Dijital Klima", "Anahtarsız Çalıştırma", "Park Sensörü"]},
                        {"name": "ST-Line / Titanium X", "level": "premium", "summary": "Sportif Zirve", "features": ["Açılır Sunroof", "Full LED Farlar", "Spor Gövde Kiti", "Geri Görüş Kamerası"]},
                    ]
                elif b_name == "Peugeot":
                    trims = [
                        {"name": "Active", "level": "dusuk", "summary": "Şehir Başlangıç Donanımı", "features": ["Dokunmatik Ekran", "Manuel Klima", "Hız Sabitleyici", "LED Gündüz Farı"]},
                        {"name": "Allure", "level": "orta", "summary": "3D i-Cockpit Konforu", "features": ["3D Dijital Gösterge", "Otomatik Klima", "Geri Görüş Kamerası", "Alaşım Jantlar"]},
                        {"name": "GT", "level": "premium", "summary": "Zirve Şıklık ve Spor Tasarım", "features": ["Açılır Cam Tavan", "Full LED 3 Pençeli Farlar", "Koltuk Isıtma", "Kör Nokta Uyarısı"]},
                    ]
                elif b_name == "Skoda":
                    trims = [
                        {"name": "Elite", "level": "dusuk", "summary": "Giriş Seviyesi", "features": ["LED Farlar", "Dijital Klima", "SmartLink", "Hız Sabitleyici"]},
                        {"name": "Premium", "level": "orta", "summary": "Yüksek Konfor", "features": ["Dijital Hayalet Gösterge", "Geri Görüş Kamerası", "Anahtarsız Çalıştırma", "Alaşım Jantlar"]},
                        {"name": "Prestige", "level": "premium", "summary": "Lüks Zirve Donanım", "features": ["Açılır Cam Tavan / Sunroof", "Matrix LED Farlar", "Koltuk Isıtma", "Elektrikli Bagaj"]},
                    ]
                elif b_name in ["Hyundai", "Kia"]:
                    trims = [
                        {"name": "Jump / Cool", "level": "dusuk", "summary": "Başlangıç Donanımı", "features": ["Manuel Klima", "Bluetooth Radyo", "Hız Sabitleyici", "Elektrikli Ön Camlar"]},
                        {"name": "Style / Elegance", "level": "orta", "summary": "Dengeli Donanım", "features": ["Dokunmatik Ekran & CarPlay", "Geri Görüş Kamerası", "Alaşım Jantlar", "Otomatik Klima"]},
                        {"name": "Elite / Prestige", "level": "premium", "summary": "En Dolu Donanım", "features": ["Açılır Sunroof", "Dijital Hayalet Kadran", "Koltuk Isıtma", "Anahtarsız Giriş & Çalıştırma"]},
                    ]
                elif b_name == "Opel":
                    trims = [
                        {"name": "Edition", "level": "dusuk", "summary": "Giriş Seviyesi", "features": ["Dokunmatik Ekran & CarPlay", "Manuel Klima", "Hız Sabitleyici", "Alaşım Jantlar"]},
                        {"name": "Elegance", "level": "orta", "summary": "Konfor Donanımı", "features": ["Dijital Sürücü Ekranı", "Otomatik Klima", "Geri Görüş Kamerası", "Katlanır Aynalar"]},
                        {"name": "GS / Ultimate", "level": "premium", "summary": "Sportif Zirve", "features": ["Cam Tavan / Sunroof", "IntelliLux LED Matrix Farlar", "Koltuk Isıtma", "Alcantara Koltuklar"]},
                    ]
                elif b_name == "Dacia":
                    trims = [
                        {"name": "Essential", "level": "dusuk", "summary": "Ekonomik Giriş", "features": ["Manuel Klima", "Elektrikli Ön Camlar", "Bluetooth", "Yokuş Kalkış Desteği"]},
                        {"name": "Expression", "level": "orta", "summary": "Kullanışlı Donanım", "features": ["8\" Dokunmatik Ekran & CarPlay", "Alaşım Jantlar", "Arka Park Sensörü", "Sis Farları"]},
                        {"name": "Extreme / Journey", "level": "premium", "summary": "En Dolu Macera Paketi", "features": ["Otomatik Klima", "Eller Serbest Kart", "Geri Görüş Kamerası", "Kör Nokta Uyarısı"]},
                    ]
                else:
                    trims = [
                        {"name": "Vision / Standart", "level": "dusuk", "summary": "Başlangıç Donanımı", "features": ["Manuel Klima", "Elektrikli Camlar", "Bluetooth", "Hız Sabitleyici"]},
                        {"name": "Comfort / Dynamic", "level": "orta", "summary": "Orta Konfor Paketi", "features": ["Dokunmatik Ekran & CarPlay", "Alaşım Jantlar", "Geri Görüş Kamerası", "Otomatik Klima"]},
                        {"name": "Premium / Exclusive", "level": "premium", "summary": "Zirve Donanım", "features": ["Sunroof", "LED Farlar", "Koltuk Isıtma", "Anahtarsız Giriş & Çalıştırma"]},
                    ]
            for tp in trims:
                trim_obj = m.TrimPackage(
                    model_id=c_obj.id,
                    name=tp["name"],
                    level=tp["level"],
                    summary=tp.get("summary", ""),
                    features=tp.get("features", []),
                )
                db.add(trim_obj)
                trim_package_count += 1
        db.flush()

        print("3. Motorlar ve Şanzımanlar ekleniyor...")
        engine_map = {}
        for k, (code, label, fuel, cc, hp, nm, tech) in ENGINES.items():
            eng_obj = m.Engine(
                code=code,
                label=label,
                fuel_type=fuel,
                displacement_cc=cc,
                power_hp=hp,
                torque_nm=nm,
                technology=tech,
            )
            db.add(eng_obj)
            engine_map[k] = eng_obj

        trans_map = {}
        for k, (t_type, label, speeds, manufacturer) in TRANSMISSIONS.items():
            tr_obj = m.Transmission(
                type=t_type,
                label=label,
                speeds=speeds,
                manufacturer=manufacturer,
            )
            db.add(tr_obj)
            trans_map[k] = tr_obj
        db.flush()

        print("4. 50 Modelin tüm aktif varyantları ekleniyor...")
        variant_count = 0
        for brand_name, model_name, e_key, t_key, y_start, y_end, price in ALL_VARIANTS:
            car_obj = car_map.get((brand_name, model_name))
            eng_obj = engine_map.get(e_key)
            tr_obj = trans_map.get(t_key)
            if not car_obj or not eng_obj or not tr_obj:
                print(f"HATA: Eşleşmeyen varyant tanımı: {brand_name} {model_name} {e_key} {t_key}")
                continue

            v_obj = m.Variant(
                model_id=car_obj.id,
                engine_id=eng_obj.id,
                transmission_id=tr_obj.id,
                year_start=y_start,
                year_end=y_end,
                used_price_tl=price,
            )
            db.add(v_obj)
            variant_count += 1
        db.flush()

        print("5. Detaylı ve doğrulanmış arıza raporları ekleniyor...")
        fault_count = 0
        for f in DETAILED_FAULTS:
            eng_id = engine_map[f["e"]].id if "e" in f else None
            tr_id = trans_map[f["t"]].id if "t" in f else None
            model_id = car_map[f["m"]].id if "m" in f else None

            fault_obj = m.FaultReport(
                engine_id=eng_id,
                transmission_id=tr_id,
                model_id=model_id,
                title=f["title"],
                description=f["description"],
                category=f["category"],
                avg_repair_cost_tl=f["avg"],
                max_repair_cost_tl=f.get("max"),
                severity_override=f.get("override"),
                occurrence_km_start=f["km"][0],
                occurrence_km_end=f["km"][1],
                report_count=f.get("n", 60),
                sources=f.get("sources", []),
                checklist=f.get("checklist", []),
                verified=True,
            )
            db.add(fault_obj)
            fault_count += 1
        db.flush()

        print("6. Stage / Yazılım paketleri ve onaylı kullanıcı deneyimleri ekleniyor...")
        mod_count = 0
        for sm in DETAILED_SOFTWARE_MODS:
            eng_id = engine_map[sm["e"]].id
            tr_id = trans_map[sm["t"]].id if sm.get("t") else None

            mod_obj = m.SoftwareMod(
                engine_id=eng_id,
                transmission_id=tr_id,
                mod_type=sm.get("mod_type", "stage1"),
                is_recommended=sm.get("rec"),
                hp_before=sm["hp"][0],
                hp_after=sm["hp"][1],
                nm_before=sm["nm"][0],
                nm_after=sm["nm"][1],
                risk_note=sm.get("risk"),
                approx_cost_tl=sm.get("cost"),
                verified=True,
            )
            db.add(mod_obj)
            db.flush()
            mod_count += 1

            for author, body, km_mod, outcome in sm.get("comments", []):
                comment_obj = m.SoftwareModComment(
                    mod_id=mod_obj.id,
                    author_name=author,
                    body=body,
                    km_at_mod=km_mod,
                    outcome=outcome,
                    status="approved",
                )
                db.add(comment_obj)

        db.commit()
        print("\n✅ TÜM 50 MODEL İÇİN SEED İŞLEMİ BAŞARIYLA TAMAMLANDI!")
        print(f"   • Markalar: {len(BRANDS)}")
        print(f"   • Toplam Model: {len(ALL_MODELS)} (50 modelin tamamı)")
        print(f"   • Tanımlı Motorlar: {len(ENGINES)}")
        print(f"   • Tanımlı Şanzımanlar: {len(TRANSMISSIONS)}")
        print(f"   • Aktif Varyant Sayısı: {variant_count}")
        print(f"   • Donanım Paketleri: {trim_package_count}")
        print(f"   • Kronik Arıza Kayıtları: {fault_count}")
        print(f"   • Stage / Yazılım Paketleri: {mod_count}")

    except Exception as e:
        db.rollback()
        print(f"HATA OLUŞTU: {e}")
        raise e
    finally:
        db.close()


if __name__ == "__main__":
    run(reset="--reset" in sys.argv)
