# KronikOto

Araç tavsiye ve kronik arıza rehberi (şimdilik yalnızca web).

```
backend/    FastAPI + SQLAlchemy (API, şema, seed)
frontend/   Next.js 15 (App Router)
data/       MVP 50 model listesi
docs/       schema.postgres.sql (PostgreSQL DDL)
```

## Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
.\.venv\Scripts\python -m app.seed            # --reset ile sıfırdan
.\.venv\Scripts\uvicorn app.main:app --reload # http://localhost:8000/docs
```

Varsayılan veritabanı SQLite'tır (`kronikoto.db`). PostgreSQL için:

```powershell
docker compose up -d
$env:DATABASE_URL="postgresql+psycopg://kronikoto:kronikoto@localhost:5432/kronikoto"
```

## Frontend (Node.js 20+ gerekir)

```powershell
cd frontend
copy .env.example .env.local
npm install
npm run dev   # http://localhost:3000
```

## Notlar
- Seed'deki arıza ve stage kayıtları **taslaktır** (`verified=false`, arayüzde "Taslak" rozeti). Gerçek veri derlemesi sonraki adımdır.
- `km_max` filtresi arayüzde var, ilan verisi entegrasyonuna kadar API'de uygulanmaz.
- Önem seviyesi `avg_repair_cost_tl`'den hesaplanır: 0–15 bin düşük, 15–50 orta, 50–100 yüksek, 100+ kritik.
