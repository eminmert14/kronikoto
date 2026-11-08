"""Önem seviyesi ve onarım maliyeti hesapları.

Kullanıcı Belirlemeleri:
- 10.000 TL'ye kadar: Düşük (0 - 10.000 TL)
- 30.000 TL'ye kadar: Orta (10.000 - 30.000 TL)
- 80.000 TL'ye kadar: Yüksek (30.000 - 80.000 TL)
- 80.000 TL üstü: Çok Yüksek (80.000 TL+)
"""

SEVERITY_ORDER = ["dusuk", "orta", "yuksek", "cok_yuksek"]
SEVERITY_WEIGHT = {"dusuk": 0.3, "orta": 1.0, "yuksek": 2.0, "cok_yuksek": 3.0}


def severity_from_cost(avg_cost_tl: float) -> str:
    """10.000 düşük, 30.000 orta, 80.000 yüksek, gerisi çok yüksek."""
    if avg_cost_tl <= 10_000:
        return "dusuk"
    if avg_cost_tl <= 30_000:
        return "orta"
    if avg_cost_tl <= 80_000:
        return "yuksek"
    return "cok_yuksek"


def fault_severity(fault) -> str:
    if fault.severity_override:
        # Eğer eski 'kritik' kaldıysa 'cok_yuksek'e çevir
        if fault.severity_override == "kritik":
            return "cok_yuksek"
        return fault.severity_override
    return severity_from_cost(float(fault.avg_repair_cost_tl))


def frequency_factor(report_count: int) -> float:
    if report_count > 50:
        return 1.0
    if report_count >= 20:
        return 0.7
    if report_count >= 5:
        return 0.4
    return 0.2
