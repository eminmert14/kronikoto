/**
 * KronikOto - Model Başına Tek ve Standart Araç Fotoğrafları Kataloğu
 * Her model için yerel yüksek hızlı ve engelsiz fotoğraf asset'lerini sağlar.
 */

export const MODEL_SINGLE_PHOTOS: Record<string, string> = {
  // Fiat
  "linea": "/cars/fiat-linea.jpg",
  "egea": "/cars/fiat-egea.jpg",
  "doblo": "/cars/fiat-doblo.jpg",

  // Renault
  "megane": "/cars/renault-megane.jpg",
  "clio": "/cars/renault-clio.jpg",
  "captur": "/cars/renault-captur.jpg",
  "kadjar": "/cars/renault-kadjar.jpg",
  "austral": "/cars/renault-austral.jpg",
  "taliant": "/cars/renault-taliant.jpg",

  // Volkswagen
  "passat": "/cars/vw-passat.jpg",
  "golf": "/cars/vw-golf.jpg",
  "polo": "/cars/vw-polo.jpg",
  "tiguan": "/cars/vw-tiguan.jpg",
  "t-roc": "/cars/vw-t-roc.jpg",
  "caddy": "/cars/vw-caddy.jpg",

  // Dacia
  "duster": "/cars/dacia-duster.jpg",
  "sandero": "/cars/dacia-sandero.jpg",

  // Toyota
  "corolla": "/cars/toyota-corolla.jpg",
  "c-hr": "/cars/toyota-c-hr.jpg",
  "yaris": "/cars/toyota-yaris.jpg",
  "rav4": "/cars/toyota-rav4.jpg",

  // Honda
  "civic": "/cars/honda-civic.jpg",
  "city": "/cars/honda-city.jpg",
  "cr-v": "/cars/honda-cr-v.jpg",
  "jazz": "/cars/honda-jazz.jpg",

  // Hyundai
  "i20": "/cars/hyundai-i20.jpg",
  "i30": "/cars/hyundai-i30.jpg",
  "elantra": "/cars/hyundai-elantra.jpg",
  "tucson": "/cars/hyundai-tucson.jpg",
  "bayon": "/cars/hyundai-bayon.jpg",

  // Kia
  "sportage": "/cars/kia-sportage.jpg",
  "ceed": "/cars/kia-ceed.jpg",
  "rio": "/cars/kia-rio.jpg",
  "stonic": "/cars/kia-stonic.jpg",

  // Ford
  "focus": "/cars/ford-focus.jpg",
  "fiesta": "/cars/ford-fiesta.jpg",
  "puma": "/cars/ford-puma.jpg",

  // Peugeot
  "208": "/cars/peugeot-208.jpg",
  "3008": "/cars/peugeot-3008.jpg",
  "301": "/cars/peugeot-301.jpg",

  // Opel
  "astra": "/cars/opel-astra.jpg",
  "corsa": "/cars/opel-corsa.jpg",
  "mokka": "/cars/opel-mokka.jpg",

  // Skoda
  "octavia": "/cars/skoda-octavia.jpg",
  "superb": "/cars/skoda-superb.jpg",
};

/**
 * Model ve marka adına göre tek standart yerel fotoğraf URL'si ve arama linklerini döndürür.
 */
export function getSingleCarPhoto(modelName: string, brandName: string) {
  const clean = modelName.toLowerCase();

  for (const [key, photoUrl] of Object.entries(MODEL_SINGLE_PHOTOS)) {
    if (clean.includes(key)) {
      return {
        photoUrl,
        googleSearchUrl: `https://www.google.com/search?tbm=isch&q=${encodeURIComponent(`${brandName} ${modelName}`)}`,
        sikayetvarSearchUrl: `https://www.google.com/search?q=${encodeURIComponent(`site:sikayetvar.com ${brandName} ${modelName}`)}`,
      };
    }
  }

  // Varsayılan
  return {
    photoUrl: null,
    googleSearchUrl: `https://www.google.com/search?tbm=isch&q=${encodeURIComponent(`${brandName} ${modelName}`)}`,
    sikayetvarSearchUrl: `https://www.google.com/search?q=${encodeURIComponent(`site:sikayetvar.com ${brandName} ${modelName}`)}`,
  };
}
