"""Mixins compartidos para los modelos."""
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from ..extensions import Base  # noqa: F401 — re-exportado


def utcnow() -> datetime:
    """Timestamp actual en UTC (naive, para MySQL DATETIME)."""
    return datetime.now(timezone.utc).replace(tzinfo=None)


class TimestampMixin:
    """Agrega creado_en."""
    creado_en: Mapped[datetime] = mapped_column(
        DateTime, default=utcnow, nullable=False
    )


class FullTimestampMixin(TimestampMixin):
    """Agrega creado_en + actualizado_en (auto-update)."""
    actualizado_en: Mapped[datetime] = mapped_column(
        DateTime, default=utcnow, onupdate=utcnow, nullable=False
    )


class SoftDeleteMixin:
    """Soft-delete: eliminado_en + eliminado_por (FK users)."""
    eliminado_en: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    eliminado_por: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )