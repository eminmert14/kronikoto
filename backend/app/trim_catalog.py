"""KronikOto - 50 Model Resmi Donanım Paketleri ve Özellikleri Kataloğu
Kaynaklar: Resmi Distribütör Fiyat Listeleri / E-Broşürler, Sahibinden.com, Arabam.com
"""

ALL_TRIM_PACKAGES = {
    # 1. RENAULT
    ("Renault", "Megane 4 Sedan"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Ekonomik Filo ve Başlangıç Paketi",
            "features": ["16\" Çelik Jantlar & Kapaklar", "Manuel Klima", "Hız Ayarlayıcı ve Sınırlayıcı (Cruise Control)", "C Şeklinde LED Gündüz Farları", "Bluetooth & USB Bağlantısı", "Elektrikli Ön Camlar"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "Popüler Konfor ve Aile Donanımı",
            "features": ["16\" Alüminyum Alaşım Jantlar", "7\" Dokunmatik Multimedya & Apple CarPlay", "Çift Bölgeli Otomatik Dijital Klima", "Eller Serbest Renault Kart Sistemi (Anahtarsız Giriş & Çalıştırma)", "Yağmur ve Far Sensörü", "Arka Park Sensörü"],
        },
        {
            "name": "Icon",
            "level": "premium",
            "summary": "En Üst Düzey Lüks ve Teknoloji Paketi",
            "features": ["Açılır Panoramik Cam Tavan / Sunroof", "Full LED Pure Vision Ön Farlar", "Multi-Sense Sürüş Modları & Ambiyans Aydınlatma", "Geri Görüş Kamerası", "Elektronik Park Freni", "Yarı Deri Koltuklar", "17\" Elmas Kesim Alüminyum Jantlar"],
        },
    ],
    ("Renault", "Megane 3"): [
        {
            "name": "Authentique",
            "level": "dusuk",
            "summary": "Temel Giriş Seviyesi",
            "features": ["Manuel Klima", "15\" Jant Kapakları", "Elektrikli Ön Camlar", "ABS & Hava Yastıkları", "CD/MP3 Çalar"],
        },
        {
            "name": "Expression / Dynamique",
            "level": "orta",
            "summary": "Dengeli Aile Donanımı",
            "features": ["16\" Alaşım Jantlar", "Çift Bölgeli Dijital Klima", "Far ve Yağmur Sensörü", "Sis Farları", "Hız Sabitleyici", "Deri Direksiyon Simidi"],
        },
        {
            "name": "Privilege / GT-Line",
            "level": "premium",
            "summary": "Döneminin En Dolu Seçeneği",
            "features": ["Açılır Cam Tavan / Sunroof", "Bi-Xenon Mercekli Farlar", "Deri & Kumaş Kombin Koltuklar", "Arka Park Sensörü", "Elektronik El Freni", "17\" Spor Alaşım Jantlar"],
        },
    ],
    ("Renault", "Clio 5"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Şehir İçi Giriş Donanımı",
            "features": ["Pure Vision Full LED Ön Farlar", "Manuel Klima", "Hız Ayarlayıcı ve Sınırlayıcı", "Elektrikli Ön Camlar", "R&Go Radyo & Bluetooth"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "Konforlu B-Segmenti",
            "features": ["7\" EASY LINK Dokunmatik Multimedya & Apple CarPlay", "16\" Alaşım Jantlar", "Arka Park Sensörü", "Elektrikli Isıtmalı Yan Aynalar", "Deri Direksiyon"],
        },
        {
            "name": "Icon / R.S. Line",
            "level": "premium",
            "summary": "Sportif ve Teknolojik Zirve",
            "features": ["Otomatik Dijital Klima", "Geri Görüş Kamerası", "Eller Serbest Kart Sistemi", "Karartılmış Arka Camlar", "Elektrikli Park Freni & Auto-Hold", "Multi-Sense Sürüş Modları", "17\" Elmas Kesim Jantlar"],
        },
    ],
    ("Renault", "Clio 4"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Giriş ve Filo Paketi",
            "features": ["Manuel Klima", "Hız Sabitleyici & Sınırlayıcı", "LED Gündüz Farları", "Elektrikli Ön Camlar", "Bass Reflex Ses Sistemi"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "Orta Seviye Konfor",
            "features": ["16\" Alaşım Jantlar", "7\" Dokunmatik Ekran & Navigasyon", "Deri Direksiyon", "Bluetooth Bağlantısı", "Sis Farları"],
        },
        {
            "name": "Icon",
            "level": "premium",
            "summary": "En Dolu Donanım",
            "features": ["Full LED Pure Vision Farlar", "Dijital Otomatik Klima", "Eller Serbest Kart Sistemi", "Arka Park Sensörü", "Yağmur ve Far Sensörü", "Karartılmış Arka Camlar", "16\"/17\" Çift Renk Jantlar"],
        },
    ],
    ("Renault", "Captur"): [
        {
            "name": "Touch",
            "level": "dusuk",
            "summary": "Kompakt SUV Başlangıcı",
            "features": ["Full LED Farlar", "Manuel Klima", "7\" EASY LINK Dokunmatik Ekran", "Hız Sabitleyici", "Elektrikli Katlanır Aynalar"],
        },
        {
            "name": "Icon",
            "level": "orta",
            "summary": "Ferah ve Teknolojik",
            "features": ["Otomatik Dijital Klima", "Geri Görüş Kamerası & Ön-Arka Park Sensörü", "Multi-Sense Ambiyans", "Karartılmış Camlar", "17\" Alaşım Jantlar", "Anahtarsız Giriş & Çalıştırma"],
        },
        {
            "name": "R.S. Line",
            "level": "premium",
            "summary": "Sportif Tasarım Zirvesi",
            "features": ["Açılır Cam Tavan / Sunroof", "9.3\" Dikey Multimedya Ekranı", "10\" Dijital Hayalet Kadran", "R.S. Line Spor Koltuklar", "Kör Nokta Uyarı Sistemi", "18\" Elmas Kesim Jantlar"],
        },
    ],
    ("Renault", "Kadjar"): [
        {
            "name": "Touch",
            "level": "dusuk",
            "summary": "Geniş Aile SUV Girişi",
            "features": ["17\" Alaşım Jantlar", "Çift Bölgeli Dijital Klima", "Arka Park Sensörü", "7\" R-Link Dokunmatik Ekran", "Elektronik Park Freni"],
        },
        {
            "name": "Icon",
            "level": "premium",
            "summary": "Full Donanımlı C-SUV",
            "features": ["Panoramik Cam Tavan", "Full LED Pure Vision Farlar", "Geri Görüş Kamerası & 360 Park Sensörü", "Kör Nokta Uyarı Sistemi", "Şerit Takip Sistemi", "19\" Elmas Kesim Jantlar", "Deri & Kumaş Koltuklar"],
        },
    ],
    ("Renault", "Austral"): [
        {
            "name": "Techno",
            "level": "dusuk",
            "summary": "Yeni Nesil Hibrit Girişi",
            "features": ["12\" OpenR Link Dokunmatik Ekran", "12.3\" Dijital Kadran", "Full LED Farlar", "Kablosuz Şarj", "Geri Görüş Kamerası & Park Sensörleri"],
        },
        {
            "name": "Techno Esprit Alpine",
            "level": "orta",
            "summary": "Alpine Ruhlu Şıklık",
            "features": ["20\" Daytona Alaşım Jantlar", "Alcantara Döşemeler", "Elektrikli Bagaj Kapağı", "Multi-Sense Ambiyans Aydınlatma", "Karartılmış Camlar", "Alpine Özel Amblemler"],
        },
        {
            "name": "Iconic Esprit Alpine",
            "level": "premium",
            "summary": "Maksimum Lüks ve Otonom Sürüş",
            "features": ["Panoramik Cam Tavan", "Matrix LED Vision Farlar", "Koltuk Isıtma (Ön)", "Masajlı Elektrikli Hafızalı Sürücü Koltuğu", "Kör Nokta & Şerit Ortalama", "Harman Kardon Premium Ses Sistemi", "360 Derece Kamera"],
        },
    ],
    ("Renault", "Taliant"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Ekonomik Şehir Sedanı",
            "features": ["Manuel Klima", "15\" Çelik Jantlar", "Elektrikli Ön Camlar", "Bluetooth Radyo & USB", "Hız Sınırlayıcı"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "Dengeli Aile Donanımı",
            "features": ["8\" Dokunmatik Multimedya & Apple CarPlay", "16\" Alüminyum Alaşım Jantlar", "Arka Park Sensörü", "Otomatik Yanan Farlar", "Elektrikli Arka Camlar", "Deri Direksiyon"],
        },
    ],

    # 2. FIAT
    ("Fiat", "Egea Sedan"): [
        {
            "name": "Easy",
            "level": "dusuk",
            "summary": "Filo ve Başlangıç Donanımı",
            "features": ["15\" Jant Kapakları", "Manuel Klima", "Elektrikli Ön Camlar", "Yokuş Kalkış Desteği", "Bluetooth Radyo", "Elektrikli Yan Aynalar"],
        },
        {
            "name": "Urban",
            "level": "orta",
            "summary": "En Çok Satan Aile Paketi",
            "features": ["16\" Alaşım Jantlar", "7\" Dokunmatik Tablet Ekran & Apple CarPlay", "Otomatik Dijital Klima", "Full LED Ön Farlar", "Arka Park Sensörü", "Deri Direksiyon ve Vites Topuzu"],
        },
        {
            "name": "Lounge / Limited",
            "level": "premium",
            "summary": "En Dolu ve Teknolojik Paket",
            "features": ["17\" Elmas Kesim Alaşım Jantlar", "10\" Dokunmatik Tablet Ekran & Kablosuz CarPlay", "7\" Dijital Renkli Gösterge Paneli (Hayalet Ekran)", "Kör Nokta Uyarı Sistemi", "Kablosuz Cep Telefonu Şarjı", "Anahtarsız Giriş & Çalıştırma", "Geri Görüş Kamerası"],
        },
    ],
    ("Fiat", "Egea Cross"): [
        {
            "name": "Street",
            "level": "dusuk",
            "summary": "Cross Başlangıç Paketi",
            "features": ["16\" Stil Jantlar", "Yükseltilmiş Cross Gövde Kiti", "Manuel Klima", "Elektrikli Ön-Arka Camlar", "Bluetooth & USB"],
        },
        {
            "name": "Urban",
            "level": "orta",
            "summary": "Dengeli Crossover Donanımı",
            "features": ["Full LED Ön Farlar & LED Stoplar", "7\" Dokunmatik Ekran & Apple CarPlay", "Otomatik Klima", "Arka Park Sensörü", "Tavan Rayları", "Deri Direksiyon"],
        },
        {
            "name": "Lounge",
            "level": "premium",
            "summary": "Zirve Cross Donanımı",
            "features": ["17\" Elmas Kesim Cross Jantlar", "10\" Multimedya & Kablosuz Apple CarPlay", "7\" Dijital Gösterge", "Geri Görüş Kamerası", "Kör Nokta Uyarısı", "Anahtarsız Giriş & Çalıştırma", "Kablosuz Şarj"],
        },
    ],
    ("Fiat", "Linea"): [
        {
            "name": "Actual",
            "level": "dusuk",
            "summary": "Giriş Seviyesi",
            "features": ["Manuel Klima", "15\" Jant Kapakları", "Elektrikli Ön Camlar", "ABS & Çift Hava Yastığı"],
        },
        {
            "name": "Active Plus",
            "level": "orta",
            "summary": "Klasik Aile Donanımı",
            "features": ["Gövde Rengi Aynalar", "Ön Sis Farları", "Elektrikli Arka Camlar", "Yol Bilgisayarı", "CD/MP3 Çalar"],
        },
        {
            "name": "Lounge",
            "level": "premium",
            "summary": "En Dolu Linea",
            "features": ["16\" Alaşım Jantlar", "Otomatik Dijital Klima", "Arka Park Sensörü", "Yağmur ve Far Sensörü", "Krom Dış Detaylar", "Blue&Me Sesli Komut"],
        },
    ],
    ("Fiat", "Doblo"): [
        {
            "name": "Easy",
            "level": "dusuk",
            "summary": "Temel Ticari Donanım",
            "features": ["Manuel Klima", "Elektrikli Ön Camlar", "Çift Sürgülü Yan Kapılar", "ABS & ESP"],
        },
        {
            "name": "Safeline",
            "level": "orta",
            "summary": "Dengeli Aile ve İş Kombisi",
            "features": ["16\" Alaşım Jantlar", "Ön Sis Farları", "5\" Dokunmatik Ekran", "Gövde Rengi Tamponlar", "Tavan Rayları"],
        },
        {
            "name": "Premio Plus",
            "level": "premium",
            "summary": "Binek Konforunda Ticari",
            "features": ["Otomatik Dijital Klima", "7\" Dokunmatik Ekran & Apple CarPlay", "Geri Görüş Kamerası", "Hız Sabitleyici", "Deri Direksiyon", "Karartılmış Arka Camlar"],
        },
    ],

    # 3. VOLKSWAGEN
    ("Volkswagen", "Passat B8"): [
        {
            "name": "Impression / Trendline",
            "level": "dusuk",
            "summary": "D-Segment Başlangıç Prestiji",
            "features": ["16\" Aragon Alaşım Jantlar", "LED Ön Farlar ve LED Gündüz Farları", "Keyless Go (Anahtarsız Çalıştırma)", "6.5\" Composition Colour Multimedya", "Elektronik Park Freni & Auto Hold", "Yorgunluk Tespit Sistemi"],
        },
        {
            "name": "Business / Comfortline",
            "level": "orta",
            "summary": "Klasik Passat Konforu (En Çok Tercih Edilen)",
            "features": ["17\" London Alaşım Jantlar", "3 Bölgeli Tam Otomatik Climatronic Klima", "8\" Composition Media & App-Connect (CarPlay)", "Ön ve Arka Park Mesafe Sensörleri", "Kendiliğinden Kararan İç Dikiz Aynası", "Hız Sabitleyici & Sınırlayıcı"],
        },
        {
            "name": "Elegance / Highline",
            "level": "premium",
            "summary": "En Üst Düzey Lüks ve Yönetici Konforu",
            "features": ["Açılır Panoramik Cam Tavan / Sunroof", "IQ.Light LED Matrix Farlar & Dinamik Kayan Sinyaller", "Koltuk Isıtma (Ön)", "Masajlı ErgoComfort Sürücü Koltuğu", "Active Info Display (10.25\" Hayalet Ekran)", "Elektrikli Bagaj Kapağı (Easy Open)", "Alcantara / Deri Koltuk Döşemesi"],
        },
    ],
    ("Volkswagen", "Passat B7"): [
        {
            "name": "Trendline",
            "level": "dusuk",
            "summary": "Giriş Seviyesi",
            "features": ["16\" Çelik Jantlar", "Climatic Yarı Otomatik Klima", "Elektromekanik Park Freni", "RCD 310 Müzik Sistemi", "Hız Sabitleyici"],
        },
        {
            "name": "Comfortline",
            "level": "orta",
            "summary": "Dengeli Konfor",
            "features": ["16\" Perpignan Alaşım Jantlar", "Çift Bölgeli Dijital Klima", "Ön ve Arka Park Sensörleri", "Otomatik Kararan Ayna", "Yağmur Sensörü", "Elektrikli Bel Destekli Koltuk"],
        },
        {
            "name": "Highline",
            "level": "premium",
            "summary": "Döneminin Zirvesi",
            "features": ["Açılır Sunroof", "Bi-Xenon Farlar & LED Gündüz Işıkları", "Koltuk Isıtma", "Alcantara/Vienna Deri Koltuklar", "17\" Fontana Alaşım Jantlar", "Karartılmış Arka Camlar"],
        },
    ],
    ("Volkswagen", "Golf 7"): [
        {
            "name": "Midline Plus",
            "level": "dusuk",
            "summary": "Kompakt Başlangıç",
            "features": ["15\" Lyon Alaşım Jantlar", "Manuel Klima", "Elektronik Park Freni & Auto Hold", "5\" Dokunmatik Ekran", "Start & Stop Sistemi"],
        },
        {
            "name": "Comfortline",
            "level": "orta",
            "summary": "En Sevilen Golf Donanımı",
            "features": ["16\" Dover Alaşım Jantlar", "Çift Bölgeli Climatronic Klima", "6.5\"/8\" Composition Media & Bluetooth", "Ön-Arka Park Sensörü", "Ön Sis Farları & Viraj Aydınlatması", "Işık ve Görüş Paketi"],
        },
        {
            "name": "Highline / R-Line",
            "level": "premium",
            "summary": "Zirve C-Hatchback Konforu",
            "features": ["Açılır Cam Tavan / Sunroof", "Bi-Xenon / LED Ön Farlar", "Alcantara Spor Koltuklar", "17\" Dijon Alaşım Jantlar", "Ambiyans Aydınlatma", "Geri Görüş Kamerası", "Karartılmış Arka Camlar"],
        },
    ],
    ("Volkswagen", "Polo"): [
        {
            "name": "Impression",
            "level": "dusuk",
            "summary": "Şehir İçi Başlangıç",
            "features": ["LED Ön Farlar ve LED Gündüz Sürüş Farları", "6.5\" Dokunmatik Ekran", "Manuel Klima", "Hız Sınırlayıcı", "Elektrikli Isıtmalı Aynalar"],
        },
        {
            "name": "Life",
            "level": "orta",
            "summary": "Popüler B-Segment Konforu",
            "features": ["15\" Essex Alaşım Jantlar", "8\" Dijital Gösterge Paneli (Digital Cockpit)", "Kablosuz App-Connect (Apple CarPlay)", "Ön-Arka Park Sensörleri", "Kablosuz Şarj"],
        },
        {
            "name": "Style",
            "level": "premium",
            "summary": "Küçük Golf Kalitesi",
            "features": ["Açılır Cam Tavan", "IQ.Light LED Matrix Farlar", "10.25\" Digital Cockpit Pro (Geniş Hayalet Ekran)", "Çift Bölgeli Climatronic Klima", "Keyless Access (Anahtarsız Giriş & Çalıştırma)", "16\" Palermo Alaşım Jantlar"],
        },
    ],
    ("Volkswagen", "Tiguan"): [
        {
            "name": "Life",
            "level": "dusuk",
            "summary": "Geniş Aile SUV Girişi",
            "features": ["17\" Montana Alaşım Jantlar", "LED Farlar", "3 Bölgeli Climatronic Klima", "8\" Multimedya & App-Connect", "Ön ve Arka Park Sensörleri"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Lüks ve Ferahlık",
            "features": ["Açılır Panoramik Cam Tavan", "IQ.Light LED Matrix Farlar", "10.25\" Dijital Gösterge (Digital Cockpit Pro)", "Koltuk Isıtma (Ön)", "Elektrikli Bagaj Kapağı (Easy Open)", "18\" Frankfurt Alaşım Jantlar"],
        },
        {
            "name": "R-Line",
            "level": "premium",
            "summary": "Sportif Zirve Donanım",
            "features": ["19\" Valencia R-Line Jantlar", "R-Line Spor Gövde Tasarımı", "Panoramik Cam Tavan", "Spor Süspansiyon", "R-Line Spor Direksiyon ve Koltuklar", "30 Renkli Ambiyans Aydınlatma"],
        },
    ],
    ("Volkswagen", "T-Roc"): [
        {
            "name": "Life",
            "level": "dusuk",
            "summary": "Crossover Başlangıç",
            "features": ["16\" Chester Alaşım Jantlar", "LED Farlar", "Dijital Gösterge Paneli", "App-Connect", "Ön-Arka Park Sensörü", "Çift Bölgeli Klima"],
        },
        {
            "name": "Style",
            "level": "orta",
            "summary": "Şık Şehir Donanımı",
            "features": ["17\" Kulmbach Alaşım Jantlar", "Geri Görüş Kamerası", "Anahtarsız Giriş & Çalıştırma", "Karartılmış Arka Camlar", "Ambiyans Aydınlatma"],
        },
        {
            "name": "R-Line",
            "level": "premium",
            "summary": "Sportif Kompakt SUV",
            "features": ["Açılır Panoramik Cam Tavan", "IQ.Light LED Matrix Farlar", "17\" Valencia Jantlar", "R-Line Gövde Kiti", "Isıtmalı Ön Koltuklar", "Spor Direksiyon"],
        },
    ],

    # 4. TOYOTA
    ("Toyota", "Corolla"): [
        {
            "name": "Vision",
            "level": "dusuk",
            "summary": "Temel Filo ve Aile Paketi",
            "features": ["15\"/16\" Çelik Jantlar", "Manuel/Otomatik Klima", "Hız Sabitleyici", "8\" Multimedya Ekranı & Apple CarPlay", "Elektrikli Camlar", "Geri Görüş Kamerası"],
        },
        {
            "name": "Dream / Flame",
            "level": "orta",
            "summary": "En Popüler Donanım",
            "features": ["16\" Alüminyum Alaşımlı Jantlar", "Çift Bölgeli Otomatik Klima", "Toyota Safety Sense (Şerit Takip, Çarpışma Önleyici, Adaptif Hız Sabitleyici)", "Kablosuz Şarj Ünitesi", "Yağmur ve Far Sensörü", "Karartılmış Arka Camlar"],
        },
        {
            "name": "Passion X-Pack",
            "level": "premium",
            "summary": "Zirve Hibrit & Benzin Konforu",
            "features": ["Açılır Sunroof", "17\" Çift Renk Alüminyum Jantlar", "10.5\" Toyota Touch Multimedya & 12.3\" Dijital Hayalet Gösterge", "Koltuk Isıtma (Ön)", "Akıllı Giriş ve Çalıştırma (Keyless Go)", "Deri & Kumaş Koltuklar", "Ambiyans Aydınlatma"],
        },
    ],
    ("Toyota", "Yaris"): [
        {
            "name": "Vision",
            "level": "dusuk",
            "summary": "Şehir Başlangıcı",
            "features": ["15\" Jant Kapakları", "Manuel Klima", "7\" Multimedya & Apple CarPlay", "Toyota Safety Sense"],
        },
        {
            "name": "Dream / Flame",
            "level": "orta",
            "summary": "Dengeli Şehir İçi",
            "features": ["15\"/16\" Alaşım Jantlar", "Dijital Otomatik Klima", "Geri Görüş Kamerası", "Yağmur Sensörü", "Deri Direksiyon"],
        },
        {
            "name": "Passion / Style",
            "level": "premium",
            "summary": "Dolu ve Şık B-Segment",
            "features": ["Çift Renk Gövde (Siyah Tavan)", "Panoramik Cam Tavan", "Anahtarsız Giriş & Çalıştırma", "16\" Çift Renkli Jantlar", "Kablosuz Şarj"],
        },
    ],
    ("Toyota", "C-HR"): [
        {
            "name": "Flame",
            "level": "dusuk",
            "summary": "Fütüristik Crossover Başlangıcı",
            "features": ["17\" Alaşım Jantlar", "Toyota Safety Sense", "Geri Görüş Kamerası", "Çift Bölgeli Dijital Klima", "8\" Dokunmatik Ekran"],
        },
        {
            "name": "Passion",
            "level": "orta",
            "summary": "Lüks Hibrit Deneyimi",
            "features": ["18\" Alüminyum Jantlar", "Akıllı Giriş & Çalıştırma", "Koltuk Isıtma (Ön)", "Kör Nokta Uyarı Sistemi", "Karartılmış Camlar"],
        },
        {
            "name": "GR Sport",
            "level": "premium",
            "summary": "Gazoo Racing Spor Paketi",
            "features": ["19\" Özel GR Sport Jantlar", "JBL Premium Ses Sistemi", "Alcantara Spor Koltuklar", "GR Sport Süspansiyon Ayarı", "Bi-LED Farlar"],
        },
    ],

    # 5. HONDA
    ("Honda", "Civic Sedan (FC5)"): [
        {
            "name": "Premium",
            "level": "dusuk",
            "summary": "Giriş Seviyesi Sedan",
            "features": ["16\" Alüminyum Jantlar", "Otomatik Klima", "5\" Multimedya & Bluetooth", "Hız Sabitleyici", "LED Gündüz Farları", "Elektrikli Park Freni & Brake Hold"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "En Çok Satan Civic Donanımı (LPG & Benzin)",
            "features": ["16\" Alaşım Jantlar", "7\" Honda Connect Dokunmatik Ekran & Apple CarPlay", "Koltuk Isıtma (Ön Koltuklar)", "Geri Görüş Kamerası", "Ön ve Arka Park Sensörleri", "Çift Bölgeli Otomatik Klima", "Yağmur ve Far Sensörü"],
        },
        {
            "name": "Executive / RS",
            "level": "premium",
            "summary": "Sunroof ve Deri Koltuklu Zirve Donanım",
            "features": ["Açılır Sunroof", "Full LED Ön Farlar", "Deri Koltuk Döşemesi", "Anahtarsız Giriş ve Çalıştırma", "17\" Spor Alaşımlı Jantlar", "Karartılmış Arka Camlar", "Bagaj Üstü Spoiler (RS)"],
        },
    ],
    ("Honda", "Civic Sedan (FB7)"): [
        {
            "name": "Dream",
            "level": "dusuk",
            "summary": "Temel Donanım",
            "features": ["15\" Jant Kapakları", "Manuel/Yarı Otomatik Klima", "Elektrikli Camlar", "VSA Araç Denge Kontrolü"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Klasik FB7 Donanımı",
            "features": ["Açılır Sunroof", "16\" Alaşım Jantlar", "Otomatik Dijital Klima", "Koltuk Isıtma (Ön)", "Geri Görüş Kamerası", "Hız Sabitleyici"],
        },
        {
            "name": "Executive",
            "level": "premium",
            "summary": "En Dolu FB7",
            "features": ["Xenon Ön Farlar & Far Yıkama", "Deri Koltuklar", "Sunroof", "Navigasyonlu Dokunmatik Ekran", "Bluetooth Telefon Bağlantısı"],
        },
    ],

    # 6. FORD
    ("Ford", "Focus 4"): [
        {
            "name": "Trend X",
            "level": "dusuk",
            "summary": "Ekonomik Filo ve Başlangıç",
            "features": ["16\" Alaşımlı Jantlar", "Manuel Klima", "Hız Kontrol Sistemi", "Deri Direksiyon", "Elektrikli Ön-Arka Camlar", "Seçilebilir Sürüş Modları"],
        },
        {
            "name": "Titanium",
            "level": "orta",
            "summary": "Prestijli ve Konforlu",
            "features": ["8\" SYNC 3 Dokunmatik Ekran & Apple CarPlay", "Çift Bölgeli Dijital Klima", "Anahtarsız Giriş & Çalıştırma", "Ön-Arka Park Sensörü", "Otomatik Katlanan Aynalar", "Karartmalı Dikiz Aynası"],
        },
        {
            "name": "ST-Line",
            "level": "premium",
            "summary": "Sportif Zirve Tasarım",
            "features": ["Açılır Panoramik Cam Tavan / Sunroof", "17\"/18\" ST-Line Spor Jantlar", "ST-Line Gövde Kiti ve Kırmızı Dikişli İç Mekan", "Full LED Farlar", "Spor Süspansiyon", "Kablosuz Şarj"],
        },
    ],
    ("Ford", "Focus 3"): [
        {
            "name": "Trend X",
            "level": "dusuk",
            "summary": "Giriş Seviyesi",
            "features": ["16\" Alüminyum Jantlar", "Manuel Klima", "Hız Sabitleyici", "Deri Kaplı Direksiyon", "Elektrikli Aynalar"],
        },
        {
            "name": "Titanium",
            "level": "orta",
            "summary": "Geleneksel Konfor",
            "features": ["8\" SYNC Dokunmatik Ekran", "Çift Bölgeli Otomatik Klima", "Anahtarsız Çalıştırma (Ford Power)", "Otomatik Katlanır Yan Aynalar", "Yağmur Sensörü"],
        },
        {
            "name": "Titanium X / Smart",
            "level": "premium",
            "summary": "Full Donanım",
            "features": ["Açılır Sunroof", "Bi-Xenon Dinamik Ön Farlar", "Geri Görüş Kamerası", "Otomatik Park Sistemi (Kendi Kendine Park Etme)", "17\" Spor Jantlar", "Isıtmalı Ön Cam"],
        },
    ],
    ("Ford", "Puma"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Şık Crossover Başlangıcı",
            "features": ["17\" Alaşım Jantlar", "8\" SYNC 3 Dokunmatik Ekran", "Arka Park Sensörü", "Manuel Klima", "Şerit Takip Sistemi"],
        },
        {
            "name": "Titanium",
            "level": "orta",
            "summary": "Konforlu Şehir SUV",
            "features": ["Otomatik Dijital Klima", "Kablosuz Şarj", "Karartılmış Arka Camlar", "Yağmur Sensörü", "Navigasyon Desteği"],
        },
        {
            "name": "ST-Line",
            "level": "premium",
            "summary": "Dinamik Spor Donanım",
            "features": ["Açılır Panoramik Cam Tavan", "12.3\" Dijital Hayalet Gösterge Paneli", "Full LED Ön Farlar", "ST-Line Gövde Kiti", "B&O Premium Ses Sistemi", "18\" Mat Siyah Jantlar"],
        },
    ],

    # 7. PEUGEOT
    ("Peugeot", "208"): [
        {
            "name": "Active",
            "level": "dusuk",
            "summary": "Giriş Şehir Donanımı",
            "features": ["7\" Dokunmatik Ekran & CarPlay", "Manuel Klima", "Hız Sabitleyici", "LED Gündüz Farları", "Şerit Takip Asistanı"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "3D i-Cockpit Konforu",
            "features": ["3D Hologram Dijital Gösterge Paneli", "Otomatik Dijital Klima", "16\" Alaşım Jantlar", "Geri Görüş Kamerası (VisioPark)", "Anahtarsız Çalıştırma", "Elektrikli El Freni"],
        },
        {
            "name": "GT",
            "level": "premium",
            "summary": "Fransız Şıklığı ve Spor Tasarım",
            "features": ["Açılır Cam Tavan", "Full LED 3 Pençeli Ön Farlar & Uzun Far Asistanı", "Koltuk Isıtma (Ön)", "Kör Nokta Uyarı Sistemi", "10\" Geniş Dokunmatik Ekran", "17\" Bronz/Siyah Elmas Jantlar"],
        },
    ],
    ("Peugeot", "2008"): [
        {
            "name": "Active",
            "level": "dusuk",
            "summary": "B-SUV Başlangıcı",
            "features": ["16\" Alaşım Jantlar", "7\" Dokunmatik Multimedya", "Manuel/Otomatik Klima", "Arka Park Sensörü", "Hız Sabitleyici"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "Popüler ve Dengeli",
            "features": ["3D Dijital Hayalet Kadran", "Otomatik Dijital Klima", "Geri Görüş Kamerası", "17\" Salamanca Alaşım Jantlar", "Elektrikli Katlanır Aynalar", "Tavan Barları"],
        },
        {
            "name": "GT",
            "level": "premium",
            "summary": "En Üst Düzey Crossover",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Ön Farlar & 3D LED Arka Stoplar", "Koltuk Isıtma", "Kablosuz Şarj", "Kör Nokta Uyarı Sistemi", "18\" Evissa Çift Renkli Jantlar"],
        },
    ],
    ("Peugeot", "3008"): [
        {
            "name": "Active Prime",
            "level": "dusuk",
            "summary": "C-SUV Giriş Seviyesi",
            "features": ["17\" Alaşım Jantlar", "12.3\" Dijital Gösterge Paneli (i-Cockpit)", "Çift Bölgeli Dijital Klima", "Geri Görüş Kamerası", "Ön-Arka Park Sensörü", "8\" Dokunmatik Ekran"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "Yüksek Konfor ve Teknoloji",
            "features": ["18\" Detroit Alaşım Jantlar", "10\" Dokunmatik Multimedya Ekranı", "Anahtarsız Giriş & Çalıştırma", "Kör Nokta Uyarı Sistemi", "Karartılmış Camlar", "Yarı Deri Koltuklar"],
        },
        {
            "name": "GT",
            "level": "premium",
            "summary": "Zirve Tasarım ve Lüks",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Ön Farlar & Statik Viraj Farları", "Koltuk Isıtma (Ön)", "Focal Premium Ses Sistemi", "Elektrikli Ayakla Açılan Bagaj Kapağı", "19\" San Francisco Alaşım Jantlar", "Alcantara İç Trimler"],
        },
    ],

    # 8. SKODA
    ("Skoda", "Octavia"): [
        {
            "name": "Elite",
            "level": "dusuk",
            "summary": "Geniş Aile Başlangıcı",
            "features": ["16\" Twister Alaşım Jantlar", "LED Ön ve Arka Farlar", "Çift Bölgeli Dijital Klima", "8.25\" Dokunmatik Ekran & SmartLink", "Anahtarsız Çalıştırma"],
        },
        {
            "name": "Premium",
            "level": "orta",
            "summary": "Çok Tercih Edilen Konfor",
            "features": ["17\" Rotare Alaşım Jantlar", "10.25\" Dijital Hayalet Gösterge Paneli", "10\" Geniş Multimedya", "Geri Görüş Kamerası", "Kablosuz Şarj", "Ön-Arka Park Sensörleri"],
        },
        {
            "name": "Prestige",
            "level": "premium",
            "summary": "En Dolu Donanım",
            "features": ["Açılır Panoramik Cam Tavan / Sunroof", "Matrix LED Farlar & Dinamik Sinyaller", "Koltuk Isıtma (Ön Koltuklar)", "Kör Nokta Algılama (Side Assist)", "Elektrikli Bagaj Kapağı (Sanal Pedal)", "18\" Perseus Alaşım Jantlar"],
        },
    ],
    ("Skoda", "Superb"): [
        {
            "name": "Elite",
            "level": "dusuk",
            "summary": "D-Segment Makam Girişi",
            "features": ["17\" Stratos Alaşım Jantlar", "LED Farlar", "Çift Bölgeli Dijital Klima", "8\" Bolero Dokunmatik Ekran", "Arka Park Sensörü", "Elektrikli Katlanır Aynalar"],
        },
        {
            "name": "Premium",
            "level": "orta",
            "summary": "Geniş Konfor ve Prestij",
            "features": ["18\" Antares Alaşım Jantlar", "Dijital Gösterge Paneli (Hayalet Ekran)", "Anahtarsız Giriş & Çalıştırma (Kessy Full)", "Ön-Arka Park Sensörü & Geri Görüş Kamerası", "Elektrikli Hafızalı Sürücü Koltuğu"],
        },
        {
            "name": "Prestige / L&K Crystal",
            "level": "premium",
            "summary": "Zirve Lüks ve Konfor",
            "features": ["Açılır Panoramik Cam Tavan", "Matrix Full LED Ön Farlar", "Deri Koltuklar & Ön-Arka Koltuk Isıtma", "Canton Premium Ses Sistemi", "Elektrikli Bagaj Kapağı", "Kör Nokta Uyarı Sistemi", "19\" Trinity Alaşım Jantlar"],
        },
    ],

    # 9. HYUNDAI
    ("Hyundai", "i20"): [
        {
            "name": "Jump",
            "level": "dusuk",
            "summary": "Şehir İçi Başlangıç",
            "features": ["15\" Jant Kapakları", "Manuel Klima", "3.8\" Gösterge Ekranı", "Hız Sabitleyici", "Elektrikli Ön Camlar"],
        },
        {
            "name": "Style",
            "level": "orta",
            "summary": "Popüler Şehir Donanımı",
            "features": ["16\" Alaşım Jantlar", "8\" Dokunmatik Ekran & Apple CarPlay", "Geri Görüş Kamerası", "Ön Sis Farları", "Arka Park Sensörü"],
        },
        {
            "name": "Elite",
            "level": "premium",
            "summary": "En Dolu B-Segment",
            "features": ["Açılır Cam Tavan / Sunroof", "10.25\" Dijital Hayalet Kadran", "Otomatik Dijital Klima", "Kablosuz Şarj", "LED Ön Farlar & LED Stoplar", "Anahtarsız Giriş & Çalıştırma", "17\" Elmas Kesim Jantlar"],
        },
    ],
    ("Hyundai", "Elantra"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Giriş Seviyesi Sedan",
            "features": ["15\" Çelik Jantlar", "Manuel Klima", "8\" Dokunmatik Ekran", "Geri Görüş Kamerası", "Hız Sabitleyici"],
        },
        {
            "name": "Style Comfort",
            "level": "orta",
            "summary": "Dengeli Konfor",
            "features": ["16\" Alaşım Jantlar", "Çift Bölgeli Otomatik Klima", "Anahtarsız Giriş & Çalıştırma", "Yağmur Sensörü", "Karartılmış Camlar"],
        },
        {
            "name": "Elite Plus",
            "level": "premium",
            "summary": "Lüks ve Fütüristik",
            "features": ["Açılır Sunroof", "10.25\" Dijital Gösterge & 10.25\" Multimedya", "Koltuk Isıtma (Ön)", "Deri Koltuklar", "Kör Nokta Çarpışma Önleme", "17\" Alaşım Jantlar", "Kablosuz Şarj"],
        },
    ],
    ("Hyundai", "Tucson"): [
        {
            "name": "Comfort",
            "level": "dusuk",
            "summary": "Kompakt SUV Başlangıcı",
            "features": ["17\" Alaşım Jantlar", "8\" Dokunmatik Ekran", "Geri Görüş Kamerası", "Manuel/Yarı Otomatik Klima", "Şerit Takip Asistanı"],
        },
        {
            "name": "Prime Plus",
            "level": "orta",
            "summary": "En Çok Satan Tucson Donanımı",
            "features": ["18\" Alaşım Jantlar", "10.25\" Dokunmatik Ekran & Apple CarPlay", "10.25\" Dijital Hayalet Kadran", "Çift Bölgeli Dijital Klima", "Anahtarsız Giriş & Çalıştırma", "Kablosuz Şarj"],
        },
        {
            "name": "Elite Plus",
            "level": "premium",
            "summary": "Zirve Donanım ve Konfor",
            "features": ["Açılır Panoramik Cam Tavan", "Koltuk Isıtma (Ön ve Arka)", "Koltuk Havalandırma (Ön)", "Krell Premium Ses Sistemi", "Kör Nokta Görüntüleme Asistanı (Kameralı Kadran)", "Elektrikli Bagaj Kapağı", "19\" Elmas Kesim Jantlar"],
        },
    ],

    # 10. KIA
    ("Kia", "Ceed"): [
        {
            "name": "Cool",
            "level": "dusuk",
            "summary": "Giriş Seviyesi",
            "features": ["16\" Çelik Jantlar", "Manuel Klima", "8\" Dokunmatik Ekran & CarPlay", "Geri Görüş Kamerası", "Hız Sabitleyici"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Dengeli Konfor",
            "features": ["16\" Alaşım Jantlar", "Çift Bölgeli Otomatik Klima", "Yağmur Sensörü", "Karartılmış Camlar", "Deri Direksiyon"],
        },
        {
            "name": "Prestige",
            "level": "premium",
            "summary": "En Dolu Donanım",
            "features": ["Açılır Cam Tavan / Sunroof", "10.25\" Geniş Multimedya", "12.3\" Dijital Gösterge Paneli", "Koltuk Isıtma (Ön)", "Anahtarsız Giriş & Çalıştırma", "Kablosuz Şarj", "17\" Alaşım Jantlar"],
        },
    ],
    ("Kia", "Sportage"): [
        {
            "name": "Cool",
            "level": "dusuk",
            "summary": "SUV Başlangıcı",
            "features": ["17\" Alaşım Jantlar", "LED Farlar", "Çift Bölgeli Otomatik Klima", "8\" Dokunmatik Ekran", "Geri Görüş Kamerası"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Popüler Konfor",
            "features": ["18\" Alaşım Jantlar", "12.3\" Kavisli Geniş Ekran", "Anahtarsız Giriş & Çalıştırma", "Ön ve Arka Park Sensörleri", "Kablosuz Şarj"],
        },
        {
            "name": "Prestige",
            "level": "premium",
            "summary": "Maksimum Lüks",
            "features": ["Açılır Panoramik Cam Tavan", "Koltuk Isıtma (Ön ve Arka)", "Koltuk Havalandırma (Ön)", "Elektrikli Bagaj Kapağı", "Kör Nokta İzleme Asistanı", "19\" Elmas Kesim Jantlar", "Harman Kardon Ses"],
        },
    ],

    # 11. OPEL
    ("Opel", "Astra K"): [
        {
            "name": "Edition",
            "level": "dusuk",
            "summary": "Başlangıç Seviyesi",
            "features": ["16\" Çelik/Alaşım Jantlar", "Manuel/Elektronik Klima", "7\" Dokunmatik IntelliLink & Apple CarPlay", "Hız Sabitleyici", "Elektrikli Camlar"],
        },
        {
            "name": "Dynamic",
            "level": "orta",
            "summary": "Sportif Aile Donanımı",
            "features": ["17\" Alaşım Jantlar", "Çift Bölgeli Otomatik Klima", "Anahtarsız Giriş & Çalıştırma", "Spor Koltuklar", "Ön-Arka Park Sensörü", "Trafik İşareti Tespit Sistemi"],
        },
        {
            "name": "Excellence",
            "level": "premium",
            "summary": "Zirve Alman Konforu",
            "features": ["Açılır Sunroof", "IntelliLux LED Matrix Farlar", "Koltuk Isıtma (Ön)", "Elektronik Park Freni", "Yarı Deri AGR Sertifikalı Ergonomik Koltuklar", "Karartılmış Camlar"],
        },
    ],
    ("Opel", "Corsa"): [
        {
            "name": "Edition",
            "level": "dusuk",
            "summary": "Şehir İçi Başlangıç",
            "features": ["16\" Alaşım Jantlar", "7\" Dokunmatik Ekran & CarPlay", "Manuel Klima", "Şerit Koruma Asistanı", "Hız Sabitleyici"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Konfor Odaklı",
            "features": ["7\" Dijital Sürücü Göstergesi", "Otomatik Klima", "Geri Görüş Kamerası", "LED Sis Farları", "Elektrikli Katlanır Yan Aynalar"],
        },
        {
            "name": "GS / Ultimate",
            "level": "premium",
            "summary": "Sportif Zirve",
            "features": ["Panoramik Cam Tavan", "17\" Çift Renkli Spor Jantlar", "Full LED Ön Farlar", "Koltuk Isıtma", "Spor Tamponlar & Siyah Tavan", "Anahtarsız Giriş & Çalıştırma"],
        },
    ],
    ("Opel", "Mokka"): [
        {
            "name": "Elegance",
            "level": "dusuk",
            "summary": "Şık Crossover Girişi",
            "features": ["17\" Alaşım Jantlar", "7\" Dijital Gösterge & 7\" Multimedya", "Otomatik Klima", "Geri Görüş Kamerası", "Şerit Takip"],
        },
        {
            "name": "GS",
            "level": "orta",
            "summary": "Sportif Tasarım",
            "features": ["18\" Çift Renkli Jantlar", "Siyah Tavan ve Karartılmış Camlar", "Geri Görüş Kamerası (180 derece)", "Alüminyum Pedallar", "Kör Nokta Uyarısı"],
        },
        {
            "name": "Ultimate",
            "level": "premium",
            "summary": "En Dolu Mokka",
            "features": ["Açılır Cam Tavan", "IntelliLux LED Matrix Farlar", "10\" Multimedya & 12\" Pure Panel Dijital Kadran", "Koltuk Isıtma & Direksiyon Isıtma", "Alcantara Koltuklar", "Anahtarsız Giriş & Çalıştırma"],
        },
    ],

    # 12. DACIA
    ("Dacia", "Duster"): [
        {
            "name": "Essential",
            "level": "dusuk",
            "summary": "Sade ve Dayanıklı Arazi Girişi",
            "features": ["16\" Çelik Jantlar", "Manuel Klima", "Elektrikli Ön Camlar", "Yokuş Kalkış Desteği", "ECO Sürüş Modu", "Bluetooth Radyo"],
        },
        {
            "name": "Expression",
            "level": "orta",
            "summary": "Dengeli ve Kullanışlı",
            "features": ["16\" Alüminyum Alaşımlı Jantlar", "8\" Dokunmatik Multimedya & Apple CarPlay", "Arka Park Sensörü", "Hız Ayarlayıcı ve Sınırlayıcı", "Elektrikli Arka Camlar", "Ön Sis Farları"],
        },
        {
            "name": "Journey / Extreme",
            "level": "premium",
            "summary": "Zirve Donanımlı Duster",
            "features": ["Otomatik Dijital Klima", "Eller Serbest Dacia Kart Sistemi (Anahtarsız Giriş & Çalıştırma)", "Kör Nokta Uyarı Sistemi", "Çok Açılı Kamera (4 Kameralı Çevre Görüş)", "17\" Tergan Yarı Elmas Jantlar", "Bakır Renkli Özel Dış & İç Tasarım Detayları (Extreme)"],
        },
    ],
    ("Dacia", "Sandero Stepway"): [
        {
            "name": "Essential",
            "level": "dusuk",
            "summary": "Yükseltilmiş Şehir Girişi",
            "features": ["16\" Kapak Jantlar", "Manuel Klima", "Elektrikli Ön Camlar", "Hız Sabitleyici", "Tavan Barları"],
        },
        {
            "name": "Expression",
            "level": "orta",
            "summary": "Popüler Donanım",
            "features": ["8\" Dokunmatik Ekran & Apple CarPlay", "Arka Park Sensörü", "Otomatik Farlar", "Elektrikli Yan Aynalar"],
        },
        {
            "name": "Extreme",
            "level": "premium",
            "summary": "Zirve Crossover",
            "features": ["Otomatik Dijital Klima", "Geri Görüş Kamerası", "Eller Serbest Kart", "Bakır Detaylar & Su Tutmaz Özel Kumaş", "Kör Nokta Uyarısı", "16\" Siyah Alaşım Jantlar"],
        },
    ],

    # ================= AUDI (5 MODEL) =================
    ("Audi", "A3 Sedan"): [
        {
            "name": "Dynamic / Ambiente",
            "level": "dusuk",
            "summary": "Premium C-Sedan Giriş Paketi",
            "features": ["16\" Hafif Alaşım Jantlar", "Çift Bölgeli Deluxe Otomatik Klima", "MMI Radyo Plus & Bluetooth", "Arka Park Mesafe Sensörü", "Yağmur ve Far Sensörü", "Deri Kaplı Çok Fonksiyonlu Direksiyon"],
        },
        {
            "name": "Advanced / Design",
            "level": "orta",
            "summary": "Zarif Tasarım ve Dijital Konfor Paketi",
            "features": ["17\" Tasarım Alaşım Jantlar", "10.25\" Audi Virtual Cockpit (Dijital Gösterge)", "10.1\" Dokunmatik MMI Multimedya & Kablosuz CarPlay", "LED Ön Farlar ve Dinamik Arka Sinyaller", "Geri Görüş Kamerası & Ön/Arka Park Sensörü", "Anahtarsız Çalıştırma (Keyless-Go)", "Kablosuz Telefon Şarj Ünitesi"],
        },
        {
            "name": "S Line",
            "level": "premium",
            "summary": "En Üst Düzey Sportif & Prestij Paketi",
            "features": ["Panoramik Açılır Cam Tavan", "S Line Dış Aerodinamik Gövde Kiti", "S Logolu Deri / Kumaş Spor Koltuklar", "Isıtmalı Ön Koltuklar ve Elektrikli Bel Desteği", "Matrix LED Ön Farlar", "18\" Audi Sport 5 Kollu Alaşım Jantlar", "Çok Renkli İç Ambiyans Aydınlatma Paketi", "Sürüş Modu Seçimi (Audi Drive Select)"],
        },
    ],
    ("Audi", "A4 Sedan"): [
        {
            "name": "Dynamic",
            "level": "dusuk",
            "summary": "Prestijli D-Segment Giriş Donanımı",
            "features": ["17\" Çok Kollu Alaşım Jantlar", "Xenon Plus / LED Ön Farlar", "3 Bölgeli Deluxe Otomatik Dijital Klima", "Ön ve Arka Park Mesafe Sensörleri", "Anahtarsız Çalıştırma", "Audi Drive Select Sürüş Modları"],
        },
        {
            "name": "Advanced / Design",
            "level": "orta",
            "summary": "Üst Düzey İş ve Makam Paketi",
            "features": ["12.3\" Audi Virtual Cockpit Plus (Tam Dijital Kadran)", "10.1\" MMI Navigation Plus Dokunmatik Ekran", "Açılır Cam Sunroof", "Isıtmalı Deri Ön Koltuklar", "Elektrikli Katlanır ve Kararan Yan Aynalar", "Geri Görüş Kamerası", "18\" Tasarım Alaşım Jantlar"],
        },
        {
            "name": "S Line",
            "level": "premium",
            "summary": "Quattro Ruhu ve Zirve Sportif Lüks",
            "features": ["Audi Matrix LED Farlar ve Dinamik Sinyaller", "S Line Spor Süspansiyon ve S Line Dış Tasarım Paketi", "Nappa Deri / Alcantara S Logolu Elektrikli Hafızalı Spor Koltuklar", "Bang & Olufsen 3D Premium Ses Sistemi", "360 Derece Çevre Görüş Kamerası", "Elektrikli Vakumlu Bagaj Kapağı (Sanal Pedal)", "19\" Audi Sport RS Jantlar"],
        },
    ],
    ("Audi", "A6 Sedan"): [
        {
            "name": "Design / Advanced",
            "level": "dusuk",
            "summary": "Üst Segment Makam Konforu",
            "features": ["Çift Dokunmatik MMI Touch Response Ekranlar (10.1\" + 8.6\")", "12.3\" Audi Virtual Cockpit", "4 Bölgeli Tam Otomatik Dijital Klima", "Elektrikli ve Hafızalı Deri Ön Koltuklar", "Ön ve Arka Koltuk Isıtma", "Vakumlu Kapılar (Soft Close)", "18\" Çok Kollu Alaşım Jantlar"],
        },
        {
            "name": "Sport",
            "level": "orta",
            "summary": "Dinamik Makam ve Teknoloji Paketi",
            "features": ["Panoramik Açılır Cam Tavan", "HD Matrix LED Ön Farlar", "360 Derece Çevre Görüş Kamerası", "Valcona Deri Spor Koltuklar", "Elektrikli Arka Makam Perdesi ve Yan Perdeler", "19\" Çift Kollu Alaşım Jantlar", "Anahtarsız Giriş ve Sanal Pedallı Elektrikli Bagaj"],
        },
        {
            "name": "S Line",
            "level": "premium",
            "summary": "Zirve E-Segment Lüks & Quattro Prestiji",
            "features": ["Bang & Olufsen 3D Advanced Ses Sistemi", "Ön Koltuk Havalandırma (Soğutma) ve Masaj Fonksiyonu", "Adaptif Havalı Süspansiyon", "Head-Up Display (Ön Cama Yansıtma)", "S Line Dış ve İç Tasarım Paketi", "20\" Audi Sport Jantlar", "Gece Görüş Asistanı & Otonom Sürüş Destek Paketi"],
        },
    ],
    ("Audi", "Q2"): [
        {
            "name": "Dynamic",
            "level": "dusuk",
            "summary": "Kompakt Premium SUV Girişi",
            "features": ["16\" Alaşım Jantlar", "Çift Bölgeli Otomatik Klima", "MMI Bilgi-Eğlence Ekranı", "Arka Park Sensörü", "Ön Çarpışma Önleyici (Audi Pre Sense Front)", "Deri Direksiyon"],
        },
        {
            "name": "Advanced",
            "level": "orta",
            "summary": "Şık Şehir SUV Donanımı",
            "features": ["Panoramik Açılır Cam Tavan", "LED Ön ve Arka Farlar", "12.3\" Audi Virtual Cockpit Dijital Gösterge", "Geri Görüş Kamerası", "Elektrikli Bagaj Kapağı", "17\" Tasarım Alaşım Jantlar", "Kontrast Gri Yan C-Sütunu (Blade)"],
        },
        {
            "name": "S Line",
            "level": "premium",
            "summary": "Sportif Premium B-SUV Zirvesi",
            "features": ["Matrix LED Farlar & Dinamik Sinyaller", "S Line Gövde Rengi Tamponlar ve Spor Difüzör", "Yarı Deri S Line Spor Koltuklar & Koltuk Isıtma", "Sonos / Audi Sound Premium Ses Sistemi", "Anahtarsız Giriş ve Çalıştırma", "18\" Audi Sport Elmas Kesim Jantlar", "Ambiyans Işık Paketi"],
        },
    ],
    ("Audi", "Q3"): [
        {
            "name": "Advanced",
            "level": "dusuk",
            "summary": "Zengin Donanımlı C-SUV Başlangıcı",
            "features": ["10.25\" Dijital Gösterge Paneli", "10.1\" MMI Dokunmatik Ekran & Apple CarPlay", "LED Ön Farlar", "Çift Bölgeli Otomatik Klima", "İleri-Geri Kaydırılabilir Arka Koltuklar (Plus)", "Ön ve Arka Park Sensörü", "18\" Alaşım Jantlar"],
        },
        {
            "name": "Design",
            "level": "orta",
            "summary": "Aile ve Uzun Yol Konfor Paketi",
            "features": ["Panoramik Açılır Cam Tavan", "Isıtmalı ve Elektrikli Ön Koltuklar", "Geri Görüş Kamerası", "Elektrikli Açılır Bagaj Kapağı", "Kablosuz Telefon Şarjı", "30 Renkli İç Ambiyans Aydınlatması"],
        },
        {
            "name": "S Line",
            "level": "premium",
            "summary": "Sportif ve Eksiksiz Q3 Deneyimi",
            "features": ["Matrix LED Farlar", "S Line Dış Aerodinamik Paket ve 19\" Jantlar", "Alcantara / Deri S Line Spor Koltuklar", "12.3\" Audi Virtual Cockpit Plus", "360 Derece Kamera & Otomatik Park Asistanı", "Sonos 3D Premium Ses Sistemi", "Şerit Takip ve Adaptif Cruise Control"],
        },
    ],

    # ================= BMW (5 MODEL) =================
    ("BMW", "1 Serisi"): [
        {
            "name": "Joy / First Edition",
            "level": "dusuk",
            "summary": "Premium Hatchback Giriş Seviyesi",
            "features": ["16\" Yıldız Kollu Alaşım Jantlar", "LED Ön Farlar ve LED Sis Farları", "Çift Bölgeli Otomatik Klima", "8.8\" iDrive Dokunmatik Ekran", "Yağmur Sensörü ve Otomatik Farlar", "Sürüş Deneyimi Modları (Eco Pro / Comfort / Sport)"],
        },
        {
            "name": "Sport Line",
            "level": "orta",
            "summary": "Dinamik Görünüm ve Dijital Kokpit",
            "features": ["Panoramik Açılır Cam Tavan", "BMW Live Cockpit Professional (10.25\" Dijital Gösterge + 10.25\" Ekran)", "Spor Ön Koltuklar ve Baldır Desteği", "Geri Görüş Kamerası & Otomatik Park Asistanı", "Kablosuz Apple CarPlay", "17\" Çift Kollu Sport Jantlar", "İç Aydınlatma Paketi"],
        },
        {
            "name": "M Sport",
            "level": "premium",
            "summary": "Gerçek M Ruhu ve En Üst Donanım",
            "features": ["M Aerodinamik Gövde Kiti ve M Spor Süspansiyon", "Trigon Kumaş / Alcantara M Spor Koltuklar (Mavi Dikişli)", "Isıtmalı ve Elektrikli Hafızalı Ön Koltuklar", "M Deri Direksiyon ve Antrasit Tavan Döşemesi", "Harman Kardon Hi-Fi Ses Sistemi", "Anahtarsız Giriş (Comfort Access)", "18\" M Çift Kollu Alaşım Jantlar"],
        },
    ],
    ("BMW", "3 Serisi"): [
        {
            "name": "Sport Line / Modern Line",
            "level": "dusuk",
            "summary": "D-Segmentinin Sportif Referansı",
            "features": ["Açılır Cam Sunroof", "LED Ön ve Arka Farlar", "3 Bölgeli Otomatik Dijital Klima", "Spor Ön Koltuklar (Baldır Destekli)", "Geri Görüş Kamerası ve Park Asistanı", "17\" Alaşım Jantlar", "Anahtarsız Çalıştırma"],
        },
        {
            "name": "Luxury Line / Edition Luxury",
            "level": "orta",
            "summary": "Krom Detaylı Prestij ve Konfor",
            "features": ["Vernasca / Dakota Hakiki Deri Döşeme", "Isıtmalı ve Elektrikli Hafızalı Ön Koltuklar", "BMW Live Cockpit Professional (Tam Hayalet Gösterge)", "Ahşap İç Trim Kaplamaları ve Krom Dış Paket", "Kablosuz Şarj & Kablosuz CarPlay", "18\" Çok Kollu Luxury Jantlar", "Elektrikli Bagaj Kapağı"],
        },
        {
            "name": "M Sport",
            "level": "premium",
            "summary": "İkonik 3 Serisi Zirve Paketi",
            "features": ["M Aerodinamik Paket & M Spor Süspansiyon", "BMW Laserlight / Adaptif LED Farlar", "Alcantara / Sensatec M Spor Koltuklar", "Harman Kardon Surround Ses Sistemi", "Head-Up Display & Sürüş Asistanı Profesyonel (Yarı Otonom)", "M Deri Direksiyon & Antrasit Tavan", "19\" M Çift Kollu Bi-Color Jantlar"],
        },
    ],
    ("BMW", "5 Serisi"): [
        {
            "name": "Prestige / Special Edition",
            "level": "dusuk",
            "summary": "E-Segmenti Makam ve Konfor Başlangıcı",
            "features": ["Açılır Cam Sunroof", "Elektrikli ve Isıtmalı Deri Ön Koltuklar", "12.3\" Dijital Gösterge Paneli ve Geniş iDrive Ekran", "Çift Bölgeli Otomatik Klima", "Geri Görüş Kamerası ve Kendi Kendine Park Asistanı", "18\" Alaşım Jantlar"],
        },
        {
            "name": "Luxury Line",
            "level": "orta",
            "summary": "Üst Düzey Yalıtım ve Makam Lüksü",
            "features": ["Vakumlu Kapılar (Soft-Close)", "Dakota / Nappa Deri Hafızalı Konfor Koltuklar", "Elektrikli Arka ve Yan Makam Perdeleri", "Adaptif LED Farlar", "Harman Kardon Ses Sistemi", "Anahtarsız Giriş ve Ayağı Uzatarak Açılan Elektrikli Bagaj", "Ekranlı Akıllı BMW Anahtarı (Display Key)"],
        },
        {
            "name": "M Sport",
            "level": "premium",
            "summary": "Sportif Makam Otomobilinin Zirvesi",
            "features": ["M Aerodinamik Gövde Kiti ve 19\"/20\" M Jantlar", "4 Bölgeli Dijital Klima & Ön Koltuk Soğutma/Isıtma", "360 Derece 3D Çevre Görüş Kamerası", "BMW Laserlight Farlar", "Head-Up Display & Hareketle Komut (Gesture Control)", "M Deri Direksiyon ve Antrasit Tavan Döşemesi", "Otonom Sürüş Asistanı Plus"],
        },
    ],
    ("BMW", "X1"): [
        {
            "name": "sDrive / Joy",
            "level": "dusuk",
            "summary": "Fonksiyonel Premium C-SUV",
            "features": ["Panoramik Açılır Cam Tavan", "LED Ön Farlar", "Çift Bölgeli Otomatik Klima", "Elektrikli Bagaj Kapağı", "Geri Görüş Kamerası ve Park Sensörleri", "17\" Alaşım Jantlar"],
        },
        {
            "name": "xLine",
            "level": "orta",
            "summary": "Arazi Şıklığı ve Zengin Konfor",
            "features": ["xLine Mat Alüminyum Dış Tasarım Paketi", "Yarı Deri / Sensatec Elektrikli Hafızalı ve Isıtmalı Koltuklar", "8.8\" / 10.25\" Dokunmatik Multimedya & CarPlay", "İç Ambiyans Aydınlatması", "18\" Y Kollu xLine Jantlar", "İleri-Geri Kayar Arka Koltuklar"],
        },
        {
            "name": "M Sport",
            "level": "premium",
            "summary": "Sportif Tasarım ve Maksimum Donanım",
            "features": ["M Aerodinamik Paket ve Gövde Rengi Çamurluk Kemerleri", "Alcantara / Deri M Spor Koltuklar", "Harman Kardon Ses Sistemi", "Head-Up Display", "Anahtarsız Giriş (Comfort Access)", "19\" M Çift Kollu Jantlar", "Parlak Siyah Shadow Dış Trimler"],
        },
    ],
    ("BMW", "X3"): [
        {
            "name": "xLine",
            "level": "dusuk",
            "summary": "Zengin Standartlı D-SUV",
            "features": ["Panoramik Açılır Cam Tavan", "Vernasca Deri Elektrikli Hafızalı ve Isıtmalı Koltuklar", "3 Bölgeli Otomatik Dijital Klima", "Adaptif LED Farlar", "Elektrikli Bagaj Kapağı", "19\" xLine Alaşım Jantlar"],
        },
        {
            "name": "Luxury Line",
            "level": "orta",
            "summary": "Prestij ve Konfor Odaklı SUV",
            "features": ["BMW Live Cockpit Professional (12.3\" Tam Dijital Ekranlar)", "Ahşap Kaplama ve Sensatec Deri Ön Konsol", "360 Derece Çevre Görüş Kamerası (Parking Assistant Plus)", "Akustik Yalıtımlı Ön Yan Camlar", "Kablosuz Şarj & Kablosuz CarPlay"],
        },
        {
            "name": "M Sport",
            "level": "premium",
            "summary": "Dinamik xDrive ve Eksiksiz Lüks",
            "features": ["M Aerodinamik Gövde Kiti & M Spor Frenler", "Harman Kardon Surround Ses Sistemi", "Head-Up Display", "Sürüş Asistanı Profesyonel (Şerit Ortalama & Adaptif Hız Sabitleme)", "Anahtarsız Giriş (Comfort Access)", "20\" M Çift Kollu Jantlar", "M Deri Direksiyon ve Antrasit Tavan"],
        },
    ],

    # ================= MERCEDES-BENZ (5 MODEL) =================
    ("Mercedes-Benz", "A Serisi"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Yıldız Dünyasına Modern Giriş",
            "features": ["Çift 7\" MBUX Dijital Gösterge ve Dokunmatik Ekran", "Artico Deri / Kumaş Koltuklar", "Geri Görüş Kamerası ve Aktif Park Asistanı", "Thermatic Otomatik Klima", "16\" Çok Kollu Alaşım Jantlar", "Aktif Fren ve Şerit Takip Asistanı"],
        },
        {
            "name": "Progressive",
            "level": "orta",
            "summary": "Şık Krom Detaylar ve Geniş Ekran",
            "features": ["Panoramik Açılır Cam Tavan", "Çift 10.25\" Geniş Widescreen MBUX Kokpit", "LED High Performance Ön Farlar", "Isıtmalı Ön Koltuklar", "64 Renkli İç Ambiyans Aydınlatması", "17\" Çift 5 Kollu Alaşım Jantlar", "Anahtarsız Çalıştırma (Keyless-Go)"],
        },
        {
            "name": "AMG",
            "level": "premium",
            "summary": "İkonik AMG Tasarımı ve Zirve Teknoloji",
            "features": ["AMG Gövde Tasarım Kiti ve Elmas Görünümlü Ön Izgara", "Artico Deri / Dinamica Mikrofiber Kırmızı Dikişli AMG Spor Koltuklar", "Elektrikli ve Hafızalı Ön Koltuklar", "Alttan Düzleştirilmiş Nappa Deri AMG Spor Direksiyon", "Burmester Surround Ses Sistemi (Opsiyon)", "18\" AMG 5 Çift Kollu Alaşım Jantlar", "Alçaltılmış Konfor Süspansiyon"],
        },
    ],
    ("Mercedes-Benz", "C Serisi"): [
        {
            "name": "Comfort / Avantgarde",
            "level": "dusuk",
            "summary": "Klasik Mercedes Konforu ve Güvenliği",
            "features": ["Artico Deri Koltuklar", "Çift Bölgeli Thermatic Otomatik Klima", "LED High Performance Ön Farlar", "Aktif Park Asistanı ve Geri Görüş Kamerası", "Agility Control Konfor Süspansiyonu", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Exclusive / Fascination",
            "level": "orta",
            "summary": "Kaput Üstü Yıldız ve Üst Düzey Prestij",
            "features": ["Panoramik Açılır Cam Tavan", "Kaput Üstü Dik Yıldız ve Klasik Krom Panjur (Exclusive)", "Elektrikli, Hafızalı ve Isıtmalı Ön Koltuklar", "12.3\" Dijital Gösterge ve 10.25\"/11.9\" Merkezi Ekran", "Ahşap Orta Konsol Kaplaması & 64 Renk Ambiyans Aydınlatma", "Elektrikli Arka Perde ve Yan Makam Perdeleri"],
        },
        {
            "name": "AMG",
            "level": "premium",
            "summary": "Türkiye'nin En Çok Tercih Edilen Sportif Lüks Sedanı",
            "features": ["AMG İç ve Dış Tasarım Paketi", "Multibeam LED / Digital Light Akıllı Farlar", "Burmester 3D Surround Ses Sistemi", "360 Derece Kamera Sistemi", "Anahtarsız Giriş (Keyless-Go) ve Elektrikli Bagaj Kapağı", "18\" / 19\" AMG Çok Kollu Alaşım Jantlar", "Spor Süspansiyon ve Delikli Ön Fren Diskleri"],
        },
    ],
    ("Mercedes-Benz", "E Serisi"): [
        {
            "name": "Edition 1 / Comfort",
            "level": "dusuk",
            "summary": "Üst Segment Makam Standardı",
            "features": ["Panoramik Açılır Cam Tavan", "Vakumlu Kapılar (Soft-Close)", "Elektrikli, Hafızalı ve Isıtmalı Deri Ön Koltuklar", "Çift 12.3\" Widescreen Cockpit Dijital Ekranlar", "64 Renkli Premium Ambiyans Aydınlatması", "18\" Alaşım Jantlar"],
        },
        {
            "name": "Exclusive",
            "level": "orta",
            "summary": "Kaput Üstü Yıldız ve Kusursuz Konfor",
            "features": ["Kaput Üstü Mercedes Yıldızı ve Exclusive Krom Izgara", "Artico Deri Kaplı Ön Konsol ve Doğal Ahşap Trimler", "360 Derece Çevre Görüş Kamerası", "Elektrikli Arka Makam Perdesi ve Yan Kapı Perdeleri", "Keyless-Go & Sanal Pedallı Elektrikli Bagaj Kapağı", "Kablosuz Telefon Şarjı ve Apple CarPlay"],
        },
        {
            "name": "AMG",
            "level": "premium",
            "summary": "Zirve Makam ve Sportif Karizma",
            "features": ["AMG Gövde Kiti ve Gece Paketi Detayları", "Multibeam LED Akıllı Far Sistemi", "Burmester Surround Ses Sistemi", "Ön Koltuk Soğutma (Havalandırma) ve Isıtma", "19\" / 20\" AMG Çok Kollu Jantlar", "Sürüş Yardım Paketi (Distronic Aktif Takip & Şerit Tutma)", "Nappa Deri AMG Spor Direksiyon"],
        },
    ],
    ("Mercedes-Benz", "CLA"): [
        {
            "name": "Urban / Style",
            "level": "dusuk",
            "summary": "Çerçevesiz Kapılı 4 Kapı Coupé Girişi",
            "features": ["Panoramik Açılır Cam Tavan", "Çerçevesiz Spor Kapı Camları", "Entegre Başlıklı Spor Koltuklar", "Geri Görüş Kamerası ve Aktif Park Asistanı", "Otomatik Klima", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Progressive / Comfort",
            "level": "orta",
            "summary": "Dijital MBUX Kokpit ve Şıklık",
            "features": ["Çift 10.25\" Geniş Ekranlı MBUX Kokpit", "LED High Performance Ön Farlar", "Isıtmalı ve Elektrikli Hafızalı Ön Koltuklar", "64 Renkli Ambiyans Aydınlatması", "Anahtarsız Giriş ve Çalıştırma (Keyless-Go)", "18\" Çok Kollu Alaşım Jantlar"],
        },
        {
            "name": "AMG",
            "level": "premium",
            "summary": "En Çok Aranan AMG Coupé Tasarımı",
            "features": ["AMG Aerodinamik Gövde Kiti ve Elmas Izgara", "Artico Deri / Mikrofiber Kırmızı Dikişli AMG Koltuklar", "Multibeam LED Farlar", "Burmester Surround Ses Sistemi", "360 Derece Kamera Sistemi", "19\" AMG Çok Kollu Siyah/Elmas Jantlar", "Nappa Deri AMG Performans Direksiyon"],
        },
    ],
    ("Mercedes-Benz", "GLA"): [
        {
            "name": "Urban / Style",
            "level": "dusuk",
            "summary": "Kompakt Premium SUV Girişi",
            "features": ["Panoramik Açılır Cam Tavan", "Yarı Deri Koltuklar", "Geri Görüş Kamerası ve Park Sensörleri", "Elektrikli Bagaj Kapağı (Easy-Pack)", "Otomatik Klima", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Progressive",
            "level": "orta",
            "summary": "Yeni Nesil Yüksek Sürüş ve Dijital Lüks",
            "features": ["Çift 10.25\" Widescreen MBUX Dijital Kokpit", "LED High Performance Farlar", "Isıtmalı ve Elektrikli Hafızalı Ön Koltuklar", "64 Renk Ambiyans Aydınlatma", "Anahtarsız Giriş (Keyless-Go)", "18\" Alaşım Jantlar"],
        },
        {
            "name": "AMG",
            "level": "premium",
            "summary": "Sportif SUV ve Zirve Donanım",
            "features": ["AMG Gövde Tasarımı ve 19\"/20\" AMG Jantlar", "Artico Deri / Dinamica Mikrofiber AMG Spor Koltuklar", "Burmester Surround Ses Sistemi", "360 Derece Çevre Görüş Kamerası", "Multibeam LED Farlar", "Kör Nokta ve Aktif Şerit Takip Asistanı"],
        },
    ],

    # ================= MEVCUT MARKALARIN YENİ EKLENEN 20 MODELİ =================
    ("Renault", "Fluence"): [
        {
            "name": "Authentique / Joy",
            "level": "dusuk",
            "summary": "Ekonomik Filo ve Aile Giriş Paketi",
            "features": ["Manuel Klima", "15\" Çelik Jant Kapakları", "Elektrikli Ön ve Arka Camlar", "Yol Bilgisayarı & Bluetooth Radyo", "Hız Sabitleyici ve Sınırlayıcı"],
        },
        {
            "name": "Touch / Extreme",
            "level": "orta",
            "summary": "En Çok Satan Konforlu Fluence",
            "features": ["Eller Serbest Renault Kart Sistemi (Anahtarsız Giriş & Çalıştırma)", "16\" Alüminyum Alaşım Jantlar", "Arka Park Sensörü", "Otomatik Katlanır Yan Aynalar", "Ön Sis Farları & Krom Detaylar", "Deri Direksiyon ve Vites Topuzu"],
        },
        {
            "name": "Icon / Privilege",
            "level": "premium",
            "summary": "Zirve Donanım & Makam Konforu",
            "features": ["Açılır Elektrikli Sunroof (Opsiyon)", "Çift Bölgeli Dijital Klima ve Arka Havalandırma Menfezi", "Yarı Deri Koltuk Döşemesi", "R-Link Dokunmatik Navigasyon Ekranı & Geri Görüş Kamerası", "Elektronik Park Freni", "Arka ve Yan Makam Perdeleri", "17\" Akihiro Elmas Kesim Jantlar"],
        },
    ],
    ("Fiat", "Fiorino Combi"): [
        {
            "name": "Pop",
            "level": "dusuk",
            "summary": "Pratik Ticari ve Şehir Girişi",
            "features": ["Manuel Klima", "Sağ ve Sol Çift Sürgülü Yan Kapılar", "Elektrikli Ön Camlar", "Yokuş Kalkış Desteği (Hill Holder)", "Radyo & USB Bağlantısı"],
        },
        {
            "name": "Safeline",
            "level": "orta",
            "summary": "Dengeli Aile ve İş Paketi",
            "features": ["5\" / 7\" Dokunmatik Multimedya Ekranı", "15\" Alüminyum Alaşım Jantlar", "Arka Park Sensörü", "Tavan Rayları", "Deri Direksiyon ve Vites Topuzu", "Karartılmış Arka Camlar"],
        },
        {
            "name": "Premio",
            "level": "premium",
            "summary": "Binek Konforunda En Dolu Fiorino",
            "features": ["Isıtmalı Ön Koltuklar", "7\" Apple CarPlay & Android Auto Destekli Ekran", "Geri Görüş Kamerası", "16\" Elmas Kesim Alaşım Jantlar", "Hız Sabitleyici (Cruise Control)", "Yağmur ve Karanlık Sensörü", "Özel Premio İç Döşeme ve Trekking Tampon Korumaları"],
        },
    ],
    ("Volkswagen", "Jetta"): [
        {
            "name": "Trendline",
            "level": "dusuk",
            "summary": "Sağlam C-Sedan Giriş Paketi",
            "features": ["Manuel Klima (Climatic)", "16\" Jantlar", "Elektrikli ve Isıtmalı Yan Aynalar", "Dokunmatik Radyo Ekranı", "Yokuş Kalkış Desteği"],
        },
        {
            "name": "Comfortline",
            "level": "orta",
            "summary": "Türkiye'de En Çok Tutulan Konfor Paketi",
            "features": ["Çift Bölgeli Otomatik Klima (Climatronic)", "Ön ve Arka Görsel Destekli Park Sensörleri", "Yarı Deri / Kumaş Konfor Koltuklar", "Yağmur ve Far Sensörü", "Hız Sabitleyici (Cruise Control)", "16\" Navarra Alaşım Jantlar", "Deri Kaplı Çok Fonksiyonlu Direksiyon"],
        },
        {
            "name": "Highline",
            "level": "premium",
            "summary": "Küçük Passat Konforunda Zirve Jetta",
            "features": ["Açılır Elektrikli Cam Sunroof", "Bi-Xenon Ön Farlar ve LED Gündüz Sürüş Farları", "Isıtmalı Ön Koltuklar (Kış Paketi)", "Anahtarsız Giriş ve Çalıştırma (Keyless Access)", "6.5\" Composition Media Ekran & Geri Görüş Kamerası", "17\" Queensland Alaşım Jantlar"],
        },
    ],
    ("Volkswagen", "Taigo"): [
        {
            "name": "Life",
            "level": "dusuk",
            "summary": "Zengin Standartlı Coupé-SUV Girişi",
            "features": ["8\" Dijital Gösterge Paneli (Digital Cockpit)", "8\" Dokunmatik Multimedya & Kablosuz App-Connect", "LED Ön Farlar ve LED Stop Lambaları", "Çift Bölgeli Dijital Klima", "Ön ve Arka Park Sensörleri", "Kablosuz Telefon Şarjı", "16\" Belmopan Alaşım Jantlar"],
        },
        {
            "name": "Style",
            "level": "orta",
            "summary": "Teknoloji ve Konfor Odaklı Paket",
            "features": ["IQ.LIGHT LED Matrix Ön Farlar & Panjur İçi LED Işık Şeridi", "10.25\" Digital Cockpit Pro (Tam Hayalet Kadran)", "Açılır Panoramik Cam Tavan", "Isıtmalı Ön Koltuklar", "Anahtarsız Giriş ve Çalıştırma", "Geri Görüş Kamerası", "17\" Aberdeen Alaşım Jantlar"],
        },
        {
            "name": "R-Line",
            "level": "premium",
            "summary": "Sportif R-Line Tasarım ve Zirve Donanım",
            "features": ["R-Line Sportif Ön/Arka Tamponlar ve Yan Marşpiyeller", "Açılır Panoramik Cam Tavan", "R-Line Logolu Özel Spor Koltuklar ve Antrasit Tavan", "IQ.LIGHT LED Matrix Farlar", "Yarı Otonom Sürüş Asistanı (Travel Assist)", "18\" Misano Siyah/Elmas Kesim Jantlar"],
        },
    ],
    ("Toyota", "Auris"): [
        {
            "name": "Life / Active",
            "level": "dusuk",
            "summary": "Sorunsuz C-Hatchback Giriş Paketi",
            "features": ["Otomatik Dijital Klima", "LED Gündüz Farları", "Elektrikli Ön ve Arka Camlar", "USB / Bluetooth Ses Sistemi", "7 Hava Yastığı ve Yokuş Kalkış Desteği"],
        },
        {
            "name": "Advance",
            "level": "orta",
            "summary": "Dengeli Aile ve Konfor Donanımı",
            "features": ["7\" Toyota Touch 2 Dokunmatik Multimedya Ekranı", "Geri Görüş Kamerası", "16\" Alüminyum Alaşım Jantlar", "Anahtarsız Çalıştırma (Push Start)", "Hız Sabitleyici", "Yağmur ve Far Sensörü", "Otomatik Katlanır Yan Aynalar"],
        },
        {
            "name": "Premium / Advance Skypack",
            "level": "premium",
            "summary": "Cam Tavanlı En Dolu Auris",
            "features": ["Boydan Boya Panoramik Cam Tavan (Skyview)", "Isıtmalı Yarı Deri Ön Koltuklar", "Bi-LED / Xenon Ön Farlar", "Kendi Kendine Otomatik Park Sistemi (S-IPA)", "Ön ve Arka Park Sensörleri", "Akıllı Anahtarsız Giriş ve Çalıştırma", "17\" Çift Renkli Alaşım Jantlar"],
        },
    ],
    ("Honda", "HR-V"): [
        {
            "name": "Premium",
            "level": "dusuk",
            "summary": "Sihirli Koltuklu SUV Giriş Paketi",
            "features": ["Honda Magic Seats (Yukarı Katlanabilen Sihirli Arka Koltuklar)", "Dokunmatik Dijital Klima Paneli", "Elektrikli Park Freni ve Brake Hold", "Hız Sabitleyici", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Zengin Güvenlik ve Konfor Paketi",
            "features": ["7\" Honda Connect Dokunmatik Ekran", "Ön ve Arka Park Sensörleri & Geri Görüş Kamerası", "Isıtmalı Ön Koltuklar", "Çift Bölgeli Dijital Klima", "Şerit Takip ve Çarpışma Önleme Uyarı Sistemi", "Yağmur ve Far Sensörü"],
        },
        {
            "name": "Executive",
            "level": "premium",
            "summary": "Panoramik Cam Tavanlı Zirve HR-V",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Ön Farlar ve LED Stop Lambaları", "Yarı Deri Koltuk Döşemesi", "Anahtarsız Giriş ve Çalıştırma (Smart Entry)", "17\" Elmas Kesim Spor Jantlar", "Tavan Rayları ve Karartılmış Arka Camlar"],
        },
    ],
    ("Hyundai", "Accent Blue"): [
        {
            "name": "Mode",
            "level": "dusuk",
            "summary": "Ekonomik ve Dayanıklı Giriş Paketi",
            "features": ["Manuel Klima", "Elektrikli Ön ve Arka Camlar", "ABS / ESP ve Yokuş Kalkış Desteği", "Radyo / MP3 Çalar", "15\" Jant Kapakları"],
        },
        {
            "name": "Mode Plus",
            "level": "orta",
            "summary": "Piyasada En Çok Tercih Edilen Paket",
            "features": ["16\" Alüminyum Alaşım Jantlar", "Dokunmatik Multimedya ve Navigasyon Ekranı", "Arka Park Sensörü", "Hız Sabitleyici (Cruise Control)", "Deri Direksiyon ve Vites Topuzu", "Ön Sis Farları"],
        },
        {
            "name": "Prime",
            "level": "premium",
            "summary": "Tam Otomatik Klimalı En Üst Paket",
            "features": ["Tam Otomatik Dijital Klima", "Geri Görüş Kamerası", "LED Gündüz Farları ve Mercekli Ön Farlar", "Otomatik Yanan Farlar ve Yağmur Sensörü", "Kendiliğinden Kararan İç Dikiz Aynası", "16\" Özel Prime Alaşım Jantlar"],
        },
    ],
    ("Hyundai", "Kona"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Dinamik B-SUV Giriş Paketi",
            "features": ["8\" Dokunmatik Multimedya & Kablosuz Apple CarPlay", "Geri Görüş Kamerası ve Arka Park Sensörü", "Hız Sabitleyici", "LED Gündüz Farları", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Smart / Elite",
            "level": "orta",
            "summary": "Cam Tavanlı ve Dijital Konfor Paketi",
            "features": ["Açılır Elektrikli Sunroof", "10.25\" Dijital Gösterge Paneli", "Otomatik Dijital Klima", "Anahtarsız Giriş ve Çalıştırma", "Kablosuz Telefon Şarj Ünitesi", "17\" Elmas Kesim Jantlar", "Kör Nokta Çarpışma Uyarı Sistemi"],
        },
        {
            "name": "Progressive / N Line",
            "level": "premium",
            "summary": "4x4 / Sportif Zirve Donanım",
            "features": ["Full LED Ön ve Arka Farlar", "Isıtmalı ve Soğutmalı Deri Koltuklar", "Krell Premium Ses Sistemi", "Head-Up Display (Ön Cam Gösterge)", "Şerit Takip ve Ön Çarpışma Önleme Asistanı", "18\" Özel Tasarım Jantlar"],
        },
    ],
    ("Kia", "XCeed"): [
        {
            "name": "Cool",
            "level": "dusuk",
            "summary": "Sportif Crossover Giriş Seviyesi",
            "features": ["LED Ön Farlar ve Küp LED Gündüz Farları", "8\" Dokunmatik Multimedya & Kablosuz CarPlay", "Geri Görüş Kamerası ve Arka Park Sensörü", "Hız Sabitleyici", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Elegance",
            "level": "orta",
            "summary": "Panoramik Cam Tavanlı Popüler Paket",
            "features": ["Açılır Panoramik Cam Tavan", "Çift Bölgeli Otomatik Dijital Klima", "Anahtarsız Giriş ve Çalıştırma", "Yarı Deri Koltuklar", "Elektrikli Park Freni & Auto Hold", "18\" Elmas Kesim Sportif Jantlar"],
        },
        {
            "name": "Prestige",
            "level": "premium",
            "summary": "Tam Dijital ve Isıtmalı Zirve Paket",
            "features": ["12.3\" Supervision Tam Dijital Hayalet Gösterge", "10.25\" Geniş Navigasyonlu Multimedya Ekranı", "Ön Koltuk Isıtma ve Direksiyon Isıtma", "Elektrikli ve Hafızalı Sürücü Koltuğu", "Elektrikli Açılır Bagaj Kapağı", "Kablosuz Telefon Şarjı", "Şerit Takip ve Akıllı Hız Sabitleyici"],
        },
    ],
    ("Kia", "Picanto"): [
        {
            "name": "Live / Feel",
            "level": "dusuk",
            "summary": "Pratik Şehir Otomobili",
            "features": ["8\" Dokunmatik Ekran & Apple CarPlay / Android Auto", "Geri Görüş Kamerası", "Manuel Klima", "Otomatik Yanan Farlar", "Elektrikli Ön ve Arka Camlar", "14\" Jantlar"],
        },
        {
            "name": "Cool",
            "level": "orta",
            "summary": "Alaşım Jantlı ve Park Sensörlü Paket",
            "features": ["15\" Alüminyum Alaşım Jantlar", "Arka Park Sensörü", "Hız Sabitleyici ve Sınırlayıcı", "Deri Direksiyon ve Vites Topuzu", "Ön Kol Dayama"],
        },
        {
            "name": "GT-Line",
            "level": "premium",
            "summary": "Sportif Görünümlü En Dolu Picanto",
            "features": ["GT-Line Sportif Ön/Arka Tampon ve Çift Egzoz Çıkışı", "Otomatik Dijital Klima", "LED Gündüz Farları ve Mercekli Farlar", "Anahtarsız Giriş ve Çalıştırma", "Çift Renkli Deri Koltuklar", "16\" GT-Line Özel Alaşım Jantlar"],
        },
    ],
    ("Ford", "Kuga"): [
        {
            "name": "Style / Trend X",
            "level": "dusuk",
            "summary": "Geniş ve Güvenli C-SUV Girişi",
            "features": ["8\" Dokunmatik SYNC Ekran & Apple CarPlay", "İleri-Geri Kaydırılabilir Arka Koltuklar", "Ön ve Arka Park Sensörleri", "Anahtarsız Çalıştırma", "Seçilebilir Sürüş Modları", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Titanium",
            "level": "orta",
            "summary": "Ailelerin Favorisi Konforlu Kuga",
            "features": ["Açılır Panoramik Cam Tavan (Opsiyon)", "12.3\" Tam Dijital Gösterge Paneli", "Çift Bölgeli Otomatik Dijital Klima", "Geri Görüş Kamerası", "Anahtarsız Giriş ve Elektrikli Bagaj Kapağı", "Kablosuz Telefon Şarj Ünitesi", "18\" Çok Kollu Titanium Jantlar"],
        },
        {
            "name": "ST-Line / Vignale",
            "level": "premium",
            "summary": "Sportif Gövde Kiti ve Maksimum Teknoloji",
            "features": ["Açılır Panoramik Cam Tavan", "B&O (Bang & Olufsen) 10 Hoparlörlü Premium Ses Sistemi", "Isıtmalı Ön ve Arka Koltuklar & Isıtmalı Direksiyon", "ST-Line Spor Gövde Kiti ve Alcantara/Deri Spor Koltuklar", "Co-Pilot 360 (Adaptif Hız Sabitleme, Kör Nokta, Otomatik Park)", "Head-Up Display", "19\" ST-Line Alaşım Jantlar"],
        },
    ],
    ("Ford", "Tourneo Courier"): [
        {
            "name": "Trend",
            "level": "dusuk",
            "summary": "Dayanıklı İş ve Aile Başlangıcı",
            "features": ["Manuel Klima", "Çift Sürgülü Yan Kapılar", "Yokuş Kalkış Desteği ve ESP", "Bluetooth Radyo & USB", "Elektrikli Ön Camlar"],
        },
        {
            "name": "Deluxe",
            "level": "orta",
            "summary": "Konforlu Camlı Kombi",
            "features": ["15\" Alüminyum Alaşım Jantlar", "Arka Park Sensörü", "Hız Sabitleyici (Cruise Control)", "Ön Sis Farları", "Deri Direksiyon", "Karartılmış Arka Camlar"],
        },
        {
            "name": "Titanium / Titanium Plus",
            "level": "premium",
            "summary": "Binek Otomobil Donanımında Zirve Courier",
            "features": ["Dokunmatik SYNC Multimedya Ekranı & Apple CarPlay", "Otomatik Dijital Klima", "Isıtmalı Ön Koltuklar ve Isıtmalı Ön Cam (Quickclear)", "Geri Görüş Kamerası", "Yağmur ve Far Sensörü", "16\" Titanium Alaşım Jantlar ve Tavan Rayları"],
        },
    ],
    ("Peugeot", "2008"): [
        {
            "name": "Active / Active Prime",
            "level": "dusuk",
            "summary": "Aslan Pençesi Tasarımlı B-SUV Girişi",
            "features": ["LED Ön Farlar (3 Pençeli Gündüz Farları)", "7\" Dokunmatik Multimedya & Apple CarPlay", "Arka Park Sensörü ve Geri Görüş Kamerası", "Hız Sabitleyici ve Şerit Takip Asistanı", "16\" / 17\" Alaşım Jantlar"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "3D i-Cockpit ve Zengin Konfor",
            "features": ["3D Hologram Dijital Gösterge Paneli (3D i-Cockpit)", "Tam Otomatik Dijital Klima", "Yarı Deri Koltuk Döşemesi", "Anahtarsız Giriş ve Çalıştırma", "Elektrikli Park Freni", "17\" Karakoy Elmas Kesim Jantlar"],
        },
        {
            "name": "GT",
            "level": "premium",
            "summary": "Cam Tavanlı ve Çift Renkli Zirve 2008",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Mercekli Ön Farlar ve Otomatik Uzun Far", "10\" HD Geniş Dokunmatik Ekran", "Isıtmalı Ön Koltuklar", "Siyah Elmas Tavan (Çift Renk Gövde) & 8 Renk Ambiyans Aydınlatma", "Kör Nokta Uyarı Sistemi ve Adaptif Cruise Control", "18\" Evissa Siyah/Elmas Jantlar"],
        },
    ],
    ("Peugeot", "408"): [
        {
            "name": "Allure",
            "level": "dusuk",
            "summary": "Üst Düzey Donanımlı Fastback Başlangıcı",
            "features": ["10\" Dijital Gösterge Paneli & 10\" HD Dokunmatik Ekran (i-Connect)", "Kablosuz Apple CarPlay & Android Auto", "Full LED Ön Farlar ve Aslan Dişi Gündüz Farları", "Isıtmalı Ön Koltuklar ve Isıtmalı Direksiyon", "180 Derece Geri Görüş Kamerası", "Anahtarsız Giriş ve Çalıştırma", "19\" Jaspe Alaşım Jantlar"],
        },
        {
            "name": "GT (Standart)",
            "level": "orta",
            "summary": "Matrix LED ve 3D i-Cockpit Lüksü",
            "features": ["Açılır Cam Sunroof", "Peugeot Matrix LED Teknolojili İnce Ön Farlar", "3D Dijital Hologram Gösterge ve i-Toggles Kısayol Ekranı", "Alcantara / Yarı Deri GT Spor Koltuklar", "Elektrikli Bagaj Kapağı", "360 Derece 4 Kameralı Çevre Görüş Sistemi"],
        },
        {
            "name": "GT (Nappa / Focal Opsiyonlu)",
            "level": "premium",
            "summary": "Masajlı Koltuklu Zirve 408",
            "features": ["AGR Onaylı Elektrikli, Hafızalı ve Masaj Fonksiyonlu Ön Koltuklar", "Nappa Deri Döşeme", "Focal Hi-Fi 10 Hoparlörlü Premium Ses Sistemi", "Gece Görüş Sistemi (Night Vision)", "Yarı Otonom Sürüş (Drive Assist 2.0)", "19\" Graphite Elmas Kesim Jantlar"],
        },
    ],
    ("Peugeot", "508"): [
        {
            "name": "Prime / Active",
            "level": "dusuk",
            "summary": "Çerçevesiz Kapılı Sportif D-Sedan",
            "features": ["Çerçevesiz Kapı Camları", "12.3\" Dijital i-Cockpit Gösterge", "8\" Dokunmatik Ekran & Apple CarPlay", "Çift Bölgeli Otomatik Klima", "Ön ve Arka Park Sensörü", "17\" Merion Alaşım Jantlar"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "Zarif Tasarım ve Yüksek Konfor",
            "features": ["Full LED Ön Farlar ve 3 Boyutlu Aslan Pençesi Stop Lambaları", "10\" HD Geniş Dokunmatik Navigasyon Ekranı", "Yarı Deri AGR Konfor Koltuklar", "Anahtarsız Giriş ve Çalıştırma", "Geri Görüş Kamerası ve Kör Nokta Uyarısı", "Kablosuz Telefon Şarjı"],
        },
        {
            "name": "GT / GT Selection",
            "level": "premium",
            "summary": "D-Segmentinin En Karizmatik Fastback Zirvesi",
            "features": ["Açılır Panoramik Cam Tavan", "Focal Hi-Fi Premium Ses Sistemi", "Nappa Deri / Alcantara Elektrikli, Hafızalı, Isıtmalı ve Masajlı Koltuklar", "Adaptif Süspansiyon (Active Suspension Control)", "Otonom Sürüş Asistanı ve 360 Derece Kamera", "Elektrikli Bagaj Kapağı", "18\" / 19\" Sperone Çift Renkli Jantlar"],
        },
    ],
    ("Opel", "Insignia"): [
        {
            "name": "Enjoy / Edition",
            "level": "dusuk",
            "summary": "Geniş ve Konforlu D-Segment Girişi",
            "features": ["Çift Bölgeli Otomatik Dijital Klima", "7\" Intellilink Dokunmatik Ekran & Apple CarPlay", "Anahtarsız Giriş ve Çalıştırma", "Ön ve Arka Park Sensörleri", "Şerit Koruma ve Çarpışma Önleme", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Excellence / Elegance",
            "level": "orta",
            "summary": "AGR Koltuklu ve IntelliLux LED Farlı Paket",
            "features": ["IntelliLux LED Matrix Ön Farlar", "AGR Onaylı Yarı Deri Ergonomik Konfor Koltuklar", "8\" Dijital Sürücü Bilgi Ekranı ve Navigasyon", "Isıtmalı Ön Koltuklar ve Isıtmalı Direksiyon", "Geri Görüş Kamerası", "18\" Çok Kollu Alaşım Jantlar"],
        },
        {
            "name": "Exclusive / Grand Sport Ultimate",
            "level": "premium",
            "summary": "Tam Dolu Alman Makam Otomobili",
            "features": ["Açılır Elektrikli Sunroof", "Nappa Deri Elektrikli, Hafızalı, Havalandırmalı (Soğutmalı) ve Masajlı Sürücü Koltuğu", "Bose 8 Hoparlörlü Premium Ses Sistemi", "Head-Up Display (Ön Cama Yansıtma)", "360 Derece Çevre Görüş Kamerası", "Isıtmalı Arka Koltuklar", "18\" / 20\" Bi-Color Elmas Kesim Jantlar"],
        },
    ],
    ("Opel", "Grandland"): [
        {
            "name": "Enjoy / Edition",
            "level": "dusuk",
            "summary": "Alman C-SUV Giriş Paketi",
            "features": ["Çift Bölgeli Dijital Klima", "Dokunmatik Multimedya Ekranı & Apple CarPlay", "LED Ön Farlar", "Ön ve Arka Park Sensörü", "Şerit Takip ve Hız Sabitleyici", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Excellence / Elegance",
            "level": "orta",
            "summary": "Pure Panel Dijital Kokpit ve Cam Tavan",
            "features": ["Panoramik Cam Tavan", "Pure Panel (12\" Dijital Gösterge + 10\" Dokunmatik Ekran)", "AGR Onaylı Yarı Deri Koltuklar ve Ön Koltuk Isıtma", "Geri Görüş Kamerası ve Anahtarsız Giriş", "Elektrikli Bagaj Kapağı", "18\" Çift Renkli Jantlar"],
        },
        {
            "name": "Ultimate",
            "level": "premium",
            "summary": "IntelliLux Pixel LED Farlı Zirve Grandland",
            "features": ["IntelliLux LED Pixel Matrix Farlar (168 LED Hücreli)", "Alcantara / Deri Isıtmalı ve Havalandırmalı (Soğutmalı) Ön Koltuklar", "Isıtmalı Arka Koltuklar ve Isıtmalı Ön Cam", "360 Derece Çevre Görüş Kamerası", "Siyah Tavan ve Siyah Kaput Opsiyonu", "Kablosuz Şarj & Otonom Sürüş Asistanı", "19\" Elmas Kesim Jantlar"],
        },
    ],
    ("Skoda", "Kamiq"): [
        {
            "name": "Elite",
            "level": "dusuk",
            "summary": "Zengin Standartlı B-SUV Girişi",
            "features": ["LED Ön Farlar ve LED Gündüz Sürüş Farları", "8\" Dijital Gösterge Paneli", "8.25\" Dokunmatik Multimedya & Apple CarPlay", "Çift Bölgeli Otomatik Dijital Klima", "Arka Park Sensörü", "16\" Cortadero Alaşım Jantlar"],
        },
        {
            "name": "Premium",
            "level": "orta",
            "summary": "Türkiye'de En Çok Satan Paket",
            "features": ["Panoramik Cam Tavan (Opsiyon)", "10.25\" Dijital Gösterge Paneli (Virtual Cockpit)", "Anahtarsız Giriş ve Çalıştırma (KESSY)", "Geri Görüş Kamerası ve Ön/Arka Park Sensörü", "Dinamik Arka Sinyalli TOP LED Stop Lambaları", "17\" Braga Alaşım Jantlar", "Krom Pencere Çerçeveleri"],
        },
        {
            "name": "Monte Carlo",
            "level": "premium",
            "summary": "Panoramik Cam Tavanlı Sportif Zirve",
            "features": ["Standart Panoramik Cam Tavan", "Full LED Matrix Ön Farlar", "Monte Carlo Özel Entegre Başlıklı Spor Koltuklar", "Parlak Siyah Ön Panjur, Difüzör ve Ayna Kapakları", "Isıtmalı Ön Koltuklar ve Elektrikli Bagaj Kapağı", "18\" Vega Siyah Elmas Kesim Jantlar"],
        },
    ],
    ("Skoda", "Karoq"): [
        {
            "name": "Ambition / Elite",
            "level": "dusuk",
            "summary": "Fonksiyonel C-SUV Başlangıcı",
            "features": ["Çift Bölgeli Otomatik Klima", "8\" Dokunmatik Bolero Multimedya & CarPlay", "LED Ön Farlar", "Ön ve Arka Park Sensörleri", "Anahtarsız Çalıştırma", "17\" Scutus Alaşım Jantlar"],
        },
        {
            "name": "Style / Premium",
            "level": "orta",
            "summary": "Dijital Kadranlı Aile Paketi",
            "features": ["Açılır Panoramik Cam Tavan", "10.25\" Dijital Gösterge Paneli (Virtual Cockpit)", "Geri Görüş Kamerası", "Anahtarsız Giriş ve Çalıştırma (KESSY)", "İç Ambiyans Aydınlatması", "18\" Miran Alaşım Jantlar"],
        },
        {
            "name": "Prestige / Sportline",
            "level": "premium",
            "summary": "Matrix LED ve Isıtmalı Koltuklu Zirve Karoq",
            "features": ["Full LED Matrix Ön Farlar", "Isıtmalı Ön ve Arka Koltuklar & Isıtmalı Direksiyon", "Elektrikli ve Hafızalı Sürücü Koltuğu", "Sanal Pedallı Elektrikli Bagaj Kapağı", "Süet / Deri Döşeme veya Sportline Spor Koltuklar", "360 Derece Çevre Görüş Kamerası", "19\" Sagitarius Alaşım Jantlar"],
        },
    ],
    ("Skoda", "Kodiaq"): [
        {
            "name": "Ambition / Elite",
            "level": "dusuk",
            "summary": "Devasa Hacimli D-SUV Girişi",
            "features": ["LED Ön ve Arka Farlar", "10.25\" Dijital Gösterge Paneli", "8\" Bolero Dokunmatik Ekran & Kablosuz CarPlay", "Çift Bölgeli Otomatik Klima", "Anahtarsız Çalıştırma", "18\" Elbrus Alaşım Jantlar"],
        },
        {
            "name": "Style / Premium",
            "level": "orta",
            "summary": "Panoramik Cam Tavanlı Geniş Aile SUV'u",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Matrix Ön Farlar", "Yarı Deri / Süet Koltuk Döşemesi", "Elektrikli ve Hafızalı Sürücü Koltuğu", "Elektrikli Bagaj Kapağı", "Geri Görüş Kamerası ve Anahtarsız Giriş", "19\" Triglav Alaşım Jantlar"],
        },
        {
            "name": "Prestige / L&K / RS",
            "level": "premium",
            "summary": "7 Koltuk Opsiyonlu Zirve Lüks Kodiaq",
            "features": ["Isıtmalı ve Havalandırmalı (Soğutmalı) Deri Ön Koltuklar & Arka Koltuk Isıtma", "Canton 12 Hoparlörlü Premium Ses Sistemi", "360 Derece Çevre Görüş Kamerası (Area View)", "3 Bölgeli Dijital Klima", "Sanal Pedallı Elektrikli Bagaj & Kapı Kenarı Koruma Barları", "20\" Ignacio / Vega Alaşım Jantlar"],
        },
    ],
    ("Renault", "Symbol"): [
        {
            "name": "Joy",
            "level": "dusuk",
            "summary": "Ekonomik ve Dayanıklı Filo/Aile Girişi",
            "features": ["Manuel Klima", "Bluetooth & USB Radyo Çalar", "LED Gündüz Sürüş Farları", "Yokuş Kalkış Destek Sistemi (Hill Holder)", "510 Litre Geniş Bagaj Hacmi", "15\" Kapaklı Sac Jantlar"],
        },
        {
            "name": "Touch",
            "level": "orta",
            "summary": "En Çok Tercih Edilen Dengeli Paket",
            "features": ["Hız Sabitleyici ve Hız Sınırlayıcı (Cruise Control)", "Elektrikli Ön ve Arka Camlar", "Yol Bilgisayarı ve Dış Sıcaklık Göstergesi", "Arka Park Sensörü", "Ön Sis Farları ve Gövde Rengi Aynalar", "15\" Alüminyum Alaşım Jantlar"],
        },
        {
            "name": "Icon / Touch Chrome",
            "level": "premium",
            "summary": "7 İnç Ekranlı ve Dijital Klimalı En Dolu Symbol",
            "features": ["7\" MediaNav Dokunmatik Multimedya ve Navigasyon Ekranı", "Otomatik Dijital Klima", "Geri Görüş Kamerası", "Deri Direksiyon Simidi ve Vites Topuzu", "Krom Ön Panjur Detayları", "16\" Çift Renkli Alaşım Jantlar"],
        },
    ],
    ("Peugeot", "308"): [
        {
            "name": "Active / Active Prime",
            "level": "dusuk",
            "summary": "Modern i-Cockpit C-Hatchback Başlangıcı",
            "features": ["10\" Dijital i-Cockpit Gösterge ve 10\" Dokunmatik Multimedya", "Kablosuz Apple CarPlay & Android Auto", "ECO LED Ön Farlar ve Aslan Dişi Gündüz Farları", "Çift Bölgeli Otomatik Klima", "Anahtarsız Çalıştırma ve Arka Park Sensörü", "16\" / 17\" Auckland Alaşım Jantlar"],
        },
        {
            "name": "Allure",
            "level": "orta",
            "summary": "Şık Tasarım ve Zengin Konfor",
            "features": ["i-Toggles Kişiselleştirilebilir Dokunmatik Kısayol Ekranı", "Yarı Deri Falgo Kumaş Koltuklar", "180 Derece HD Geri Görüş Kamerası ve Ön Park Sensörü", "Anahtarsız Giriş ve Çalıştırma", "Otomatik Uzun Far Asistanı ve Karartılmış Arka Camlar", "17\" Halong Elmas Kesim Jantlar"],
        },
        {
            "name": "GT",
            "level": "premium",
            "summary": "Matrix LED ve Cam Tavanlı Sportif Zirve",
            "features": ["Açılır Panoramik Cam Tavan", "Peugeot Matrix LED Teknolojili İnce Ön Farlar ve 3D Aslan Pençesi Stoplar", "3D Hologram Dijital Gösterge Paneli", "Alcantara / Yarı Deri Isıtmalı Spor Koltuklar ve Isıtmalı GT Direksiyon", "360 Derece 4 Kameralı Çevre Görüş ve Kör Nokta Uyarı Sistemi", "18\" Kamakura Çift Renkli Jantlar"],
        },
    ],
    ("Peugeot", "Rifter"): [
        {
            "name": "Active / Allure",
            "level": "dusuk",
            "summary": "Otomobil Konforunda Pratik Aile MPV'si",
            "features": ["Peugeot i-Cockpit Kompakt Direksiyon", "8\" Dokunmatik Multimedya Ekranı & Apple CarPlay", "Çift Sürgülü Yan Kapılar ve 775 Litre Devasa Bagaj", "Hız Sabitleyici ve Şerit Takip Asistanı", "Elektrikli Park Freni ve Arka Park Sensörü", "16\" Taranaki Alaşım Jantlar"],
        },
        {
            "name": "Allure Pack",
            "level": "orta",
            "summary": "Dijital Klimalı ve Geri Görüş Kameralı Paket",
            "features": ["Çift Bölgeli Otomatik Dijital Klima", "180 Derece VisioPark Geri Görüş Kamerası", "3 Bağımsız Katlanabilir Arka Koltuk (Magic Flat)", "Açılabilir Bagaj Camı", "Anahtarsız Giriş ve Çalıştırma", "Tavan Barları ve Karartılmış Arka Camlar"],
        },
        {
            "name": "GT / GT-Line",
            "level": "premium",
            "summary": "Zenith Cam Tavanlı ve Grip Control'lü Zirve Rifter",
            "features": ["Zenith Panoramik Cam Tavan ve Tavanda Aydınlatmalı Saklama Gözü", "Advanced Grip Control (Kar, Çamur, Kum Sürüş Modları) & Yokuş İniş Desteği", "10\" Dijital Gösterge Paneli (Yeni Makyajlı Kasa)", "Kör Nokta Uyarı Sistemi ve Adaptif Cruise Control", "Kablosuz Telefon Şarjı ve 220V Priz", "17\" Aoraki Elmas Kesim Jantlar"],
        },
    ],
    ("Dacia", "Jogger"): [
        {
            "name": "Essential",
            "level": "dusuk",
            "summary": "Ulaşılabilir 7 Kişilik Aile Crossover Girişi",
            "features": ["Y-Şekilli LED Ön Farlar", "Media Control (Telefon Sabitlemeli Radyo & Bluetooth)", "Manuel Klima", "Acil Fren Destek Sistemi ve Otomatik Farlar", "Modüler Tavan Barları", "16\" Sac / Flexwheel Jantlar"],
        },
        {
            "name": "Expression",
            "level": "orta",
            "summary": "8 İnç Ekranlı Dengeli Aile Paketi",
            "features": ["8\" Media Display Dokunmatik Ekran & Apple CarPlay / Android Auto", "Geri Görüş Kamerası ve Arka Park Sensörü", "Hız Sabitleyici ve Hız Sınırlayıcı", "Ön Sis Farları ve Elektrikli Arka Camlar", "Yükseklik ve Derinlik Ayarlı Soft Feel Direksiyon", "16\" Flexwheel Jantlar"],
        },
        {
            "name": "Extreme",
            "level": "premium",
            "summary": "Bakır Detaylı ve Extended Grip'li Zirve Jogger",
            "features": ["Otomatik Dijital Klima", "Eller Serbest Dacia Kart Sistemi (Anahtarsız Giriş ve Çalıştırma)", "Extended Grip (Zorlu Zemin Çekiş Sistemi)", "Kör Nokta Uyarı Sistemi ve Elektronik Park Freni", "Bakır Kahve Ayna Kapakları, MicroCloud Özel Döşeme ve Arka Koltuk Servis Masaları", "16\" Mahalia Siyah Alaşım Jantlar"],
        },
    ],
    ("Skoda", "Scala"): [
        {
            "name": "Elite",
            "level": "dusuk",
            "summary": "Geniş Bagajlı C-Hatchback Başlangıcı",
            "features": ["LED Ön Farlar ve LED Gündüz Sürüş Farları", "8\" Dijital Gösterge Paneli", "8.25\" Dokunmatik Multimedya & Kablosuz Apple CarPlay", "Çift Bölgeli Otomatik Klima", "Arka Park Sensörü ve Anahtarsız Çalıştırma", "16\" Cortadero Alaşım Jantlar"],
        },
        {
            "name": "Premium",
            "level": "orta",
            "summary": "Uzatılmış Arka Camlı ve Dijital Kadranlı Paket",
            "features": ["Bagaj Kapağına Uzanan Siyah Cam Tasarımı ve Dinamik Sinyalli TOP LED Stoplar", "10.25\" Dijital Gösterge Paneli (Virtual Cockpit)", "Anahtarsız Giriş ve Çalıştırma (KESSY)", "Geri Görüş Kamerası ve Ön/Arka Park Sensörü", "İç Ambiyans Aydınlatması ve Krom Pencere Çerçeveleri", "17\" Stratos / Propus Alaşım Jantlar"],
        },
        {
            "name": "Monte Carlo",
            "level": "premium",
            "summary": "Panoramik Cam Tavanlı ve Matrix LED'li Zirve Scala",
            "features": ["Boydan Boya Panoramik Cam Tavan", "Full LED Matrix Ön Farlar", "Monte Carlo Özel Entegre Başlıklı Kırmızı Şeritli Spor Koltuklar", "Parlak Siyah Ön Panjur, Spoiler ve Difüzör", "Isıtmalı Ön Koltuklar ve Elektrikli Bagaj Kapağı", "18\" Vega Siyah Alaşım Jantlar"],
        },
    ],
    ("Skoda", "Fabia"): [
        {
            "name": "Elite",
            "level": "dusuk",
            "summary": "Sınıfının En Geniş B-Hatchback Girişi",
            "features": ["LED Ön Farlar", "8\" Dijital Gösterge Paneli", "8.25\" Dokunmatik Multimedya & Apple CarPlay", "Çift Bölgeli Otomatik Klima", "Şerit Takip ve Ön Bölge Frenleme Asistanı", "15\" Rotare Alaşım Jantlar"],
        },
        {
            "name": "Premium",
            "level": "orta",
            "summary": "Konfor ve Teknoloji Odaklı B-Hatchback",
            "features": ["Anahtarsız Giriş ve Çalıştırma (KESSY)", "Geri Görüş Kamerası ve Ön/Arka Park Sensörleri", "10.25\" Dijital Gösterge Paneli (Opsiyon/Standart)", "Ön Sis Farları ve Karartılmış Arka Camlar", "Ambiyans Aydınlatma ve Kol Dayama", "16\" Proxima Alaşım Jantlar"],
        },
        {
            "name": "Monte Carlo",
            "level": "premium",
            "summary": "Bi-Color Siyah Tavanlı Sportif Fabia",
            "features": ["Siyah Tavanlı Çift Renk Gövde ve Parlak Siyah Gövde Detayları", "Full LED Mercekli Ön Farlar", "Monte Carlo Özel Spor Koltuklar ve 3 Kollu Spor Direksiyon", "10.25\" Virtual Cockpit Dijital Gösterge Paneli", "Panoramik Cam Tavan (Opsiyon) & Kablosuz Şarj", "17\" Procyon Siyah Elmas Kesim Jantlar"],
        },
    ],
    ("Mercedes-Benz", "GLC"): [
        {
            "name": "Style / Exclusive",
            "level": "dusuk",
            "summary": "Klasik Mercedes Konforu ve 4MATIC Güveni",
            "features": ["4MATIC Dört Çeker Sistemi", "LED High Performance Ön Farlar", "MBUX Geniş Dokunmatik Ekran ve Dijital Gösterge", "Elektrikli ve Isıtmalı Ön Koltuklar", "Elektrikli Bagaj Kapağı (EASY-PACK)", "Geri Görüş Kamerası ve Aktif Park Asistanı", "18\" / 19\" Çok Kollu Alaşım Jantlar"],
        },
        {
            "name": "AMG Line",
            "level": "orta",
            "summary": "Türkiye'de En Çok Tercih Edilen Sportif Lüks SUV",
            "features": ["Panoramik Açılır Cam Tavan", "AMG Gövde Tasarımı ve Elmas Görünümlü Yıldız Panjur", "11.9\" Dikey OLED MBUX Merkezi Ekran & 12.3\" Dijital Gösterge", "Artico Deri / Dinamica Mikrofiber AMG Spor Koltuklar (Hafızalı)", "64 Renkli Ambiyans Aydınlatma", "360 Derece Çevre Görüş Kamerası", "19\" / 20\" AMG 5 Çift Kollu Jantlar"],
        },
        {
            "name": "AMG Line (Digital Light & Burmester)",
            "level": "premium",
            "summary": "Arka Aks Yönlendirmeli ve Burmester'li Zirve GLC",
            "features": ["DIGITAL LIGHT Projeksiyonlu Akıllı Farlar", "Burmester 3D Surround 15 Hoparlörlü Ses Sistemi", "Airmatic Havalı Süspansiyon ve 4.5 Derece Arka Aks Yönlendirme", "Head-Up Display & Artırılmış Gerçeklikli Navigasyon", "Isıtmalı ve Soğutmalı Hakiki Deri Koltuklar", "20\" Çok Kollu AMG Jantlar"],
        },
    ],
    ("Nissan", "Qashqai"): [
        {
            "name": "Tekna",
            "level": "dusuk",
            "summary": "Zengin Güvenlik Donanımlı C-SUV Girişi",
            "features": ["Bi-LED Ön Farlar", "8\" / 9\" Dokunmatik Multimedya & Kablosuz Apple CarPlay", "Çift Bölgeli Otomatik Klima", "Geri Görüş Kamerası ve Ön/Arka Park Sensörü", "Akıllı Çarpışma Önleme, Şerit Takip ve Kör Nokta Uyarı Sistemi", "Anahtarsız Giriş ve Çalıştırma", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Design Pack / Skypack",
            "level": "orta",
            "summary": "Panoramik Cam Tavanlı ve 12.3\" Dijital Ekranlı Paket",
            "features": ["Panoramik Cam Tavan ve Elektrikli Tavan Perdesi", "12.3\" Tam Dijital Gösterge Paneli ve 12.3\" Dokunmatik Navigasyon Ekranı", "360 Derece Akıllı Çevre Görüş Kamerası (AVM)", "Kablosuz Telefon Şarjı ve İç Ambiyans Aydınlatması", "Tavan Rayları ve Karartılmış Arka Camlar", "18\" Elmas Kesim Alaşım Jantlar"],
        },
        {
            "name": "Platinum Premium",
            "level": "premium",
            "summary": "Bose Ses Sistemli ve Masajlı Nappa Deri Zirve Qashqai",
            "features": ["Özel Kapitone Nappa Deri Koltuklar", "Elektrikli, Hafızalı, Isıtmalı ve Masaj Fonksiyonlu Ön Koltuklar", "10.8\" Head-Up Display (Ön Cama Yansıtma)", "Bose 10 Hoparlörlü Premium Ses Sistemi", "Adaptif Matrix LED Ön Farlar", "Eller Serbest Elektrikli Bagaj Kapağı ve ProPILOT Yarı Otonom Sürüş", "19\" / 20\" Alaşım Jantlar"],
        },
    ],
    ("Nissan", "Juke"): [
        {
            "name": "Tekna",
            "level": "dusuk",
            "summary": "Karakteristik Tasarımlı B-SUV Girişi",
            "features": ["Full LED Ön ve Arka Farlar", "8\" Dokunmatik Ekran & Apple CarPlay / Android Auto", "Monoform Sportif Ön Koltuklar", "Geri Görüş Kamerası ve Arka Park Sensörü", "Akıllı Şerit Takip ve Çarpışma Önleme Sistemi", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Platinum",
            "level": "orta",
            "summary": "Yarı Deri Koltuklu ve Konfor Odaklı Paket",
            "features": ["Otomatik Dijital Klima", "Yarı Deri Koltuk Döşemesi ve Deri Kaplı Ön Konsol", "Anahtarsız Giriş ve Çalıştırma (I-Key)", "Isıtmalı Ön Koltuklar ve Isıtmalı Ön Cam", "7\" / 12.3\" Dijital Sürücü Ekranı ve Ön Park Sensörü", "17\" / 19\" Çift Renkli Jantlar"],
        },
        {
            "name": "Platinum Premium",
            "level": "premium",
            "summary": "Koltuk Başlığı Hoparlörlü Bose Personal Plus Zirvesi",
            "features": ["Bose Personal Plus 10 Hoparlörlü Ses Sistemi (Ön Koltuk Başlıklarında UltraNearfield Hoparlörler)", "Alcantara / Deri Özel Kabin ve Koltuk Döşemesi", "360 Derece Çevre Görüş Kamerası", "ProPILOT Yarı Otonom Sürüş, Adaptif Cruise Control ve Kör Nokta Müdahalesi", "Çift Renk Gövde (Siyah/Kırmızı Tavan)", "19\" Akari Elmas Kesim Jantlar"],
        },
    ],
    ("Nissan", "Micra"): [
        {
            "name": "Visia / Match",
            "level": "dusuk",
            "summary": "Şehir İçi Pratik B-Hatchback Girişi",
            "features": ["LED Gündüz Sürüş Farları", "Manuel Klima", "Bluetooth & USB Bağlantılı Radyo", "Yokuş Kalkış Desteği ve Otomatik Farlar", "Hız Sabitleyici", "15\" / 16\" Jantlar"],
        },
        {
            "name": "Tekna",
            "level": "orta",
            "summary": "Dokunmatik Ekranlı ve Park Destekli Paket",
            "features": ["7\" Dokunmatik Multimedya Ekranı & Apple CarPlay", "Otomatik Dijital Klima", "Geri Görüş Kamerası ve Arka Park Sensörü", "Akıllı Çarpışma Önleme ve Şerit Takip Uyarısı", "Yağmur Sensörü ve Karartılmış Arka Camlar", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Platinum / IG-T Bose",
            "level": "premium",
            "summary": "360 Kameralı ve Bose Ses Sistemli En Dolu Micra",
            "features": ["Full LED Ön Farlar", "360 Derece Çevre Görüş Kamerası ve Kör Nokta Uyarı Sistemi", "Anahtarsız Giriş ve Çalıştırma", "Bose Personal Ses Sistemi (Sürücü Koltuk Başlığı Hoparlörlü)", "Çift Renkli Özel İç Kokpit Döşemesi", "17\" Elmas Kesim Alaşım Jantlar"],
        },
    ],
    ("Nissan", "X-Trail"): [
        {
            "name": "Skypack",
            "level": "dusuk",
            "summary": "Panoramik Cam Tavanlı Geniş D-SUV Başlangıcı",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Ön Farlar", "12.3\" Dijital Gösterge & 8\" / 12.3\" Dokunmatik Ekran", "3 Bölgeli Otomatik Dijital Klima", "Ön ve Arka Park Sensörü & Geri Görüş Kamerası", "ProPILOT Güvenlik Paketleri", "18\" Alaşım Jantlar"],
        },
        {
            "name": "Platinum",
            "level": "orta",
            "summary": "Deri Koltuklu ve 360 Kameralı Lüks Aile SUV'u",
            "features": ["Deri Koltuk Döşemesi", "Elektrikli ve Isıtmalı Ön ve Arka Koltuklar", "360 Derece Akıllı Çevre Görüş Kamerası", "Eller Serbest Elektrikli Bagaj Kapağı", "Kablosuz Apple CarPlay ve Kablosuz Şarj", "19\" Alaşım Jantlar"],
        },
        {
            "name": "Platinum Premium (e-4ORCE)",
            "level": "premium",
            "summary": "7 Koltuk Opsiyonlu ve Nappa Derili Zirve X-Trail",
            "features": ["Özel Kapitone Nappa Deri Koltuklar (Hafızalı)", "10.8\" Head-Up Display (Ön Cama Yansıtma)", "Bose 10 Hoparlörlü Premium Ses Sistemi", "Adaptif Matrix LED Ön Farlar", "e-4ORCE Dört Çeker Çift Elektrik Motorlu Çekiş (e-POWER versiyonda)", "5 veya 7 Koltuk Seçeneği", "19\" / 20\" Elmas Kesim Jantlar"],
        },
    ],
    ("Seat", "Leon"): [
        {
            "name": "Style / Style Plus",
            "level": "dusuk",
            "summary": "Zengin Standartlı İspanyol C-Hatchback",
            "features": ["EcoLED Ön ve Arka Farlar", "10.25\" Dijital Gösterge Paneli (MK4)", "8.25\" Dokunmatik Multimedya & Full Link (Apple CarPlay)", "3 Bölgeli Otomatik Dijital Klima (Climatronic)", "Anahtarsız Çalıştırma ve Arka Park Sensörü", "16\" / 17\" Alaşım Jantlar"],
        },
        {
            "name": "Xcellence",
            "level": "orta",
            "summary": "Krom Detaylı ve Konfor Odaklı Paket",
            "features": ["Full LED Mercekli Ön Farlar ve Boydan Boya Sonsuz LED Stop Lambası", "Açılır Cam Sunroof", "Yarı Deri / Alcantara Konfor Koltuklar", "Anahtarsız Giriş ve Çalıştırma (KESSY)", "Geri Görüş Kamerası ve Ambiyans Aydınlatması", "17\" Dynamic Alaşım Jantlar"],
        },
        {
            "name": "FR",
            "level": "premium",
            "summary": "Gençlerin Favorisi Sportif Tasarım ve Sürüş Zirvesi",
            "features": ["Panoramik Açılır Cam Tavan", "FR Özel Tamponlar, Çift Egzoz Görünümü ve Alçaltılmış Spor Süspansiyon", "10\" Geniş Dokunmatik Navigasyon Ekranı ve Akıllı Wraparound Ambiyans Aydınlatma", "Kırmızı Dikişli FR Spor Koltuklar ve Kesik Tabanlı FR Direksiyon", "Seat Sürüş Profili Seçimi (Eco, Normal, Sport, Individual)", "17\" / 18\" FR Performance Alaşım Jantlar"],
        },
    ],
    ("Seat", "Ibiza"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Dinamik ve Ekonomik B-Hatchback Girişi",
            "features": ["EcoLED Ön Farlar", "8.25\" Dokunmatik Multimedya Ekranı", "Çift Bölgeli Otomatik Dijital Klima", "Hız Sabitleyici ve Arka Park Sensörü", "Yorgunluk Tespit ve Şerit Takip Asistanı", "15\" / 16\" Alaşım Jantlar"],
        },
        {
            "name": "Style Plus",
            "level": "orta",
            "summary": "Apple CarPlay ve Geri Görüş Kameralı Paket",
            "features": ["Full Link (Apple CarPlay & Android Auto)", "Geri Görüş Kamerası ve Ön/Arka Park Sensörü", "8\" Dijital Gösterge Paneli", "Katlanır Yan Aynalar ve Karartılmış Arka Camlar", "16\" Design Alaşım Jantlar"],
        },
        {
            "name": "FR",
            "level": "premium",
            "summary": "Panoramik Cam Tavanlı ve Full LED'li Sportif Ibiza",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Mercekli Ön Farlar ve LED Stoplar", "10.25\" Dijital Gösterge Paneli & 9.2\" Geniş Multimedya Ekranı", "FR Özel Spor Tamponlar, Siyah İç Tavan ve Kırmızı Havalandırma Çerçeveleri", "Sürüş Profili Seçimi ve Anahtarsız Giriş/Çalıştırma", "17\" Dynamic / 18\" Performance FR Jantlar"],
        },
    ],
    ("Seat", "Arona"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Şehir İçi Çevik B-SUV Girişi",
            "features": ["EcoLED Ön Farlar", "8.25\" Dokunmatik Multimedya Ekranı", "Çift Bölgeli Otomatik Klima", "Arka Park Sensörü ve Hız Sabitleyici", "Şerit Takip ve Ön Bölge Frenleme Asistanı", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Xperience / Xcellence",
            "level": "orta",
            "summary": "Çift Renk Tavanlı ve Anahtarsız Girişli Paket",
            "features": ["Kontrast Renkli Tavan (Siyah, Gri veya Beyaz)", "Full LED Ön Farlar", "8\" / 10.25\" Dijital Gösterge Paneli & Full Link (CarPlay)", "Anahtarsız Giriş ve Çalıştırma (KESSY)", "Geri Görüş Kamerası ve Otomatik Park Asistanı", "17\" Dynamic Alaşım Jantlar"],
        },
        {
            "name": "FR / FR Plus",
            "level": "premium",
            "summary": "Sportif Difüzörlü ve Büyük Ekranlı Zirve Arona",
            "features": ["10.25\" Dijital Gösterge Paneli & 9.2\" Geniş Dokunmatik Ekran", "FR Özel Ön Panjur, Çift Egzoz Çıkışı Görünümü ve Spor Koltuklar", "Sürüş Profili Seçimi (Seat Drive Profile)", "Kör Nokta Uyarı Sistemi ve Adaptif Cruise Control", "BeatsAudio Ses Sistemi (Opsiyon) ve Kablosuz Şarj", "17\" / 18\" FR Performance Jantlar"],
        },
    ],
    ("Seat", "Ateca"): [
        {
            "name": "Style",
            "level": "dusuk",
            "summary": "Keskin Hatlı C-SUV Başlangıcı",
            "features": ["Full LED Ön ve Arka Farlar", "8.25\" Dokunmatik Multimedya & Full Link", "Çift Bölgeli Otomatik Klima", "Anahtarsız Çalıştırma ve Arka Park Sensörü", "Hız Sabitleyici", "17\" Dynamic Alaşım Jantlar"],
        },
        {
            "name": "Xperience / Xcellence",
            "level": "orta",
            "summary": "Cam Tavanlı ve Alcantara Koltuklu Aile SUV'u",
            "features": ["Açılır Panoramik Cam Tavan", "10.25\" Dijital Gösterge Paneli ve 9.2\" Dokunmatik Ekran", "Siyah Alcantara / Deri Koltuk Döşemesi", "Anahtarsız Giriş ve Çalıştırma & Geri Görüş Kamerası", "Sanal Pedallı Elektrikli Bagaj Kapağı", "18\" Performance Alaşım Jantlar"],
        },
        {
            "name": "FR",
            "level": "premium",
            "summary": "Gövde Rengi Çamurluklu Sportif Zirve Ateca",
            "features": ["Açılır Panoramik Cam Tavan", "FR Özel Gövde Rengi Tamponlar, Çamurluk Dodikleri ve Tavan Spoileri", "Elektrikli, Hafızalı ve Isıtmalı Alcantara FR Spor Koltuklar", "Isıtmalı FR Direksiyon ve Sürüş Profili Seçimi", "360 Derece Çevre Görüş Kamerası ve Kör Nokta Uyarı Sistemi", "18\" / 19\" FR Machined Elmas Kesim Jantlar"],
        },
    ],
    ("Citroen", "C5 Aircross"): [
        {
            "name": "Feel / Feel Bold",
            "level": "dusuk",
            "summary": "Uçan Halı Süspansiyonlu ve 3 Bağımsız Koltuklu Giriş",
            "features": ["Progressive Hydraulic Cushions (Kademeli Hidrolik Destekli Konfor Süspansiyon)", "Kızaklı ve Katlanabilir 3 Bağımsız Arka Koltuk", "12.3\" Dijital Gösterge Paneli ve 8\" Dokunmatik Ekran", "LED Ön Farlar ve Çift Bölgeli Otomatik Klima", "Geri Görüş Kamerası ve Anahtarsız Giriş/Çalıştırma", "18\" Swirl Elmas Kesim Jantlar"],
        },
        {
            "name": "Shine",
            "level": "orta",
            "summary": "Panoramik Cam Tavanlı ve Advanced Comfort Koltuklu Paket",
            "features": ["Açılır Panoramik Cam Tavan", "Advanced Comfort Yarı Deri / Alcantara ekstra dolgulu Konfor Koltuklar", "10\" Yeni Nesil Geniş Dokunmatik Ekran (Makyajlı Kasa)", "Elektrikli Bagaj Kapağı ve Kablosuz Telefon Şarjı", "Adaptif Cruise Control, Kör Nokta Uyarı ve Yarı Otonom Sürüş", "Akustik Yalıtımlı Ön Yan Camlar"],
        },
        {
            "name": "Shine Bold / E-Series",
            "level": "premium",
            "summary": "Nappa Derili ve Masajlı Konfor Zirvesi",
            "features": ["Elektrikli, Isıtmalı ve Çok Noktalı Masaj Fonksiyonlu Ön Koltuklar", "Nappa Deri / Paloma Deri Koltuk Döşemesi", "360 Derece Çevre Görüş Kamerası ve Otomatik Park Asistanı", "Grip Control (Kar, Çamur, Kum Çekiş Modu) & Yokuş İniş Desteği", "Siyah Çift Renk Tavan", "19\" Art Çift Renkli / Siyah Alaşım Jantlar"],
        },
    ],
    ("Citroen", "C4 X"): [
        {
            "name": "Feel",
            "level": "dusuk",
            "summary": "Yüksek Yapılı Crossover-Sedan Başlangıcı",
            "features": ["Progressive Hydraulic Cushions Konfor Süspansiyonu", "LED Ön Farlar ve LED Gündüz Sürüş Farları", "10\" Dokunmatik Multimedya Ekranı & Kablosuz CarPlay", "Çift Bölgeli Otomatik Klima", "Arka Park Sensörü ve Hız Sabitleyici", "16\" / 17\" Jantlar"],
        },
        {
            "name": "Feel Bold",
            "level": "orta",
            "summary": "Advanced Comfort Koltuklu ve Kameralı Paket",
            "features": ["Citroen Advanced Comfort Özel Dolgulu Koltuklar", "Geri Görüş Kamerası ve Ön/Arka Park Sensörü", "Dijital Sürücü Gösterge Ekranı ve Yolcu Tarafı Tablet Tutucu (Smart Pad Support)", "Yağmur Sensörü ve Elektrikli Katlanır Yan Aynalar", "18\" Aeroblade Alaşım Jantlar"],
        },
        {
            "name": "Shine / Shine Bold",
            "level": "premium",
            "summary": "Cam Tavanlı, Head-Up Display'li Zirve C4 X",
            "features": ["Açılır Cam Sunroof", "Renkli Head-Up Display (Ön Cama Yansıtma)", "Yarı Deri / Alcantara Isıtmalı Ön ve Arka Koltuklar, Isıtmalı Direksiyon ve Masajlı Ön Koltuk", "Anahtarsız Giriş ve Çalıştırma", "Otoyol Sürüş Asistanı (Yarı Otonom), Kör Nokta Uyarısı ve Kablosuz Şarj", "18\" Aeroblade Elmas Kesim Jantlar"],
        },
    ],
    ("Citroen", "C3 Aircross"): [
        {
            "name": "Feel",
            "level": "dusuk",
            "summary": "Ferah Kabinli B-SUV Girişi",
            "features": ["EcoLED Ön Farlar", "7\" Dokunmatik Multimedya Ekranı & Apple CarPlay", "Manuel / Otomatik Klima", "Şerit İhlal Uyarısı ve Hız Sabitleyici", "Arka Park Sensörü", "16\" Jantlar"],
        },
        {
            "name": "Feel Bold",
            "level": "orta",
            "summary": "Dijital Klimalı ve Geri Görüş Kameralı Paket",
            "features": ["Otomatik Dijital Klima", "Geri Görüş Kamerası (Makyajlı Kasa)", "Advanced Comfort Koltuklar", "Yağmur Sensörü, Otomatik Farlar ve Karartılmış Arka Camlar", "16\" X Cross Elmas Kesim Alaşım Jantlar"],
        },
        {
            "name": "Shine",
            "level": "premium",
            "summary": "Panoramik Cam Tavanlı ve Çift Renkli En Dolu C3 Aircross",
            "features": ["Açılır Panoramik Cam Tavan", "9\" Geniş Dokunmatik Ekran & Navigasyon", "Kızaklı (İleri-Geri Kayar) Arka Koltuklar ve Katlanır Ön Yolcu Koltuğu", "Anahtarsız Giriş ve Çalıştırma & Grip Control (Opsiyon)", "Çift Renk Gövde (Siyah/Beyaz Tavan) ve Renk Paketi Detayları", "17\" Origami Elmas Kesim Jantlar"],
        },
    ],
    ("Citroen", "C-Elysee"): [
        {
            "name": "Attraction / Live",
            "level": "dusuk",
            "summary": "Geniş Bagajlı ve Ekonomik Filo/Aile Girişi",
            "features": ["Manuel Klima", "Radyo / MP3 Çalar ve Yol Bilgisayarı", "506 Litre Geniş Bagaj Hacmi", "ESP ve Yokuş Kalkış Desteği", "Elektrikli Ön Camlar", "15\" Kapaklı Sac Jantlar"],
        },
        {
            "name": "Confort / Feel",
            "level": "orta",
            "summary": "Hız Sabitleyicili ve 4 Cam Otomatik Dengeli Paket",
            "features": ["Hız Sabitleyici ve Hız Sınırlayıcı", "LED Gündüz Sürüş Farları ve Ön Sis Farları", "Elektrikli Ön ve Arka Camlar", "Bluetooth Telefon Bağlantısı", "Arka Park Sensörü (Feel)", "15\" / 16\" Jantlar"],
        },
        {
            "name": "Exclusive / Shine",
            "level": "premium",
            "summary": "Dijital Göstergeli Klimalı ve Dokunmatik Ekranlı C-Elysee",
            "features": ["7\" Dokunmatik Multimedya Ekranı & Apple CarPlay (Makyajlı Shine)", "Dijital Ekranlı Klima ve Mono-Zone Otomatik Mod", "Geri Görüş Kamerası ve Arka Park Sensörü", "Krom Cam Çerçeveleri ve Deri Direksiyon Simidi", "Ön Kol Dayama", "16\" Boston Alaşım Jantlar"],
        },
    ],
    ("Volvo", "XC40"): [
        {
            "name": "Momentum / Core",
            "level": "dusuk",
            "summary": "İskandinav Güvenliğiyle Premium C-SUV Başlangıcı",
            "features": ["Thor'un Çekici Tasarımlı Full LED Ön Farlar", "12.3\" Dijital Sürücü Ekranı ve 9\" Dikey Dokunmatik Ekran", "Volvo City Safety (Yaya/Bisikletli/Büyük Hayvan Algılamalı Çarpışma Önleme)", "Çift Bölgeli Otomatik Klima ve CleanZone Hava Kalitesi Sistemi", "Elektrikli Bagaj Kapağı ve Geri Görüş Kamerası", "18\" 5 Kollu Alaşım Jantlar"],
        },
        {
            "name": "Inscription / Plus",
            "level": "orta",
            "summary": "Orrefors Kristal Vites Topuzlu ve Cam Tavanlı Lüks Paket",
            "features": ["Açılır Panoramik Cam Tavan", "Orrefors İsveç Kristali Vites Topuzu ve Ahşap (Driftwood) İç Dekor", "Deri Koltuk Döşemesi, Elektrikli ve Hafızalı Ön Koltuklar", "Isıtmalı Ön ve Arka Koltuklar & Isıtmalı Direksiyon", "Anahtarsız Giriş ve Ayak Hareketiyle Açılan Bagaj", "19\" Elmas Kesim Jantlar"],
        },
        {
            "name": "R-Design / Ultimate",
            "level": "premium",
            "summary": "Harman Kardon ve Pilot Assist'li Zirve XC40",
            "features": ["Harman Kardon 13 Hoparlörlü Premium Ses Sistemi", "Pilot Assist (Yarı Otonom Sürüş), Adaptif Cruise Control ve Kör Nokta (BLIS)", "360 Derece Çevre Görüş Kamerası", "Pixel Teknolojili Aktif Viraj Farları", "Nubuk / Nappa Deri R-Design Spor Koltuklar ve Siyah Tavan (R-Design)", "19\" / 20\" 5 Çift Kollu Matt Black Jantlar"],
        },
    ],
    ("Volvo", "XC60"): [
        {
            "name": "Momentum",
            "level": "dusuk",
            "summary": "Dört Çeker (AWD) Güvenlikli Lüks D-SUV Girişi",
            "features": ["AWD Dört Çeker Sistemi", "Full LED Thor'un Çekici Ön Farlar", "12.3\" Dijital Gösterge ve 9\" Sensus / Google Yerleşik Dikey Ekran", "Deri Koltuklar ve Elektrikli Ön Koltuklar", "City Safety, Şerit Koruma ve Elektrikli Bagaj", "18\" / 19\" Alaşım Jantlar"],
        },
        {
            "name": "Inscription / Plus",
            "level": "orta",
            "summary": "Nappa Derili, Isıtmalı/Soğutmalı İskandinav Lüksü",
            "features": ["Açılır Panoramik Cam Tavan", "Delikli Nappa Deri Isıtmalı ve Havalandırmalı (Soğutmalı) Ön Koltuklar", "Orrefors Kristal Vites Topuzu ve Doğal Ahşap İç Kaplama", "Pilot Assist (Yarı Otonom Sürüş) ve BLIS Kör Nokta Uyarısı", "360 Derece Kamera ve 4 Bölgeli Dijital Klima", "19\" / 20\" Inscription Elmas Kesim Jantlar"],
        },
        {
            "name": "R-Design / Ultimate / Polestar",
            "level": "premium",
            "summary": "Havalı Süspansiyonlu ve Bowers & Wilkins Ses Sistemli Zirve",
            "features": ["Aktif Havalı Süspansiyon (Four-C Şasi)", "Bowers & Wilkins veya Harman Kardon Premium Ses Sistemi", "Head-Up Display (Ön Cama Yansıtma)", "Masaj Fonksiyonlu Nappa Deri Koltuklar ve Deri Kaplı Ön Konsol", "Aktif Gölgelemeli Full LED Viraj Farları", "20\" / 21\" Çift Renkli Jantlar"],
        },
    ],
    ("Volvo", "S60"): [
        {
            "name": "Inscription / Plus",
            "level": "dusuk",
            "summary": "250 HP B5 AWD Standartlarında Zengin D-Sedan",
            "features": ["2.0 B5 250 HP Mild-Hybrid Motor & AWD Dört Çeker", "Açılır Panoramik Cam Tavan", "Deri Koltuklar, Elektrikli ve Hafızalı Ön Koltuklar", "Isıtmalı Ön/Arka Koltuklar ve Isıtmalı Direksiyon", "Orrefors Kristal Vites Topuzu", "Pilot Assist, Adaptif Cruise Control ve BLIS", "18\" / 19\" Inscription Jantlar"],
        },
        {
            "name": "R-Design",
            "level": "orta",
            "summary": "Parlak Siyah Detaylı ve Spor Şasili Dinamik S60",
            "features": ["R-Design Parlak Siyah Ön Panjur, Ayna Kapakları ve Tamponlar", "Nappa Deri / Açık Grid Tekstil R-Design Spor Koltuklar", "Metal Mesh Alüminyum İç Dekor ve Siyah Tavan Döşemesi", "360 Derece Çevre Görüş Kamerası", "Harman Kardon Premium Ses Sistemi", "19\" 5 Üçlü Kollu Matt Black Jantlar"],
        },
        {
            "name": "Ultimate (Dark / Bright)",
            "level": "premium",
            "summary": "Head-Up Display ve Bowers & Wilkins Zirvesi",
            "features": ["Head-Up Display (Ön Cama Yansıtma)", "Harman Kardon (Standart) veya Bowers & Wilkins 15 Hoparlörlü Ses Sistemi", "Havalandırmalı (Soğutmalı) ve Masaj Opsiyonlu Nappa Deri Koltuklar", "4 Bölgeli Otomatik Klima", "Google Yerleşik Bilgi-Eğlence Sistemi", "19\" / 20\" Elmas Kesim Jantlar"],
        },
    ],
    ("Cupra", "Formentor"): [
        {
            "name": "Formentor 1.5 TSI (Standart)",
            "level": "dusuk",
            "summary": "Standart Paketi Bile Üst Seviye Olan Sportif C-SUV",
            "features": ["Açılır Panoramik Cam Tavan (Türkiye Paketlerinde Yaygın)", "Full LED Mercekli Ön Farlar ve Boydan Boya Sonsuz LED Arka Stop", "10.25\" Dijital Gösterge Paneli & 10\" / 12\" Dokunmatik Multimedya", "Bakır Dikişli Yarı Deri / Kumaş Cupra Spor Koltuklar", "3 Bölgeli Otomatik Klima, Geri Görüş Kamerası ve Anahtarsız Giriş", "Akıllı Wraparound Ambiyans Aydınlatması", "19\" Exclusive Machined Sport Black/Silver Jantlar"],
        },
        {
            "name": "Formentor (Bucket Koltuk & BeatsAudio Paketli)",
            "level": "orta",
            "summary": "Entegre Başlıklı Yarış Koltuklu ve Bakır Jantlı Paket",
            "features": ["Entegre Başlıklı Elektrikli, Hafızalı ve Isıtmalı Deri Bucket Spor Koltuklar", "Uydu Butonlu (Direksiyon Üzerinden Motor Çalıştırma ve Cupra Modu) Spor Direksiyon", "BeatsAudio 9 Hoparlörlü + Subwoofer Ses Sistemi", "Sanal Pedallı Elektrikli Bagaj Kapağı", "Yarı Otonom Sürüş (Travel Assist) ve Kör Nokta Uyarısı", "19\" Exclusive Copper (Bakır Detaylı) Jantlar"],
        },
        {
            "name": "VZ / VZ-Line (2.0 TSI 310 HP 4Drive)",
            "level": "premium",
            "summary": "310 Beygir Dört Çeker Safkan Performans Zirvesi",
            "features": ["2.0 TSI 310 HP Motor, 4Drive Dört Çeker ve 4.9 Saniye 0-100 Hızlanma", "DCC (Adaptif Şasi Kontrolü - 15 Kademeli Sertlik Ayarı)", "4 Çıkışlı Gerçek Spor Egzoz Sistemi ve Brembo Fren Opsiyonu", "Matrix LED Ön Farlar ve 360 Derece Çevre Görüş Kamerası", "Petrol Mavisi veya Siyah Hakiki Deri Bucket Koltuklar", "Mat Petrol Mavisi / Mat Manyetik Gri Özel Gövde Renkleri"],
        },
    ],
    ("Chery", "Tiggo 7 Pro"): [
        {
            "name": "Comfort",
            "level": "dusuk",
            "summary": "Cam Tavanlı ve Deri Koltuklu Zengin Giriş Paketi",
            "features": ["Açılır Panoramik Cam Tavan", "Full LED Ön Farlar ve Kayar LED Sinyaller", "12.3\" Dijital Gösterge ve 10.25\" Dokunmatik Multimedya & Kablosuz CarPlay", "Suni Deri Koltuklar ve Elektrikli Sürücü Koltuğu", "Anahtarsız Giriş ve Çalıştırma & Uzaktan Motor Çalıştırma", "Geri Görüş Kamerası ve Çift Bölgeli Dijital Klima", "18\" Alaşım Jantlar"],
        },
        {
            "name": "Luxury",
            "level": "orta",
            "summary": "360 Derece Kamera ve Isıtmalı Koltuklu Favori Paket",
            "features": ["360 Derece HD Kuşbakışı Çevre Görüş Kamerası", "Isıtmalı Ön Koltuklar ve Elektrikli Ön Yolcu Koltuğu", "Elektrikli Bagaj Kapağı", "Kablosuz Telefon Şarjı ve Çok Renkli Sesli Komutlu Ambiyans Aydınlatma", "8\" Dokunmatik Klima Kontrol Ekranı", "18\" Parlak Alaşım Jantlar"],
        },
        {
            "name": "Excellent / Avantgarde",
            "level": "premium",
            "summary": "ADAS Otonom Sürüş ve Soğutmalı Koltuklu Zirve Tiggo 7",
            "features": ["Isıtmalı ve Havalandırmalı (Soğutmalı) Ön Koltuklar & Hafızalı Sürücü Koltuğu (Avantgarde)", "24.6\" Kavisli Çift Ekran ve Sony 8 Hoparlörlü Ses Sistemi (Pro Max / Avantgarde)", "12+ ADAS Sürüş Destek Sistemi (Adaptif Cruise Control, Kör Nokta, Şerit Takip, Otomatik Frenleme)", "540 Derece Şeffaf Şasi Görüş Kamerası", "Çift Renk Tavan Seçeneği", "19\" Elmas Kesim Jantlar"],
        },
    ],
    ("Chery", "Tiggo 8 Pro"): [
        {
            "name": "Luxury",
            "level": "dusuk",
            "summary": "7 Kişilik Panoramik Cam Tavanlı D-SUV Başlangıcı",
            "features": ["7 Kişilik Koltuk Düzeni", "Açılır Panoramik Cam Tavan", "24.6\" Kavisli Çift Dijital Ekran + 8\" Dokunmatik Klima Ekranı", "Deri Koltuklar, Isıtmalı Ön Koltuklar ve Elektrikli Sürücü Koltuğu", "360 Derece HD Çevre Görüş Kamerası ve Elektrikli Bagaj Kapağı", "Sony 8 Hoparlörlü Ses Sistemi ve Kablosuz Şarj", "18\" Alaşım Jantlar"],
        },
        {
            "name": "Excellent",
            "level": "orta",
            "summary": "Soğutmalı Koltuklu ve Tam ADAS Güvenlikli Paket",
            "features": ["Isıtmalı ve Havalandırmalı (Soğutmalı) Ön Koltuklar", "Hafızalı Sürücü Koltuğu ve Elektrikli Ön Yolcu Koltuğu", "Gelişmiş ADAS Paketi (Adaptif Hız Sabitleyici, Kör Nokta, ŞeritOrtalama, Çarpışma Önleme)", "Akıllı Sesli Komut Sistemi ve Çok Renkli Ambiyans Aydınlatma", "Akustik Ön Camlar ve Karartılmış Arka Camlar"],
        },
        {
            "name": "Avantgarde (Pro Max)",
            "level": "premium",
            "summary": "Masajlı Kraliçe Koltuğu ve HUD'lu Zirve Tiggo 8",
            "features": ["Masaj Fonksiyonlu ve Elektrikli Bacak Destekli Ön Yolcu Koltuğu", "Head-Up Display (Ön Cama Yansıtma) & Sony 10 Hoparlörlü Ses Sistemi", "540 Derece Şeffaf Şasi Çevre Görüş Kamerası ve Dahili Araç İçi Kamera (DVR)", " Kahverengi Özel Deri Kabin Döşemesi", "9 Hava Yastığı", "19\" Çok Kollu Lüks Jantlar"],
        },
    ],
    ("Chery", "Omoda 5"): [
        {
            "name": "Comfort",
            "level": "dusuk",
            "summary": "Sportif Coupe-SUV Giriş Paketi",
            "features": ["20.5\" Çift Bitişik Dijital Ekran", "Kablosuz Apple CarPlay & Android Auto", "Anahtarsız Giriş ve Çalıştırma", "Geri Görüş Kamerası & Arka Park Sensörü", "17\" Alaşım Jantlar"],
        },
        {
            "name": "Luxury",
            "level": "orta",
            "summary": "360 Kamera ve Sunroof'lu Popüler Omoda 5",
            "features": ["Elektrikli Açılır Sunroof", "360 Derece Çevre Görüş Kamerası", "Elektrikli Bagaj Kapağı", "Isıtmalı Ön Koltuklar & Deri Döşeme", "Kablosuz Şarj Ünitesi", "18\" Spor Alaşım Jantlar"],
        },
        {
            "name": "Excellent",
            "level": "premium",
            "summary": "Soğutmalı Koltuklu ve Tam ADAS Zirve Paketi",
            "features": ["Isıtmalı ve Soğutmalı Ön Koltuklar", "Gelişmiş ADAS Paketi (Adaptif Hız Sabitleyici, Kör Nokta, Şerit Takip)", "Sony 8 Hoparlörlü Ses Sistemi", "Çok Renkli Ambiyans Aydınlatma", "18\" Çift Renkli Kırmızı Vurgulu Spor Jantlar"],
        },
    ],
    ("Togg", "T10X"): [
        {
            "name": "V1 RWD Standart Menzil",
            "level": "dusuk",
            "summary": "314 km Menzilli Akıllı C-SUV Başlangıcı",
            "features": ["Uçtan Uca 29\" Geniş Dijital Ekran + 12\" Gösterge", "8\" Alt Dokunmatik Kumanda Ekranı", "Trumore Akıllı Yaşam Platformu & OTA Güncelleme", "Çift Bölgeli Otomatik Klima & Kablosuz Şarj", "18\" Alaşım Jantlar"],
        },
        {
            "name": "V2 RWD Standart / Uzun Menzil",
            "level": "orta",
            "summary": "523 km Menzil Seçeneği ve Konfor Donanımı",
            "features": ["523 km (WLTP) Uzun Menzil Batarya Seçeneği", "Elektrikli & Hafızalı Isıtmalı Ön Koltuklar", "Elektrikli Bagaj Kapağı & Anahtarsız Giriş", "360 Derece Çevre Görüş Kamerası & Otomatik Park", "19\" Elmas Kesim Alaşım Jantlar"],
        },
        {
            "name": "V2 RWD Uzun Menzil + Meridian & Cam Tavan",
            "level": "premium",
            "summary": "Panoramik Cam Tavan ve Meridian Sesli Zirve T10X",
            "features": ["Açılır Panoramik Cam Tavan", "Meridian 12 Hoparlörlü Premium Ses Sistemi (470W)", "Ön ve Arka Koltuk Isıtma + Isıtmalı Ön Cam", "Krem/Siyah Vegan Deri Koltuklar", "Gelişmiş ADAS Sürüş Destek Paketi (Adaptif Cruise & Trafik Pilotu)"],
        },
    ],
    ("Opel", "Astra J"): [
        {
            "name": "Edition / Business",
            "level": "dusuk",
            "summary": "Ekonomik Giriş & Filo Donanımı",
            "features": ["Manuel Klima", "Hız Sabitleyici (Cruise Control)", "16\" Yapısal Kapaklı Jantlar", "CD400 Ses Sistemi & AUX/USB", "Yokuş Kalkış Desteği"],
        },
        {
            "name": "Sport / Design",
            "level": "orta",
            "summary": "Türkiye'de En Çok Tutulan Konfor Paketi",
            "features": ["Çift Bölgeli Dijital Klima", "Elektronik El Freni", "Yağmur ve Far Sensörü", "17\" Alaşım Jantlar", "Kırmızı İç Ambiyans Aydınlatma", "Arka Park Sensörü"],
        },
        {
            "name": "Cosmo",
            "level": "premium",
            "summary": "AFL+ Bi-Xenon Farlı Zirve Astra J",
            "features": ["AFL+ Akıllı Bi-Xenon Adaptif Ön Farlar & LED Gündüz Farı", "Yarı Deri Spor Koltuklar", "Açılır Elektrikli Sunroof (Opsiyonel)", "Elektrikli Katlanır Yan Aynalar", "Ön-Arka Park Sensörleri & 17\"/18\" Cosmo Jantlar"],
        },
    ],
    ("Opel", "Crossland"): [
        {
            "name": "Essential",
            "level": "dusuk",
            "summary": "Şehir İçi Pratik B-SUV Başlangıcı",
            "features": ["7\" Dokunmatik Multimedya & CarPlay", "LED Ön Farlar", "Şerit İhlali Uyarı Sistemi", "Manuel Klima", "16\" Jantlar"],
        },
        {
            "name": "Edition",
            "level": "orta",
            "summary": "Dijital Klimalı ve Park Kameralı Paket",
            "features": ["Çift Bölgeli Otomatik Klima", "180 Derece Panoramik Geri Görüş Kamerası", "Ön ve Arka Park Sensörleri", "16\" Alaşım Jantlar", "Yağmur ve Far Sensörü"],
        },
        {
            "name": "Elegance / Ultimate",
            "level": "premium",
            "summary": "AGR Ergonomik Koltuklu & Cam Tavanlı Zirve",
            "features": ["AGR Onaylı Ergonomik Yarı Deri Koltuklar", "Panoramik Cam Tavan & Çift Renk Tavan", "Anahtarsız Giriş ve Çalıştırma", "Isıtmalı Ön Koltuklar ve Direksiyon", "17\" Elmas Kesim Jantlar"],
        },
    ],
    ("Volkswagen", "Golf 8"): [
        {
            "name": "Impression",
            "level": "dusuk",
            "summary": "Dijital Kokpitli Yeni Nesil Giriş Paketi",
            "features": ["10.25\" Dijital Gösterge Paneli (Digital Cockpit)", "8.25\" Dokunmatik Multimedya Ekranı", "LED Ön ve Arka Farlar", "Anahtarsız Çalıştırma (Keyless Start)", "Şerit Takip Asistanı"],
        },
        {
            "name": "Life",
            "level": "orta",
            "summary": "3 Bölgeli Klima ve Kablosuz CarPlay'li Popüler Paket",
            "features": ["3 Bölgeli Tam Otomatik Climatronic Klima", "Kablosuz Apple CarPlay & Kablosuz Şarj", "10 Renkli İç Ambiyans Aydınlatma", "Ön ve Arka Park Sensörleri", "16\" Norfolk Alaşım Jantlar"],
        },
        {
            "name": "Style / R-Line",
            "level": "premium",
            "summary": "IQ.Light Matrix Farlı ve Cam Tavanlı Zirve Golf 8",
            "features": ["Açılır Panoramik Cam Tavan", "IQ.Light LED Matrix Ön Farlar & Dinamik Sinyal", "10\" Discover Pro Navigasyonlu Büyük Ekran", "30 Renkli Ambiyans Aydınlatma & ErgoActive Koltuklar", "17\"/18\" R-Line Alaşım Jantlar"],
        },
    ],
    ("Volkswagen", "T-Cross"): [
        {
            "name": "Life",
            "level": "dusuk",
            "summary": "Pratik Kayar Arka Koltuklu B-SUV Girişi",
            "features": ["14 cm İleri-Geri Kaydırılabilen Arka Koltuklar", "8\" Dokunmatik Ekran & App-Connect", "Dijital Gösterge Paneli", "Ön Bölge Asistanı & Şerit Takip", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Style",
            "level": "orta",
            "summary": "Full LED Farlı ve Çift Bölgeli Klimalı Paket",
            "features": ["Full LED Ön Farlar & IQ.Light Arka Stoplar", "Çift Bölgeli Otomatik Climatronic Klima", "Geri Görüş Kamerası & Park Sensörleri", "Kablosuz Şarj & Ambiyans Aydınlatma", "17\" Alaşım Jantlar"],
        },
        {
            "name": "R-Line",
            "level": "premium",
            "summary": "Sportif Gövde Kitli Zirve T-Cross",
            "features": ["R-Line Dış Tasarım Paketi & Spor Koltuklar", "Adaptif Hız Sabitleyici (ACC)", "Anahtarsız Giriş ve Çalıştırma", "Kör Nokta Uyarı Sistemi", "18\" Nevada Alüminyum Alaşım Jantlar"],
        },
    ],
    ("Hyundai", "i10"): [
        {
            "name": "Jump",
            "level": "dusuk",
            "summary": "Ekonomik Şehir İçi Başlangıç Paketi",
            "features": ["Manuel Klima", "Bluetooth & USB Bağlantısı", "Elektrikli Ön Camlar", "Şerit Takip & Çarpışma Önleme (Yeni Nesil)", "14\" Çelik Jantlar"],
        },
        {
            "name": "Style",
            "level": "orta",
            "summary": "8\" Dokunmatik Ekranlı Popüler i10",
            "features": ["8\" Dokunmatik Multimedya & Kablosuz CarPlay", "Geri Görüş Kamerası & Arka Park Sensörü", "15\" Alaşım Jantlar", "Deri Direksiyon ve Vites Topuzu", "Elektrikli Arka Camlar"],
        },
        {
            "name": "Elite",
            "level": "premium",
            "summary": "Sunroof ve Çift Renk Tavanlı En Dolu i10",
            "features": ["Elektrikli Açılır Sunroof", "Otomatik Dijital Klima", "Anahtarsız Giriş ve Çalıştırma", "Çift Renk Siyah Tavan Seçeneği", "16\" Elmas Kesim Alaşım Jantlar"],
        },
    ],
    ("Hyundai", "Accent Era"): [
        {
            "name": "Start / Team",
            "level": "dusuk",
            "summary": "Ekonomik Aile ve Taksi/Filo Başlangıcı",
            "features": ["Manuel Klima", "Elektrikli Ön Camlar", "Hidrolik / EPS Direksiyon", "Radyo CD/MP3 Çalar", "14\" Jantlar"],
        },
        {
            "name": "Mode / Select",
            "level": "orta",
            "summary": "En Çok Aranan Temiz İkinci El Paketi",
            "features": ["4 Cam Elektrikli & Elektrikli Yan Aynalar", "ABS & Çift Hava Yastığı", "Ön Sis Farları", "Yol Bilgisayarı & USB/AUX", "Direksiyondan Kumandalı Ses Sistemi"],
        },
        {
            "name": "Style",
            "level": "premium",
            "summary": "Dijital Klimalı ve Sunroof'lu En Dolu Era",
            "features": ["Otomatik Dijital Klima", "Elektrikli Açılır Sunroof (Opsiyonel)", "15\" Alüminyum Alaşım Jantlar", "Deri Direksiyon & Metalik Orta Konsol", "Arka Kol Dayama"],
        },
    ],
    ("Fiat", "Punto"): [
        {
            "name": "Active / Pop",
            "level": "dusuk",
            "summary": "City Direksiyonlu Ekonomik Şehir Girişi",
            "features": ["City Modlu Elektrikli Direksiyon", "Manuel Klima", "Elektrikli Ön Camlar", "ABS & Çift Hava Yastığı", "15\" Jant Kapakları"],
        },
        {
            "name": "Dynamic / Easy",
            "level": "orta",
            "summary": "Blue&Me ve Alaşım Jantlı Popüler Paket",
            "features": ["Blue&Me Bluetooth & USB Ses Sistemi", "15\"/16\" Alaşım Jantlar", "Ön Sis Farları & Viraj Aydınlatma", "Deri Direksiyon", "Yokuş Kalkış Desteği (Hill Holder)"],
        },
        {
            "name": "Emotion / Lounge",
            "level": "premium",
            "summary": "Skydome Cam Tavanlı En Dolu Punto",
            "features": ["Skydome Panoramik Açılır Cam Tavan", "Çift Bölgeli Otomatik Dijital Klima", "Hız Sabitleyici (Cruise Control)", "Arka Park Sensörü", "16\" Elmas Kesim Alaşım Jantlar"],
        },
    ],
    ("Citroen", "C3"): [
        {
            "name": "Feel",
            "level": "dusuk",
            "summary": "Airbump Tasarımlı Şehir Giriş Paketi",
            "features": ["LED Gündüz Farları & Şerit İhlali Uyarısı", "Manuel Klima", "Hız Sabitleyici ve Sınırlayıcı", "Bluetooth & USB", "16\" Jantlar"],
        },
        {
            "name": "Feel Bold",
            "level": "orta",
            "summary": "Airbump Korumalı ve CarPlay'li Favori Paket",
            "features": ["7\" Dokunmatik Multimedya & Apple CarPlay", "Otomatik Dijital Klima", "Yan Airbump Koruma Panelleri", "Arka Park Sensörü & Elektrikli Katlanır Aynalar", "16\" Alaşım Jantlar"],
        },
        {
            "name": "Shine",
            "level": "premium",
            "summary": "Çift Renk Tavanlı ve Advanced Comfort Koltuklu Zirve",
            "features": ["Advanced Comfort Ekstra Konforlu Koltuklar", "Çift Renk Tavan Seçeneği", "Geri Görüş Kamerası & Anahtarsız Giriş", "ConnectedCAM Entegre Araç Kamerası (Opsiyonel)", "17\" Elmas Kesim Alaşım Jantlar"],
        },
    ],
}
