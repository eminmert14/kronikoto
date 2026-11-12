"""KronikOto - 50 Model Tam Kapsamlı Veri Tabanı

Yenilikler:
- Gerçekçi Konfor Puanı (10/10 kaldırıldı, her araca yalıtım ve süspansiyonuna göre gerçek puan)
- Yeni Maliyet Ölçeği (<= 10k: Düşük, <= 30k: Orta, <= 80k: Yüksek, > 80k: Çok Yüksek)
- https://www.sikayetvar.com/ Kullanıcı Şikayetleri ve Usta/Ekspertiz Raporları
- Donanım Paketleri & Özellikleri (Düşük / Orta / Premium paketler; Sunroof, Koltuk Isıtma vb.)
- Sahibinden ve Arabam.com kategori eşleştirmeleri
"""

BRANDS = [
    ("Renault", "Fransa"),
    ("Fiat", "İtalya"),
    ("Volkswagen", "Almanya"),
    ("Toyota", "Japonya"),
    ("Honda", "Japonya"),
    ("Ford", "ABD"),
    ("Peugeot", "Fransa"),
    ("Skoda", "Çekya"),
    ("Hyundai", "Güney Kore"),
    ("Kia", "Güney Kore"),
    ("Opel", "Almanya"),
    ("Dacia", "Romanya"),
    ("Audi", "Almanya"),
    ("BMW", "Almanya"),
    ("Mercedes-Benz", "Almanya"),
    ("Nissan", "Japonya"),
    ("Seat", "İspanya"),
    ("Citroen", "Fransa"),
    ("Volvo", "İsveç"),
    ("Cupra", "İspanya"),
    ("Chery", "Çin"),
    ("Togg", "Türkiye"),
    ("Tesla", "ABD"),
    ("BYD", "Çin"),
    ("MG", "İngiltere / Çin"),
    ("Suzuki", "Japonya"),
]

# (marka, model_adi, kasa_tipi, yil_bas, yil_son, konfor_puani, sahibinden_slug, arabam_slug)
ALL_MODELS = [
    # Renault (10)
    ("Renault", "Megane 4 Sedan", "sedan", 2016, None, 7.9, "renault-megane", "renault/megane"),
    ("Renault", "Megane 3", "sedan", 2008, 2016, 6.8, "renault-megane", "renault/megane"),
    ("Renault", "Fluence", "sedan", 2009, 2016, 6.6, "renault-fluence", "renault/fluence"),
    ("Renault", "Clio 5", "hatchback", 2019, None, 7.3, "renault-clio", "renault/clio"),
    ("Renault", "Clio 4", "hatchback", 2012, 2019, 6.5, "renault-clio", "renault/clio"),
    ("Renault", "Captur", "suv", 2013, None, 7.2, "renault-captur", "renault/captur"),
    ("Renault", "Kadjar", "suv", 2015, None, 7.7, "renault-kadjar", "renault/kadjar"),
    ("Renault", "Austral", "suv", 2022, None, 8.5, "renault-austral", "renault/austral"),
    ("Renault", "Taliant", "sedan", 2021, None, 6.2, "renault-taliant", "renault/taliant"),
    ("Renault", "Symbol", "sedan", 2013, 2021, 5.6, "renault-symbol", "renault/symbol"),

    # Fiat (5)
    ("Fiat", "Egea Sedan", "sedan", 2015, None, 6.7, "fiat-egea", "fiat/egea"),
    ("Fiat", "Egea Cross", "suv", 2020, None, 6.9, "fiat-egea-cross", "fiat/egea-cross"),
    ("Fiat", "Linea", "sedan", 2007, 2018, 5.8, "fiat-linea", "fiat/linea"),
    ("Fiat", "Doblo", "kombi", 2010, None, 6.0, "fiat-doblo", "fiat/doblo"),
    ("Fiat", "Fiorino Combi", "kombi", 2008, None, 5.7, "fiat-fiorino", "fiat/fiorino"),

    # Volkswagen (9)
    ("Volkswagen", "Passat B8", "sedan", 2015, 2023, 8.8, "volkswagen-passat", "volkswagen/passat"),
    ("Volkswagen", "Passat B7", "sedan", 2011, 2015, 8.2, "volkswagen-passat", "volkswagen/passat"),
    ("Volkswagen", "Jetta", "sedan", 2011, 2018, 7.8, "volkswagen-jetta", "volkswagen/jetta"),
    ("Volkswagen", "Golf 7", "hatchback", 2012, 2020, 8.3, "volkswagen-golf", "volkswagen/golf"),
    ("Volkswagen", "Polo", "hatchback", 2017, None, 7.5, "volkswagen-polo", "volkswagen/polo"),
    ("Volkswagen", "Taigo", "suv", 2021, None, 7.6, "volkswagen-taigo", "volkswagen/taigo"),
    ("Volkswagen", "Tiguan", "suv", 2016, None, 8.5, "volkswagen-tiguan", "volkswagen/tiguan"),
    ("Volkswagen", "T-Roc", "suv", 2017, None, 7.8, "volkswagen-t-roc", "volkswagen/t-roc"),
    ("Volkswagen", "Caddy", "kombi", 2010, None, 6.6, "volkswagen-caddy", "volkswagen/caddy"),

    # Toyota (6)
    ("Toyota", "Corolla E210", "sedan", 2019, None, 8.0, "toyota-corolla", "toyota/corolla"),
    ("Toyota", "Corolla E180", "sedan", 2013, 2018, 7.4, "toyota-corolla", "toyota/corolla"),
    ("Toyota", "Auris", "hatchback", 2013, 2018, 7.4, "toyota-auris", "toyota/auris"),
    ("Toyota", "C-HR", "suv", 2016, None, 7.8, "toyota-c-hr", "toyota/c-hr"),
    ("Toyota", "Yaris", "hatchback", 2020, None, 7.2, "toyota-yaris", "toyota/yaris"),
    ("Toyota", "RAV4", "suv", 2019, None, 8.6, "toyota-rav4", "toyota/rav4"),

    # Honda (5)
    ("Honda", "Civic FC5", "sedan", 2016, 2021, 8.1, "honda-civic", "honda/civic"),
    ("Honda", "City", "sedan", 2020, None, 6.9, "honda-city", "honda/city"),
    ("Honda", "CR-V", "suv", 2017, None, 8.6, "honda-cr-v", "honda/cr-v"),
    ("Honda", "HR-V", "suv", 2015, None, 7.8, "honda-hr-v", "honda/hr-v"),
    ("Honda", "Jazz", "hatchback", 2015, None, 7.3, "honda-jazz", "honda/jazz"),

    # Hyundai (7)
    ("Hyundai", "i20", "hatchback", 2014, None, 7.0, "hyundai-i20", "hyundai/i20"),
    ("Hyundai", "i30", "hatchback", 2012, None, 7.6, "hyundai-i30", "hyundai/i30"),
    ("Hyundai", "Accent Blue", "sedan", 2011, 2018, 6.4, "hyundai-accent-blue", "hyundai/accent-blue"),
    ("Hyundai", "Elantra", "sedan", 2016, None, 7.7, "hyundai-elantra", "hyundai/elantra"),
    ("Hyundai", "Tucson", "suv", 2015, None, 8.2, "hyundai-tucson", "hyundai/tucson"),
    ("Hyundai", "Kona", "suv", 2018, None, 7.6, "hyundai-kona", "hyundai/kona"),
    ("Hyundai", "Bayon", "suv", 2021, None, 7.1, "hyundai-bayon", "hyundai/bayon"),

    # Kia (6)
    ("Kia", "Sportage", "suv", 2016, None, 8.2, "kia-sportage", "kia/sportage"),
    ("Kia", "XCeed", "suv", 2019, None, 7.9, "kia-xceed", "kia/xceed"),
    ("Kia", "Ceed", "hatchback", 2018, None, 7.7, "kia-ceed", "kia/ceed"),
    ("Kia", "Rio", "hatchback", 2017, None, 6.9, "kia-rio", "kia/rio"),
    ("Kia", "Picanto", "hatchback", 2017, None, 6.5, "kia-picanto", "kia/picanto"),
    ("Kia", "Stonic", "suv", 2017, None, 7.1, "kia-stonic", "kia/stonic"),

    # Ford (6)
    ("Ford", "Focus 3", "sedan", 2011, 2018, 7.7, "ford-focus", "ford/focus"),
    ("Ford", "Focus 4", "sedan", 2018, 2025, 8.4, "ford-focus", "ford/focus"),
    ("Ford", "Fiesta", "hatchback", 2008, 2023, 7.1, "ford-fiesta", "ford/fiesta"),
    ("Ford", "Puma", "suv", 2019, None, 7.6, "ford-puma", "ford/puma"),
    ("Ford", "Kuga", "suv", 2013, None, 8.3, "ford-kuga", "ford/kuga"),
    ("Ford", "Tourneo Courier", "kombi", 2014, None, 6.3, "ford-tourneo-courier", "ford/tourneo-courier"),

    # Peugeot (8)
    ("Peugeot", "208", "hatchback", 2019, None, 7.5, "peugeot-208", "peugeot/208"),
    ("Peugeot", "308", "hatchback", 2014, None, 8.0, "peugeot-308", "peugeot/308"),
    ("Peugeot", "2008", "suv", 2019, None, 7.8, "peugeot-2008", "peugeot/2008"),
    ("Peugeot", "3008", "suv", 2016, None, 8.6, "peugeot-3008", "peugeot/3008"),
    ("Peugeot", "408", "suv", 2022, None, 8.5, "peugeot-408", "peugeot/408"),
    ("Peugeot", "508", "sedan", 2018, None, 8.6, "peugeot-508", "peugeot/508"),
    ("Peugeot", "Rifter", "kombi", 2019, None, 7.3, "peugeot-rifter", "peugeot/rifter"),
    ("Peugeot", "301", "sedan", 2013, None, 5.7, "peugeot-301", "peugeot/301"),

    # Opel (5)
    ("Opel", "Astra K", "sedan", 2015, 2021, 7.8, "opel-astra", "opel/astra"),
    ("Opel", "Insignia", "sedan", 2017, 2022, 8.6, "opel-insignia", "opel/insignia"),
    ("Opel", "Corsa F", "hatchback", 2019, None, 7.3, "opel-corsa", "opel/corsa"),
    ("Opel", "Mokka", "suv", 2020, None, 7.8, "opel-mokka", "opel/mokka"),
    ("Opel", "Grandland", "suv", 2017, None, 8.2, "opel-grandland", "opel/grandland"),

    # Dacia (3)
    ("Dacia", "Duster", "suv", 2010, None, 6.3, "dacia-duster", "dacia/duster"),
    ("Dacia", "Sandero Stepway", "suv", 2013, None, 6.4, "dacia-sandero", "dacia/sandero"),
    ("Dacia", "Jogger", "suv", 2022, None, 6.8, "dacia-jogger", "dacia/jogger"),

    # Skoda (7)
    ("Skoda", "Octavia", "sedan", 2013, None, 8.4, "skoda-octavia", "skoda/octavia"),
    ("Skoda", "Superb", "sedan", 2015, None, 8.9, "skoda-superb", "skoda/superb"),
    ("Skoda", "Scala", "hatchback", 2019, None, 7.8, "skoda-scala", "skoda/scala"),
    ("Skoda", "Fabia", "hatchback", 2015, None, 7.3, "skoda-fabia", "skoda/fabia"),
    ("Skoda", "Kamiq", "suv", 2019, None, 7.8, "skoda-kamiq", "skoda/kamiq"),
    ("Skoda", "Karoq", "suv", 2018, None, 8.3, "skoda-karoq", "skoda/karoq"),
    ("Skoda", "Kodiaq", "suv", 2017, None, 8.7, "skoda-kodiaq", "skoda/kodiaq"),

    # Audi (5)
    ("Audi", "A3 Sedan", "sedan", 2013, None, 8.6, "audi-a3", "audi/a3"),
    ("Audi", "A4 Sedan", "sedan", 2015, None, 9.0, "audi-a4", "audi/a4"),
    ("Audi", "A6 Sedan", "sedan", 2015, None, 9.4, "audi-a6", "audi/a6"),
    ("Audi", "Q2", "suv", 2016, None, 8.0, "audi-q2", "audi/q2"),
    ("Audi", "Q3", "suv", 2018, None, 8.6, "audi-q3", "audi/q3"),

    # BMW (5)
    ("BMW", "1 Serisi", "hatchback", 2012, None, 8.2, "bmw-1-serisi", "bmw/1-serisi"),
    ("BMW", "3 Serisi", "sedan", 2012, None, 8.9, "bmw-3-serisi", "bmw/3-serisi"),
    ("BMW", "5 Serisi", "sedan", 2011, None, 9.4, "bmw-5-serisi", "bmw/5-serisi"),
    ("BMW", "X1", "suv", 2015, None, 8.3, "bmw-x1", "bmw/x1"),
    ("BMW", "X3", "suv", 2017, None, 9.0, "bmw-x3", "bmw/x3"),

    # Mercedes-Benz (6)
    ("Mercedes-Benz", "A Serisi", "hatchback", 2013, None, 8.2, "mercedes-benz-a-serisi", "mercedes-benz/a-serisi"),
    ("Mercedes-Benz", "C Serisi", "sedan", 2014, None, 9.0, "mercedes-benz-c-serisi", "mercedes-benz/c-serisi"),
    ("Mercedes-Benz", "E Serisi", "sedan", 2013, None, 9.5, "mercedes-benz-e-serisi", "mercedes-benz/e-serisi"),
    ("Mercedes-Benz", "CLA", "sedan", 2013, None, 8.1, "mercedes-benz-cla", "mercedes-benz/cla"),
    ("Mercedes-Benz", "GLA", "suv", 2014, None, 8.3, "mercedes-benz-gla", "mercedes-benz/gla"),
    ("Mercedes-Benz", "GLC", "suv", 2015, None, 9.2, "mercedes-benz-glc", "mercedes-benz/glc"),

    # Nissan (4)
    ("Nissan", "Qashqai", "suv", 2014, None, 8.1, "nissan-qashqai", "nissan/qashqai"),
    ("Nissan", "Juke", "suv", 2014, None, 7.3, "nissan-juke", "nissan/juke"),
    ("Nissan", "Micra", "hatchback", 2017, None, 7.1, "nissan-micra", "nissan/micra"),
    ("Nissan", "X-Trail", "suv", 2014, None, 8.5, "nissan-x-trail", "nissan/x-trail"),

    # Seat (4)
    ("Seat", "Leon", "hatchback", 2013, None, 8.0, "seat-leon", "seat/leon"),
    ("Seat", "Ibiza", "hatchback", 2017, None, 7.3, "seat-ibiza", "seat/ibiza"),
    ("Seat", "Arona", "suv", 2017, None, 7.5, "seat-arona", "seat/arona"),
    ("Seat", "Ateca", "suv", 2016, None, 8.1, "seat-ateca", "seat/ateca"),

    # Citroen (4)
    ("Citroen", "C5 Aircross", "suv", 2019, None, 8.8, "citroen-c5-aircross", "citroen/c5-aircross"),
    ("Citroen", "C4 X", "suv", 2022, None, 8.3, "citroen-c4-x", "citroen/c4-x"),
    ("Citroen", "C3 Aircross", "suv", 2017, None, 7.5, "citroen-c3-aircross", "citroen/c3-aircross"),
    ("Citroen", "C-Elysee", "sedan", 2013, 2021, 5.7, "citroen-c-elysee", "citroen/c-elysee"),

    # Volvo (3)
    ("Volvo", "XC40", "suv", 2018, None, 8.8, "volvo-xc40", "volvo/xc40"),
    ("Volvo", "XC60", "suv", 2017, None, 9.3, "volvo-xc60", "volvo/xc60"),
    ("Volvo", "S60", "sedan", 2019, None, 9.1, "volvo-s60", "volvo/s60"),

    # Cupra (1)
    ("Cupra", "Formentor", "suv", 2020, None, 8.6, "cupra-formentor", "cupra/formentor"),

    # Chery (3)
    ("Chery", "Tiggo 7 Pro", "suv", 2023, None, 8.1, "chery-tiggo-7-pro", "chery/tiggo-7-pro"),
    ("Chery", "Tiggo 8 Pro", "suv", 2023, None, 8.4, "chery-tiggo-8-pro", "chery/tiggo-8-pro"),
    ("Chery", "Omoda 5", "suv", 2023, None, 8.0, "chery-omoda-5", "chery/omoda-5"),

    # Togg (1)
    ("Togg", "T10X", "suv", 2023, None, 8.7, "togg-t10x", "togg/t10x"),

    # Yeni Popüler Türkiye Modelleri
    ("Opel", "Astra J", "sedan", 2010, 2018, 7.6, "opel-astra", "opel/astra"),
    ("Opel", "Crossland", "suv", 2017, None, 7.4, "opel-crossland", "opel/crossland"),
    ("Volkswagen", "Golf 8", "hatchback", 2020, None, 8.5, "volkswagen-golf", "volkswagen/golf"),
    ("Volkswagen", "T-Cross", "suv", 2019, None, 7.6, "volkswagen-t-cross", "volkswagen/t-cross"),
    ("Hyundai", "i10", "hatchback", 2014, None, 6.8, "hyundai-i10", "hyundai/i10"),
    ("Hyundai", "Accent Era", "sedan", 2006, 2012, 6.1, "hyundai-accent-era", "hyundai/accent-era"),
    ("Fiat", "Punto", "hatchback", 2006, 2018, 6.2, "fiat-punto", "fiat/punto"),
    ("Citroen", "C3", "hatchback", 2016, None, 7.3, "citroen-c3", "citroen/c3"),

    # Elektrikli Modeller (5)
    ("Tesla", "Model Y", "suv", 2022, None, 8.9, "tesla-model-y", "tesla/model-y"),
    ("BYD", "Atto 3", "suv", 2023, None, 8.4, "byd-atto-3", "byd/atto-3"),
    ("BYD", "Seal U", "suv", 2024, None, 8.7, "byd-seal-u", "byd/seal-u"),
    ("MG", "MG4 Electric", "hatchback", 2023, None, 8.2, "mg-mg4", "mg/mg4"),
    ("Renault", "Megane E-Tech", "hatchback", 2022, None, 8.5, "renault-megane-e-tech", "renault/megane-e-tech"),

    # Station Wagon Modeller (6)
    ("Volkswagen", "Passat Variant", "station", 2015, 2023, 8.9, "volkswagen-passat-variant", "volkswagen/passat-variant"),
    ("Skoda", "Octavia Combi", "station", 2013, None, 8.5, "skoda-octavia-combi", "skoda/octavia-combi"),
    ("Renault", "Megane Sport Tourer", "station", 2016, None, 8.0, "renault-megane-sport-tourer", "renault/megane-sport-tourer"),
    ("Fiat", "Egea Station Wagon", "station", 2016, None, 6.8, "fiat-egea-station-wagon", "fiat/egea-station-wagon"),
    ("Volvo", "V60", "station", 2018, None, 9.2, "volvo-v60", "volvo/v60"),
    ("Ford", "Focus SW", "station", 2018, 2025, 8.4, "ford-focus-sw", "ford/focus-sw"),

    # Coupe Modeller (5)
    ("BMW", "4 Serisi Coupe", "coupe", 2014, None, 8.8, "bmw-4-serisi", "bmw/4-serisi"),
    ("Mercedes-Benz", "C Serisi Coupe", "coupe", 2015, 2023, 8.9, "mercedes-benz-c-serisi-coupe", "mercedes-benz/c-serisi-coupe"),
    ("Audi", "A5 Coupe", "coupe", 2016, None, 8.9, "audi-a5", "audi/a5"),
    ("Volkswagen", "Scirocco", "coupe", 2009, 2017, 7.6, "volkswagen-scirocco", "volkswagen/scirocco"),
    ("BMW", "2 Serisi Coupe", "coupe", 2014, None, 8.3, "bmw-2-serisi", "bmw/2-serisi"),

    # Ticari / Kombi Modeller (5)
    ("Renault", "Kangoo", "kombi", 2013, None, 6.7, "renault-kangoo", "renault/kangoo"),
    ("Citroen", "Berlingo", "kombi", 2018, None, 7.3, "citroen-berlingo", "citroen/berlingo"),
    ("Volkswagen", "Transporter", "kombi", 2015, None, 7.7, "volkswagen-transporter", "volkswagen/transporter"),
    ("Opel", "Combo", "kombi", 2018, None, 7.2, "opel-combo", "opel/combo"),
    ("Ford", "Tourneo Connect", "kombi", 2014, None, 7.4, "ford-tourneo-connect", "ford/tourneo-connect"),

    # Türkiye Piyasası Ek Popüler Modeller (8)
    ("MG", "ZS", "suv", 2021, None, 7.6, "mg-zs", "mg/zs"),
    ("MG", "HS", "suv", 2021, None, 8.2, "mg-hs", "mg/hs"),
    ("Suzuki", "Vitara", "suv", 2015, None, 7.7, "suzuki-vitara", "suzuki/vitara"),
    ("Suzuki", "Swift", "hatchback", 2017, None, 7.2, "suzuki-swift", "suzuki/swift"),
    ("Peugeot", "206", "hatchback", 2000, 2012, 6.0, "peugeot-206", "peugeot/206"),
    ("Opel", "Vectra C", "sedan", 2002, 2009, 7.4, "opel-vectra", "opel/vectra"),
    ("Skoda", "Rapid", "sedan", 2013, 2019, 7.1, "skoda-rapid", "skoda/rapid"),
    ("Toyota", "Corolla Cross", "suv", 2022, None, 8.4, "toyota-corolla-cross", "toyota/corolla-cross"),
]

# (kod, etiket, yakıt, cc, hp, nm, teknoloji)
ENGINES = {
    # Renault & Dacia
    "ren_k9k_110": ("K9K 656", "1.5 dCi 110 HP", "dizel", 1461, 110, 260, "Turbo Dizel Common-Rail"),
    "ren_k9k_115": ("K9K 872", "1.5 Blue dCi 115 HP", "dizel", 1461, 115, 260, "Turbo Dizel AdBlue"),
    "ren_13_tce": ("H5Ht", "1.3 TCe 140 HP", "benzin", 1332, 140, 240, "Direkt Enjeksiyon Turbo"),
    "ren_13_tce_150": ("H5Ht-150", "1.3 TCe 150 HP", "benzin", 1332, 150, 250, "Direkt Enjeksiyon Turbo"),
    "ren_12_tce_sorunlu": ("H5Ft", "1.2 TCe 125 HP (Sorunlu Seri)", "benzin", 1197, 125, 205, "Direkt Enjeksiyon Turbo"),
    "ren_16_sce": ("H4M", "1.6 SCe 115 HP", "benzin", 1598, 115, 156, "Atmosferik Çok Nokta Enjeksiyon"),
    "ren_10_tce": ("H4D", "1.0 TCe 100 HP", "benzin", 999, 100, 160, "Turbo 3 Silindir"),
    "ren_10_tce_lpg": ("H4Dt-LPG", "1.0 ECO-G LPG 100 HP", "lpg", 999, 100, 170, "Fabrikasyon LPG Turbo"),
    "ren_09_tce": ("H4Bt", "0.9 TCe 90 HP", "benzin", 898, 90, 140, "Turbo 3 Silindir"),
    "ren_10_sce": ("B4D", "1.0 SCe 72 HP", "benzin", 999, 72, 95, "Atmosferik 3 Silindir"),

    # Fiat
    "fiat_14_fire": ("Fire 350A1000", "1.4 Fire 95 HP", "benzin", 1368, 95, 127, "Atmosferik 16V"),
    "fiat_13_mjet": ("199B1000", "1.3 Multijet II 95 HP", "dizel", 1248, 95, 200, "Turbo Dizel DPF"),
    "fiat_16_mjet": ("55280444", "1.6 Multijet II 120 HP", "dizel", 1598, 120, 320, "Değişken Geometrili Turbo Dizel"),
    "fiat_16_mjet_130": ("46346020", "1.6 Multijet II 130 HP", "dizel", 1598, 130, 320, "Euro 6D Dizel"),
    "fiat_15_t4_hyb": ("FireFly-T4", "1.5 T4 Hibrit 130 HP", "hibrit", 1469, 130, 240, "48V BSG Mild-Hybrid Turbo"),

    # VAG
    "vag_16_tdi": ("EA288", "1.6 TDI 120 HP", "dizel", 1598, 120, 250, "Turbo Dizel Common-Rail"),
    "vag_16_tdi_cayc": ("EA189-CAYC", "1.6 TDI 105 HP (CAYC)", "dizel", 1598, 105, 250, "Turbo Dizel Common-Rail"),
    "vag_14_tsi": ("EA211", "1.4 TSI 150 HP", "benzin", 1395, 150, 250, "Turbo Direkt Enjeksiyon ACT"),
    "vag_14_tsi_122": ("EA111-CAXA", "1.4 TSI 122 HP (Zincirli Seri)", "benzin", 1390, 122, 200, "Turbo Direkt Enjeksiyon Zincirli"),
    "vag_15_tsi": ("EA211 evo", "1.5 TSI 150 HP ACT", "benzin", 1498, 150, 250, "Miller Döngüsü Değişken Turbo"),
    "vag_15_etec": ("EA211 e-TEC", "1.5 e-TEC 150 HP mHEV", "hibrit", 1498, 150, 250, "48V Mild-Hybrid Değişken Turbo"),
    "vag_12_tsi": ("EA211", "1.2 TSI 105 HP", "benzin", 1197, 105, 175, "Turbo Direkt Enjeksiyon"),
    "vag_10_tsi": ("EA211", "1.0 TSI 110 HP", "benzin", 999, 110, 200, "Turbo 3 Silindir"),
    "vag_20_tdi": ("EA288", "2.0 TDI 150 HP", "dizel", 1968, 150, 340, "Turbo Dizel Common-Rail"),
    "vag_20_tdi_190": ("EA288-190", "2.0 TDI 190 HP", "dizel", 1968, 190, 400, "Çift Kademeli Turbo Dizel"),

    # Toyota
    "toy_18_hyb": ("2ZR-FXE", "1.8 Hybrid 122 HP", "hibrit", 1798, 122, 142, "Atkinson Döngüsü + Elektrik Motor"),
    "toy_16_valv": ("1ZR-FAE", "1.6 Valvematic 132 HP", "benzin", 1598, 132, 160, "Sürekli Değişken Sübap Kaldırma"),
    "toy_15_dyn": ("M15A-FKS", "1.5 Dynamic Force 123 HP", "benzin", 1490, 123, 153, "Yüksek Sıkıştırmalı 3 Silindir"),
    "toy_12_turbo": ("8NR-FTS", "1.2 Turbo 116 HP", "benzin", 1197, 116, 185, "Direkt Enjeksiyon Turbo D-4T"),
    "toy_14_d4d": ("1ND-TV", "1.4 D-4D 90 HP", "dizel", 1364, 90, 205, "Common-Rail Turbo Dizel"),
    "toy_25_hyb": ("A25A-FXS", "2.5 Hybrid 222 HP (4x4)", "hibrit", 2487, 222, 221, "E-Four Elektrikli 4x4"),

    # Honda
    "hon_16_vtec": ("R16B", "1.6 i-VTEC Eco 125 HP", "lpg", 1597, 125, 152, "Fabrikasyon LPG Atmosferik i-VTEC"),
    "hon_15_turbo": ("L15B7", "1.5 VTEC Turbo 182 HP", "benzin", 1498, 182, 240, "Direkt Enjeksiyon Turbo DOHC"),
    "hon_16_dtec": ("N16A1", "1.6 i-DTEC 120 HP", "dizel", 1597, 120, 300, "Alüminyum Blok Turbo Dizel"),
    "hon_16_dtec_160": ("N16A4", "1.6 i-DTEC Bi-Turbo 160 HP", "dizel", 1597, 160, 350, "Çift Turbo 4x4"),
    "hon_15_vtec": ("L15ZF", "1.5 i-VTEC 121 HP", "benzin", 1498, 121, 145, "DOHC i-VTEC Atmosferik"),
    "hon_13_vtec": ("L13B", "1.3 i-VTEC 102 HP", "benzin", 1318, 102, 123, "Atkinson Döngülü i-VTEC"),

    # Hyundai & Kia
    "hk_12_mpi": ("G4LA", "1.2 MPI 84 HP", "benzin", 1197, 84, 118, "Atmosferik 4 Silindir"),
    "hk_14_mpi": ("G4LC", "1.4 MPI 100 HP", "benzin", 1368, 100, 134, "Atmosferik 16V Çok Nokta"),
    "hk_10_tgdi": ("G3LC", "1.0 T-GDI 100 HP", "benzin", 998, 100, 172, "Direkt Enjeksiyon Turbo 3 Silindir"),
    "hk_16_tgdi": ("G4FJ", "1.6 T-GDI 177 HP", "benzin", 1591, 177, 265, "Turbo GDI 4 Silindir"),
    "hk_16_crdi": ("D4FB", "1.6 CRDi 136 HP", "dizel", 1598, 136, 320, "Değişken Geometrili Turbo Dizel"),
    "hk_16_crdi_48v": ("D4FE", "1.6 CRDi 136 HP 48V MHEV", "hibrit", 1598, 136, 320, "48V Hafif Hibrit Dizel"),

    # Ford
    "ford_16_tdci": ("DV6C", "1.6 TDCi 115 HP", "dizel", 1560, 115, 270, "8V Turbo Dizel SOHC"),
    "ford_15_tdci": ("DLD-415", "1.5 TDCi 120 HP", "dizel", 1499, 120, 270, "Turbo Dizel DPF"),
    "ford_15_ecoblue": ("EcoBlue-120", "1.5 EcoBlue 120 HP", "dizel", 1499, 120, 300, "Yeni Nesil EcoBlue Dizel"),
    "ford_10_ecob": ("Fox", "1.0 EcoBoost 125 HP", "benzin", 999, 125, 170, "Turbo 3 Silindir Değişken Eksantrik"),
    "ford_10_ecob_mhev": ("Fox-mHEV", "1.0 EcoBoost mHEV 125 HP", "hibrit", 999, 125, 210, "48V Hibrit Destekli Turbo"),
    "ford_16_tivct": ("Sigma", "1.6 Ti-VCT 125 HP", "benzin", 1596, 125, 159, "Çift Bağımsız Değişken Kam Zamanlaması"),

    # Peugeot & Opel (Stellantis)
    "psa_12_pure75": ("EB2FB", "1.2 PureTech 75 HP", "benzin", 1199, 75, 118, "Atmosferik 3 Silindir"),
    "psa_12_pure100": ("EB2ADTD", "1.2 PureTech 100 HP", "benzin", 1199, 100, 205, "Islak Trigerli Turbo 3 Silindir"),
    "psa_12_pure130": ("EB2DTS", "1.2 PureTech 130 HP", "benzin", 1199, 130, 230, "Islak Trigerli Turbo 3 Silindir"),
    "psa_15_hdi": ("DV5RD", "1.5 BlueHDi 130 HP", "dizel", 1499, 130, 300, "16V Kam Zincirli Turbo Dizel AdBlue"),
    "psa_16_hdi": ("DV6DTED", "1.6 HDi 92 HP", "dizel", 1560, 92, 230, "8V Güvenilir Düşük Basınç Dizel"),
    "opel_16_cdti": ("B16DTH", "1.6 CDTI 136 HP (Fısıltı Dizel)", "dizel", 1598, 136, 320, "Motor Arkası Zincirli Dizel"),
    "opel_14_turbo": ("B14XFT", "1.4 Turbo Ecotec 150 HP", "benzin", 1399, 150, 245, "Direkt Enjeksiyon Turbo"),
    "psa_16_pure180": ("EP6FADTXD", "1.6 PureTech 180 HP", "benzin", 1598, 180, 250, "Twin-Scroll Turbo Direkt Enjeksiyon"),
    "ford_15_ecob": ("Dragon", "1.5 EcoBoost 182 HP", "benzin", 1497, 182, 240, "Turbo Direkt Enjeksiyon"),

    # Audi
    "audi_35_tfsi": ("EA211 evo", "35 TFSI 1.5 150 HP", "benzin", 1498, 150, 250, "Silindir Kapama (CoD) Turbo"),
    "audi_30_tfsi": ("EA211", "30 TFSI 1.0 110 HP", "benzin", 999, 110, 200, "Turbo Direkt Enjeksiyon"),
    "audi_40_tdi": ("EA288 evo", "40 TDI 2.0 204 HP Quattro", "dizel", 1968, 204, 400, "Mild-Hybrid Common-Rail Quattro"),
    "audi_45_tfsi": ("EA888 Gen3", "45 TFSI 2.0 245 HP Quattro", "benzin", 1984, 245, 370, "TFSI Quattro Direkt Enjeksiyon"),

    # BMW
    "bmw_15_b38": ("B38B15", "118i / X1 sDrive18i 1.5 Turbo 140 HP", "benzin", 1499, 140, 220, "TwinPower Turbo 3 Silindir"),
    "bmw_15_b37d": ("B37C15", "116d 1.5 Dizel 116 HP", "dizel", 1496, 116, 270, "TwinPower Turbo Dizel"),
    "bmw_16_n13": ("N13B16", "320i ED / 116i 1.6 Turbo 170 HP", "benzin", 1598, 170, 250, "TwinScroll Turbo Valvetronic"),
    "bmw_16_b48": ("B48B16", "320i / 520i 1.6 Turbo 170 HP", "benzin", 1597, 170, 250, "Yeni Nesil B48 TwinPower Turbo"),
    "bmw_20_b47d": ("B47D20", "20d 2.0 Dizel 190 HP xDrive", "dizel", 1995, 190, 400, "TwinPower Turbo Dizel"),

    # Mercedes-Benz
    "mb_13_m282": ("M282", "A180 / A200 / CLA200 / GLA200 1.33 Turbo 163 HP", "benzin", 1332, 163, 250, "Silindir Kapamalı Turbo"),
    "mb_15_om608": ("OM608", "180d 1.5 Dizel 116 HP", "dizel", 1461, 116, 260, "Common-Rail Turbo Dizel"),
    "mb_16_m274": ("M274 DE16", "C180 / E180 1.6 Turbo 156 HP", "benzin", 1595, 156, 250, "BlueDIRECT Turbo Enjeksiyon"),
    "mb_15_m264": ("M264 E15", "C200 / E200 1.5 EQ Boost 184 HP", "hibrit", 1497, 184, 280, "48V EQ Boost Mild-Hybrid"),
    "mb_16_om626": ("OM626 / OM654", "C200d 1.6 Dizel 136-160 HP", "dizel", 1598, 160, 360, "Turbo Dizel Common-Rail"),
    "mb_20_om654": ("OM654", "E220d / GLC220d 2.0 Dizel 194 HP", "dizel", 1950, 194, 400, "Nanoslide Alüminyum Blok Dizel"),

    # Nissan
    "nis_13_digt": ("HR13DDT", "1.3 DIG-T 158 HP Mild-Hybrid", "hibrit", 1332, 158, 270, "12V Mild-Hybrid Turbo Direkt Enjeksiyon"),
    "nis_12_digt": ("HRA2DDT", "1.2 DIG-T 115 HP", "benzin", 1197, 115, 190, "Turbo Direkt Enjeksiyon"),
    "nis_16_dci": ("R9M", "1.6 dCi 130 HP", "dizel", 1598, 130, 320, "Çift Su Soğutmalı EGR Turbo Dizel"),

    # Volvo
    "vol_20_b4": ("B420T", "2.0 B4 Mild-Hybrid 197 HP", "hibrit", 1969, 197, 300, "48V Mild-Hybrid Turbo"),
    "vol_20_b5": ("B420T2", "2.0 B5 AWD Mild-Hybrid 250 HP", "hibrit", 1969, 250, 350, "48V Mild-Hybrid AWD"),
    "vol_20_d4": ("D4204T14", "2.0 D4 AWD 190 HP", "dizel", 1969, 190, 400, "Çift Turbo i-ART Common-Rail"),
    "vol_15_t3": ("B3154T", "1.5 T3 163 HP", "benzin", 1477, 163, 265, "Drive-E Turbo Direkt Enjeksiyon"),

    # Chery
    "chery_16_tgdi": ("SQRF4J16", "1.6 TGDI Acteco 183 HP", "benzin", 1598, 183, 275, "Acteco 3. Nesil Direkt Enjeksiyon Turbo"),

    # Togg
    "togg_ev_160": ("Togg-RWD-160", "V1 / V2 RWD 218 HP (160 kW) Elektrikli", "elektrik", 0, 218, 350, "Kalıcı Mıknatıslı Senkron Elektrik Motoru"),

    # Yeni Modeller İçin Ek Motorlar
    "opel_14_t140": ("A14NET", "1.4 Turbo 140 HP (Astra J)", "benzin", 1364, 140, 200, "Çok Nokta Enjeksiyonlu Turbo"),
    "hyu_10_mpi": ("G3LA", "1.0 MPI 67 HP", "benzin", 998, 67, 96, "Atmosferik 3 Silindir"),
    "hyu_15_crdi": ("D4FA", "1.5 CRDi VGT 110 HP", "dizel", 1493, 110, 235, "Değişken Geometrili Turbo Dizel"),
    "hyu_14_era": ("G4EE", "1.4 DOHC 97 HP", "benzin", 1399, 97, 125, "Atmosferik Çok Nokta Enjeksiyon"),
    "fiat_14_fire_77": ("350A1000-77", "1.4 Fire 77 HP", "benzin", 1368, 77, 115, "Atmosferik 8V"),

    # Elektrikli & Yeni Marka Motorları
    "tesla_rwd_220": ("Tesla-3D6", "RWD Standart Menzil 299 HP (220 kW)", "elektrik", 0, 299, 420, "Kalıcı Mıknatıslı Senkron Elektrik Motoru"),
    "tesla_lr_awd": ("Tesla-AWD", "Long Range AWD 514 HP Çift Motor", "elektrik", 0, 514, 493, "Çift Motorlu Dört Çeker Elektrikli"),
    "byd_atto_150": ("BYD-TZ200", "204 HP (150 kW) Blade Batarya", "elektrik", 0, 204, 310, "LFP Blade Batarya Elektrik Motoru"),
    "byd_seal_ev": ("BYD-EV160", "218 HP (160 kW) Design EV", "elektrik", 0, 218, 330, "LFP Blade Batarya Elektrik Motoru"),
    "byd_seal_phev": ("BYD-DMi", "1.5 DM-i Plug-in Hibrit 218 HP", "hibrit", 1498, 218, 300, "DM-i Şarj Edilebilir Hibrit"),
    "mg4_ev_150": ("MG-EV150", "Comfort / Luxury 204 HP (64 kWh)", "elektrik", 0, 204, 250, "Arkadan İtişli MSP Platform Elektrik Motoru"),
    "ren_meg_ev_160": ("Renault-EV60", "EV60 220 HP (160 kW) Optimum Charge", "elektrik", 0, 220, 300, "Sargılı Rotorlu Senkron Elektrik Motoru"),
    "mg_zs_15": ("15S4C", "1.5 VTi-tech 106 HP", "benzin", 1498, 106, 141, "Atmosferik Çok Nokta Enjeksiyon"),
    "mg_zs_ev": ("MG-ZS-EV", "ZS EV 156 HP (72.6 kWh)", "elektrik", 0, 156, 280, "Önden Çekişli Elektrik Motoru"),
    "mg_hs_15t": ("15E4E", "1.5 T-GDI 162 HP", "benzin", 1490, 162, 250, "Direkt Enjeksiyon Turbo"),
    "suz_14_boos": ("K14D", "1.4 Boosterjet 129 HP Mild-Hybrid", "hibrit", 1373, 129, 235, "48V SHVS Mild-Hybrid Turbo"),
    "suz_12_dual": ("K12D", "1.2 Dualjet 83 HP Mild-Hybrid", "hibrit", 1197, 83, 107, "12V SHVS Mild-Hybrid"),
    "psa_14_hdi": ("DV4TD", "1.4 HDi 68 HP", "dizel", 1398, 68, 160, "8V Ekonomik Common-Rail Dizel"),
    "opel_16_ecotec": ("Z16XEP", "1.6 Twinport 105-115 HP", "benzin", 1598, 115, 155, "Atmosferik 16V Ecotec"),
}

TRANSMISSIONS = {
    "man5": ("manuel", "5 İleri Manuel", 5, "Üretici"),
    "man6": ("manuel", "6 İleri Manuel", 6, "Üretici"),
    "edc6": ("dct", "EDC 6 İleri Kuru (DC4)", 6, "Getrag"),
    "edc7": ("dct", "EDC 7 İleri Islak (DW5)", 7, "Getrag"),
    "xtronic": ("cvt", "X-Tronic CVT", None, "Jatco"),
    "fiat_dct": ("dct", "Fiat 6 İleri Kuru Çift Kavrama (C635)", 6, "FPT"),
    "dsg7_kuru": ("dct", "DSG 7 İleri Kuru Kavrama (DQ200)", 7, "Volkswagen"),
    "dsg6_islak": ("dct", "DSG 6 İleri Islak Kavrama (DQ250)", 6, "Volkswagen"),
    "dsg7_islak": ("dct", "DSG 7 İleri Islak Kavrama (DQ381)", 7, "Volkswagen"),
    "stronic7": ("dct", "S-Tronic 7 İleri Çift Kavrama", 7, "Audi / VAG"),
    "zf8": ("otomatik", "ZF 8HP 8 İleri Tork Konvertörlü Steptronic", 8, "ZF Friedrichshafen"),
    "bmw_7dct": ("dct", "7 İleri Steptronic Çift Kavrama (Getrag 7DCT300)", 7, "Getrag / Magna"),
    "9gtronic": ("otomatik", "9G-Tronic 9 İleri Tork Konvertörlü Otomatik", 9, "Mercedes-Benz"),
    "7gtronic": ("otomatik", "7G-Tronic Plus 7 İleri Tork Konvertörlü", 7, "Mercedes-Benz"),
    "7gdct": ("dct", "7G-DCT 7 İleri Çift Kavrama", 7, "Mercedes-Benz / Getrag"),
    "volvo_8at": ("otomatik", "8 İleri Geartronic Tork Konvertörlü Otomatik", 8, "Aisin AW"),
    "chery_7dct": ("dct", "7 İleri Islak Çift Kavrama (7DCT)", 7, "Getrag"),
    "toy_ecvt": ("cvt", "e-CVT Elektronik Planet Dişli", None, "Toyota"),
    "toy_mds": ("cvt", "Multidrive S Kademeli CVT", None, "Aisin"),
    "toy_mmt": ("amt", "MultiMode Robotize Tek Kavrama", 5, "Toyota"),
    "hon_cvt": ("cvt", "Honda Earth Dreams CVT", None, "Honda"),
    "hon_9at": ("otomatik", "9 İleri Tork Konvertörlü Otomatik", 9, "ZF"),
    "powershift": ("dct", "PowerShift 6 İleri Kuru (DPS6)", 6, "Getrag / Ford"),
    "selectshift": ("otomatik", "Ford 6 İleri Otomatik (SelectShift)", 6, "Ford"),
    "ford_8at": ("otomatik", "8 İleri Döner Seçicili Otomatik (8F35)", 8, "Ford"),
    "eat6": ("otomatik", "EAT6 6 İleri Tork Konvertörlü", 6, "Aisin"),
    "eat8": ("otomatik", "EAT8 8 İleri Tork Konvertörlü", 8, "Aisin"),
    "hk_7dct": ("dct", "7 İleri Kuru Çift Kavrama (7-DCT)", 7, "Hyundai Transys"),
    "hk_6at": ("otomatik", "Hyundai 6 İleri Otomatik (H-Matic)", 6, "Hyundai"),
    "hk_ivt": ("cvt", "IVT Akıllı Zincirli Değişken Şanzıman", None, "Hyundai"),
    "opel_6at": ("otomatik", "Opel 6 İleri Otomatik (ActiveSelect)", 6, "GM / Aisin"),
    "ev_single": ("otomatik", "Tek Vitesli Elektrikli Redüktör (EV)", 1, "Togg / Bosch"),
}

ALL_VARIANTS = [
    # Renault Megane 4 Sedan
    ("Renault", "Megane 4 Sedan", "ren_k9k_110", "man6", 2016, 2020, 850_000),
    ("Renault", "Megane 4 Sedan", "ren_k9k_110", "edc6", 2016, 2020, 930_000),
    ("Renault", "Megane 4 Sedan", "ren_k9k_115", "edc7", 2020, None, 1_180_000),
    ("Renault", "Megane 4 Sedan", "ren_13_tce", "edc7", 2019, None, 1_120_000),
    ("Renault", "Megane 4 Sedan", "ren_16_sce", "man5", 2016, 2019, 760_000),

    # Renault Megane 3
    ("Renault", "Megane 3", "ren_k9k_110", "man6", 2009, 2016, 520_000),
    ("Renault", "Megane 3", "ren_k9k_110", "edc6", 2011, 2016, 580_000),
    ("Renault", "Megane 3", "ren_16_sce", "man5", 2008, 2014, 460_000),

    # Renault Clio 5
    ("Renault", "Clio 5", "ren_10_tce", "man6", 2019, None, 750_000),
    ("Renault", "Clio 5", "ren_10_tce", "xtronic", 2020, None, 860_000),
    ("Renault", "Clio 5", "ren_k9k_115", "man6", 2019, 2022, 890_000),
    ("Renault", "Clio 5", "ren_10_sce", "man5", 2019, None, 660_000),

    # Renault Clio 4
    ("Renault", "Clio 4", "ren_09_tce", "man5", 2012, 2019, 530_000),
    ("Renault", "Clio 4", "ren_k9k_110", "man5", 2012, 2019, 580_000),
    ("Renault", "Clio 4", "ren_k9k_110", "edc6", 2013, 2019, 640_000),

    # Renault Captur
    ("Renault", "Captur", "ren_09_tce", "man5", 2013, 2019, 620_000),
    ("Renault", "Captur", "ren_k9k_110", "edc6", 2013, 2019, 740_000),
    ("Renault", "Captur", "ren_13_tce", "edc7", 2019, None, 1_150_000),

    # Renault Kadjar
    ("Renault", "Kadjar", "ren_k9k_110", "edc6", 2015, 2019, 890_000),
    ("Renault", "Kadjar", "ren_12_tce_sorunlu", "edc6", 2015, 2018, 760_000),
    ("Renault", "Kadjar", "ren_13_tce", "edc7", 2019, 2022, 1_180_000),

    # Renault Austral
    ("Renault", "Austral", "ren_13_tce_150", "xtronic", 2022, None, 1_850_000),

    # Renault Taliant
    ("Renault", "Taliant", "ren_10_tce", "xtronic", 2021, None, 780_000),
    ("Renault", "Taliant", "ren_10_sce", "man5", 2021, None, 640_000),

    # Fiat Egea Sedan
    ("Fiat", "Egea Sedan", "fiat_14_fire", "man6", 2015, None, 610_000),
    ("Fiat", "Egea Sedan", "fiat_13_mjet", "man5", 2015, None, 690_000),
    ("Fiat", "Egea Sedan", "fiat_16_mjet", "man6", 2015, None, 770_000),
    ("Fiat", "Egea Sedan", "fiat_16_mjet", "fiat_dct", 2016, None, 870_000),

    # Fiat Egea Cross
    ("Fiat", "Egea Cross", "fiat_14_fire", "man6", 2020, None, 740_000),
    ("Fiat", "Egea Cross", "fiat_16_mjet_130", "man6", 2020, None, 920_000),
    ("Fiat", "Egea Cross", "fiat_15_t4_hyb", "fiat_dct", 2022, None, 1_150_000),

    # Fiat Linea
    ("Fiat", "Linea", "fiat_13_mjet", "man5", 2007, 2018, 380_000),
    ("Fiat", "Linea", "fiat_14_fire", "man5", 2007, 2016, 340_000),

    # Fiat Doblo
    ("Fiat", "Doblo", "fiat_13_mjet", "man5", 2010, 2022, 490_000),
    ("Fiat", "Doblo", "fiat_16_mjet", "man6", 2010, 2022, 590_000),

    # Volkswagen Passat B8
    ("Volkswagen", "Passat B8", "vag_16_tdi", "dsg7_kuru", 2015, 2020, 1_280_000),
    ("Volkswagen", "Passat B8", "vag_16_tdi", "man6", 2015, 2019, 1_140_000),
    ("Volkswagen", "Passat B8", "vag_14_tsi", "dsg7_kuru", 2015, 2018, 1_220_000),
    ("Volkswagen", "Passat B8", "vag_15_tsi", "dsg7_kuru", 2018, 2023, 1_550_000),
    ("Volkswagen", "Passat B8", "vag_20_tdi", "dsg7_islak", 2015, 2023, 1_850_000),

    # Volkswagen Passat B7
    ("Volkswagen", "Passat B7", "vag_16_tdi_cayc", "man6", 2011, 2015, 750_000),
    ("Volkswagen", "Passat B7", "vag_16_tdi_cayc", "dsg7_kuru", 2011, 2015, 820_000),
    ("Volkswagen", "Passat B7", "vag_14_tsi_122", "dsg7_kuru", 2011, 2015, 710_000),

    # Volkswagen Golf 7
    ("Volkswagen", "Golf 7", "vag_12_tsi", "dsg7_kuru", 2012, 2017, 880_000),
    ("Volkswagen", "Golf 7", "vag_14_tsi", "dsg7_kuru", 2013, 2020, 1_060_000),
    ("Volkswagen", "Golf 7", "vag_14_tsi", "man6", 2013, 2020, 970_000),
    ("Volkswagen", "Golf 7", "vag_16_tdi", "dsg7_kuru", 2013, 2020, 1_030_000),
    ("Volkswagen", "Golf 7", "vag_10_tsi", "dsg7_kuru", 2017, 2020, 1_080_000),

    # Volkswagen Polo
    ("Volkswagen", "Polo", "vag_10_tsi", "dsg7_kuru", 2017, None, 890_000),
    ("Volkswagen", "Polo", "vag_10_tsi", "man5", 2017, None, 780_000),
    ("Volkswagen", "Polo", "vag_16_tdi", "dsg7_kuru", 2017, 2020, 840_000),

    # Volkswagen Tiguan
    ("Volkswagen", "Tiguan", "vag_14_tsi", "dsg6_islak", 2016, 2019, 1_350_000),
    ("Volkswagen", "Tiguan", "vag_15_tsi", "dsg7_kuru", 2019, None, 1_680_000),
    ("Volkswagen", "Tiguan", "vag_20_tdi_190", "dsg7_islak", 2016, None, 1_950_000),

    # Volkswagen T-Roc
    ("Volkswagen", "T-Roc", "vag_15_tsi", "dsg7_kuru", 2018, None, 1_380_000),

    # Volkswagen Caddy
    ("Volkswagen", "Caddy", "vag_16_tdi_cayc", "man5", 2010, 2015, 540_000),
    ("Volkswagen", "Caddy", "vag_20_tdi", "dsg6_islak", 2015, None, 880_000),

    # Toyota Corolla E210
    ("Toyota", "Corolla E210", "toy_18_hyb", "toy_ecvt", 2019, None, 1_320_000),
    ("Toyota", "Corolla E210", "toy_16_valv", "toy_mds", 2019, 2021, 1_160_000),
    ("Toyota", "Corolla E210", "toy_16_valv", "man6", 2019, 2021, 1_040_000),
    ("Toyota", "Corolla E210", "toy_15_dyn", "toy_mds", 2021, None, 1_120_000),

    # Toyota Corolla E180
    ("Toyota", "Corolla E180", "toy_16_valv", "toy_mds", 2013, 2018, 850_000),
    ("Toyota", "Corolla E180", "toy_14_d4d", "toy_mmt", 2013, 2018, 760_000),
    ("Toyota", "Corolla E180", "toy_14_d4d", "man6", 2013, 2018, 740_000),

    # Toyota C-HR
    ("Toyota", "C-HR", "toy_18_hyb", "toy_ecvt", 2016, None, 1_250_000),
    ("Toyota", "C-HR", "toy_12_turbo", "toy_mds", 2016, 2020, 1_080_000),

    # Toyota Yaris
    ("Toyota", "Yaris", "toy_15_dyn", "toy_mds", 2020, None, 920_000),
    ("Toyota", "Yaris", "toy_18_hyb", "toy_ecvt", 2020, None, 1_100_000),

    # Toyota RAV4
    ("Toyota", "RAV4", "toy_25_hyb", "toy_ecvt", 2019, None, 2_600_000),

    # Honda Civic FC5
    ("Honda", "Civic FC5", "hon_16_vtec", "hon_cvt", 2016, 2021, 1_060_000),
    ("Honda", "Civic FC5", "hon_15_turbo", "hon_cvt", 2017, 2021, 1_220_000),
    ("Honda", "Civic FC5", "hon_16_dtec", "hon_9at", 2018, 2021, 1_190_000),
    ("Honda", "Civic FC5", "hon_16_dtec", "man6", 2018, 2021, 1_040_000),

    # Honda City
    ("Honda", "City", "hon_15_vtec", "hon_cvt", 2020, None, 870_000),

    # Honda CR-V
    ("Honda", "CR-V", "hon_16_dtec_160", "hon_9at", 2015, 2019, 1_450_000),
    ("Honda", "CR-V", "hon_15_turbo", "hon_cvt", 2018, None, 1_850_000),

    # Honda Jazz
    ("Honda", "Jazz", "hon_13_vtec", "hon_cvt", 2015, 2020, 780_000),

    # Hyundai i20
    ("Hyundai", "i20", "hk_14_mpi", "hk_6at", 2014, 2020, 680_000),
    ("Hyundai", "i20", "hk_12_mpi", "man5", 2014, 2020, 620_000),
    ("Hyundai", "i20", "hk_10_tgdi", "hk_7dct", 2020, None, 920_000),
    ("Hyundai", "i20", "hk_14_mpi", "hk_6at", 2020, None, 840_000),

    # Hyundai i30
    ("Hyundai", "i30", "hk_16_crdi", "hk_7dct", 2015, 2020, 820_000),
    ("Hyundai", "i30", "hk_14_mpi", "man6", 2012, 2017, 590_000),

    # Hyundai Elantra
    ("Hyundai", "Elantra", "hk_16_crdi", "hk_7dct", 2016, 2020, 890_000),
    ("Hyundai", "Elantra", "hk_16_tgdi", "hk_ivt", 2021, None, 1_180_000),

    # Hyundai Tucson
    ("Hyundai", "Tucson", "hk_16_tgdi", "hk_7dct", 2015, 2020, 1_150_000),
    ("Hyundai", "Tucson", "hk_16_crdi_48v", "hk_7dct", 2018, None, 1_480_000),

    # Hyundai Bayon
    ("Hyundai", "Bayon", "hk_14_mpi", "hk_6at", 2021, None, 890_000),
    ("Hyundai", "Bayon", "hk_10_tgdi", "hk_7dct", 2021, None, 980_000),

    # Kia Sportage
    ("Kia", "Sportage", "hk_16_tgdi", "hk_7dct", 2016, 2021, 1_120_000),
    ("Kia", "Sportage", "hk_16_crdi_48v", "hk_7dct", 2018, None, 1_450_000),

    # Kia Ceed
    ("Kia", "Ceed", "hk_16_crdi", "hk_7dct", 2018, 2022, 880_000),
    ("Kia", "Ceed", "hk_10_tgdi", "hk_7dct", 2020, None, 950_000),

    # Kia Rio
    ("Kia", "Rio", "hk_14_mpi", "hk_6at", 2017, 2022, 690_000),
    ("Kia", "Rio", "hk_12_mpi", "man5", 2017, 2022, 630_000),

    # Kia Stonic
    ("Kia", "Stonic", "hk_14_mpi", "hk_6at", 2017, None, 850_000),

    # Ford Focus 3
    ("Ford", "Focus 3", "ford_16_tdci", "man6", 2011, 2015, 620_000),
    ("Ford", "Focus 3", "ford_15_tdci", "selectshift", 2015, 2018, 790_000),
    ("Ford", "Focus 3", "ford_10_ecob", "man6", 2012, 2018, 680_000),
    ("Ford", "Focus 3", "ford_16_tivct", "powershift", 2011, 2016, 560_000),

    # Ford Focus 4
    ("Ford", "Focus 4", "ford_15_ecoblue", "ford_8at", 2018, 2023, 1_280_000),
    ("Ford", "Focus 4", "ford_10_ecob_mhev", "man6", 2020, None, 1_150_000),

    # Ford Fiesta
    ("Ford", "Fiesta", "ford_10_ecob", "powershift", 2013, 2017, 560_000),
    ("Ford", "Fiesta", "ford_15_tdci", "man6", 2017, 2022, 720_000),

    # Ford Puma
    ("Ford", "Puma", "ford_10_ecob_mhev", "powershift", 2020, None, 1_180_000),

    # Peugeot 208
    ("Peugeot", "208", "psa_12_pure100", "eat8", 2019, None, 930_000),
    ("Peugeot", "208", "psa_12_pure100", "man6", 2019, None, 810_000),
    ("Peugeot", "208", "psa_12_pure130", "eat8", 2019, None, 1_050_000),
    ("Peugeot", "208", "psa_15_hdi", "eat8", 2019, None, 990_000),

    # Peugeot 3008
    ("Peugeot", "3008", "psa_12_pure130", "eat8", 2016, None, 1_450_000),
    ("Peugeot", "3008", "psa_15_hdi", "eat8", 2018, None, 1_650_000),
    ("Peugeot", "3008", "ford_16_tdci", "eat6", 2016, 2018, 1_280_000),

    # Peugeot 301
    ("Peugeot", "301", "psa_16_hdi", "man5", 2013, 2020, 520_000),
    ("Peugeot", "301", "psa_12_pure75", "man5", 2013, 2018, 420_000),

    # Opel Astra K
    ("Opel", "Astra K", "opel_16_cdti", "opel_6at", 2015, 2020, 890_000),
    ("Opel", "Astra K", "opel_16_cdti", "man6", 2015, 2020, 810_000),
    ("Opel", "Astra K", "opel_14_turbo", "opel_6at", 2015, 2020, 850_000),

    # Opel Corsa F
    ("Opel", "Corsa F", "psa_12_pure100", "eat8", 2020, None, 890_000),
    ("Opel", "Corsa F", "psa_12_pure75", "man5", 2020, None, 710_000),

    # Opel Mokka
    ("Opel", "Mokka", "psa_12_pure130", "eat8", 2021, None, 1_250_000),

    # Dacia Duster
    ("Dacia", "Duster", "ren_k9k_110", "man6", 2013, 2018, 640_000),
    ("Dacia", "Duster", "ren_k9k_115", "edc6", 2018, 2023, 940_000),
    ("Dacia", "Duster", "ren_10_tce_lpg", "man6", 2020, None, 860_000),
    ("Dacia", "Duster", "ren_13_tce_150", "edc6", 2021, None, 1_120_000),

    # Skoda Octavia
    ("Skoda", "Octavia", "vag_16_tdi", "dsg7_kuru", 2013, 2020, 960_000),
    ("Skoda", "Octavia", "vag_10_tsi", "dsg7_kuru", 2017, None, 1_060_000),
    ("Skoda", "Octavia", "vag_15_etec", "dsg7_kuru", 2020, None, 1_580_000),
    ("Skoda", "Octavia", "vag_14_tsi", "dsg7_kuru", 2013, 2018, 980_000),

    # Skoda Superb
    ("Skoda", "Superb", "vag_16_tdi", "dsg7_kuru", 2015, 2020, 1_350_000),
    ("Skoda", "Superb", "vag_15_tsi", "dsg7_kuru", 2018, None, 1_680_000),
    ("Skoda", "Superb", "vag_20_tdi", "dsg7_islak", 2015, None, 1_980_000),

    # --- YENİ EKLENEN 35 MODELİN VARYANTLARI ---
    # Renault Fluence
    ("Renault", "Fluence", "ren_k9k_110", "edc6", 2011, 2016, 610_000),
    ("Renault", "Fluence", "ren_k9k_110", "man6", 2009, 2016, 540_000),
    ("Renault", "Fluence", "ren_16_sce", "man5", 2009, 2015, 480_000),

    # Fiat Fiorino Combi
    ("Fiat", "Fiorino Combi", "fiat_13_mjet", "man5", 2008, None, 540_000),
    ("Fiat", "Fiorino Combi", "fiat_14_fire", "man5", 2014, None, 490_000),

    # Volkswagen Jetta
    ("Volkswagen", "Jetta", "vag_16_tdi_cayc", "dsg7_kuru", 2011, 2015, 790_000),
    ("Volkswagen", "Jetta", "vag_12_tsi", "dsg7_kuru", 2012, 2017, 770_000),
    ("Volkswagen", "Jetta", "vag_14_tsi", "dsg7_kuru", 2014, 2018, 920_000),

    # Volkswagen Taigo
    ("Volkswagen", "Taigo", "vag_10_tsi", "dsg7_kuru", 2021, None, 1_240_000),
    ("Volkswagen", "Taigo", "vag_15_tsi", "dsg7_kuru", 2021, None, 1_450_000),

    # Toyota Auris
    ("Toyota", "Auris", "toy_16_valv", "toy_mds", 2013, 2018, 840_000),
    ("Toyota", "Auris", "toy_14_d4d", "man6", 2013, 2018, 720_000),
    ("Toyota", "Auris", "toy_18_hyb", "toy_ecvt", 2013, 2018, 910_000),

    # Honda HR-V
    ("Honda", "HR-V", "hon_15_vtec", "hon_cvt", 2015, 2021, 1_120_000),
    ("Honda", "HR-V", "hon_15_turbo", "hon_cvt", 2019, 2021, 1_350_000),

    # Hyundai Accent Blue
    ("Hyundai", "Accent Blue", "hk_16_crdi", "hk_7dct", 2015, 2018, 690_000),
    ("Hyundai", "Accent Blue", "hk_16_crdi", "man6", 2011, 2018, 610_000),
    ("Hyundai", "Accent Blue", "hk_14_mpi", "hk_6at", 2011, 2018, 590_000),

    # Hyundai Kona
    ("Hyundai", "Kona", "hk_10_tgdi", "hk_7dct", 2018, None, 1_050_000),
    ("Hyundai", "Kona", "hk_16_tgdi", "hk_7dct", 2018, None, 1_190_000),
    ("Hyundai", "Kona", "hk_16_crdi", "hk_7dct", 2018, 2022, 1_080_000),

    # Kia XCeed
    ("Kia", "XCeed", "hk_16_crdi", "hk_7dct", 2019, 2022, 1_180_000),
    ("Kia", "XCeed", "vag_15_tsi", "hk_7dct", 2021, None, 1_340_000),

    # Kia Picanto
    ("Kia", "Picanto", "hk_12_mpi", "hk_6at", 2017, None, 720_000),

    # Ford Kuga
    ("Ford", "Kuga", "ford_15_tdci", "powershift", 2015, 2019, 1_060_000),
    ("Ford", "Kuga", "ford_15_ecoblue", "ford_8at", 2020, None, 1_580_000),
    ("Ford", "Kuga", "ford_15_ecob", "selectshift", 2015, None, 1_380_000),

    # Ford Tourneo Courier
    ("Ford", "Tourneo Courier", "ford_15_tdci", "man6", 2014, None, 620_000),
    ("Ford", "Tourneo Courier", "ford_16_tdci", "man5", 2014, 2018, 560_000),
    ("Ford", "Tourneo Courier", "ford_10_ecob", "ford_8at", 2023, None, 980_000),

    # Peugeot 2008
    ("Peugeot", "2008", "psa_12_pure130", "eat8", 2020, None, 1_240_000),
    ("Peugeot", "2008", "psa_15_hdi", "eat8", 2020, None, 1_290_000),

    # Peugeot 408
    ("Peugeot", "408", "psa_12_pure130", "eat8", 2022, None, 1_680_000),

    # Peugeot 508
    ("Peugeot", "508", "psa_15_hdi", "eat8", 2019, None, 1_580_000),
    ("Peugeot", "508", "psa_16_pure180", "eat8", 2019, None, 1_650_000),

    # Opel Insignia
    ("Opel", "Insignia", "opel_16_cdti", "opel_6at", 2017, 2022, 1_250_000),
    ("Opel", "Insignia", "psa_15_hdi", "eat8", 2020, 2022, 1_520_000),

    # Opel Grandland
    ("Opel", "Grandland", "psa_15_hdi", "eat8", 2018, None, 1_390_000),
    ("Opel", "Grandland", "psa_12_pure130", "eat8", 2018, None, 1_320_000),

    # Skoda Kamiq
    ("Skoda", "Kamiq", "vag_10_tsi", "dsg7_kuru", 2019, None, 1_190_000),
    ("Skoda", "Kamiq", "vag_15_tsi", "dsg7_kuru", 2019, None, 1_320_000),

    # Skoda Karoq
    ("Skoda", "Karoq", "vag_16_tdi", "dsg7_kuru", 2018, 2021, 1_360_000),
    ("Skoda", "Karoq", "vag_15_tsi", "dsg7_kuru", 2018, None, 1_590_000),

    # Skoda Kodiaq
    ("Skoda", "Kodiaq", "vag_15_tsi", "dsg7_islak", 2017, None, 1_850_000),
    ("Skoda", "Kodiaq", "vag_20_tdi_190", "dsg7_islak", 2017, None, 2_350_000),

    # Audi A3 Sedan
    ("Audi", "A3 Sedan", "vag_16_tdi", "stronic7", 2014, 2020, 1_290_000),
    ("Audi", "A3 Sedan", "audi_35_tfsi", "stronic7", 2019, None, 1_780_000),
    ("Audi", "A3 Sedan", "audi_30_tfsi", "stronic7", 2020, None, 1_590_000),

    # Audi A4 Sedan
    ("Audi", "A4 Sedan", "audi_40_tdi", "stronic7", 2016, None, 2_250_000),
    ("Audi", "A4 Sedan", "audi_45_tfsi", "stronic7", 2019, None, 2_480_000),
    ("Audi", "A4 Sedan", "vag_14_tsi", "stronic7", 2016, 2019, 1_650_000),

    # Audi A6 Sedan
    ("Audi", "A6 Sedan", "audi_40_tdi", "stronic7", 2018, None, 3_350_000),
    ("Audi", "A6 Sedan", "audi_45_tfsi", "stronic7", 2019, None, 3_550_000),

    # Audi Q2
    ("Audi", "Q2", "audi_30_tfsi", "stronic7", 2017, None, 1_380_000),
    ("Audi", "Q2", "audi_35_tfsi", "stronic7", 2019, None, 1_580_000),
    ("Audi", "Q2", "vag_16_tdi", "stronic7", 2017, 2020, 1_320_000),

    # Audi Q3
    ("Audi", "Q3", "audi_35_tfsi", "stronic7", 2019, None, 2_180_000),

    # BMW 1 Serisi
    ("BMW", "1 Serisi", "bmw_15_b38", "bmw_7dct", 2019, None, 1_480_000),
    ("BMW", "1 Serisi", "bmw_15_b37d", "zf8", 2015, 2019, 1_180_000),
    ("BMW", "1 Serisi", "bmw_16_n13", "zf8", 2012, 2015, 980_000),

    # BMW 3 Serisi
    ("BMW", "3 Serisi", "bmw_16_b48", "zf8", 2019, None, 2_450_000),
    ("BMW", "3 Serisi", "bmw_16_n13", "zf8", 2012, 2016, 1_350_000),
    ("BMW", "3 Serisi", "bmw_20_b47d", "zf8", 2015, None, 1_950_000),

    # BMW 5 Serisi
    ("BMW", "5 Serisi", "bmw_16_b48", "zf8", 2017, 2023, 2_950_000),
    ("BMW", "5 Serisi", "bmw_20_b47d", "zf8", 2017, 2023, 3_250_000),

    # BMW X1
    ("BMW", "X1", "bmw_15_b38", "bmw_7dct", 2016, None, 1_750_000),
    ("BMW", "X1", "bmw_20_b47d", "zf8", 2016, 2022, 1_920_000),

    # BMW X3
    ("BMW", "X3", "bmw_16_b48", "zf8", 2018, None, 2_850_000),
    ("BMW", "X3", "bmw_20_b47d", "zf8", 2018, None, 3_150_000),

    # Mercedes-Benz A Serisi
    ("Mercedes-Benz", "A Serisi", "mb_13_m282", "7gdct", 2018, None, 1_650_000),
    ("Mercedes-Benz", "A Serisi", "mb_15_om608", "7gdct", 2015, 2021, 1_350_000),

    # Mercedes-Benz C Serisi
    ("Mercedes-Benz", "C Serisi", "mb_16_m274", "9gtronic", 2015, 2021, 1_950_000),
    ("Mercedes-Benz", "C Serisi", "mb_16_om626", "9gtronic", 2015, 2021, 1_980_000),
    ("Mercedes-Benz", "C Serisi", "mb_15_m264", "9gtronic", 2019, None, 2_650_000),

    # Mercedes-Benz E Serisi
    ("Mercedes-Benz", "E Serisi", "mb_16_m274", "9gtronic", 2016, 2021, 2_950_000),
    ("Mercedes-Benz", "E Serisi", "mb_20_om654", "9gtronic", 2016, None, 3_450_000),

    # Mercedes-Benz CLA
    ("Mercedes-Benz", "CLA", "mb_13_m282", "7gdct", 2019, None, 1_950_000),
    ("Mercedes-Benz", "CLA", "mb_15_om608", "7gdct", 2015, 2021, 1_450_000),

    # Mercedes-Benz GLA
    ("Mercedes-Benz", "GLA", "mb_13_m282", "7gdct", 2020, None, 2_050_000),
    ("Mercedes-Benz", "GLA", "mb_15_om608", "7gdct", 2015, 2020, 1_420_000),

    # --- 2. PARTİ YENİ EKLENEN 25 MODELİN VARYANTLARI ---
    # Renault Symbol
    ("Renault", "Symbol", "ren_k9k_110", "man5", 2013, 2021, 520_000),
    ("Renault", "Symbol", "ren_09_tce", "man5", 2013, 2020, 480_000),

    # Peugeot 308
    ("Peugeot", "308", "psa_12_pure130", "eat8", 2022, None, 1_480_000),
    ("Peugeot", "308", "psa_15_hdi", "eat8", 2018, 2022, 1_190_000),

    # Peugeot Rifter
    ("Peugeot", "Rifter", "psa_15_hdi", "eat8", 2019, None, 1_180_000),
    ("Peugeot", "Rifter", "psa_15_hdi", "man6", 2019, None, 1_020_000),

    # Dacia Sandero Stepway
    ("Dacia", "Sandero Stepway", "ren_10_tce", "xtronic", 2021, None, 920_000),
    ("Dacia", "Sandero Stepway", "ren_10_tce_lpg", "man6", 2021, None, 860_000),
    ("Dacia", "Sandero Stepway", "ren_09_tce", "man5", 2013, 2020, 610_000),

    # Dacia Jogger
    ("Dacia", "Jogger", "ren_10_tce_lpg", "man6", 2022, None, 1_080_000),
    ("Dacia", "Jogger", "ren_10_tce", "man6", 2022, None, 1_050_000),

    # Skoda Scala
    ("Skoda", "Scala", "vag_10_tsi", "dsg7_kuru", 2019, None, 1_180_000),
    ("Skoda", "Scala", "vag_15_tsi", "dsg7_kuru", 2019, None, 1_320_000),
    ("Skoda", "Scala", "vag_16_tdi", "dsg7_kuru", 2019, 2021, 1_140_000),

    # Skoda Fabia
    ("Skoda", "Fabia", "vag_10_tsi", "dsg7_kuru", 2018, None, 980_000),
    ("Skoda", "Fabia", "vag_15_tsi", "dsg7_kuru", 2022, None, 1_240_000),

    # Mercedes-Benz GLC
    ("Mercedes-Benz", "GLC", "mb_20_om654", "9gtronic", 2016, None, 3_650_000),
    ("Mercedes-Benz", "GLC", "mb_16_om626", "9gtronic", 2019, 2022, 2_950_000),

    # Nissan Qashqai
    ("Nissan", "Qashqai", "nis_13_digt", "xtronic", 2021, None, 1_680_000),
    ("Nissan", "Qashqai", "ren_k9k_110", "edc6", 2015, 2020, 1_120_000),
    ("Nissan", "Qashqai", "nis_12_digt", "xtronic", 2014, 2018, 960_000),
    ("Nissan", "Qashqai", "nis_16_dci", "xtronic", 2014, 2018, 1_150_000),

    # Nissan Juke
    ("Nissan", "Juke", "ren_10_tce", "edc7", 2020, None, 1_240_000),
    ("Nissan", "Juke", "ren_k9k_110", "man6", 2014, 2019, 780_000),
    ("Nissan", "Juke", "nis_12_digt", "man6", 2014, 2019, 750_000),

    # Nissan Micra
    ("Nissan", "Micra", "ren_10_tce", "xtronic", 2019, 2023, 890_000),
    ("Nissan", "Micra", "ren_09_tce", "man5", 2017, 2020, 740_000),

    # Nissan X-Trail
    ("Nissan", "X-Trail", "nis_16_dci", "xtronic", 2014, 2020, 1_380_000),
    ("Nissan", "X-Trail", "nis_13_digt", "edc7", 2019, 2022, 1_650_000),

    # Seat Leon
    ("Seat", "Leon", "vag_16_tdi", "dsg7_kuru", 2014, 2020, 1_050_000),
    ("Seat", "Leon", "vag_14_tsi", "dsg7_kuru", 2014, 2018, 1_080_000),
    ("Seat", "Leon", "vag_15_etec", "dsg7_kuru", 2020, None, 1_450_000),

    # Seat Ibiza
    ("Seat", "Ibiza", "vag_10_tsi", "dsg7_kuru", 2017, None, 920_000),
    ("Seat", "Ibiza", "vag_10_tsi", "man5", 2017, None, 790_000),

    # Seat Arona
    ("Seat", "Arona", "vag_10_tsi", "dsg7_kuru", 2018, None, 1_080_000),
    ("Seat", "Arona", "vag_16_tdi", "dsg7_kuru", 2018, 2020, 990_000),

    # Seat Ateca
    ("Seat", "Ateca", "vag_15_tsi", "dsg7_kuru", 2019, None, 1_550_000),
    ("Seat", "Ateca", "vag_16_tdi", "dsg7_kuru", 2017, 2020, 1_280_000),

    # Citroen C5 Aircross
    ("Citroen", "C5 Aircross", "psa_15_hdi", "eat8", 2019, None, 1_580_000),
    ("Citroen", "C5 Aircross", "psa_16_pure180", "eat8", 2019, None, 1_540_000),
    ("Citroen", "C5 Aircross", "psa_12_pure130", "eat8", 2020, None, 1_460_000),

    # Citroen C4 X
    ("Citroen", "C4 X", "psa_12_pure130", "eat8", 2022, None, 1_360_000),
    ("Citroen", "C4 X", "psa_15_hdi", "eat8", 2022, None, 1_420_000),

    # Citroen C3 Aircross
    ("Citroen", "C3 Aircross", "psa_12_pure130", "eat6", 2019, None, 1_040_000),
    ("Citroen", "C3 Aircross", "psa_15_hdi", "eat6", 2019, 2023, 1_080_000),

    # Citroen C-Elysee
    ("Citroen", "C-Elysee", "psa_16_hdi", "man5", 2013, 2020, 520_000),
    ("Citroen", "C-Elysee", "psa_15_hdi", "man6", 2019, 2021, 640_000),

    # Volvo XC40
    ("Volvo", "XC40", "vol_15_t3", "volvo_8at", 2019, 2022, 1_950_000),
    ("Volvo", "XC40", "vol_20_b4", "volvo_8at", 2021, None, 2_350_000),

    # Volvo XC60
    ("Volvo", "XC60", "vol_20_d4", "volvo_8at", 2017, 2021, 2_850_000),
    ("Volvo", "XC60", "vol_20_b5", "volvo_8at", 2021, None, 3_650_000),

    # Volvo S60
    ("Volvo", "S60", "vol_20_b5", "volvo_8at", 2020, None, 2_750_000),

    # Cupra Formentor
    ("Cupra", "Formentor", "vag_15_tsi", "dsg7_kuru", 2021, None, 1_850_000),

    # Chery Tiggo 7 Pro
    ("Chery", "Tiggo 7 Pro", "chery_16_tgdi", "chery_7dct", 2023, None, 1_450_000),

    # Chery Tiggo 8 Pro
    ("Chery", "Tiggo 8 Pro", "chery_16_tgdi", "chery_7dct", 2023, None, 1_680_000),

    # Chery Omoda 5
    ("Chery", "Omoda 5", "chery_16_tgdi", "chery_7dct", 2023, None, 1_360_000),

    # Togg T10X
    ("Togg", "T10X", "togg_ev_160", "ev_single", 2023, None, 1_650_000),

    # Opel Astra J
    ("Opel", "Astra J", "opel_16_cdti", "opel_6at", 2014, 2018, 690_000),
    ("Opel", "Astra J", "opel_16_cdti", "man6", 2014, 2018, 620_000),
    ("Opel", "Astra J", "opel_14_t140", "opel_6at", 2011, 2018, 670_000),
    ("Opel", "Astra J", "opel_14_t140", "man6", 2011, 2018, 600_000),

    # Opel Crossland
    ("Opel", "Crossland", "psa_12_pure130", "eat6", 2017, None, 980_000),
    ("Opel", "Crossland", "psa_15_hdi", "eat6", 2019, None, 1_060_000),

    # Volkswagen Golf 8
    ("Volkswagen", "Golf 8", "vag_10_tsi", "man6", 2020, None, 1_190_000),
    ("Volkswagen", "Golf 8", "vag_15_etec", "dsg7_kuru", 2021, None, 1_480_000),

    # Volkswagen T-Cross
    ("Volkswagen", "T-Cross", "vag_10_tsi", "dsg7_kuru", 2019, None, 1_180_000),
    ("Volkswagen", "T-Cross", "vag_10_tsi", "man5", 2019, None, 1_040_000),

    # Hyundai i10
    ("Hyundai", "i10", "hyu_10_mpi", "man5", 2014, None, 580_000),
    ("Hyundai", "i10", "hk_12_mpi", "hk_6at", 2014, None, 690_000),

    # Hyundai Accent Era
    ("Hyundai", "Accent Era", "hyu_15_crdi", "man5", 2006, 2012, 390_000),
    ("Hyundai", "Accent Era", "hyu_14_era", "man5", 2006, 2012, 360_000),

    # Fiat Punto
    ("Fiat", "Punto", "fiat_13_mjet", "man5", 2006, 2018, 370_000),
    ("Fiat", "Punto", "fiat_14_fire_77", "man5", 2006, 2018, 340_000),

    # Citroen C3
    ("Citroen", "C3", "psa_12_pure100", "eat6", 2017, None, 860_000),
    ("Citroen", "C3", "psa_12_pure75", "man5", 2017, None, 720_000),
    ("Citroen", "C3", "psa_15_hdi", "man6", 2018, None, 840_000),

    # Elektrikli Modeller (5)
    ("Tesla", "Model Y", "tesla_rwd_220", "ev_single", 2023, None, 1_890_000),
    ("Tesla", "Model Y", "tesla_lr_awd", "ev_single", 2022, None, 2_450_000),
    ("BYD", "Atto 3", "byd_atto_150", "ev_single", 2023, None, 1_490_000),
    ("BYD", "Seal U", "byd_seal_ev", "ev_single", 2024, None, 1_850_000),
    ("BYD", "Seal U", "byd_seal_phev", "toy_ecvt", 2024, None, 1_950_000),
    ("MG", "MG4 Electric", "mg4_ev_150", "ev_single", 2023, None, 1_320_000),
    ("Renault", "Megane E-Tech", "ren_meg_ev_160", "ev_single", 2022, None, 1_480_000),

    # Station Wagon Modeller (6)
    ("Volkswagen", "Passat Variant", "vag_15_tsi", "dsg7_kuru", 2018, 2023, 1_620_000),
    ("Volkswagen", "Passat Variant", "vag_20_tdi", "dsg7_islak", 2015, 2023, 1_890_000),
    ("Skoda", "Octavia Combi", "vag_15_etec", "dsg7_kuru", 2020, None, 1_490_000),
    ("Skoda", "Octavia Combi", "vag_16_tdi", "dsg7_kuru", 2015, 2020, 1_120_000),
    ("Renault", "Megane Sport Tourer", "ren_k9k_115", "edc7", 2019, None, 1_140_000),
    ("Renault", "Megane Sport Tourer", "ren_13_tce", "edc7", 2019, None, 1_180_000),
    ("Fiat", "Egea Station Wagon", "fiat_16_mjet", "fiat_dct", 2016, None, 920_000),
    ("Fiat", "Egea Station Wagon", "fiat_13_mjet", "man5", 2016, None, 740_000),
    ("Volvo", "V60", "vol_20_b4", "volvo_8at", 2019, None, 2_450_000),
    ("Volvo", "V60", "vol_20_d4", "volvo_8at", 2018, 2021, 1_950_000),
    ("Ford", "Focus SW", "ford_15_ecoblue", "ford_8at", 2019, 2025, 1_240_000),

    # Coupe Modeller (5)
    ("BMW", "4 Serisi Coupe", "bmw_16_b48", "zf8", 2017, None, 2_650_000),
    ("BMW", "4 Serisi Coupe", "bmw_20_b47d", "zf8", 2015, 2020, 2_150_000),
    ("Mercedes-Benz", "C Serisi Coupe", "mb_16_m274", "7gtronic", 2015, 2018, 1_950_000),
    ("Mercedes-Benz", "C Serisi Coupe", "mb_15_m264", "9gtronic", 2018, 2023, 2_680_000),
    ("Audi", "A5 Coupe", "audi_40_tdi", "stronic7", 2017, None, 2_550_000),
    ("Audi", "A5 Coupe", "audi_45_tfsi", "stronic7", 2019, None, 2_750_000),
    ("Volkswagen", "Scirocco", "vag_14_tsi_122", "dsg7_kuru", 2009, 2014, 780_000),
    ("Volkswagen", "Scirocco", "vag_14_tsi", "dsg7_kuru", 2014, 2017, 1_050_000),
    ("BMW", "2 Serisi Coupe", "bmw_15_b38", "zf8", 2015, 2021, 1_450_000),

    # Ticari / Kombi Modeller (5)
    ("Renault", "Kangoo", "ren_k9k_115", "man6", 2019, None, 790_000),
    ("Renault", "Kangoo", "ren_13_tce", "edc7", 2022, None, 1_050_000),
    ("Citroen", "Berlingo", "psa_15_hdi", "eat8", 2019, None, 980_000),
    ("Citroen", "Berlingo", "psa_15_hdi", "man6", 2019, None, 860_000),
    ("Volkswagen", "Transporter", "vag_20_tdi", "dsg7_islak", 2015, None, 1_380_000),
    ("Volkswagen", "Transporter", "vag_20_tdi", "man6", 2015, None, 1_150_000),
    ("Opel", "Combo", "psa_15_hdi", "eat8", 2019, None, 960_000),
    ("Ford", "Tourneo Connect", "ford_15_ecoblue", "ford_8at", 2020, None, 1_120_000),

    # Türkiye Piyasası Ek Popüler Modeller (8)
    ("MG", "ZS", "mg_zs_15", "man5", 2021, None, 860_000),
    ("MG", "ZS", "mg_zs_ev", "ev_single", 2022, None, 1_190_000),
    ("MG", "HS", "mg_hs_15t", "chery_7dct", 2021, None, 1_280_000),
    ("Suzuki", "Vitara", "suz_14_boos", "hk_6at", 2019, None, 1_150_000),
    ("Suzuki", "Swift", "suz_12_dual", "xtronic", 2018, None, 840_000),
    ("Peugeot", "206", "psa_14_hdi", "man5", 2002, 2012, 310_000),
    ("Opel", "Vectra C", "opel_16_ecotec", "man5", 2003, 2009, 360_000),
    ("Skoda", "Rapid", "vag_16_tdi", "dsg7_kuru", 2013, 2019, 760_000),
    ("Toyota", "Corolla Cross", "toy_18_hyb", "toy_ecvt", 2022, None, 1_690_000),
]

# Detaylı Arıza Raporları (Şikayetvar & Usta & TÜVTÜRK Entegrasyonlu)
DETAILED_FAULTS = [
    # Şanzımanlar
    {
        "t": "dsg7_kuru",
        "title": "DQ200 Mekatronik Basınç Tüpü Çatlaması / Basınç Kaybı",
        "description": "Kuru kavramalı 7 ileri DSG şanzımanın mekatronik gövdesindeki basınç tüpü yuvası çatlar. P17BF / P189C arıza kodları verir; araç vitesten düşer ve yolda kalır.",
        "category": "mekanik",
        "avg": 32_000,
        "max": 75_000,
        "override": "yuksek",
        "km": (60_000, 130_000),
        "n": 220,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Passat Türkiye", "tuv:TÜV Report"],
        "checklist": [
            "Geri vitese (R) takarken 2 saniyeden uzun gecikme veya vuruntu var mı?",
            "Şikayetvar'da sıkça bildirilen göstergede İngiliz anahtarı veya vites seçici yanıp sönmesi",
            "Güçlendirilmiş çelik mekatronik tüpü takılmış mı veya revizyon faturası mevcut mu?",
        ],
    },
    {
        "t": "dsg7_kuru",
        "title": "DQ200 Kuru Kavrama Aşınması ve Titreme",
        "description": "Dur-kalk trafikte 1'den 2. vitese geçerken ve rampada kalkışta araç gövdesinde şiddetli titreme (silkeleme) yapar. Şikayetvar'da en çok şikayet edilen kavrama sorunudur.",
        "category": "mekanik",
        "avg": 34_000,
        "max": 52_000,
        "override": "yuksek",
        "km": (70_000, 120_000),
        "n": 240,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Passat Türkiye"],
        "checklist": [
            "Hafif rampada gaza az basarak kalkarken göğüs panelinde zıplama ve titreme kontrolü",
            "OBD ile kavrama kalan balata milimetre değerinin okunması",
        ],
    },
    {
        "t": "hk_7dct",
        "title": "Hyundai/Kia 7-DCT Kuru Çift Kavrama Aşırı Isınma & Titreme",
        "description": "Tucson, Sportage, i20 ve Ceed modellerindeki 7 ileri kuru çift kavramada sıkışık trafikte 'Şanzıman Sıcaklığı Yüksek, Güvenli Bir Yerde Durun' uyarısı ve 1-2 vites geçişlerinde silkeleme yaşanır.",
        "category": "mekanik",
        "avg": 42_000,
        "max": 78_000,
        "override": "yuksek",
        "km": (50_000, 110_000),
        "n": 160,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:DonanımHaber"],
        "checklist": [
            "Yokuş yukarı dur-kalk manevralarında kavrama kaçırma ve koku kontrolü",
            "Şanzıman yazılımının (TCU) en güncel bültende olup olmadığı",
        ],
    },
    {
        "t": "powershift",
        "title": "PowerShift DPS6 Çift Kavrama & TCM Beyin Arızası",
        "description": "Ford kuru çift kavramasında kavrama çatalı sıkışması, keçelerden yağ sızması ve TCM lehim çatlağı. Araç 'Şanzıman Arızası Servis Gerekli' uyarısı verir ve vitese geçmez.",
        "category": "mekanik",
        "avg": 55_000,
        "max": 95_000,
        "override": "yuksek",
        "km": (40_000, 110_000),
        "n": 210,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Focus Kulübü"],
        "checklist": [
            "Düşük hızlarda dur-kalk yaparken şanzımanın aşırı sarsıntı ve tıkırtı yapması",
            "TCM beyni revizyon veya değişim servis kaydı kontrolü",
            "Geri vites dişlisinin kaybolup kaybolmadığı testi",
        ],
    },
    {
        "t": "edc6",
        "title": "EDC 6 İleri (DC4) Çift Kavrama Aşınması ve Isınma Uyarısı",
        "description": "Renault ve Dacia modellerinde kuru tip EDC şanzımanda yoğun trafikte 'Vites Kutusunu Kontrol Ettirin' ve 'Aşırı Isınma' uyarısı.",
        "category": "mekanik",
        "avg": 42_000,
        "max": 68_000,
        "override": "yuksek",
        "km": (80_000, 140_000),
        "n": 180,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Renault Kulübü"],
        "checklist": [
            "Yokuşta durup kalkarken kavrama kaçırma ve vuruntu kontrolü",
            "Şanzıman beyni arıza hafızasının klip cihazı ile taranması",
        ],
    },
    {
        "t": "xtronic",
        "title": "X-Tronic CVT Kasnak & Çelik Kayış Aşınması (Ötme Sesi)",
        "description": "Sürekli agresif sürüş veya 60.000 km'de bir CVT yağı değişmemesi durumunda çelik kayış kasnak yüzeyinde aşınma yapar. Hızlanırken ıslık/ötme sesi duyulur.",
        "category": "mekanik",
        "avg": 58_000,
        "max": 95_000,
        "override": "yuksek",
        "km": (70_000, 130_000),
        "n": 95,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir"],
        "checklist": [
            "60.000 km periyodunda orijinal NS-3 CVT yağı değişim faturası",
            "40-70 km/s arası sabit gazda şanzımandan gelen ince ötme/ıslık sesi dinlenmeli",
        ],
    },
    {
        "t": "fiat_dct",
        "title": "Fiat C635 DCT Kavrama Titremesi",
        "description": "Fiat Egea 1.6 Multijet DCT modellerinde kuru kavramanın şehir içinde erken yıpranması ve 1. vitesten 2. vitese sert geçiş.",
        "category": "mekanik",
        "avg": 38_000,
        "max": 62_000,
        "override": "yuksek",
        "km": (70_000, 120_000),
        "n": 80,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Egea Kulübü"],
        "checklist": ["1-2 vites geçişinde silkeleme kontrolü", "Kavrama seti değişim geçmişi"],
    },

    # Motorlar
    {
        "e": "opel_16_cdti",
        "title": "1.6 CDTI Motor Arkası Eksantrik Zincir Şakırtısı & Zincir Kopması",
        "description": "Opel Astra K 'Fısıltı Dizel' motorunda eksantrik zinciri motor ile şanzıman arasında (arkada) konumlandırılmıştır. Zincir paletleri aşınır ve soğuk marşta şakırtı yapar. Değişim için motor komple indirilir.",
        "category": "mekanik",
        "avg": 52_000,
        "max": 95_000,
        "override": "yuksek",
        "km": (80_000, 140_000),
        "n": 150,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "forum:DonanımHaber"],
        "checklist": [
            "Motor soğukken ilk çalıştırmada motorun arka kısmından 3-5 saniye metalik şakırtı sesi geliyor mu?",
            "Zincir gergi contası ve palet setinin güncellenip güncellenmediği",
        ],
    },
    {
        "e": "opel_14_turbo",
        "title": "1.4 Turbo Ecotec Piston Kırma / Segman Kanalı Hasarı (LSPI)",
        "description": "Direkt enjeksiyonlu 1.4 Turbo motorlarda düşük devirde yüksek gaz verildiğinde erken tutuşma (LSPI) yaşanır. Piston segman kanalları çatlar; motor kompresyon kaybeder.",
        "category": "mekanik",
        "avg": 55_000,
        "max": 110_000,
        "override": "cok_yuksek",
        "km": (50_000, 120_000),
        "n": 110,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir"],
        "checklist": [
            "Yalnızca Dexos 1 Gen 2/Gen 3 onaylı motor yağı kullanılmış mı?",
            "4 silindirin kompresyon testi değerleri ölçülmeli",
        ],
    },
    {
        "e": "ren_12_tce_sorunlu",
        "title": "1.2 TCe (H5Ft) Aşırı Motor Yağı Yakma & Motor Hasarı",
        "description": "Renault ve Dacia'nın Kadjar, Captur ve Duster modellerinde kullandığı 1.2 TCe H5Ft motorunda segman tolerans hatası nedeniyle her 1.000 km'de 1L üzeri yağ tüketir. Şikayetvar'da en yüksek bildirim alan motorlardan biridir.",
        "category": "mekanik",
        "avg": 65_000,
        "max": 140_000,
        "override": "cok_yuksek",
        "km": (40_000, 100_000),
        "n": 190,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "forum:Renault Kulübü"],
        "checklist": [
            "Yetkili servis motor değişim/revizyon geçmişi sorgulanmalı",
            "Yağ seviye çubuğu kuru olmamalı; egzoz ucu yağlı kurum kontrol edilmeli",
        ],
    },
    {
        "e": "psa_12_pure100",
        "title": "1.2 PureTech Islak Triger Kayışı Parçalanması & Yağ Pompası Tıkanması",
        "description": "Motor yağı içinde çalışan triger kayışı zamanla kimyasal olarak çözülür. Kayıştan kopan kauçuk parçacıkları yağ pompası süzgecini ve vakum pompasını tıkar; motor yağsız kalır.",
        "category": "mekanik",
        "avg": 48_000,
        "max": 120_000,
        "override": "cok_yuksek",
        "km": (40_000, 90_000),
        "n": 240,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "youtube:And Çetin"],
        "checklist": [
            "Yağ dolum kapağı açılarak kayışın genişliği özel mastarla kontrol edilmeli (şişme var mı?)",
            "Karter açılarak yağ süzgecinde kauçuk çapak kontrolü yapılmış mı?",
        ],
    },
    {
        "e": "psa_15_hdi",
        "title": "1.5 BlueHDi 7mm Eksantrik Kam Mili Zinciri Kopması",
        "description": "1.5 BlueHDi motorlarda iki eksantrik milini bağlayan 7mm zincir malzeme yorulması sonucu uzar ve aniden kopar. Süpaplar pistona çarparak hasar verir. PSA 8mm kite geçmiştir.",
        "category": "mekanik",
        "avg": 55_000,
        "max": 130_000,
        "override": "cok_yuksek",
        "km": (60_000, 120_000),
        "n": 160,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Peugeot Forum"],
        "checklist": [
            "Soğuk çalıştırmada külbütör kapağı altından gelen şıkırtı/zincir sesi dinlenmeli",
            "8mm revize edilmiş eksantrik zincir kiti değişimi yapılmış mı?",
        ],
    },
    {
        "e": "fiat_14_fire",
        "title": "1.4 Fire 95 HP Kronik Motor Yağı Eksiltme",
        "description": "Fabrikasyon segman toleransları gereği her 1.000 - 2.000 km'de 0.5 ile 1 litre arası yağ eksiltir. Şikayetvar'da Egea başlığında en çok açılan şikayet konusudur.",
        "category": "mekanik",
        "avg": 22_000,
        "max": 45_000,
        "override": "orta",
        "km": (30_000, 100_000),
        "n": 230,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "forum:Egea Kulübü"],
        "checklist": [
            "Yağ çubuğu çekilerek seviye derhal kontrol edilmeli",
            "Egzoz ucunda yağlı kurum ve gaz vermede mavi duman atma kontrolü",
        ],
    },
    {
        "e": "fiat_13_mjet",
        "title": "1.3 Multijet Triger Zincir Uzaması & Yağ Pompası Karter Tıkanması",
        "description": "Egea, Linea ve Doblo'da triger zinciri 120.000 - 150.000 km aralığında uzar. İlk çalıştırmada zincir şıkırtısı yapar.",
        "category": "mekanik",
        "avg": 18_000,
        "max": 35_000,
        "override": "orta",
        "km": (100_000, 160_000),
        "n": 190,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor"],
        "checklist": ["İlk marşta sol ön çamurluk hizasından gelen metalik zincir sesi"],
    },
    {
        "e": "ford_10_ecob",
        "title": "1.0 EcoBoost Antifriz Hortumu Çatlaması & Aniden Hararet (EcoBoom)",
        "description": "Genleşme kabına giden plastik geri dönüş hortumunun kırılması sonucu motor soğutma sıvısını kaybeder. Hararet göstergesi tepki vermeden silindir kapağı eğilir.",
        "category": "mekanik",
        "avg": 85_000,
        "max": 170_000,
        "override": "cok_yuksek",
        "km": (50_000, 110_000),
        "n": 140,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "forum:Focus Kulübü"],
        "checklist": [
            "Geri çağırma kapsamında hortum revize edilmiş kauçuk tip hortumla değiştirilmiş mi?",
            "Genleşme kabında antifriz seviyesi kontrolü",
        ],
    },
    {
        "e": "vag_16_tdi",
        "title": "1.6 TDI Su Devirdaim Pompası Kilitlenmesi & Hararet",
        "description": "VAG grubu 1.6 TDI motorlarda elektronik yakalı su pompasının klepesi sıkışır. Hararet aniden yükselir.",
        "category": "mekanik",
        "avg": 16_000,
        "max": 28_000,
        "override": "orta",
        "km": (70_000, 120_000),
        "n": 110,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Passat Türkiye"],
        "checklist": ["Hararet ibresinde 90 dereceden yukarı oynama var mı?"],
    },
    {
        "e": "hon_16_vtec",
        "title": "1.6 Eco LPG Sübap Ayarı Bozulması & Sübap Erimesi",
        "description": "LPG yanma odası sıcaklığı nedeniyle 40-50 bin km'de bir sübap ayarı gerekir. Şikayetvar'da rölantide stop etme şikayetleri yaygındır.",
        "category": "mekanik",
        "avg": 14_000,
        "max": 42_000,
        "override": "orta",
        "km": (50_000, 100_000),
        "n": 95,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:CivicTR"],
        "checklist": ["Sabah rölanti dalgalanması / stop etme var mı?"],
    },
    {
        "e": "ren_10_tce_lpg",
        "title": "1.0 ECO-G LPG Basınç Sensörü & Gazdan Benzine Atma",
        "description": "Dacia Duster ve Clio LPG modellerinde MAP basınç sensörünün tıkanması sonucu araç gazdan benzine atar.",
        "category": "mekanik",
        "avg": 8_500,
        "max": 16_000,
        "override": "dusuk",
        "km": (30_000, 80_000),
        "n": 105,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:DonanımHaber Duster Kulübü"],
        "checklist": ["LPG filtresi değişim aralıkları ve sensör parça kodu"],
    },

    # Şikayetvar Genel Araç Gövde, Multimedya & Donanım Şikayetleri
    {
        "m": ("Honda", "Civic FC5"),
        "title": "C Sütunu Göçük & Dalgalanma Problemi",
        "description": "Tavan ile arka çamurluk birleşim bölgesinde (C sütunu) sacın kendiliğinden içe göçmesi ve dalgalanması.",
        "category": "konfor",
        "avg": 14_000,
        "max": 28_000,
        "override": "orta",
        "km": (5_000, 50_000),
        "n": 190,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:CivicTR", "youtube:Otorapor"],
        "checklist": ["Arka çamurluk üstü C sütunu sacına göz hizasında bakılarak dalgalanma var mı?"],
    },
    {
        "m": ("Renault", "Megane 4 Sedan"),
        "title": "R-Link 2 / Easy Link Multimedya Ekran Donması & Bluetooth Kopması",
        "description": "Şikayetvar'da sıkça bildirilen dikey multimedya ekranının donması, Bluetooth ses kesilmesi ve geri görüş kamerası gecikmesi.",
        "category": "yazilim_multimedya",
        "avg": 8_500,
        "max": 18_000,
        "override": "dusuk",
        "km": (20_000, 80_000),
        "n": 140,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Renault Kulübü"],
        "checklist": ["Geri vitese takıldığında kameranın gecikmesiz açılması ve ekran yazılım sürümü"],
    },
    {
        "m": ("Fiat", "Egea Sedan"),
        "title": "City Modu / Elektrikli Direksiyon (EPS) Sertleşmesi",
        "description": "Direksiyon tork sensörünün arızalanması sonucu sürüş esnasında direksiyonun aniden sertleşmesi.",
        "category": "guvenlik",
        "avg": 16_000,
        "max": 32_000,
        "override": "orta",
        "km": (60_000, 130_000),
        "n": 120,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "tuv:TÜVTÜRK Raporları"],
        "checklist": ["Direksiyonu tam sağ-sol yaparken City modunda takılma veya ikaz lambası kontrolü"],
    },
    {
        "m": ("Fiat", "Egea Sedan"),
        "title": "7 İnç Uconnect Ekran Dokunmatik Arızası (Hayalet Dokunma)",
        "description": "Dokunmatik panelin basmadığı halde kendi kendine basması, radyo frekansını değiştirmesi.",
        "category": "yazilim_multimedya",
        "avg": 9_000,
        "max": 18_000,
        "override": "dusuk",
        "km": (30_000, 90_000),
        "n": 130,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Egea Kulübü"],
        "checklist": ["Ekranın tüm bölgelerine dokunarak dokunmatik hassasiyeti testi"],
    },
    {
        "m": ("Volkswagen", "Passat B8"),
        "title": "Panoramik Cam Tavan Tahliye Tıkanması & Su Alma",
        "description": "Cam tavanın tahliye hortumlarının tozla tıkanarak yağmur suyunu tavan döşemesine sızdırması.",
        "category": "konfor",
        "avg": 9_000,
        "max": 24_000,
        "override": "dusuk",
        "km": (30_000, 90_000),
        "n": 85,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Passat Türkiye"],
        "checklist": ["Tavan döşemesinde su lekesi veya taban halısında nem kontrolü"],
    },
    {
        "m": ("Toyota", "Corolla E210"),
        "title": "Ön Konsol & Kapı İçi Trim Tıkırtısı (Şikayetvar Bildirimi)",
        "description": "Bozuk ve parke taşlı yollarda ön konsol, tablet ekran arkası ve kapı döşemelerinden gelen tıkırtı sesi.",
        "category": "konfor",
        "avg": 4_500,
        "max": 9_000,
        "override": "dusuk",
        "km": (15_000, 70_000),
        "n": 90,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Toyota Club TR"],
        "checklist": ["Bozuk yolda test sürüşü yapılarak trim seslerinin seviyesi"],
    },
    {
        "m": ("Dacia", "Duster"),
        "title": "4x4 Arka Diferansiyel Uğultusu & Şaft Askı Bilyası",
        "description": "Duster 4x4 modellerde 70-90 km/s hız bandında arka diferansiyelden gelen rezonanslı uğultu.",
        "category": "mekanik",
        "avg": 22_000,
        "max": 45_000,
        "override": "orta",
        "km": (60_000, 120_000),
        "n": 95,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor"],
        "checklist": ["80 km/s hızda gaz kesip verirken arka uğultu kontrolü"],
    },
    {
        "m": ("Skoda", "Octavia"),
        "title": "A8 Kasa MIB3 Multimedya Donmaları & SOS Acil Arama Uyarısı",
        "description": "SOS modülü arızası nedeniyle göstergede sürekli sarı uyarı vermesi ve merkezi ekranın kendiliğinden reset atması.",
        "category": "yazilim_multimedya",
        "avg": 8_000,
        "max": 20_000,
        "override": "dusuk",
        "km": (10_000, 60_000),
        "n": 115,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Skoda Forum"],
        "checklist": ["Göstergede SOS arıza ikazı olup olmadığı ve yazılım güncellemesi geçmişi"],
    },
    {
        "m": ("Renault", "Clio 4"),
        "title": "A Sütunu Kelebek Camı Fitilinden Rüzgar Sesi",
        "description": "90 km/s üzerindeki hızlarda ön kelebek camı üçgen plastik contasından kabin içine belirgin rüzgar ıslığı gelmesi.",
        "category": "konfor",
        "avg": 3_500,
        "max": 7_000,
        "override": "dusuk",
        "km": (20_000, 80_000),
        "n": 140,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Renault Kulübü"],
        "checklist": ["Kelebek camı fitilinin mastikle izolasyon yapılıp yapılmadığı"],
    },
    {
        "m": ("Fiat", "Doblo"),
        "title": "Arka Yaprak Makas Burçları Boşluğu & Lokurtu Sesi",
        "description": "Arka makas takozları ve burçlarının ezilmesi sonucu tümseklerde arkadan gelen şiddetli lokurtu sesi.",
        "category": "konfor",
        "avg": 6_500,
        "max": 14_000,
        "override": "dusuk",
        "km": (50_000, 110_000),
        "n": 130,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "tuv:TÜVTÜRK Raporları"],
        "checklist": ["Arka makas burçlarının boşluk kontrolü"],
    },
    # --- AUDI, BMW, MERCEDES VE YENİ MODELLERİN KRONİK ARIZALARI ---
    {
        "t": "stronic7",
        "title": "S-Tronic 7 İleri Mekatronik Basınç Tüpü & Kavrama Titremesi",
        "description": "Audi A3, A4 ve Q2 modellerindeki S-Tronic çift kavramalı şanzımanda dur-kalk trafikte 1-2 vites geçişinde silkeleme ve mekatronik basınç kaybı.",
        "category": "mekanik",
        "avg": 38_000,
        "max": 85_000,
        "override": "yuksek",
        "km": (65_000, 130_000),
        "n": 175,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Audi Forum TR"],
        "checklist": [
            "Yokuşta kalkışta ve D1-D2 geçişinde titreme/vuruntu testi",
            "VCDS/ODIS ile mekatronik basınç ve kavrama tolerans ölçümü",
        ],
    },
    {
        "t": "7gdct",
        "title": "7G-DCT Çift Kavrama Silkelemesi & Termostat Uyarısı",
        "description": "Mercedes A, CLA ve GLA serilerinde kullanılan 7G-DCT şanzımanda soğukken vites geçişlerinde vuruntu ve sıkışık trafikte kavrama ısınması.",
        "category": "mekanik",
        "avg": 42_000,
        "max": 82_000,
        "override": "yuksek",
        "km": (70_000, 130_000),
        "n": 135,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir"],
        "checklist": [
            "R ve D konumları arasında geçiş yaparken gecikme ve vuruntu kontrolü",
            "Şanzıman yağı ve filtresinin 60.000 km'de değişip değişmediği",
        ],
    },
    {
        "e": "bmw_16_n13",
        "title": "N13 1.6 Turbo Su Flanşı Çatlaması, Devirdaim & Yağ Eksiltme",
        "description": "BMW F20 1 Serisi ve F30 320i ED modellerindeki N13 motorda motor arkası plastik su flanşı çatlaması, tahrik kayışı kasnağı soyulması ve valf lastiklerinden yağ eksiltme.",
        "category": "mekanik",
        "avg": 35_000,
        "max": 78_000,
        "override": "yuksek",
        "km": (60_000, 120_000),
        "n": 210,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "forum:BMW Team TR"],
        "checklist": [
            "Motor arkası su flanşı ve turbo su borularında antifriz terlemesi kontrolü",
            "Rölantide 5 dakika çalıştıktan sonra gaza basınca egzozdan mavi duman çıkıyor mu?",
        ],
    },
    {
        "e": "bmw_16_b48",
        "title": "B48 1.6 Turbo Yağ Filtre Kütüğü & Genleşme Tankı Hortumu Kaçağı",
        "description": "BMW G20 320i ve G30 520i modellerindeki B48 motorda plastik yağ filtre gövdesi (oil cooler housing) çatlaması ve genleşme kabı geri dönüş hortumu kırılması.",
        "category": "mekanik",
        "avg": 28_000,
        "max": 55_000,
        "override": "orta",
        "km": (70_000, 130_000),
        "n": 145,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:BMW Team TR"],
        "checklist": [
            "Yağ filtre kütüğü altından motor bloğuna sızan antifriz veya yağ izi kontrolü",
            "Yedek su deposu üst ince hortumunun gevrekliği",
        ],
    },
    {
        "e": "bmw_20_b47d",
        "title": "B47 2.0 Dizel EGR Soğutucu Geri Çağırma & Emme Manifoldu Kurumu",
        "description": "BMW 320d, 520d, X1 ve X3 modellerinde EGR soğutucusunun su eksiltmesi (geri çağırma kapsamındadır) ve 100 bin km üzeri manifold klape kurum bağlaması.",
        "category": "mekanik",
        "avg": 26_000,
        "max": 52_000,
        "override": "orta",
        "km": (80_000, 150_000),
        "n": 130,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "tuv:TÜV Report"],
        "checklist": [
            "Yetkili serviste EGR soğutucu geri çağırma (recall) aksiyonunun yapılıp yapılmadığı",
            "Soğutma suyu eksiltme kontrolü",
        ],
    },
    {
        "e": "mb_16_m274",
        "title": "M274 1.6 Turbo Eksantrik Dişlisi (Vanus) & Termostat Arızası",
        "description": "Mercedes C180 ve E180 modellerindeki M274 motorda soğuk marşta eksantrik zincir/dişli sesi, elektronik termostatın açık kalması ve karter havalandırma valfi arızası.",
        "category": "mekanik",
        "avg": 34_000,
        "max": 68_000,
        "override": "yuksek",
        "km": (75_000, 140_000),
        "n": 165,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir", "forum:MBClubTR"],
        "checklist": [
            "Sabah ilk marşta 3-4 saniye süren metalik zincir/dişli şakırtısı var mı?",
            "Motor hararetinin 90 dereceye hızlı ulaşıp sabit kalıp kalmadığı",
        ],
    },
    {
        "m": ("BMW", "3 Serisi"),
        "title": "İç Kapı Çekme Kollarının Erimesi & Sunroof Fitil Sesi",
        "description": "F30 kasa 3 Serisi'nde iç kapı kollarındaki kauçuk kaplamanın sıcaktan eriyerek ele yapışması ve G20 kasada sunroof fitilinden gelen çıtırtı sesi.",
        "category": "konfor",
        "avg": 6_500,
        "max": 15_000,
        "override": "dusuk",
        "km": (40_000, 110_000),
        "n": 185,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:BMW Team TR"],
        "checklist": ["Sağ ön ve arka iç kapı tutamaklarında soyulma/yapışkanlık kontrolü"],
    },
    {
        "m": ("Mercedes-Benz", "C Serisi"),
        "title": "Panoramik Cam Tavan Kızak Takılması & Orta Konsol Trim Sesi",
        "description": "W205 C Serisi modellerde panoramik cam tavan ayaklarının kırılması sonucu kapanmama problemi ve sert AMG süspansiyonda orta konsol tıkırtısı.",
        "category": "konfor",
        "avg": 14_000,
        "max": 28_000,
        "override": "orta",
        "km": (50_000, 110_000),
        "n": 155,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:MBClubTR"],
        "checklist": ["Cam tavanın tam açılıp takılmadan kapanması mutlaka test edilmeli"],
    },
    {
        "e": "nis_12_digt",
        "title": "1.2 DIG-T (HRA2DDT) Kronik Yağ Yakma & Triger Zincir Uzaması",
        "description": "Nissan Qashqai ve Juke 1.2 DIG-T motorlarda segman kurum bağlaması sonucu yüksek yağ tüketimi ve triger zincir gergisi boşalması.",
        "category": "mekanik",
        "avg": 62_000,
        "max": 135_000,
        "override": "cok_yuksek",
        "km": (45_000, 105_000),
        "n": 195,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Sekizsilindir"],
        "checklist": [
            "Motor yağ seviyesi ve kompresyon değerleri mutlaka ölçülmeli",
            "Soğuk ilk çalıştırmada zincir şakırtısı dinlenmeli",
        ],
    },
    {
        "e": "vol_20_d4",
        "title": "2.0 D4 EGR Valfi & Soğutucu Tıkanması ve Hortum Terlemesi",
        "description": "Volvo XC60 D4 dizel motorlarda şehir içi kısa mesafe kullanımda EGR soğutucusunun kurum bağlaması ve turbo intercooler hortumu yırtılması.",
        "category": "mekanik",
        "avg": 28_000,
        "max": 54_000,
        "override": "orta",
        "km": (80_000, 150_000),
        "n": 110,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "tuv:TÜV Report"],
        "checklist": ["EGR soğutucu temizlik geçmişi ve turbo basınç hortumu kontrolü"],
    },
    {
        "m": ("Chery", "Tiggo 7 Pro"),
        "title": "Multimedya & Kamera Yazılım Gecikmesi ve Şehir İçi Yakıt Tüketimi",
        "description": "Şikayetvar bildirimlerinde 360 derece kamera ve CarPlay ekranında zaman zaman donma yaşanması ve şehir içi kısa mesafede 9.5-11L yakıt tüketimi.",
        "category": "yazilim_multimedya",
        "avg": 6_500,
        "max": 14_000,
        "override": "dusuk",
        "km": (5_000, 45_000),
        "n": 125,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:DonanımHaber"],
        "checklist": ["Yetkili serviste son multimedya ve şanzıman yazılım güncellemesinin yapılıp yapılmadığı"],
    },
    {
        "m": ("Cupra", "Formentor"),
        "title": "MIB3 Dokunmatik Ekran & Tavan SOS Modülü Yazılım Uyarısı",
        "description": "Tavan kontrol ünitesi ve SOS modülünün anlık hata vermesi veya multimedya ekranının yeniden başlaması (yazılım güncellemesi ile giderilir).",
        "category": "yazilim_multimedya",
        "avg": 9_000,
        "max": 22_000,
        "override": "dusuk",
        "km": (10_000, 50_000),
        "n": 95,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Cupra Forum"],
        "checklist": ["Tavan dokunmatik aydınlatma ve SOS modülü hata kaydı kontrolü"],
    },
    {
        "m": ("Togg", "T10X"),
        "title": "Trumore Multimedya Ekran Donması & 12V Akü Uyarıları",
        "description": "Şikayetvar bildirimlerinde 1.5 öncesi yazılım sürümlerinde uçtan uca ekranın anlık kararması, kamera gecikmesi ve park halindeyken 12V yardımcı akünün zayıflaması.",
        "category": "yazilim_multimedya",
        "avg": 5_000,
        "max": 12_000,
        "override": "dusuk",
        "km": (5_000, 40_000),
        "n": 140,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Togg Kullanıcı Kulübü"],
        "checklist": [
            "Son OTA / servis yazılım güncellemesinin yüklü olup olmadığı",
            "AC/DC şarj soketi kilit mekanizması ve 12V akü sağlığı testi",
        ],
    },
    {
        "e": "opel_14_t140",
        "title": "1.4 Turbo (A14NET) Termostat Gövdesi & Devirdaim Antifriz Kaçağı",
        "description": "Astra J 1.4 Turbo motorlarda plastik termostat gövdesi, genleşme tankı ve turbo yağlama/su dönüş borularından antifriz sızdırması ve hararet riski.",
        "category": "mekanik",
        "avg": 18_000,
        "max": 38_000,
        "override": "orta",
        "km": (70_000, 140_000),
        "n": 230,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "youtube:Otorapor", "forum:Opelx"],
        "checklist": [
            "Motor soğutma suyu genleşme kabında yağ karışımı veya eksiltme kontrolü",
            "Subap kapağı (külbütör) diyaframından ıslık/hava emme sesi kontrolü",
        ],
    },
    {
        "m": ("Volkswagen", "Golf 8"),
        "title": "Dokunmatik Klima/Direksiyon & 48V Alternatör (eTSI) Uyarısı",
        "description": "Golf 8 eTSI modellerde 48V marş-jeneratör modülü arızası veya SOS / seyahat asistanı (Travel Assist) direksiyon kapasitif sensör hatası.",
        "category": "yazilim_multimedya",
        "avg": 26_000,
        "max": 58_000,
        "override": "orta",
        "km": (25_000, 85_000),
        "n": 135,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Golftutkusu"],
        "checklist": [
            "Göstergede Travel Assist veya 48V elektrik sistemi arıza uyarısı kontrolü",
            "Dokunmatik ekran ve direksiyon tuşlarının tepki testi",
        ],
    },
    {
        "e": "hyu_15_crdi",
        "title": "1.5 CRDi Enjektör Şakırtısı & Turbo Islık Sesi (Yüksek Km)",
        "description": "Accent Era 1.5 CRDi motorlarda yüksek kilometrede mazot pompası / enjektör geri dönüş kaçakları ve turbo mil boşluğuna bağlı ıslık sesi.",
        "category": "mekanik",
        "avg": 20_000,
        "max": 42_000,
        "override": "orta",
        "km": (150_000, 260_000),
        "n": 165,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:HyundaiClubTR"],
        "checklist": [
            "Soğuk marşta egzozdan siyah/beyaz duman ve enjektör vuruntusu kontrolü",
            "EPS (elektrikli direksiyon) tıkırtı burcu boşluğu kontrolü",
        ],
    },
    {
        "m": ("Chery", "Omoda 5"),
        "title": "Şerit Takip Hassasiyeti & Arka Süspansiyon Sertliği",
        "description": "Omoda 5 modellerinde ADAS şerit takip sisteminin şehir içinde agresif müdahale etmesi ve bozuk zeminlerde arka süspansiyondan gelen vuruntu.",
        "category": "yazilim_multimedya",
        "avg": 6_000,
        "max": 14_000,
        "override": "dusuk",
        "km": (5_000, 40_000),
        "n": 95,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:DonanımHaber"],
        "checklist": ["Yetkili serviste ADAS ve multimedya yazılım kalibrasyonunun yapılıp yapılmadığı"],
    },
    {
        "m": ("Tesla", "Model Y"),
        "title": "Sert Süspansiyon Trim Sesi & Ön Salıncak Burcu Gıcırtısı",
        "description": "Model Y araçlarda bozuk yollarda ön üst salıncak bilyasından gelen gıcırtı ve cam tavan/bagaj kapağı fitillerinden gelen rüzgar/trim sesi.",
        "category": "konfor",
        "avg": 14_000,
        "max": 28_000,
        "override": "orta",
        "km": (20_000, 70_000),
        "n": 145,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "tuv:TÜV Report"],
        "checklist": [
            "Direksiyonu çevirirken ön takımdan gıcırtı gelip gelmediği",
            "Isı pompası ve batarya SoH (sağlık) yüzdesi kontrolü",
        ],
    },
    {
        "m": ("BYD", "Atto 3"),
        "title": "12V Yardımcı Akü Boşalması & Fabrika Lastik Tutunma Sorunu",
        "description": "Uzun süre park halinde 12V akünün zayıflaması ve orijinal fabrika lastiklerinin ıslak zeminde erken kayması (lastik değişimi ile çözülür).",
        "category": "yazilim_multimedya",
        "avg": 7_500,
        "max": 16_000,
        "override": "dusuk",
        "km": (10_000, 50_000),
        "n": 80,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:BYD Türkiye"],
        "checklist": ["OTA yazılım sürümü ve DC hızlı şarj soketi kilidi kontrolü"],
    },
    {
        "m": ("Volkswagen", "Transporter"),
        "title": "2.0 TDI Çift Kütleli Volan & EGR Soğutucu Çatlağı",
        "description": "T6 Transporter ticari araçlarda yüksek tork nedeniyle volan vuruntusu ve EGR soğutucusundan gizli antifriz eksiltmesi.",
        "category": "mekanik",
        "avg": 38_000,
        "max": 72_000,
        "override": "yuksek",
        "km": (120_000, 220_000),
        "n": 150,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "tuv:TÜV Report"],
        "checklist": ["Rölantide şanzıman tarafından gelen tıkırtı ve antifriz seviyesi kontrolü"],
    },
    {
        "m": ("Peugeot", "206"),
        "title": "Arka Torsiyon Dingili Boşluğu & COM2000 Sinyal Kolu Arızası",
        "description": "Arka tekerleklerin içe yatması (torsiyon bilyası dağılması) ve direksiyon altındaki COM2000 sinyal/far kolu grubunun temassızlığı.",
        "category": "mekanik",
        "avg": 15_000,
        "max": 28_000,
        "override": "orta",
        "km": (130_000, 240_000),
        "n": 190,
        "sources": ["sikayetvar:Şikayetvar Kullanıcı Bildirimleri", "forum:Peugeot Türkiye"],
        "checklist": ["Arka lastiklerde kamber açısı (içe yatma) ve tümseklerde gıcırtı kontrolü"],
    },
]

# Stage 1 / Stage 2 Paketleri
DETAILED_SOFTWARE_MODS = [
    {
        "e": "ren_k9k_110",
        "t": "man6",
        "mod_type": "stage1",
        "rec": True,
        "hp": (110, 135),
        "nm": (260, 310),
        "risk": "1.5 dCi motor bloğu ve enjektörleri son derece dayanıklıdır. Manuel şanzıman baskı balatası 310 Nm torku rahat kaldırır.",
        "cost": 8_500,
        "comments": [
            ("Mehmet K.", "30 bin km önce Megane 4 manuel aracıma Stage 1 yaptırdım. Şehir içi yakıt 0.5L düştü, sollamalarda araç çok rahatladı.", 85_000, "sorunsuz"),
        ],
    },
    {
        "e": "ren_k9k_110",
        "t": "edc6",
        "mod_type": "stage1",
        "rec": None,
        "hp": (110, 130),
        "nm": (260, 290),
        "risk": "EDC 6 ileri (DC4) kuru kavrama tork sınırı 280-290 Nm civarındadır. Tork yazılımla sınırlandırılmazsa kuru kavrama hızla kaçırma yapar.",
        "cost": 9_500,
        "comments": [
            ("Ufuk A.", "Kuru kavrama EDC'de torku 290 Nm'ye kilitledik. 15 bin km oldu sıkıntı yok ama rampalarda zorlamamaya dikkat ediyorum.", 95_000, "sorunsuz"),
        ],
    },
    {
        "e": "ren_13_tce",
        "t": "edc7",
        "mod_type": "stage1",
        "rec": True,
        "hp": (140, 170),
        "nm": (240, 285),
        "risk": "1.3 TCe motor yazılıma çok yatkındır. 7 ileri ıslak kavramalı EDC (DW5) şanzıman 300 Nm üzeri torkları dahi güvenle taşır.",
        "cost": 10_000,
        "comments": [
            ("Caner Y.", "Megane 4 1.3 TCe EDC aracıma Stage 1 yaptırdım, 172 HP ölçüldü. Şanzıman ıslak olduğu için harika aktarıyor.", 45_000, "sorunsuz"),
        ],
    },
    {
        "e": "fiat_16_mjet",
        "t": "man6",
        "mod_type": "stage1",
        "rec": True,
        "hp": (120, 155),
        "nm": (320, 380),
        "risk": "1.6 Multijet motor hacmine göre inanılmaz tork üretir. Manuel şanzıman ve debriyaj seti 380 Nm torka dayanıklıdır.",
        "cost": 8_000,
        "comments": [
            ("Ali Rıza", "Egea 1.6 Multijet tam bir tork canavarına dönüştü.", 70_000, "sorunsuz"),
        ],
    },
    {
        "e": "fiat_14_fire",
        "t": "man6",
        "mod_type": "stage1",
        "rec": False,
        "hp": (95, 99),
        "nm": (127, 134),
        "risk": "Atmosferik motorda yazılımla maksimum 3-4 HP güç alınır, kesinlikle hissedilmez. Paranıza değmez.",
        "cost": 6_000,
        "comments": [
            ("Okan V.", "Yazılım yaptırdım hiçbir fark hissetmedim, boşa giden masraf oldu.", 40_000, "sorunlu"),
        ],
    },
    {
        "e": "vag_16_tdi",
        "t": "dsg7_kuru",
        "mod_type": "stage1",
        "rec": None,
        "hp": (120, 145),
        "nm": (250, 310),
        "risk": "DQ200 kuru kavrama fabrika sınırı 250 Nm'dir. 310 Nm tork kavramayı hızla bitirir. Mutlaka TCU (şanzıman) yazılımı yapılmalıdır.",
        "cost": 11_000,
        "comments": [
            ("Engin D.", "Passat B8 aracıma motor + DSG yazılımı yaptırdım. DSG yazılımı olmadan kesinlikle yaptırmayın.", 105_000, "sorunsuz"),
        ],
    },
    {
        "e": "vag_14_tsi",
        "t": "dsg7_kuru",
        "mod_type": "stage1",
        "rec": True,
        "hp": (150, 180),
        "nm": (250, 300),
        "risk": "1.4 TSI 150 HP ACT motor Stage 1 ile çok dengeli güç verir.",
        "cost": 9_500,
        "comments": [
            ("Burak G.", "Golf 7 1.4 TSI aracıma soft Stage 1 yaptık, 178 HP aldık. Çok memnunum.", 65_000, "sorunsuz"),
        ],
    },
    {
        "e": "hon_15_turbo",
        "t": "hon_cvt",
        "mod_type": "stage1",
        "rec": True,
        "hp": (182, 220),
        "nm": (240, 315),
        "risk": "Ktuner / Hondata ile uygulanan Stage 1 haritası motoru bambaşka bir seviyeye taşır.",
        "cost": 14_000,
        "comments": [
            ("Emre K.", "Civic FC5 RS Ktuner ile 220 HP oldu. 0-100 6.9 saniyeye indi.", 55_000, "sorunsuz"),
        ],
    },
]

# DONANIM PAKETLERİ (Düşük / Orta / Premium)
# Her model için spesifik donanım paketleri ve somut özellik listeleri
TRIM_PACKAGES_DATA = {
    ("Renault", "Megane 4 Sedan"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Giriş Seviyesi - Şehir ve Filo Odaklı",
            "features": ["Manuel Klima", "16\" Çelik Jant Kapakları", "4.2\" Radyo & Bluetooth", "Hız Sabitleyici & Sınırlayıcı", "Elektrikli Ön Camlar", "Kumaş Koltuklar"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "Dengeli Aile ve Konfor Paketi",
            "features": ["Çift Bölgeli Otomatik Dijital Klima", "7\" Easy Link Dokunmatik Ekran & Apple CarPlay", "16\" Alüminyum Alaşım Jantlar", "Arka Park Sensörü", "Eller Serbest Renault Kart Sistemi", "Yağmur ve Far Sensörü"],
        },
        {
            "name": "Icon",
            "level": "premium",
            "summary": "En Üst Düzey Lüks ve Teknoloji Paketi",
            "features": ["Açılır Panoramik Cam Tavan", "Pure Vision Full LED Ön Farlar", "8.7\" Dikey Tablet Easy Link Ekran", "Geri Görüş Kamerası", "Multi-Sense Sürüş Modları & Ambiyans Aydınlatma", "Yarı Deri Koltuklar", "17\" Elmas Kesim Alaşım Jantlar", "Elektronik Park Freni"],
        },
    ],
    ("Renault", "Clio 5"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Ekonomik Giriş Paketi",
            "features": ["Pure Vision Full LED Ön Farlar", "Manuel Klima", "Hız Sabitleyici", "Elektrikli Ön Camlar", "Radyo & Bluetooth"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "Popüler Konfor Paketi",
            "features": ["7\" Dokunmatik Easy Link & CarPlay", "Arka Park Sensörü", "16\" Alaşım Jantlar", "Elektrikli Arka Camlar", "Deri Direksiyon"],
        },
        {
            "name": "Icon",
            "level": "premium",
            "summary": "Full Donanım & Şehir İçi Lüks",
            "features": ["9.3\" Dikey Navigasyonlu Ekran", "7\" Renkli TFT Hayalet Gösterge", "Kablosuz Telefon Şarjı", "Elektronik Park Freni & Auto Hold", "Otomatik Dijital Klima", "Anahtarsız Giriş & Çalıştırma", "Karartılmış Arka Camlar"],
        },
    ],
    ("Fiat", "Egea Sedan"): [
        {
            "name": "Easy",
            "level": "dusuk",
            "summary": "Temel Giriş Paketi",
            "features": ["Manuel Klima", "15\" Jant Kapakları", "Elektrikli Ön Camlar", "Yokuş Kalkış Desteği (Hill Holder)", "Radyo / Bluetooth"],
        },
        {
            "name": "Urban",
            "level": "orta",
            "summary": "En Çok Satan Orta Konfor Paketi",
            "features": ["7\" Dokunmatik Tablet Ekran", "Apple CarPlay & Android Auto", "Full LED Ön Farlar & LED Gündüz Farları", "Otomatik Dijital Klima", "Arka Park Sensörü", "16\" Stil Alaşım Jantlar", "Deri Direksiyon ve Vites Topuzu"],
        },
        {
            "name": "Lounge",
            "level": "premium",
            "summary": "En Üst Zengin Donanım Seviyesi",
            "features": ["10.25\" Geniş HD Multimedya Ekranı", "7\" Dijital Hayalet Kadran", "Kablosuz Şarj Ünitesi", "Kör Nokta Uyarı Sistemi", "Anahtarsız Giriş ve Çalıştırma", "17\" Elmas Kesim Çift Renkli Jantlar", "Krom Dış Detaylar", "Geri Görüş Kamerası"],
        },
    ],
    ("Volkswagen", "Passat B8"): [
        {
            "name": "Impression / Trendline",
            "level": "dusuk",
            "summary": "Giriş Seviyesi D Segment",
            "features": ["16\" Aragon Alaşım Jantlar", "Manuel Klima", "6.5\" Dokunmatik Multimedya", "Anahtarsız Çalıştırma (Keyless Go)", "Elektronik Park Freni & Auto Hold", "LED Arka Stop Lambaları"],
        },
        {
            "name": "Business / Comfortline",
            "level": "orta",
            "summary": "İş Dünyası ve Üst Düzey Aile Konforu",
            "features": ["3 Bölgeli Climatronic Dijital Klima", "Ön ve Arka Park Sensörleri (ParkPilot)", "ErgoComfort Elektrikli & Masajlı Sürücü Koltuğu", "8\" Composition Media Dokunmatik Ekran", "Otomatik Katlanır Yan Aynalar", "Hız Sabitleyici (Cruise Control)", "17\" London Jantlar"],
        },
        {
            "name": "Elegance / Highline",
            "level": "premium",
            "summary": "Zirve Donanım & Prestij",
            "features": ["Açılır Panoramik Cam Tavan", "IQ.LIGHT Matrix LED Ön Farlar & Dinamik Sinyaller", "Active Info Display (Hayalet Gösterge Paneli)", "Isıtmalı Ön Koltuklar", "Koltuk Hafızası", "Nappa / Viyana Deri Döşeme", "Geri Görüş Kamerası", "Kolay Açılır Elektrikli Bagaj Kapağı (Sanal Pedal)", "18\" Dartford Alaşım Jantlar"],
        },
    ],
    ("Volkswagen", "Golf 7"): [
        {
            "name": "Midline Plus",
            "level": "dusuk",
            "summary": "Giriş Paketi",
            "features": ["6.5\" Renkli Dokunmatik Ekran", "Manuel Klima", "15\" Lyon Alaşım Jantlar", "Yorgunluk Tespit Sistemi", "Elektronik Diferansiyel Kilidi (XDS)", "Deri Direksiyon"],
        },
        {
            "name": "Comfortline",
            "level": "orta",
            "summary": "Klasik Golf Konforu",
            "features": ["Çift Bölgeli Otomatik Dijital Klima (Climatronic)", "Ön ve Arka Park Mesafe Sensörleri", "16\" Toronto Alaşım Jantlar", "Yağmur ve Far Sensörü", "Hız Sabitleyici"],
        },
        {
            "name": "Highline",
            "level": "premium",
            "summary": "Premium Golf Donanımı",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED / Bi-Xenon Farlar", "Alcantara Spor Koltuklar", "8\" Composition Media Ekran", "17\" Dijon Alaşım Jantlar", "İç Ambiyans Aydınlatması", "Karartılmış Arka Camlar"],
        },
    ],
    ("Toyota", "Corolla E210"): [
        {
            "name": "Vision",
            "level": "dusuk",
            "summary": "Standart Güvenlik ve Giriş",
            "features": ["Toyota Safety Sense (Otomatik Acil Fren)", "15\" Çelik Jantlar", "Manuel Klima", "4.2\" Renkli Ekran", "LED Gündüz Farları", "Elektrikli Isıtmalı Aynalar"],
        },
        {
            "name": "Dream / Flame",
            "level": "orta",
            "summary": "Dengeli Aile Donanımı",
            "features": ["8\" Toyota Touch 2 Dokunmatik Ekran", "Apple CarPlay & Android Auto", "Çift Bölgeli Dijital Klima", "Geri Görüş Kamerası", "16\" Alüminyum Alaşım Jantlar", "Yağmur Sensörü & Kendiliğinden Kararan Ayna"],
        },
        {
            "name": "Passion X-Pack",
            "level": "premium",
            "summary": "Hibritin En Üst Lüks Versiyonu",
            "features": ["Açılır Elektrikli Sunroof", "Ön Koltuk Isıtma", "Kablosuz Şarj Ünitesi", "Deri Koltuk Döşemeleri", "Head-Up Display (Ön Cama Bilgi Yansıtma)", "7\" Renkli Dijital Hayalet Kadran", "Akıllı Giriş ve Çalıştırma (Keyless)", "17\" Çift Renkli Alüminyum Jantlar"],
        },
    ],
    ("Honda", "Civic FC5"): [
        {
            "name": "Premium",
            "level": "dusuk",
            "summary": "Standart Giriş",
            "features": ["16\" Alaşım Jantlar", "Otomatik Dijital Klima", "Geri Görüş Kamerası", "Elektrikli Park Freni & Brake Hold", "Hız Sabitleyici", "Kumaş Koltuklar"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Türkiye'de En Çok Tercih Edilen Paket",
            "features": ["Açılır Elektrikli Sunroof", "Isıtmalı Ön Koltuklar", "7\" Honda Connect Dokunmatik Multimedya & CarPlay", "Ön ve Arka Park Sensörleri", "Çift Bölgeli Dijital Klima", "Otomatik Kararan Dikiz Aynası"],
        },
        {
            "name": "Executive / RS",
            "level": "premium",
            "summary": "Zirve Donanım & Spor Karakter",
            "features": ["Full LED Ön Farlar & LED Sis Farları", "Hakiki Deri Koltuk Döşemesi", "Isıtmalı Ön Koltuklar", "Anahtarsız Giriş ve Çalıştırma", "Kör Nokta Bilgi Sistemi (LaneWatch Kamera)", "17\" Spor Alaşım Jantlar", "Alüminyum Spor Pedallar"],
        },
    ],
    ("Ford", "Focus 3"): [
        {
            "name": "Trend X",
            "level": "dusuk",
            "summary": "Ekonomik Filo ve Aile Paketi",
            "features": ["16\" Alaşımlı Jantlar", "Manuel Klima", "Hız Kontrol Sistemi", "Deri Kaplı Direksiyon", "Elektrikli Ön-Arka Camlar"],
        },
        {
            "name": "Titanium",
            "level": "orta",
            "summary": "Klasik Ford Konforu",
            "features": ["8\" Dokunmatik SYNC Ekran & Sesli Komut", "Çift Bölgeli Dijital Klima", "Anahtarsız Çalıştırma (Ford Power)", "Otomatik Katlanır Yan Aynalar", "Ön-Arka Park Sensörleri", "İç Ambiyans Aydınlatma"],
        },
        {
            "name": "Titanium X / ST-Line",
            "level": "premium",
            "summary": "Spor & Lüks Zirve Donanım",
            "features": ["Açılır Sunroof", "Bi-Xenon Farlar & Dinamik Far Sistemi", "Geri Görüş Kamerası", "Isıtmalı Ön Koltuklar", "Otomatik Park Sistemi (Kendi Kendine Park Etme)", "17\" Spor Jantlar", "ST-Line Spor Gövde Kiti"],
        },
    ],
    ("Peugeot", "208"): [
        {
            "name": "Active",
            "level": "dusuk",
            "summary": "Giriş Şehir Paketi",
            "features": ["7\" Dokunmatik Multimedya", "Manuel Klima", "Analog i-Cockpit", "Hız Sabitleyici & Şerit Takip", "16\" Jant Kapakları"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "Yeni Nesil 3D i-Cockpit Konforu",
            "features": ["3D Hologram Dijital Hayalet Kadran", "Çift Bölgeli Dijital Klima", "16\" Elmas Kesim Alaşım Jantlar", "Geri Görüş Kamerası & VisioPark", "Anahtarsız Çalıştırma", "Elektrikli El Freni"],
        },
        {
            "name": "GT",
            "level": "premium",
            "summary": "En Üst Düzey Spor & Fransız Şıklığı",
            "features": ["Açılır Cam Tavan", "Full LED 3 Pençeli Ön Farlar & Otomatik Uzun Far", "Koltuk Isıtma", "Alcantara & Yarı Deri Spor Koltuklar", "Kör Nokta Uyarı Sistemi", "10\" HD Geniş Multimedya Ekranı", "17\" Bronz/Siyah Elmas Jantlar"],
        },
    ],
    ("Dacia", "Duster"): [
        {
            "name": "Comfort / Essential",
            "level": "dusuk",
            "summary": "Sade ve Dayanıklı Arazi Girişi",
            "features": ["Manuel Klima", "16\" Çelik Jantlar", "Elektrikli Ön Camlar", "Yokuş Kalkış Desteği", "ECO Sürüş Modu"],
        },
        {
            "name": "Prestige",
            "level": "orta",
            "summary": "Popüler Konfor Donanımı",
            "features": ["8\" Media Nav Dokunmatik Ekran & CarPlay", "Geri Görüş Kamerası ve Arka Park Sensörü", "16\" Alaşım Jantlar", "Hız Sabitleyici", "Ön Sis Farları", "Deri Direksiyon"],
        },
        {
            "name": "Journey / Extreme",
            "level": "premium",
            "summary": "En Dolu Macera ve Arazi Paketi",
            "features": ["360 Derece Çevre Görüş Kamerası (Multiview)", "Kör Nokta Uyarı Sistemi", "Eller Serbest Dacia Kartı (Keyless)", "Otomatik Dijital Klima", "Ön Koltuk Isıtma (Opsiyonel)", "17\" Siyah Alüminyum Jantlar", "Bakır/Turuncu İç ve Dış Tasarım Vurguları"],
        },
    ],
    ("Skoda", "Octavia"): [
        {
            "name": "Ambition",
            "level": "dusuk",
            "summary": "Giriş Seviyesi",
            "features": ["8\" Swing Dokunmatik Multimedya", "Çift Bölgeli Dijital Klima", "LED Ön ve Arka Farlar", "Anahtarsız Çalıştırma", "16\" Twister Alaşım Jantlar"],
        },
        {
            "name": "Style",
            "level": "orta",
            "summary": "Geniş Aile & İş Donanımı",
            "features": ["10.25\" Virtual Cockpit (Hayalet Gösterge)", "10\" Bolero Dokunmatik Geniş Ekran", "Full LED Matrix Ön Farlar", "Ön ve Arka Park Sensörleri", "Elektrikli Katlanır Kararan Yan Aynalar", "17\" Rotare Jantlar"],
        },
        {
            "name": "Premium / RS",
            "level": "premium",
            "summary": "Zirve Prestij ve Lüks",
            "features": ["Panoramik Açılır Cam Tavan", "Canton 12 Hoparlörlü Premium Ses Sistemi", "Koltuk Isıtma (Ön ve Arka)", "Elektrikli & Hafızalı Sürücü Koltuğu", "Kablosuz Şarj & Kablosuz CarPlay", "Elektrikli Bagaj Kapağı ve Sanal Pedal", "18\" Perseus Alaşım Jantlar"],
        },
    ],
}
