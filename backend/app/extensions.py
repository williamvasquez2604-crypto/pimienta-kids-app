"""Extensiones Flask + Base declarativa compartida."""
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base declarativa común para todos los modelos."""
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()