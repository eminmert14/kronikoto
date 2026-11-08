import urllib.request
import os

os.makedirs("c:/ProjeAraba/frontend/public/cars", exist_ok=True)

# Wikimedia Direct Full-Size Images (200 OK)
URLS = {
    "fiat-linea.jpg": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Fiat_Linea.jpg",
    "fiat-egea.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/05/2016_Fiat_Tipo_Easy_1.4_Front.jpg",
    "fiat-doblo.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4b/Fiat_Doblo_%282015%29.jpg",
    "renault-megane.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/82/Renault_M%C3%A9gane_IV_%28Front%29.jpg",
    "renault-clio.jpg": "https://upload.wikimedia.org/wikipedia/commons/d/d4/Renault_Clio_V_%28Front%29.jpg",
    "renault-captur.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/22/2019_Renault_Captur_Iconic_TCe_1.3_Front.jpg",
    "renault-kadjar.jpg": "https://upload.wikimedia.org/wikipedia/commons/1/14/2016_Renault_Kadjar_Dynamique_Nav_dCi_1.5_Front.jpg",
    "renault-austral.jpg": "https://upload.wikimedia.org/wikipedia/commons/c/c5/Renault_Austral_E-Tech_1.2_IMG_8239.jpg",
    "renault-taliant.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/00/Renault_Taliant_1.0_TCe_90_Joy_in_Istanbul.jpg",
    "vw-passat.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/52/Volkswagen_Passat_B8_Facelift_IMG_2803.jpg",
    "vw-golf.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4c/VW_Golf_VII_2.0_TDI_Highline_Tornadorot.JPG",
    "vw-polo.jpg": "https://upload.wikimedia.org/wikipedia/commons/2/23/VW_Polo_VI_IMG_0083.jpg",
    "vw-tiguan.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/30/2017_Volkswagen_Tiguan_SE_Nav_TDi_2.0_Front.jpg",
    "vw-t-roc.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5e/Volkswagen_T-Roc_1.0_TSI_Style_Front.jpg",
    "vw-caddy.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/60/2016_Volkswagen_Caddy_C20_Startline_TDi_2.0_Front.jpg",
    "dacia-duster.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/ec/2020_Dacia_Duster_Comfort_TCe_1.0_Front.jpg",
    "dacia-sandero.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/36/2021_Dacia_Sandero_Stepway_Comfort_TCe_90_1.0_Front.jpg",
    "toyota-corolla.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b8/2019_Toyota_Corolla_Icon_Tech_HEV_CVT_1.8_Front.jpg",
    "toyota-c-hr.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/98/Toyota_C-HR_Hybrid_Excel_%28Front%29.jpg",
    "toyota-yaris.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4e/2020_Toyota_Yaris_Design_HEV_CVT_1.5_Front.jpg",
    "toyota-rav4.jpg": "https://upload.wikimedia.org/wikipedia/commons/6/69/2019_Toyota_RAV4_Excel_HEV_CVT_2.5_Front.jpg",
    "honda-civic.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/47/2017_Honda_Civic_SR_VTEC_1.0_Front.jpg",
    "honda-cr-v.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/07/2018_Honda_CR-V_EX-L_1.5L_front_4.2.19.jpg",
    "honda-city.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/a2/Honda_City_%28seventh_generation%29_in_Brunei.jpg",
    "honda-jazz.jpg": "https://upload.wikimedia.org/wikipedia/commons/7/7b/2020_Honda_Jazz_SR_i-MMD_CVT_1.5_Front.jpg",
    "ford-focus.jpg": "https://upload.wikimedia.org/wikipedia/commons/3/3d/2019_Ford_Focus_Titanium_EcoBoost_1.0_Front.jpg",
    "ford-fiesta.jpg": "https://upload.wikimedia.org/wikipedia/commons/8/80/2018_Ford_Fiesta_Zetec_Turbo_1.0_Front.jpg",
    "ford-puma.jpg": "https://upload.wikimedia.org/wikipedia/commons/f/f6/2020_Ford_Puma_ST-Line_EcoBoost_mHEV_1.0_Front.jpg",
    "peugeot-3008.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/02/Peugeot_3008_B_%28Facelift%29_IMG_3962.jpg",
    "peugeot-2008.jpg": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Peugeot_2008_Allure_PureTech_130_EAT8_IMG_2773.jpg",
    "peugeot-208.jpg": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Peugeot_208_Allure_PureTech_100_IMG_2755.jpg",
    "hyundai-tucson.jpg": "https://upload.wikimedia.org/wikipedia/commons/9/91/Hyundai_Tucson_NX4_IMG_3841.jpg",
    "hyundai-i20.jpg": "https://upload.wikimedia.org/wikipedia/commons/e/e1/Hyundai_i20_1.2_Comfort_%28III%29_%E2%80%93_Frontansicht%2C_13._M%C3%A4rz_2021%2C_D%C3%BCsseldorf.jpg",
    "hyundai-elantra.jpg": "https://upload.wikimedia.org/wikipedia/commons/0/07/2021_Hyundai_Elantra_SEL%2C_front_right%2C_08-25-2021.jpg",
    "opel-astra.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/52/Opel_Astra_1.6_CDTI_Innovation_%28K%29_%E2%80%93_Frontansicht%2C_12._Juni_2016%2C_Ratingen.jpg",
    "opel-corsa.jpg": "https://upload.wikimedia.org/wikipedia/commons/a/ae/Opel_Corsa_F_IMG_2628.jpg",
    "opel-mokka.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Opel_Mokka_B_IMG_3655.jpg",
    "skoda-octavia.jpg": "https://upload.wikimedia.org/wikipedia/commons/5/5a/2020_Skoda_Octavia_SE_First_Edition_e-TEC_1.0_Front.jpg",
    "skoda-superb.jpg": "https://upload.wikimedia.org/wikipedia/commons/4/4e/2016_Skoda_Superb_SE_L_Executive_TDi_2.0_Front.jpg",
}

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

print("Fotograflar indiriliyor...")
downloaded = 0
for fname, url in URLS.items():
    outpath = f"c:/ProjeAraba/frontend/public/cars/{fname}"
    if os.path.exists(outpath) and os.path.getsize(outpath) > 5000:
        downloaded += 1
        continue
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            with open(outpath, "wb") as f:
                f.write(data)
            downloaded += 1
            print(f"OK: {fname} ({len(data)} bayt)")
    except Exception as e:
        print(f"HATA {fname}: {e}")

print(f"Tamamlandi! {downloaded}/{len(URLS)} fotograf hazir.")
