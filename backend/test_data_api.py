from fastapi.testclient import TestClient
from app.main import app

with TestClient(app) as client:
    # 1. Arama testi
    res = client.get("/api/v1/vehicles/search")
    models = res.json()
    print(f"Toplam listelenen model: {len(models)}")
    print("\nÖrnek Modeller:")
    for m in models[:10]:
        print(f"  • {m['brand']} {m['name']} ({m['body_type']}) -> {m['variants_count']} varyant, En iyi skor: {m['best_reliability']}")

    # 2. Megane 4 testi
    megane = next((x for x in models if "Megane" in x["name"]), None)
    if megane:
        m_detail = client.get(f"/api/v1/models/{megane['id']}").json()
        print(f"\n{megane['brand']} {megane['name']} Varyantları ({len(m_detail['variants'])} adet):")
        for v in m_detail["variants"]:
            print(f"  - {v['engine']} + {v['transmission']} | Skor: {v['reliability_score']} | İkinci El: {v['used_price_tl']} TL")

        edc_v = next((v for v in m_detail["variants"] if "EDC 6" in v["transmission"]), None)
        if edc_v:
            report = client.get(f"/api/v1/variants/{edc_v['id']}/faults").json()
            print(f"\nDetay Arıza Raporu: {report['variant']['engine']} + {report['variant']['transmission']}")
            print(f"  Güvenilirlik Skoru: {report['variant']['reliability_score']} / 10")
            print(f"  Arıza Sayıları: {report['fault_summary']['counts']}")
            print(f"  Tahmini Masraf Aralığı: {report['fault_summary']['expected_cost_range_tl']} TL")
            print("  Kronik Sorunlar:")
            for f in report["faults"]:
                print(f"    * [{f['severity'].upper()}] {f['title']} (Ort. {f['avg_repair_cost_tl']} TL, Doğrulandı: {f['verified']})")
                print(f"      Checklist: {f['checklist']}")
                print(f"      Kaynaklar: {f['sources']}")
            print("  Stage & Yazılım Bilgisi:")
            for s in report["software_mods"]:
                print(f"    * Mod: {s['mod_type']} | Tavsiye: {s['is_recommended']} | HP: {s['hp']} | Risk: {s['risk_note']}")
                for c in s["comments"]:
                    print(f"      Yorum ({c['author']} - {c['outcome']}): {c['body']}")

    # 3. Honda Civic FC5 testi
    civic = next((x for x in models if "Civic" in x["name"]), None)
    if civic:
        c_detail = client.get(f"/api/v1/models/{civic['id']}").json()
        print(f"\n{civic['brand']} {civic['name']} Varyantları ({len(c_detail['variants'])} adet):")
        for v in c_detail["variants"]:
            print(f"  - {v['engine']} + {v['transmission']} | Skor: {v['reliability_score']}")
