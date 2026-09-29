"""Catálogo: categorías, productos, imágenes y log de vistas."""
from datetime import datetime

from sqlalchemy import (
    BigInteger, Boolean, DateTime, Enum, ForeignKey, Index, Integer,
    JSON, Numeric, String, Text, UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import (
    Base, FullTimestampMixin, SoftDeleteMixin, TimestampMixin, utcnow,
)


class Category(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(80), nullable=False)
    slug: Mapped[str] = mapped_column(String(100), nullable=False)
    tipo: Mapped[str] = mapped_column(
        Enum("tela", "prenda", name="category_tipo_enum"), nullable=False
    )
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    orden: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    products: Mapped[list["Product"]] = relationship(back_populates="categoria")

    __table_args__ = (
        UniqueConstraint("tipo", "slug", name="uq_category_tipo_slug"),
    )


class Product(Base, FullTimestampMixin, SoftDeleteMixin):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    slug: Mapped[str] = mapped_column(String(180), nullable=False)
    tipo: Mapped[str] = mapped_column(
        Enum("tela", "prenda", name="product_tipo_enum"), nullable=False
    )
    categoria_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), nullable=False
    )
    color: Mapped[str | None] = mapped_column(String(60), nullable=True)
    estado_stock: Mapped[str] = mapped_column(
        Enum("disponible", "poco", "agotado", name="product_stock_enum"),
        default="disponible", nullable=False,
    )
    descripcion: Mapped[str | None] = mapped_column(Text, nullable=True)
    cantidad: Mapped[int | None] = mapped_column(Integer, nullable=True)
    genero: Mapped[str | None] = mapped_column(
        Enum(
            "nino", "nina", "bebe", "hombre", "dama", "unisex",
            name="product_genero_enum",
        ),
        nullable=True,
    )
    tallas: Mapped[list | None] = mapped_column(JSON, nullable=True)
    precio: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    mostrar_precio: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    peso_medida: Mapped[str | None] = mapped_column(String(60), nullable=True)
    mostrar_peso: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    vistas_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    activo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    categoria: Mapped["Category"] = relationship(back_populates="products")
    images: Mapped[list["Image"]] = relationship(
        back_populates="producto", cascade="all, delete-orphan"
    )
    view_logs: Mapped[list["ViewLog"]] = relationship(
        back_populates="producto", cascade="all, delete-orphan"
    )

    __table_args__ = (
        UniqueConstraint("tipo", "slug", name="uq_product_tipo_slug"),
        Index("idx_products_tipo_activo", "tipo", "activo"),
        Index("idx_products_categoria", "categoria_id"),
        Index("idx_products_creado", "creado_en"),
    )


class Image(Base, TimestampMixin):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    producto_id: Mapped[int | None] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=True
    )
    contexto: Mapped[str] = mapped_column(
        Enum(
            "producto", "hero", "oferta", "promo_modal",
            name="image_contexto_enum",
        ),
        nullable=False,
    )
    url_original: Mapped[str] = mapped_column(String(500), nullable=False)
    url_grid: Mapped[str] = mapped_column(String(500), nullable=False)
    url_thumb: Mapped[str] = mapped_column(String(500), nullable=False)
    alt: Mapped[str | None] = mapped_column(String(200), nullable=True)
    orden: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    producto: Mapped["Product | None"] = relationship(back_populates="images")


class ViewLog(Base):
    __tablename__ = "view_logs"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    producto_id: Mapped[int] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"), nullable=False
    )
    ip_hash: Mapped[str] = mapped_column(String(64), nullable=False)
    session_id: Mapped[str] = mapped_column(String(64), nullable=False)
    user_agent: Mapped[str | None] = mapped_column(String(300), nullable=True)
    creado_en: Mapped[datetime] = mapped_column(
        DateTime, default=utcnow, nullable=False
    )

    producto: Mapped["Product"] = relationship(back_populates="view_logs")

    __table_args__ = (
        UniqueConstraint(
            "producto_id", "ip_hash", "session_id", name="uq_view_log"
        ),
    )