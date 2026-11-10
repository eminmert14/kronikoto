"""KronikOto - Araç Karakteristik Analizi ve Motora/Döneme Özel Görseller.

Kullanıcı Belirlemeleri:
- Karakteristik analizinde yakıt hariç () açıklamaları kaldırıldı, net ve sade terimler kullanıldı.
- Yakıt tüketiminde parantez içi lt/100km verisi korundu.
- Fotoğraflar stüdyo ve beyaz arka plan odaklı yüksek kaliteli otomobil çekimleriyle eşleştirildi.
"""

def get_variant_media_specs(brand: str, model_name: str, fuel_type: str, body_type: str, hp: int):
    """Her varyant ve motor kombinasyonu için avantaj/dezavantaj ve karakteristik analizi üretir."""

    # 1. Motor Performansı (Parantezsiz sade net terim)
    if hp >= 150:
        perf = "Çok İyi"
    elif hp >= 115:
        perf = "İyi"
    elif hp >= 90:
        perf = "Orta"
    else:
        perf = "Düşük"

    # 3. Yakıt Tüketimi (YALNIZCA BURADA PARANTEZ BULUNUR)
    f = fuel_type.lower()
    if f == "dizel":
        fuel_eval = "Çok Az (~4.2 - 5.2 lt / 100km)"
    elif f == "hibrit":
        fuel_eval = "Çok Az (~3.8 - 4.6 lt / 100km)"
    elif f == "lpg":
        fuel_eval = "Ekonomik (~6.5 - 8.0 lt / 100km LPG)"
    elif hp > 140:
        fuel_eval = "Fazla (~7.8 - 9.5 lt / 100km)"
    else:
        fuel_eval = "Normal (~6.0 - 7.2 lt / 100km)"

    # 4. Yol Tutuşu (Parantezsiz)
    m_low = model_name.lower()
    if any(k in m_low for k in ["focus", "golf", "3 serisi", "5 serisi", "a4", "a6", "c serisi", "e serisi", "508", "insignia", "leon", "formentor", "s60", "308"]):
        handling = "Üst Düzey"
    elif body_type.lower() in ["suv", "kombi"]:
        handling = "Dengeli"
    elif any(k in m_low for k in ["egea", "linea", "taliant", "accent", "fiorino", "symbol", "c-elysee", "sandero"]):
        handling = "Standart"
    else:
        handling = "İyi & Dengeli"

    # 5. İç Hacim (Parantezsiz)
    if any(k in m_low for k in ["superb", "passat", "octavia", "a6", "5 serisi", "e serisi", "kodiaq", "insignia", "x-trail", "tiggo 8", "xc60", "c5 aircross", "rifter", "jogger", "glc"]):
        interior = "Çok Geniş"
    elif body_type.lower() == "sedan":
        interior = "Geniş"
    elif body_type.lower() in ["suv", "arazi/suv", "kombi"]:
        interior = "Ferah & Yüksek"
    else:
        interior = "Kompakt"

    # 6. İç Malzeme Kalitesi (Parantezsiz)
    if brand in ["Audi", "BMW", "Mercedes-Benz", "Volvo", "Cupra", "Volkswagen", "Skoda", "Peugeot"]:
        quality = "Yüksek"
    elif brand in ["Toyota", "Honda", "Ford", "Opel", "Kia", "Nissan", "Seat", "Citroen", "Chery"]:
        quality = "İyi & Dayanıklı"
    else:
        quality = "Orta"

    # 7. Kabin & Yol Yalıtımı (Parantezsiz)
    if any(k in m_low for k in ["passat", "superb", "austral", "a4", "a6", "3 serisi", "5 serisi", "c serisi", "e serisi", "glc", "x3", "q3", "kodiaq", "508", "insignia", "xc60", "s60", "xc40", "c5 aircross", "formentor"]):
        insulation = "Çok Başarılı"
    elif any(k in m_low for k in ["megane", "corolla", "focus", "a3", "1 serisi", "a serisi", "cla", "gla", "x1", "q2", "kuga", "408", "308", "karoq", "tiguan", "qashqai", "x-trail", "leon", "ateca", "tiggo 7", "tiggo 8", "c4 x"]):
        insulation = "İyi"
    else:
        insulation = "Orta"

    # 8. Model Artıları (Avantajlar) ve Eksileri (Dezavantajlar)
    advantages = [
        "Türkiye 2. el piyasasında yüksek talep ve hızlı nakite dönebilme",
        "Türkiye geneline yayılmış çok yaygın servis ve yedek parça ağı",
        "Piyasada bol bulunan uygun fiyatlı orijinal ve eşdeğer parça desteği",
    ]
    if f in ["dizel", "hibrit"]:
        advantages.insert(0, "Düşük yakıt tüketimi ile uzun yolda yüksek menzil")

    disadvantages = [
        "Kronik arıza listesinde belirtilen kritik periyodik kontroller aksatılmamalıdır",
        "Yetkili servis ve ağır bakım maliyetleri dikkat gerektirir",
    ]
    if "clio" in model_name.lower() or "egea" in model_name.lower() or "linea" in model_name.lower():
        disadvantages.append("Bozuk zeminlerde arka süspansiyon sertliği")

    return {
        "characteristics": {
            "motor_performansi": perf,
            "yakit_tuketimi": fuel_eval,
            "yol_tutusu": handling,
            "ic_hacim": interior,
            "malzeme_kalitesi": quality,
            "yalitim": insulation,
        },
        "advantages": advantages,
        "disadvantages": disadvantages,
    }
