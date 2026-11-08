from fastapi.testclient import TestClient
from app.main import app

with TestClient(app) as c:
    r = c.get('/api/v1/vehicles/search', params={'fuel_type': 'dizel', 'transmission_type': 'dct', 'exclude_brands': 'Fiat'}).json()
    print('dizel+dct:', [(x['brand'], x['name'], x['best_reliability']) for x in r])
    allm = c.get('/api/v1/vehicles/search').json()
    print('toplam model:', len(allm))
    for x in allm:
        if x['variants_count']:
            md = c.get('/api/v1/models/' + x['id']).json()
            for v in md['variants']:
                if 'DSG 7' in v['transmission'] and 'TDI' in v['engine']:
                    f = c.get('/api/v1/variants/' + v['id'] + '/faults').json()
                    print(md['name'], v['engine'], '| skor', f['variant']['reliability_score'], f['fault_summary'])
                    print([(a['title'], a['severity']) for a in f['faults']], 'stage:', len(f['software_mods']))
                    raise SystemExit
