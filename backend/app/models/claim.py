"""Libro de Reclamaciones INDECOPI."""
from sqlalchemy import (
    Enum, Index, Integer, Numeric, String, Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, FullTimestampMixin


class Claim(Base, FullTimestampMixin):
    __tablename__ = "claims"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    codigo: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    nombre_completo: Mapped[str] = mapped_column(String(150), nullable=False)
    dni: Mapped[str] = mapped_column(String(15), nullable=False)
    domicilio: Mapped[str] = mapped_column(String(250), nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False)
    tipo_bien: Mapped[str] = mapped_column(
        Enum("producto", "servicio", name="claim_tipo_bien_enum"), nullable=False
    )
    monto_reclamado: Mapped[float | None] = mapped_column(
        Numeric(10, 2), nullable=True
    )
    descripcion_bien: Mapped[str] = mapped_column(Text, nullable=False)
    tipo_reclamo: Mapped[str] = mapped_column(
        Enum("reclamo", "queja", name="claim_tipo_reclamo_enum"), nullable=False
    )
    detalle: Mapped[str] = mapped_column(Text, nullable=False)
    pedido: Mapped[str] = mapped_column(Text, nullable=False)
    estado: Mapped[str] = mapped_column(
        Enum(
            "pendiente", "en_proceso", "resuelto",
            name="claim_estado_enum",
        ),
        default="pendiente", nullable=False,
    )
    respuesta: Mapped[str | None] = mapped_column(Text, nullable=True)

    __table_args__ = (Index("idx_claims_estado", "estado"),)