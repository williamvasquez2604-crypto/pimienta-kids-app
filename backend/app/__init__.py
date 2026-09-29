from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import text

from .config import Config
from .extensions import db, migrate
from . import models  # noqa: F401 — registra todos los modelos en db.metadata

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    CORS(
        app,
        origins=app.config["CORS_ORIGINS"],
        supports_credentials=True,
    )
    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/api/health")
    def health():
        db_status = "ok"
        try:
            db.session.execute(text("SELECT 1"))
        except Exception as e:
            db_status = f"error: {e}"

        return jsonify(
            {
                "status": "ok",
                "service": "pimienta-kids-backend",
                "environment": app.config.get("ENV", "development"),
                "database": db_status,
            }
        )

    @app.route("/api/ping")
    def ping():
        return jsonify({"pong": True})

    return app
