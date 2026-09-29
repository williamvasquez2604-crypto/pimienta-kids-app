"""Sistema: OTP, auditoría, configuración y vendedoras."""
from datetime import datetime

from sqlalchemy import (
    Boolean, DateTime, ForeignKey, Index, Integer, JSON,
    String, Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin, utcnow


class Otp(Base, TimestampMixin):
    __tablename__ = "otps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    telefono: Mapped[str] = mapped_column(String(20), nullable=False)
    codigo_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    expira_en: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    usado: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    intentos: Mapped[int] = mapped_column(Integer, default=0, nullable=False)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    accion: Mapped[str] = mapped_column(String(60), nullable=False)
    entidad: Mapped[str] = mapped_column(String(60), nullable=False)
    entidad_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    detalles: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    ip: Mapped[str | None] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(300), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime, default=utcnow, nullable=False
    )

    __table_args__ = (
        Index("idx_audit_user", "user_id"),
        Index("idx_audit_accion", "accion"),
        Index("idx_audit_creado", "creado_en"),
    )


class Setting(Base):
    __tablename__ = "settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    clave: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    valor: Mapped[str | None] = mapped_column(Text, nullable=True)
    descripcion: Mapped[str | None] = mapped_column(String(200), nullable=True)
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime, default=utcnow, onupdate=utcnow, nullable=False
    )


class Vendedora(Base, TimestampMixin):
    __tablename__ = "vendedoras"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    whatsapp: Mapped[str] = mapped_column(String(20), nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    orden: Mapped[int] = mapped_column(Integer, default=0, nullable=False)