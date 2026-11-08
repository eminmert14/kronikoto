/**
 * Model Jenerasyon Fotoğrafları Kataloğu
 * Her model için:
 * - earlyPhoto: İlk üretim yılı / erken kasa fotoğrafı
 * - modernPhoto: Makyajlı / güncel kasa fotoğrafı
 * - googleSearchUrl: Google Görsellerde anında arama linki
 */

export interface ModelGenerationPhoto {
  earlyTitle: string;
  earlyYear: string;
  earlyImg: string;
  modernTitle: string;
  modernYear: string;
  modernImg: string;
}

export const MODEL_GENERATION_PHOTOS: Record<string, ModelGenerationPhoto> = {
  // Dacia Duster
  "duster": {
    earlyTitle: "İlk Kasa (1. Jenerasyon)",
    earlyYear: "2010 – 2017",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Dacia_Duster_1.5_dCi_110_4x4_Prestige_%28Facelift%29_%E2%80%93_Frontansicht%2C_28._Dezember_2013%2C_D%C3%BCsseldorf.jpg/640px-Dacia_Duster_1.5_dCi_110_4x4_Prestige_%28Facelift%29_%E2%80%93_Frontansicht%2C_28._Dezember_2013%2C_D%C3%BCsseldorf.jpg",
    modernTitle: "Yeni Nesil / Makyajlı Kasa",
    modernYear: "2018 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/2024_Dacia_Duster_Journey_TCe_130_4x2_in_Sandstone%2C_Front_Right.jpg/640px-2024_Dacia_Duster_Journey_TCe_130_4x2_in_Sandstone%2C_Front_Right.jpg",
  },

  // Renault Megane
  "megane": {
    earlyTitle: "İlk Çıkış Kasası (Pre-Facelift)",
    earlyYear: "2016 – 2020",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Renault_Megane_Grandcoupe_1.2_TCe_130_Bose_Edition_%E2%80%93_Frontansicht%2C_18._Juni_2017%2C_D%C3%BCsseldorf.jpg/640px-Renault_Megane_Grandcoupe_1.2_TCe_130_Bose_Edition_%E2%80%93_Frontansicht%2C_18._Juni_2017%2C_D%C3%BCsseldorf.jpg",
    modernTitle: "Makyajlı Kasa (LED & Dijital Kokpit)",
    modernYear: "2021 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Renault_Megane_Sedan_Facelift_%282022%29_IMG_6404.jpg/640px-Renault_Megane_Sedan_Facelift_%282022%29_IMG_6404.jpg",
  },

  // Renault Clio
  "clio": {
    earlyTitle: "Clio 4 (Önceki Kasa)",
    earlyYear: "2012 – 2019",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Renault_Clio_IV_front_20130105.jpg/640px-Renault_Clio_IV_front_20130105.jpg",
    modernTitle: "Clio 5 / Makyajlı Yeni Kasa",
    modernYear: "2020 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Renault_Clio_V_Facelift_IMG_8604.jpg/640px-Renault_Clio_V_Facelift_IMG_8604.jpg",
  },

  // Fiat Egea
  "egea": {
    earlyTitle: "Egea İlk Çıkış Kasası (Sedan)",
    earlyYear: "2015 – 2020",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Fiat_Tipo_1.6_MultiJet_120_Lounge_%28Sedan%29_%E2%80%93_Frontansicht%2C_12._Juni_2016%2C_Ratingen.jpg/640px-Fiat_Tipo_1.6_MultiJet_120_Lounge_%28Sedan%29_%E2%80%93_Frontansicht%2C_12._Juni_2016%2C_Ratingen.jpg",
    modernTitle: "Egea Cross & Makyajlı Kasa",
    modernYear: "2021 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Fiat_Tipo_Cross_1.0_FireFly_100_Gala_Edition_%E2%80%93_Frontansicht%2C_28._August_2021%2C_D%C3%BCsseldorf.jpg/640px-Fiat_Tipo_Cross_1.0_FireFly_100_Gala_Edition_%E2%80%93_Frontansicht%2C_28._August_2021%2C_D%C3%BCsseldorf.jpg",
  },

  // Volkswagen Passat
  "passat": {
    earlyTitle: "Passat B8 İlk Kasa",
    earlyYear: "2015 – 2019",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/VW_Passat_B8_Limousine_2.0_TDI_Highline_Deep_Black_Front.JPG/640px-VW_Passat_B8_Limousine_2.0_TDI_Highline_Deep_Black_Front.JPG",
    modernTitle: "Passat B8 Makyajlı Kasa",
    modernYear: "2020 – 2023",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Volkswagen_Passat_B8_Facelift_IMG_2803.jpg/640px-Volkswagen_Passat_B8_Facelift_IMG_2803.jpg",
  },

  // Volkswagen Golf
  "golf": {
    earlyTitle: "Golf 7 (Önceki Kasa)",
    earlyYear: "2012 – 2019",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/VW_Golf_VII_2.0_TDI_Highline_Tornadorot.JPG/640px-VW_Golf_VII_2.0_TDI_Highline_Tornadorot.JPG",
    modernTitle: "Golf 8 / Güncel Kasa",
    modernYear: "2020 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/VW_Golf_VIII_IMG_3251.jpg/640px-VW_Golf_VIII_IMG_3251.jpg",
  },

  // Toyota Corolla
  "corolla": {
    earlyTitle: "Corolla E180 (Önceki Kasa)",
    earlyYear: "2013 – 2018",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/2016_Toyota_Corolla_%28ZRE172R%29_Ascent_sedan_%282016-06-23%29_01.jpg/640px-2016_Toyota_Corolla_%28ZRE172R%29_Ascent_sedan_%282016-06-23%29_01.jpg",
    modernTitle: "Corolla E210 Hybrid / Güncel Kasa",
    modernYear: "2019 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/2019_Toyota_Corolla_Icon_Tech_HEV_CVT_1.8_Front.jpg/640px-2019_Toyota_Corolla_Icon_Tech_HEV_CVT_1.8_Front.jpg",
  },

  // Honda Civic
  "civic": {
    earlyTitle: "Civic FC5 İlk Kasa",
    earlyYear: "2016 – 2019",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/2017_Honda_Civic_%28FC%29_VTi-LX_sedan_%282018-10-01%29_01.jpg/640px-2017_Honda_Civic_%28FC%29_VTi-LX_sedan_%282018-10-01%29_01.jpg",
    modernTitle: "Civic FE / Makyajlı Güncel Kasa",
    modernYear: "2020 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/2022_Honda_Civic_Touring_in_Morning_Mist_Metallic%2C_front_left.jpg/640px-2022_Honda_Civic_Touring_in_Morning_Mist_Metallic%2C_front_left.jpg",
  },

  // Ford Focus
  "focus": {
    earlyTitle: "Focus 3 (Önceki Kasa)",
    earlyYear: "2011 – 2018",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Ford_Focus_Sedan_front_20110327.jpg/640px-Ford_Focus_Sedan_front_20110327.jpg",
    modernTitle: "Focus 4 / Güncel Kasa",
    modernYear: "2019 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/2019_Ford_Focus_Titanium_EcoBoost_1.0_Front.jpg/640px-2019_Ford_Focus_Titanium_EcoBoost_1.0_Front.jpg",
  },

  // Peugeot 3008
  "3008": {
    earlyTitle: "3008 İlk Kasa (Pre-Facelift)",
    earlyYear: "2016 – 2020",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Peugeot_3008_II_Allure_BlueHDi_120_Automatic_%E2%80%93_Frontansicht%2C_1._April_2017%2C_D%C3%BCsseldorf.jpg/640px-Peugeot_3008_II_Allure_BlueHDi_120_Automatic_%E2%80%93_Frontansicht%2C_1._April_2017%2C_D%C3%BCsseldorf.jpg",
    modernTitle: "3008 Çentikli LED Makyajlı Kasa",
    modernYear: "2021 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/Peugeot_3008_B_%28Facelift%29_IMG_3962.jpg/640px-Peugeot_3008_B_%28Facelift%29_IMG_3962.jpg",
  },

  // Hyundai Tucson
  "tucson": {
    earlyTitle: "Tucson TL (Önceki Kasa)",
    earlyYear: "2015 – 2020",
    earlyImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Hyundai_Tucson_2.0_CRDi_4WD_Premium_%28TL%29_%E2%80%93_Frontansicht%2C_24._August_2015%2C_D%C3%BCsseldorf.jpg/640px-Hyundai_Tucson_2.0_CRDi_4WD_Premium_%28TL%29_%E2%80%93_Frontansicht%2C_24._August_2015%2C_D%C3%BCsseldorf.jpg",
    modernTitle: "Tucson NX4 / Parametrik Kasa",
    modernYear: "2021 – Günümüz",
    modernImg: "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Hyundai_Tucson_NX4_IMG_3841.jpg/640px-Hyundai_Tucson_NX4_IMG_3841.jpg",
  },
};

/**
 * Model ismi ve markaya göre fotoğraf verisi ve Google Görseller arama linki döndürür.
 */
export function getModelGenerationPhotos(modelName: string, brandName: string, yearStart: number, yearEnd: number | null) {
  const clean = modelName.toLowerCase();

  for (const [key, photoData] of Object.entries(MODEL_GENERATION_PHOTOS)) {
    if (clean.includes(key)) {
      return {
        ...photoData,
        googleSearchUrl: `https://www.google.com/search?tbm=isch&q=${encodeURIComponent(`${brandName} ${modelName} studio shot`)}`,
      };
    }
  }

  // Eşleşmeyen modeller için dinamik şablon
  const earlyYr = String(yearStart);
  const modernYr = yearEnd ? String(yearEnd) : "2024";

  return {
    earlyTitle: `${earlyYr} İlk Model`,
    earlyYear: `${earlyYr}`,
    earlyImg: `https://images.unsplash.com/photo-1542362567-b07e5359b773?auto=format&fit=crop&w=640&q=80`,
    modernTitle: `${modernYr} Güncel Kasa`,
    modernYear: `${modernYr}`,
    modernImg: `https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=640&q=80`,
    googleSearchUrl: `https://www.google.com/search?tbm=isch&q=${encodeURIComponent(`${brandName} ${modelName} studio shot`)}`,
  };
}
