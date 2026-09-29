"""Modelos de usuarios, permisos y su relación N:M."""
from datetime import datetime

from sqlalchemy import (
    Boolean, DateTime, Enum, ForeignKey, Index, Integer,
    String, Text, UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, FullTimestampMixin, TimestampMixin, utcnow


class User(Base, FullTimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    telefono: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    rol_base: Mapped[str] = mapped_column(
        Enum("root", "dueno", "operativo", name="user_rol_base_enum"),
        nullable=False,
    )
    plantilla_permisos: Mapped[str] = mapped_column(String(60), nullable=False)
    estado: Mapped[str] = mapped_column(
        Enum("activo", "inactivo", name="user_estado_enum"),
        default="activo", nullable=False,
    )
    totp_secret: Mapped[str | None] = mapped_column(String(255), nullable=True)
    debe_cambiar_password: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    intentos_fallidos: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    bloqueado_hasta: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    ultimo_login: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    permissions: Mapped[list["UserPermission"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    __table_args__ = (Index("idx_users_estado", "estado"),)


class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    codigo: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(120), nullable=False)
    categoria: Mapped[str] = mapped_column(String(60), nullable=False)
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)


class UserPermission(Base):
    __tablename__ = "user_permissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey("permissions.id", ondelete="CASCADE"), nullable=False
    )
    asignado_en: Mapped[datetime] = mapped_column(
        DateTime, default=utcnow, nullable=False
    )

    user: Mapped["User"] = relationship(back_populates="permissions")
    permission: Mapped["Permission"] = relationship()

    __table_args__ = (
        UniqueConstraint("user_id", "permission_id", name="uq_user_permission"),
    )