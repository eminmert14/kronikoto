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
}
