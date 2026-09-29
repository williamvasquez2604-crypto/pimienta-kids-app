# Pimienta Kids App 🌶️

Catálogo web público + Panel administrativo privado para **Pimienta Kids** (WAWALAND PERU E.I.R.L.).

> **Modelo de negocio:** Catálogo digital con conversión a WhatsApp. SIN pasarela de pago.

## 🛠️ Stack

| Capa | Tecnología |
|---|---|
| Backend | Flask 3.0 + SQLAlchemy 2.0 + Alembic |
| Frontend | React 18 + Vite 5 + Tailwind CSS 3 |
| Base de datos | MySQL 8 (utf8mb4) |
| Infraestructura | Docker + Docker Compose |
| Producción | Nginx + Gunicorn + Let's Encrypt (pendiente) |

## 🚀 Levantar el proyecto (dev)

```bash
# Clonar
git clone git@github.com:williamvasquez2604-crypto/pimienta-kids-app.git
cd pimienta-kids-app

# Configurar variables de entorno
cp .env.example .env
# Editar .env y poner SECRET_KEY real + passwords

# Levantar los 3 contenedores
docker compose up -d

# Verificar
docker compose ps
curl http://192.168.1.4:5000/api/health

