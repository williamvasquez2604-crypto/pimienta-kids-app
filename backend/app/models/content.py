"""Contenido del sitio: ofertas, promo modals y testimonios."""
from datetime import datetime

from sqlalchemy import (
    Boolean, DateTime, Enum, ForeignKey, Integer, String, Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, TimestampMixin


class Offer(Base, TimestampMixin):
    __tablename__ = "offers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)
    imagen_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    url_redireccion: Mapped[str | None] = mapped_column(String(500), nullable=True)
    descuento_porcentaje: Mapped[int | None] = mapped_column(Integer, nullable=True)
    fecha_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    fecha_fin: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class PromoModal(Base, TimestampMixin):
    __tablename__ = "promo_modals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    mensaje: Mapped[str] = mapped_column(Text, nullable=False)
    imagen_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    texto_eta: Mapped[str | None] = mapped_column(String(60), nullable=True)
    url_eta: Mapped[str | None] = mapped_column(String(500), nullable=True)
    fecha_inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    fecha_fin: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    delay_segundos: Mapped[int] = mapped_column(Integer, default=8, nullable=False)
    una_vez_por_session: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


class Testimonial(Base, TimestampMixin):
    __tablename__ = "testimonials"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    cliente_nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    calificacion: Mapped[int] = mapped_column(Integer, nullable=False)
    texto: Mapped[str] = mapped_column(Text, nullable=False)
    imagen_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    producto_id: Mapped[int | None] = mapped_column(
        ForeignKey("products.id", ondelete="SET NULL"), nullable=True
    )
    estado: Mapped[str] = mapped_column(
        Enum(
            "pendiente", "aprobado", "rechazado",
            name="testimonial_estado_enum",
        ),
        default="pendiente", nullable=False,
    )
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)