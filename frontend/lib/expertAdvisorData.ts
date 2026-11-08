/**
 * KronikOto - Modele ve Motora Özel Gerçekçi Ekspertiz ve Satın Alma Danışmanı Motoru
 * Her modelin kronik arızaları, sikayetvar.com kullanıcı bildirimleri,
 * şanzıman ve motor tipi bazlı gerçek kilometre ömürlerine göre hesaplanır.
 */

export interface ExpertModelProfile {
  title: string;
  reliabilityScoreBase: number; // 100 üzerinden temel sağlamlık
  engineKeyCheck: string;
  gearboxKeyCheck: string;
  kmThresholds: {
    lowRiskUpTo: number; // Bu km'ye kadar sorunsuz
    mediumRiskUpTo: number; // Aşınma başlangıcı
    heavyMaintenanceAt: number; // Ağır bakım aralığı
    chainOrBeltName: string; // Triger kayışı / zinciri
    chainOrBeltInterval: string; // Değişim periyodu
  };
  modelSpecificChecks: {
    id: string;
    category: string;
    title: string;
    desc: string;
    critical: boolean;
    sikayetvarIssue: string; // Şikayetvar'da en çok geçen sorun
  }[];
  negotiationSuggestion: {
    normalRange: string;
    criticalDefectRange: string;
    notes: string;
  };
}

export const EXPERT_MODEL_PROFILES: Record<string, ExpertModelProfile> = {
  // FIAT LINEA
  "linea": {
    title: "Fiat Linea",
    reliabilityScoreBase: 78,
    engineKeyCheck: "1.3 Multijet motorlarda yağ soğutucusu (eşanjör) yağ-su karışımı ve turbo emiş hortumu terlemesi; 1.4 Fire motorlarda yüksek devirde sarı motor arıza lambası ve buji yağlanması.",
    gearboxKeyCheck: "Manuel şanzımanlarda debriyaj alt merkezi hidrolik kaçakları ve vites körüğü altı mekanizma boşluğu.",
    kmThresholds: {
      lowRiskUpTo: 100000,
      mediumRiskUpTo: 160000,
      heavyMaintenanceAt: 160000,
      chainOrBeltName: "1.3 Multijet Triger Zinciri (1.4 Fire Triger Kayışı)",
      chainOrBeltInterval: "Zincir için 160.000 km (veya ses yapınca), Kayış için 80.000 km / 5 yıl",
    },
    modelSpecificChecks: [
      {
        id: "lin-1",
        category: "İç Mekan & Güvenlik",
        title: "Torpido (Ön Göğüs) & Airbag Kapağı Çatlağı",
        desc: "Yolcu airbag kapağının üzerinde güneşten kaynaklı kendiliğinden oluşan çatlak/yarılma olup olmadığını kontrol edin.",
        critical: true,
        sikayetvarIssue: "Torpido ve yolcu airbag üstünde kendiliğinden oluşan derin çatlak şikayeti.",
      },
      {
        id: "lin-2",
        category: "Motor Soğutma & Yağ",
        title: "1.3 Multijet Yağ Soğutucusu (Eşanjör) Kaçağı",
        desc: "Antifriz genleşme kabı içine bakın; yağ tabakası veya çamurlaşma varsa yağ soğutucu patlamış demektir.",
        critical: true,
        sikayetvarIssue: "Radyatör suyuna motor yağı karışması ve hararet problemi.",
      },
      {
        id: "lin-3",
        category: "Ateşleme & Çekiş",
        title: "1.4 Fire Sarı Motor Arıza Lambası & Tekleme",
        desc: "3000 devir üzerinde rampada gaza yüklenildiğinde motor arıza lambasının yanıp sönmediğini ve tekleme yapmadığını test edin.",
        critical: true,
        sikayetvarIssue: "Yokuşta çekişten düşme, tekleme ve sarı motor arıza lambası yakma.",
      },
      {
        id: "lin-4",
        category: "Ön Takım",
        title: "Ön Amortisör Üst Takozları & Z Rotlar",
        desc: "Direksiyonu yerinde sağa sola çevirirken tıkırtı veya takılma olup olmadığını, bozuk yolda lokurtu sesini dinleyin.",
        critical: false,
        sikayetvarIssue: "Kasislerde ön takımdan gelen tok lokurtu ve amortisör sesi.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "15.000 – 25.000 TL",
      criticalDefectRange: "30.000 – 45.000 TL",
      notes: "Torpido çatlağı ve yağ soğutucu kaçağı tespit edilirse parça ve işçilik bedelini direkt fiyattan düşürün.",
    },
  },

  // FIAT EGEA
  "egea": {
    title: "Fiat Egea",
    reliabilityScoreBase: 82,
    engineKeyCheck: "1.4 Fire motorda kronik yağ eksiltme (2.000 km'de 1 litreye varan); 1.6 Multijet motorda DPF doluluğu ve turbo intercooler hortumu terlemesi.",
    gearboxKeyCheck: "1.6 Multijet DCT çift kavrama dur-kalk ısınması; Manuel modellerde debriyaj pedalı gıcırtısı ve çatal sesi.",
    kmThresholds: {
      lowRiskUpTo: 70000,
      mediumRiskUpTo: 140000,
      heavyMaintenanceAt: 120000,
      chainOrBeltName: "Triger Kayışı (1.4 Fire / 1.6 Multijet)",
      chainOrBeltInterval: "100.000 – 120.000 km veya 5 yıl",
    },
    modelSpecificChecks: [
      {
        id: "eg-1",
        category: "Motor Tüketimi (1.4 Fire)",
        title: "1.4 Fire Motor Yağ Seviyesi & Egzoz Kurumu",
        desc: "Yağ çubuğunu çekip seviyeyi kontrol edin. Egzoz ucunda yağlı siyah kurum ve bujilerde yağlanma var mı baktırın.",
        critical: true,
        sikayetvarIssue: "Her 2.000-3.000 km'de 1 litre yağ eksiltme ve katalizör arızası.",
      },
      {
        id: "eg-2",
        category: "Elektronik & Kokpit",
        title: "Uconnect Multimedya & Geri Görüş Ekranı",
        desc: "Dokunmatik ekranın donup donmadığını, radyo kanal geçişlerini ve geri vitese takıldığında kameranın siyah ekranda kalmadığını test edin.",
        critical: false,
        sikayetvarIssue: "Multimedya ekranının donması, kendi kendine kapanması ve Bluetooth kopması.",
      },
      {
        id: "eg-3",
        category: "Debriyaj & Şanzıman",
        title: "Debriyaj Pedalı Gıcırtısı & DCT Vites Geçişi",
        desc: "Manuel modellerde debriyaj pedalına basıp bırakırken gıcırtı; DCT otomatiklerde 1'den 2'ye geçerken sarsıntı testi.",
        critical: true,
        sikayetvarIssue: "Debriyaj pedalından gelen gıcırtı ve DCT şanzıman ısınma uyarısı.",
      },
      {
        id: "eg-4",
        category: "Arka Yürüyen Aksam",
        title: "Arka Torsiyon Burçları Kasis Lokurtusu",
        desc: "Arka koltukta yolcu varken kasisten geçerken arkadan gelen vuruntu ve gıcırtı sesini dinleyin.",
        critical: false,
        sikayetvarIssue: "Bozuk yollarda arka süspansiyondan gelen sert vuruntu sesi.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "15.000 – 25.000 TL",
      criticalDefectRange: "30.000 – 50.000 TL",
      notes: "1.4 Fire alınıyorsa yağ yakma geçmişi sorgulanmalı; DCT şanzıman kavrama payı cihazla ölçtürülmelidir.",
    },
  },

  // RENAULT MEGANE 4
  "megane": {
    title: "Renault Megane 4",
    reliabilityScoreBase: 84,
    engineKeyCheck: "1.5 dCi motorda termostat plastik kütüğü antifriz sızıntısı; 1.3 TCe motorda turbo wastegate metalik çıngırtı sesi.",
    gearboxKeyCheck: "7 ileri ıslak/kuru EDC şanzımanlarda 3. vitesten 4. vitese geçerken mekanik 'vuup' uğultusu ve kavrama aşınması.",
    kmThresholds: {
      lowRiskUpTo: 80000,
      mediumRiskUpTo: 140000,
      heavyMaintenanceAt: 100000,
      chainOrBeltName: "1.5 dCi Triger Kayışı (1.3 TCe Triger Zinciri)",
      chainOrBeltInterval: "1.5 dCi: 100.000 km / 4 yıl; 1.3 TCe: Zincirli (ömürlük / 200k+ km)",
    },
    modelSpecificChecks: [
      {
        id: "meg-1",
        category: "Şanzıman (EDC)",
        title: "EDC 3. Vitesten 4. Vitese Geçiş 'Vuup' Sesi",
        desc: "Sakin hızlanmada 3'ten 4'e geçerken motordan veya şanzımandan gelen 'vuup / uğultu' sesini dikkatle dinleyin.",
        critical: true,
        sikayetvarIssue: "EDC şanzıman vites geçişlerinde vuup sesi ve yoğun trafikte ısınma uyarısı.",
      },
      {
        id: "meg-2",
        category: "Soğutma Sistemi",
        title: "Termostat Plastik Kütüğü Antifriz Kaçağı",
        desc: "Motorun sağ tarafındaki plastik termostat yuvasının altına bakın; pembe antifriz kuruması var mı kontrol edin.",
        critical: true,
        sikayetvarIssue: "Termostat gövdesinden su eksiltme ve motor hararet riski.",
      },
      {
        id: "meg-3",
        category: "Elektronik & Multimedya",
        title: "R-Link 2 Dikey Ekran Kararması & Donma",
        desc: "Büyük multimedya ekranının dokunmatiğini ve klima kontrollerinin ekrandan gecikmesiz çalıştığını test edin.",
        critical: false,
        sikayetvarIssue: "R-Link ekranının siyah ekranda kalması ve geri görüş kamerasının açılmaması.",
      },
      {
        id: "meg-4",
        category: "Aydınlatma & Gövde",
        title: "Pure Vision LED Far İçi Buğulanma / Su Alma",
        desc: "Far camlarının iç köşelerinde su damlacıkları veya buğu lekesi olup olmadığını kontrol edin.",
        critical: false,
        sikayetvarIssue: "Yağmur sonrası ön LED farların içine buğu ve nem alması.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "20.000 – 35.000 TL",
      criticalDefectRange: "40.000 – 65.000 TL",
      notes: "EDC şanzımanda titreme veya vuup sesi varsa yetkili servis kavrama değişim masrafı talep edilmelidir.",
    },
  },

  // VOLKSWAGEN PASSAT B8
  "passat": {
    title: "Volkswagen Passat B8",
    reliabilityScoreBase: 86,
    engineKeyCheck: "1.6 / 2.0 TDI motorda devirdaim su pompası kilitlenmesi ve termostat gövdesi kaçağı; 1.5 TSI ACT silindir kapatma silkelemesi.",
    gearboxKeyCheck: "DQ200 7 ileri kuru kavrama DSG: Mekatronik gövde basınç tüpü gevşemesi/çatlağı (P17BF arızası) ve kavrama bitişi.",
    kmThresholds: {
      lowRiskUpTo: 90000,
      mediumRiskUpTo: 150000,
      heavyMaintenanceAt: 120000,
      chainOrBeltName: "Triger Kayışı ve Devirdaim Seti",
      chainOrBeltInterval: "120.000 km veya 5 yıl (Devirdaim su pompasıyla birlikte)",
    },
    modelSpecificChecks: [
      {
        id: "pas-1",
        category: "Şanzıman (DSG)",
        title: "DSG Mekatronik Basınç Tüpü & Kavrama Payı",
        desc: "Ekspertiz arıza tespit cihazına (VCDS/OBD) bağlatıp şanzıman mekatronik hidrolik basınç değerini ve kalan kavrama balata payını okutun.",
        critical: true,
        sikayetvarIssue: "DSG mekatronik arızası sonucu vites geçişlerinin devre dışı kalması ve 'Şanzıman Hatası' uyarısı.",
      },
      {
        id: "pas-2",
        category: "Motor Soğutma",
        title: "Elektronik Devirdaim Su Pompası Kaçağı",
        desc: "TDI motorlarda devirdaim pompasının açılır-kapanır perdesi takılı kalabilir veya antifriz sızdırabilir; motor alt muhafazasına baktırın.",
        critical: true,
        sikayetvarIssue: "Soğutma sıvısı seviye uyarısı ve devirdaim su pompası kilitlemesi.",
      },
      {
        id: "pas-3",
        category: "Gövde & Konfor",
        title: "Sunroof / Panoramik Tavan Su Tahliye Hortumu",
        desc: "A sütunu iç trimlerine ve tavan döşemesine bakın; tahliye boruları tıkandığında içeriye su sızıp tavanı lekelendirir.",
        critical: true,
        sikayetvarIssue: "Yağmurda sunroof tahliyesinin tıkanması ve taban halısına su dolması.",
      },
      {
        id: "pas-4",
        category: "Ön Süspansiyon",
        title: "Ön Salıncak Arka Burçları (Gıcırtı)",
        desc: "Kasislerden yavaşça geçerken ön takımdan gelen 'lastik gıcırtısı' sesini dinleyin.",
        critical: false,
        sikayetvarIssue: "Kasislerde ön takımdan gelen gıcırtı sesi.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "25.000 – 40.000 TL",
      criticalDefectRange: "50.000 – 85.000 TL",
      notes: "DSG kavrama payı sınırda veya devirdaim kaçağı varsa doğrudan 45.000 TL üzeri pazarlık payı istenmelidir.",
    },
  },

  // DACIA DUSTER
  "duster": {
    title: "Dacia Duster",
    reliabilityScoreBase: 83,
    engineKeyCheck: "1.5 dCi motor kaya gibi sağlamdır; ECO-G modellerde LPG şamandıra seviye sensörü tutarsızlığı.",
    gearboxKeyCheck: "4x4 modellerde şaft askı bilyası ve arka elektro-manyetik diferansiyel kilidi; EDC otomatiklerde kavrama.",
    kmThresholds: {
      lowRiskUpTo: 90000,
      mediumRiskUpTo: 160000,
      heavyMaintenanceAt: 100000,
      chainOrBeltName: "1.5 dCi Triger Kayışı (1.0 / 1.3 TCe Triger Zinciri)",
      chainOrBeltInterval: "1.5 dCi için 100.000 km / 4 yıl; TCe motorlar zincirlidir.",
    },
    modelSpecificChecks: [
      {
        id: "dus-1",
        category: "Çekiş & 4x4 Sistemi",
        title: "4x4 Şaft Askı Bilyası & Diferansiyel Kilidi",
        desc: "4x4 modellerde 70-90 km/s hızda tabandan gelen titreşimi ve 4WD Lock modunun takılmadan devreye girdiğini test edin.",
        critical: true,
        sikayetvarIssue: "4x4 sisteminde şaft ötmesi ve diferansiyel kilit uyarısı.",
      },
      {
        id: "dus-2",
        category: "Yakıt Sistemi (ECO-G)",
        title: "LPG Şamandıra Göstergesi Tutarsızlığı",
        desc: "Gösterge panelindeki LPG yakıt seviyesinin dalgalanma yapmadığını ve benzinden gaza geçişte silkeleme olmadığını kontrol edin.",
        critical: false,
        sikayetvarIssue: "LPG deposu doluyken göstergenin boş göstermesi veya ani düşüşler.",
      },
      {
        id: "dus-3",
        category: "Gövde & Yalıtım",
        title: "Kapı & Bagaj Fitil Toz / Su Sızdırmazlığı",
        desc: "Kapı eşiklerinde ve bagaj fitillerinde içeriye toz veya su alma izi var mı kontrol edin.",
        critical: false,
        sikayetvarIssue: "Kapı fitillerinden yüksek hızda rüzgar sesi ve içeri toz alması.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "15.000 – 25.000 TL",
      criticalDefectRange: "30.000 – 45.000 TL",
      notes: "4x4 yürüyen aksamı ve şaft askı bilyası kontrol edilmeden kesinlikle alınmamalıdır.",
    },
  },

  // PEUGEOT 3008
  "3008": {
    title: "Peugeot 3008",
    reliabilityScoreBase: 76,
    engineKeyCheck: "1.2 PureTech motorda motor yağı içinde çalışan 'ıslak triger kayışı' ufalanması; 1.5 BlueHDi motorda AdBlue deposu/pompası kristalleşme arızası.",
    gearboxKeyCheck: "EAT6 / EAT8 tam otomatik tork konvertörlü şanzımanlar çok sağlamdır; soğutucu eşanjör kontrol edilmeli.",
    kmThresholds: {
      lowRiskUpTo: 50000,
      mediumRiskUpTo: 90000,
      heavyMaintenanceAt: 60000,
      chainOrBeltName: "1.2 PureTech Islak Triger Kayışı (1.5 BlueHDi Eksantrik Zincir/Kayış)",
      chainOrBeltInterval: "1.2 PureTech için 50.000 – 60.000 km veya 4 yıl (Özel aparatla kayış kalınlığı ölçülmeli!)",
    },
    modelSpecificChecks: [
      {
        id: "p3-1",
        category: "Hayati Motor Riski (PureTech)",
        title: "1.2 PureTech Islak Triger Kayışı Ufalanması",
        desc: "Yağ dolum kapağını açıp triger kayışının sırtına bakın; çatlak, genişleme veya ufalanma var mı? Yağ süzgecini tıkarsa motor kilitler!",
        critical: true,
        sikayetvarIssue: "Yağ basıncı düşük uyarısı, triger kayışının eriyip karter süzgecini tıkaması.",
      },
      {
        id: "p3-2",
        category: "Emisyon & Egzoz (BlueHDi)",
        title: "1.5 BlueHDi AdBlue Deposu & Pompa Arızası",
        desc: "Göstergede 'Üre / AdBlue Sistemi Arızası - 1100 km sonra motor çalışmayacak' uyarısı geçmişi olup olmadığını OBD ile sorgulatın.",
        critical: true,
        sikayetvarIssue: "AdBlue deposu ve pompa arızası nedeniyle komple fahiş depo değişim maliyeti.",
      },
      {
        id: "p3-3",
        category: "Kabin & Multimedya",
        title: "i-Cockpit Ekran & Klima Menü Tepkisi",
        desc: "Dokunmatik ekranda klima menüsüne basınca geçişlerin takılmadığını ve geri görüş kamerasının net açıldığını kontrol edin.",
        critical: false,
        sikayetvarIssue: "Multimedya ekranının geç tepki vermesi ve donması.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "25.000 – 40.000 TL",
      criticalDefectRange: "60.000 – 100.000 TL",
      notes: "PureTech motorda triger kayışı yetkili serviste revize parçayla değişmemişse acil 40.000 TL masraf bütçesi ayrılmalıdır.",
    },
  },

  // OPEL ASTRA K
  "astra": {
    title: "Opel Astra K",
    reliabilityScoreBase: 77,
    engineKeyCheck: "1.6 CDTI (B16DTH) motorda şanzıman tarafındaki triger zincirinin uzaması ve soğuk çalıştırmada metalik şıkırtı sesi.",
    gearboxKeyCheck: "Manuel modellerde debriyaj alt merkezi ve baskı balata; Otomatiklerde tork konvertörlü 6 ileri sağlamdır.",
    kmThresholds: {
      lowRiskUpTo: 70000,
      mediumRiskUpTo: 110000,
      heavyMaintenanceAt: 100000,
      chainOrBeltName: "1.6 CDTI Arka Triger Zincir Seti",
      chainOrBeltInterval: "100.000 – 120.000 km (Motor indirilerek değişir)",
    },
    modelSpecificChecks: [
      {
        id: "ast-1",
        category: "Motor Mekanik (1.6 CDTI)",
        title: "Arka Triger Zincir Şıkırtısı (Soğuk Başlatma)",
        desc: "Motor tamamen soğukken marşa basın; ilk 3-5 saniye metalik zincir şıkırtısı geliyorsa zincir uzamıştır. Değişim için motor iner!",
        critical: true,
        sikayetvarIssue: "1.6 CDTI triger zincir sesi ve motor indirme işçilik maliyeti.",
      },
      {
        id: "ast-2",
        category: "Debriyaj & Hidrolik",
        title: "Debriyaj Alt Merkezi Kaçağı & Pedal Düşmesi",
        desc: "Debriyaj pedalının tabanda kalıp kalmadığını ve şanzıman altından fren hidroliği damlaması olup olmadığını kontrol edin.",
        critical: true,
        sikayetvarIssue: "Debriyaj pedalının boşalması ve alt merkez patlaması.",
      },
      {
        id: "ast-3",
        category: "Soğutma Sistemi",
        title: "Soğutma Suyu Genleşme Deposu Çatlağı",
        desc: "Antifriz bidonunun dikiş yerlerinde ve hortum bağlantı boğazında kılcal çatlak terlemesi var mı bakın.",
        critical: false,
        sikayetvarIssue: "Su eksiltme ve antifriz kabı çatlaması.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "20.000 – 35.000 TL",
      criticalDefectRange: "50.000 – 80.000 TL",
      notes: "Zincir değişmemiş bir 1.6 CDTI için en az 45.000 TL pazarlık payı istenmelidir.",
    },
  },

  // TOYOTA COROLLA
  "corolla": {
    title: "Toyota Corolla",
    reliabilityScoreBase: 92,
    engineKeyCheck: "1.8 Hybrid e-CVT motor mekanik olarak dünyanın en sorunsuz sistemlerindendir; 1.6 Valvematic LPG ile sübap erimesi.",
    gearboxKeyCheck: "e-CVT ve Multidrive S şanzımanlarda kavrama diski yoktur, sorunsuz çalışır.",
    kmThresholds: {
      lowRiskUpTo: 140000,
      mediumRiskUpTo: 220000,
      heavyMaintenanceAt: 150000,
      chainOrBeltName: "Triger Zinciri (Ömürlük)",
      chainOrBeltInterval: "Zincir 250.000+ km sorunsuzdur; Sadece hibrit batarya soğutma fanı temizlenmelidir.",
    },
    modelSpecificChecks: [
      {
        id: "cor-1",
        category: "Hibrit Sistemi (1.8 Hybrid)",
        title: "Hibrit Batarya Fan Filtresi Toz Tıkanıklığı",
        desc: "Arka koltuk altındaki batarya soğutma hava ızgarasını kontrol ettirin; tıkanırsa batarya hücreleri aşırı ısınır.",
        critical: true,
        sikayetvarIssue: "Hibrit batarya fanı toz tıkanması ve çekiş düşüklüğü.",
      },
      {
        id: "cor-2",
        category: "Direksiyon & Ön Takım",
        title: "Direksiyon Kolonu Tıkırtı Burcu",
        desc: "Parke taşlı yolda direksiyondan elinize gelen hafif tıkırtı sesini dinleyin.",
        critical: false,
        sikayetvarIssue: "Bozuk yolda direksiyondan gelen tıkırtı sesi.",
      },
      {
        id: "cor-3",
        category: "Yalıtım & Trim",
        title: "Davlumbaz Yol Sesi ve Ön Göğüs Trimleri",
        desc: "100 km/s hızda yol ve lastik ses seviyesini dinleyin; yalıtım zayıf olduğundan beklentinizle kıyaslayın.",
        critical: false,
        sikayetvarIssue: "Yüksek hızda tekerlek yuvalarından gelen aşırı yol uğultusu.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "10.000 – 20.000 TL",
      criticalDefectRange: "25.000 – 35.000 TL",
      notes: "Toyota mekaniği çok dayanıklıdır; sadece hibrit batarya sağlık testi ve rutin bakım geçmişi aranmalıdır.",
    },
  },

  // HONDA CIVIC FC5
  "civic": {
    title: "Honda Civic FC5",
    reliabilityScoreBase: 85,
    engineKeyCheck: "1.6 Eco fabrikasyon LPG motorunda sübap boşluk ayarı daralması; 1.5 VTEC Turbo motorda benzin-yağ karışımı (kısa mesafe).",
    gearboxKeyCheck: "CVT şanzımanlarda yağ değişim periyodu (40.000 km'de bir) aksatılmamış olmalıdır.",
    kmThresholds: {
      lowRiskUpTo: 90000,
      mediumRiskUpTo: 160000,
      heavyMaintenanceAt: 120000,
      chainOrBeltName: "Triger Zinciri",
      chainOrBeltInterval: "Zincirli sistemdir, 200.000 km'ye kadar dayanıklıdır.",
    },
    modelSpecificChecks: [
      {
        id: "civ-1",
        category: "Kaporta & Gövde",
        title: "C Sütununda Sac Dalgalanması & Göçük",
        desc: "Arka kelebek camının üstündeki C sütununa güneş ışığı altında açılı bakın; fabrikasyon dalgalanma veya çökme var mı kontrol edin.",
        critical: true,
        sikayetvarIssue: "C sütunu sacında kendiliğinden oluşan göçük ve dalgalanma şikayeti.",
      },
      {
        id: "civ-2",
        category: "LPG & Motor (1.6 Eco)",
        title: "Subap Ayarı Boşluğu & Soğukta Stop Etme",
        desc: "LPG'li modellerde 40.000-50.000 km'de bir manuel subap ayarı gerekir. Soğuk ilk çalıştırmada devir dalgalanması var mı bakın.",
        critical: true,
        sikayetvarIssue: "Sabah ilk çalıştırmada gaz yememe, stop etme ve subap ayarı ihtiyacı.",
      },
      {
        id: "civ-3",
        category: "Direksiyon Kutusu",
        title: "Elektrikli Direksiyon Kutusu Boşluğu / Tıkırtı",
        desc: "Araç dururken direksiyonu hafifçe sağa sola oynatıp tıkırtı boşluğu olup olmadığını kontrol ettirin.",
        critical: false,
        sikayetvarIssue: "Direksiyon kutusu boşluğu ve manevrada ses yapması.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "15.000 – 25.000 TL",
      criticalDefectRange: "35.000 – 50.000 TL",
      notes: "C sütunu göçüğü olan araçlarda değer kaybı pazarlığı yapılmalıdır.",
    },
  },
};

/**
 * Genel modeller için markaya veya genel araç segmentine göre özel uzman profili üretir.
 */
export function getModelExpertProfile(modelName: string, brandName: string, transmissionType: string): ExpertModelProfile {
  const clean = modelName.toLowerCase();

  for (const [key, profile] of Object.entries(EXPERT_MODEL_PROFILES)) {
    if (clean.includes(key)) {
      return profile;
    }
  }

  // Varsayılan dinamik profil
  const isAuto = transmissionType === "otomatik";
  return {
    title: `${brandName} ${modelName}`,
    reliabilityScoreBase: 80,
    engineKeyCheck: `${brandName} motorlarında antifriz kütüğü kaçakları, yağ seviye stabilitesi ve turbo emiş hortumu terlemeleri kontrol edilmelidir.`,
    gearboxKeyCheck: isAuto
      ? "Otomatik şanzımanda dur-kalk trafikte kavrama ısınması ve vites geçiş silkelemesi test edilmelidir."
      : "Manuel şanzımanda debriyaj kavrama noktası ve baskı balata geri kaçırma durumu incelenmelidir.",
    kmThresholds: {
      lowRiskUpTo: 80000,
      mediumRiskUpTo: 140000,
      heavyMaintenanceAt: 100000,
      chainOrBeltName: "Triger ve Kayış Seti",
      chainOrBeltInterval: "90.000 – 120.000 km veya 5 yıl",
    },
    modelSpecificChecks: [
      {
        id: "gen-1",
        category: "Motor Mekanik",
        title: "Karter Havalandırma & Yağ Sızıntısı",
        desc: "Motor bloğu çevresinde, külbütör kapağında ve karter tapasında yağ terlemesi olup olmadığını kontrol ettirin.",
        critical: true,
        sikayetvarIssue: "Motor altından yağ terlemesi ve eksiltme şikayetleri.",
      },
      {
        id: "gen-2",
        category: "Soğutma Sistemi",
        title: "Termostat Gövdesi & Genleşme Tankı Kaçağı",
        desc: "Antifriz haznesinde pembe kurum lekesi veya kılcal çatlak kaçağı olup olmadığını inceleyin.",
        critical: true,
        sikayetvarIssue: "Soğutma sıvısı seviye düşüşü ve termostat yuvası kaçakları.",
      },
      {
        id: "gen-3",
        category: "Şanzıman",
        title: isAuto ? "Otomatik Vites Geçiş & Isınma Testi" : "Debriyaj Kavrama Noktası & Baskı Balata",
        desc: isAuto
          ? "Rampada dur-kalk yaparak geri kaçırma ve 1-2 vites geçişlerinde vuruntu olup olmadığını test edin."
          : "Debriyaj pedalının sertliğini ve yüksekte kavrayıp kavramadığını test edin.",
        critical: true,
        sikayetvarIssue: isAuto ? "Otomatik vites geçişlerinde titreme." : "Debriyaj sertleşmesi ve kavrama kaçırması.",
      },
      {
        id: "gen-4",
        category: "Yürüyen Aksam",
        title: "Ön Takım Salıncak Burçları & Amortisörler",
        desc: "Bozuk yollarda çukurlara girildiğinde içeri gelen tok darbe sesini ve salıncak burç lastiklerini inceletin.",
        critical: false,
        sikayetvarIssue: "Kasislerde ön takımdan gelen sesler.",
      },
    ],
    negotiationSuggestion: {
      normalRange: "15.000 – 25.000 TL",
      criticalDefectRange: "30.000 – 50.000 TL",
      notes: "Ekspertizde çıkabilecek ağır bakım eksiklikleri ve yürüyen aksam masrafları fiyattan düşülmelidir.",
    },
  };
}
