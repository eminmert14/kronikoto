import uuid
from datetime import datetime

from sqlalchemy import (JSON, Boolean, DateTime, Float, ForeignKey, Integer, Numeric,
                        SmallInteger, String, Text, UniqueConstraint, Uuid, func)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


def _uuid() -> uuid.UUID:
    return uuid.uuid4()


class Brand(Base):
    __tablename__ = "brands"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    country: Mapped[str | None] = mapped_column(String(100))
    logo_url: Mapped[str | None] = mapped_column(Text)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    models: Mapped[list["CarModel"]] = relationship(back_populates="brand")


class CarModel(Base):
    __tablename__ = "models"
    __table_args__ = (UniqueConstraint("brand_id", "name", "year_start"),)
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    brand_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("brands.id"), index=True)
    name: Mapped[str] = mapped_column(String(150))
    # sedan | hatchback | suv | station | coupe | kombi
    body_type: Mapped[str] = mapped_column(String(50), index=True)
    year_start: Mapped[int] = mapped_column(SmallInteger)
    year_end: Mapped[int | None] = mapped_column(SmallInteger)  # NULL = hâlâ üretimde
    comfort_score: Mapped[float] = mapped_column(Float, default=7.0)  # Gerçekçi konfor puanı (10 üzerinden)
    sahibinden_slug: Mapped[str | None] = mapped_column(String(100))  # sahibinden.com kategori slug
    arabam_slug: Mapped[str | None] = mapped_column(String(100))       # arabam.com kategori slug
    tags: Mapped[list] = mapped_column(JSON, default=list)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    brand: Mapped[Brand] = relationship(back_populates="models")
    variants: Mapped[list["Variant"]] = relationship(back_populates="model")
    trim_packages: Mapped[list["TrimPackage"]] = relationship(back_populates="model", cascade="all, delete-orphan")


class TrimPackage(Base):
    """Donanım Paketleri (Düşük / Orta / Premium Seviye)."""
    __tablename__ = "trim_packages"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    model_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("models.id"), index=True)
    name: Mapped[str] = mapped_column(String(100))        # örn. "Joy", "Touch", "Icon"
    level: Mapped[str] = mapped_column(String(50))       # "dusuk", "orta", "premium"
    summary: Mapped[str | None] = mapped_column(String(255))
    features: Mapped[list] = mapped_column(JSON, default=list)
    model: Mapped[CarModel] = relationship(back_populates="trim_packages")


class Engine(Base):
    __tablename__ = "engines"
    __table_args__ = (UniqueConstraint("code", "label"),)
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    code: Mapped[str] = mapped_column(String(50))              # K9K, EA211...
    label: Mapped[str] = mapped_column(String(100))            # 1.5 dCi 110 HP
    fuel_type: Mapped[str] = mapped_column(String(20), index=True)  # benzin|dizel|lpg|hibrit|elektrik
    displacement_cc: Mapped[int | None] = mapped_column(Integer)
    power_hp: Mapped[int | None] = mapped_column(SmallInteger)
    torque_nm: Mapped[int | None] = mapped_column(SmallInteger)
    technology: Mapped[str | None] = mapped_column(String(100))


class Transmission(Base):
    __tablename__ = "transmissions"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    type: Mapped[str] = mapped_column(String(20), index=True)  # manuel|otomatik|dct|cvt|amt
    label: Mapped[str] = mapped_column(String(100), unique=True)
    speeds: Mapped[int | None] = mapped_column(SmallInteger)
    manufacturer: Mapped[str | None] = mapped_column(String(100))


class Variant(Base):
    """Model x Motor x Şanzıman x Yıl aralığı."""
    __tablename__ = "variants"
    __table_args__ = (UniqueConstraint("model_id", "engine_id", "transmission_id", "year_start"),)
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    model_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("models.id"), index=True)
    engine_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("engines.id"), index=True)
    transmission_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("transmissions.id"), index=True)
    year_start: Mapped[int] = mapped_column(SmallInteger)
    year_end: Mapped[int | None] = mapped_column(SmallInteger)
    trim_level: Mapped[str | None] = mapped_column(String(100))
    price_new_tl: Mapped[float | None] = mapped_column(Numeric(12, 2))
    used_price_tl: Mapped[float | None] = mapped_column(Numeric(12, 2))  # ikinci el tahmini (bütçe filtresi)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    model: Mapped[CarModel] = relationship(back_populates="variants")
    engine: Mapped[Engine] = relationship()
    transmission: Mapped[Transmission] = relationship()


class FaultReport(Base):
    """Kapsam: engine_id / transmission_id / model_id'den dolu olanların HEPSİ eşleşmeli."""
    __tablename__ = "fault_reports"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    engine_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("engines.id"), index=True)
    transmission_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("transmissions.id"), index=True)
    model_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("models.id"), index=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    # mekanik | elektronik | guvenlik | konfor | yazilim_multimedya
    category: Mapped[str] = mapped_column(String(50), index=True)
    avg_repair_cost_tl: Mapped[float] = mapped_column(Numeric(10, 2))
    max_repair_cost_tl: Mapped[float | None] = mapped_column(Numeric(10, 2))
    severity_override: Mapped[str | None] = mapped_column(String(20))  # güvenlik riski için elle yükseltme
    occurrence_km_start: Mapped[int | None] = mapped_column(Integer)
    occurrence_km_end: Mapped[int | None] = mapped_column(Integer)
    report_count: Mapped[int] = mapped_column(Integer, default=1)
    sources: Mapped[list] = mapped_column(JSON, default=list)
    checklist: Mapped[list] = mapped_column(JSON, default=list)  # ekspertizde bakılacak noktalar
    verified: Mapped[bool] = mapped_column(Boolean, default=False)  # False = taslak
    last_updated: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())


class SoftwareMod(Base):
    __tablename__ = "software_mods"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    engine_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("engines.id"), index=True)
    transmission_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("transmissions.id"))
    mod_type: Mapped[str] = mapped_column(String(30))  # stage1|stage2|eco_tune|tcu_tune|multimedya|diger
    is_recommended: Mapped[bool | None] = mapped_column(Boolean)  # NULL = belirsiz
    hp_before: Mapped[int | None] = mapped_column(SmallInteger)
    hp_after: Mapped[int | None] = mapped_column(SmallInteger)
    nm_before: Mapped[int | None] = mapped_column(SmallInteger)
    nm_after: Mapped[int | None] = mapped_column(SmallInteger)
    risk_note: Mapped[str | None] = mapped_column(Text)
    approx_cost_tl: Mapped[float | None] = mapped_column(Numeric(10, 2))
    verified: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    comments: Mapped[list["SoftwareModComment"]] = relationship(back_populates="mod")


class SoftwareModComment(Base):
    __tablename__ = "software_mod_comments"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    mod_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("software_mods.id", ondelete="CASCADE"), index=True)
    author_name: Mapped[str | None] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(Text)
    km_at_mod: Mapped[int | None] = mapped_column(Integer)
    outcome: Mapped[str | None] = mapped_column(String(20))  # sorunsuz|sorunlu|geri_alindi
    status: Mapped[str] = mapped_column(String(20), default="pending")  # moderasyon
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    mod: Mapped[SoftwareMod] = relationship(back_populates="comments")

class UserComment(Base):
    __tablename__ = "user_comments"
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=_uuid)
    variant_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("variants.id", ondelete="CASCADE"), index=True)
    author_name: Mapped[str] = mapped_column(String(100), default="Anonim Sürücü")
    ownership_status: Mapped[str | None] = mapped_column(String(50))  # Sahibiyim, Eski Sahibiyim, Test Ettim
    mileage_km: Mapped[int | None] = mapped_column(Integer)
    rating: Mapped[int] = mapped_column(SmallInteger, default=5)  # 1-5 yıldız
    recommend: Mapped[bool] = mapped_column(Boolean, default=True)  # Tavsiye ediyor mu?
    body: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
