import os
import re
import urllib.request
import time

CARS_DIR = r"c:\ProjeAraba\frontend\public\cars"
os.makedirs(CARS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}

MODELS_TO_FETCH = [
    ("fiat", "linea", "fiat-linea.jpg"),
    ("fiat", "egea", "fiat-egea.jpg"),
    ("fiat", "doblo", "fiat-doblo.jpg"),
    ("renault", "megane", "renault-megane.jpg"),
    ("renault", "clio", "renault-clio.jpg"),
    ("renault", "captur", "renault-captur.jpg"),
    ("renault", "kadjar", "renault-kadjar.jpg"),
    ("renault", "austral", "renault-austral.jpg"),
    ("renault", "taliant", "renault-taliant.jpg"),
    ("volkswagen", "passat", "vw-passat.jpg"),
    ("volkswagen", "golf", "vw-golf.jpg"),
    ("volkswagen", "polo", "vw-polo.jpg"),
    ("volkswagen", "tiguan", "vw-tiguan.jpg"),
    ("volkswagen", "t-roc", "vw-t-roc.jpg"),
    ("volkswagen", "caddy", "vw-caddy.jpg"),
    ("dacia", "duster", "dacia-duster.jpg"),
    ("dacia", "sandero", "dacia-sandero.jpg"),
    ("toyota", "corolla", "toyota-corolla.jpg"),
    ("toyota", "c-hr", "toyota-c-hr.jpg"),
    ("toyota", "yaris", "toyota-yaris.jpg"),
    ("toyota", "rav4", "toyota-rav4.jpg"),
    ("honda", "civic", "honda-civic.jpg"),
    ("honda", "city", "honda-city.jpg"),
    ("honda", "cr-v", "honda-cr-v.jpg"),
    ("honda", "jazz", "honda-jazz.jpg"),
    ("hyundai", "i20", "hyundai-i20.jpg"),
    ("hyundai", "i30", "hyundai-i30.jpg"),
    ("hyundai", "elantra", "hyundai-elantra.jpg"),
    ("hyundai", "tucson", "hyundai-tucson.jpg"),
    ("hyundai", "bayon", "hyundai-bayon.jpg"),
    ("kia", "sportage", "kia-sportage.jpg"),
    ("kia", "ceed", "kia-ceed.jpg"),
    ("kia", "rio", "kia-rio.jpg"),
    ("kia", "stonic", "kia-stonic.jpg"),
    ("ford", "focus", "ford-focus.jpg"),
    ("ford", "fiesta", "ford-fiesta.jpg"),
    ("ford", "puma", "ford-puma.jpg"),
    ("peugeot", "208", "peugeot-208.jpg"),
    ("peugeot", "3008", "peugeot-3008.jpg"),
    ("peugeot", "301", "peugeot-301.jpg"),
    ("opel", "astra", "opel-astra.jpg"),
    ("opel", "corsa", "opel-corsa.jpg"),
    ("opel", "mokka", "opel-mokka.jpg"),
    ("skoda", "octavia", "skoda-octavia.jpg"),
    ("skoda", "superb", "skoda-superb.jpg"),
]

results = {}

for brand, model_slug, filename in MODELS_TO_FETCH:
    dest_path = os.path.join(CARS_DIR, filename)
    # If already downloaded and > 5KB, skip
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 5000:
        print(f"[OK EXISTS] {filename} ({os.path.getsize(dest_path)} bytes)")
        results[filename] = True
        continue

    url = f"https://www.sikayetvar.com/{brand}/{model_slug}"
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', 'ignore')
        
        # Look for model image first: https://files.sikayetvar.com/model/...
        model_imgs = re.findall(r'https://files\.sikayetvar\.com/model/[^\s\"\'<>]+\.(?:jpg|png|webp|jpeg)', html)
        img_url = None
        if model_imgs:
            img_url = model_imgs[0]
        else:
            # Fallback to complaint images or og:image
            og_imgs = re.findall(r'<meta property="og:image" content="([^"]+)"', html)
            if og_imgs and 'share-card' not in og_imgs[0]:
                img_url = og_imgs[0]
            else:
                other_imgs = re.findall(r'https://files\.sikayetvar\.com/complaint/[^\s\"\'<>]+\.(?:jpg|png|webp|jpeg)', html)
                if other_imgs:
                    img_url = other_imgs[0]

        if img_url:
            img_req = urllib.request.Request(img_url, headers=HEADERS)
            img_data = urllib.request.urlopen(img_req, timeout=10).read()
            if len(img_data) > 1000:
                with open(dest_path, 'wb') as f:
                    f.write(img_data)
                print(f"[DOWNLOADED] {filename} from {img_url} ({len(img_data)} bytes)")
                results[filename] = True
            else:
                print(f"[WARN TOO SMALL] {filename} from {img_url}")
                results[filename] = False
        else:
            print(f"[NOT FOUND] No image for {brand}/{model_slug}")
            results[filename] = False
    except Exception as e:
        print(f"[ERROR] {brand}/{model_slug}: {e}")
        results[filename] = False

    time.sleep(0.3)

print("\n--- SUMMARY ---")
downloaded_count = sum(1 for v in results.values() if v)
print(f"Total: {downloaded_count} / {len(MODELS_TO_FETCH)} images downloaded in {CARS_DIR}")
