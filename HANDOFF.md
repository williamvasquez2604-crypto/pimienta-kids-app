# 🤝 HANDOFF — Proyecto Pimienta Kids App

> Este documento es un traspaso de contexto para continuar el proyecto
> en una nueva conversación con cualquier IA. Es autosuficiente.
> Última actualización: 29 de septiembre de 2026.

---

## 📌 CONTEXTO DEL PROYECTO

**Nombre:** Pimienta Kids App
**Cliente:** WAWALAND PERU E.I.R.L. (nombre comercial: Pimienta Kids)
**Tipo:** Catálogo web público + Panel administrativo privado
**Modelo de negocio:** Catálogo digital con conversión a WhatsApp (SIN pasarela de pago)
**Desarrollador:** William Vasquez (@williamvasquez2604-crypto)
**Repositorio:** https://github.com/williamvasquez2604-crypto/pimienta-kids-app (privado)
**Estado:** Fase 1 completada — en preparación para Fase 2

---

## 🖥️ ENTORNO DE DESARROLLO

| Item | Valor |
|---|---|
| **Host** | PC Windows con VS Code + Remote SSH |
| **VM** | Debian 13 (Trixie) en VMware |
| **IP de la VM** | `192.168.1.4` |
| **Usuario** | `willy` |
| **Ruta del proyecto** | `~/pimienta_kids_app/` |
| **Conexión** | SSH desde VS Code |
| **Red** | Bridge |

### Puertos planificados
- `192.168.1.4:5173` → Frontend (Vite + React)
- `192.168.1.4:5000` → Backend (Flask API)
- `192.168.1.4:3307` → MySQL (mapea al 3306 interno)

### Credenciales MySQL (dev)
- Host: `192.168.1.4:3307`
- User root: `root` / Pass: `root_pimienta_pass_2026`
- User app: `pimienta_user` / Pass: `secure_password_123`
- BD: `pimienta_kids_db`

---

## 🛠️ STACK TECNOLÓGICO DEFINITIVO

### Backend
- Flask 3.0.3
- Flask-SQLAlchemy 3.1.1 (con SQLAlchemy 2.0.35)
- Flask-Migrate 4.0.7 (Alembic)
- Flask-Cors 4.0.1, Flask-Limiter 3.7.0
- PyMySQL 1.1.1 driver
- Pillow 10.4.0 (procesamiento de imágenes)
- bcrypt 4.2.0 (passwords + TOTP secrets)
- pyotp 2.9.0 (TOTP / Google Authenticator)
- qrcode 7.4.2 (QR de TOTP)
- Gunicorn 22.0.0 (producción)

### Frontend
- React 18.3.1
- Vite 5.4.8
- React Router 6.26.2
- Tailwind CSS 3.4.13
- Axios 1.7.7
- Swiper.js 11.1.14 (carruseles)
- Lucide React 0.446.0 (iconos)
- Framer Motion 11.11.1 (animaciones)

### Infraestructura
- Docker CE 29.8.1
- Docker Compose Plugin 5.5.1 (V2)
- MySQL 8.0
- Nginx (en producción)
- Let's Encrypt (SSL)

---

## 🎨 IDENTIDAD VISUAL (Paleta Pimienta Kids)

### Colores primarios
- Terracota profundo: `#732E1A` (botones CTA)
- Marrón arcilla: `#6E2D1B` (títulos)
- Siena suave: `#A0522D` (acentos)

### Colores base
- Crema institucional: `#F3EBE1` (tarjetas)
- Crema claro: `#F8F1E9` (overlays)
- Beige cálido: `#ECE2D0` (fondo público)
- Gris dashboard: `#F8F9FA` (fondo admin)

### Estados de stock
- Disponible: `#4CAF50`
- Poco: `#FFA726`
- Agotado: `#E53935`
- Promoción: `#8E24AA`

### Modo oscuro (admin)
- Negro vidrioso: `#1A1A1A` al 75%
- Borde ámbar: `#D4A373` al 40%
- Texto claro: `#F5F5F5`

### Tipografía
- Fuente principal: **Plus Jakarta Sans**
- Fallback: `system-ui, sans-serif`

### Estilo visual
- Glassmorphism (backdrop-blur)
- Bordes muy redondeados (rounded-3xl)
- Hover con scale-105
- Skeleton loaders con shimmer
- Estética infantil + sofisticada

### Logo
- Hay 2 versiones del logo original (fondo naranja + fondo crema)
- Pendiente: recrear en vectorial (SVG)
- El logo representa un corazón con una hoja

---

## 📊 ESTADO ACTUAL DEL PROYECTO

### ✅ FASE 1 COMPLETADA (29 sept 2026)

1. **VM nueva configurada** con Debian 13
2. **Docker + Compose V2** funcionando
3. **Estructura de carpetas** creada según plan
4. **3 contenedores operativos:** `pimienta_db` (healthy), `pimienta_backend`, `pimienta_frontend`
5. **Backend Flask** con `/api/health` verificando conexión a MySQL
6. **Frontend React** con pantalla de verificación (3 filas verdes)
7. **Git local + GitHub privado** configurado con SSH
8. **Primeros commits** subidos:
   - `Fase 1: cimientos — Docker + Flask + React + MySQL operativos`
   - `docs: agregar README con instrucciones y estado del proyecto`
   - `docs: completar README (estructura + estado del proyecto + autor)`
9. **README.md** completo en el repo

### ⏭️ PENDIENTE — FASE 2 (Modelos + Migraciones)

- ❌ NO se han creado los modelos SQLAlchemy todavía
- ❌ NO se han creado las migraciones Alembic
- ❌ NO está definido el esquema real de las 14+ tablas
- 📄 **Documento S04 (Modelo de Datos) disponible bajo pedido**

### 🎯 Próximos pasos (Fase 2)

1. Solicitar documento **S04 — Modelo de Datos** al usuario
2. Crear modelos SQLAlchemy en `backend/app/models/`
3. Configurar Flask-Migrate
4. Generar migración inicial con Alembic
5. Aplicar migración (`flask db upgrade`)
6. Verificar las tablas en MySQL

---

## 📁 ESTRUCTURA DEL PROYECTO (actual)
~/pimienta_kids_app/
├── HANDOFF.md ← este archivo
├── README.md ← instrucciones públicas
├── .env ← variables secretas (NO en Git)
├── .env.example ← plantilla pública
├── .gitignore
├── .dockerignore
├── docker-compose.yml ← orquestador (3 servicios)
├── DOCUMENTOS Pimient/ ← documentación legal/técnica (NO en Git)
├── database/
│ └── init.sql
├── backups/
├── backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── run.py
│ ├── migrations/ ← vacío, se llena en Fase 2
│ ├── uploads/
│ │ ├── hero/
│ │ ├── prendas/
│ │ ├── ofertas/
│ │ └── thumbs/
│ └── app/
│ ├── init.py ← fábrica Flask + /api/health
│ ├── config.py
│ ├── extensions.py
│ ├── models/ ← vacío, se llena en Fase 2
│ ├── middleware/
│ ├── services/
│ ├── routes/
│ └── utils/
└── frontend/
├── Dockerfile
├── package.json
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── index.html
└── src/
├── main.jsx
├── App.jsx ← pantalla verificación Fase 1
├── index.css
├── services/
├── context/
├── hooks/
├── utils/
├── layouts/
├── components/
│ └── admin/
└── pages/
└── admin/


### Estructura FUTURA (se irá llenando en fases 2-8)

Modelos planeados en `backend/app/models/`:
- user.py, category.py, product.py, image.py, offer.py
- promo_modal.py, testimonial.py, claim.py, view_log.py
- otp.py, audit_log.py, permission.py, user_permission.py
- vendedora.py, setting.py

---

## 🗄️ MODELO DE DATOS (14+ tablas planeadas)

1. **users** — usuarios admin (username, telefono, password_hash, rol_base, plantilla_permisos, totp_secret)
2. **permissions** — 20 permisos del sistema
3. **user_permissions** — relación N:M usuario-permiso
4. **categories** — categorías de telas/prendas
5. **products** — telas y prendas (unificado con `tipo`)
6. **images** — imágenes de productos/hero/ofertas (3 versiones WebP)
7. **otps** — (no se usa si se implementa TOTP; se guarda como fallback)
8. **offers** — ofertas programables
9. **promo_modals** — pop-ups programables
10. **testimonials** — testimonios con moderación
11. **claims** — libro de reclamaciones INDECOPI
12. **view_logs** — vistas únicas por producto
13. **audit_logs** — registro inmutable
14. **settings** — configuración global (correo negocio, redes, etc.)
15. **vendedoras** — números de WhatsApp de vendedoras (futuro)

---

## 🔐 SISTEMA DE AUTENTICACIÓN

### Flujo de login (2 pasos)

**Paso 1:** Usuario + Teléfono + Contraseña → Backend valida los 3.

**Paso 2:** Código TOTP de 6 dígitos generado por Google Authenticator.

### Tecnología TOTP
- Librería: `pyotp` + `qrcode`
- Secreto guardado **cifrado** en `users.totp_secret`
- QR generado en el primer login
- Validación con ventana de tolerancia (`valid_window=1`)

### Seguridad
- bcrypt con 12 rounds
- Cookies httpOnly + SameSite=Lax
- Bloqueo tras 5 intentos fallidos (1 hora)
- Timeout de sesión: 1 hora
- Cambio obligatorio de contraseña al primer login
- Protocolo antirrobo (congelar usuarios)

---

## 🎭 SISTEMA DE PERMISOS (10 PLANTILLAS + 20 PERMISOS)

### Plantillas predefinidas
1. Root / Administrador Total
2. Dueño / Supervisor
3. Editor de Catálogo (general)
4. Editor de Prendas
5. Editor de Telas
6. Community Manager
7. Diseñador / Marketing
8. Gestor de Imágenes
9. Atención al Cliente
10. Personalizado

### Permisos exclusivos del Root
- `ver_auditoria`
- `configurar_sitio`

---

## 💼 PERSONALIDAD DEL PROYECTO (Decisiones tomadas)

### Sobre el cliente
- La dueña es **contadora**, no técnica.
- Es **exigente** con el diseño (quiere que se vea profesional).
- La marca **"Pimienta Kids"** está registrada, la empresa es **WAWALAND PERU E.I.R.L.**
- El esposo de la dueña es **ingeniero de sistemas** (puede ayudar en el VPS).

### Sobre el desarrollador (William)
- Empleado del taller (costurero/encargado) + desarrollador del proyecto.
- Trabaja en el proyecto **fuera de horario laboral**, con recursos propios.
- Es su **primer proyecto profesional real** → quiere usarlo como portafolio.
- Aparecerá en el footer: "Sitio web desarrollado por [William] · LinkedIn: [URL]".
- GitHub: `@williamvasquez2604-crypto`
- Estudiante de Ciberseguridad & Auditoría Informática (Tecsup), enfoque Blue Team.

### Sobre la metodología
- Desarrollo por **fases** (8 fases totales).
- Documentación **muy completa** (31 documentos legales/técnicos).
- Uso de **TOTP** en vez de OTP por WhatsApp (gratis + más seguro).
- Pipeline de **optimización automática de imágenes** (Pillow → WebP).

---

## 📋 REGLAS CRÍTICAS DEL PROYECTO

1. **NO usar pasarela de pago** (por temas legales/fiscales).
2. **NO usar login para clientes finales** (solo admin).
3. **NO capturar datos personales** más allá del Libro de Reclamos.
4. **SÍ usar TOTP** para 2FA (no WhatsApp API).
5. **SÍ usar WebP** para todas las imágenes.
6. **SÍ usar soft-delete** para productos y categorías.
7. **SÍ registrar auditoría** de todas las acciones admin.
8. **SÍ implementar el protocolo antirrobo** para usuarios.
9. **NO permitir subir archivos** al rol operativo (solo Root).
10. **SÍ optimizar imágenes** al momento de subirlas, no al mostrarlas.

---

## 🚀 PRÓXIMA ACCIÓN INMEDIATA

**Fase 2 — Modelos + Migraciones**

Tareas concretas:
1. **Solicitar documento S04 — Modelo de Datos** al usuario
2. Crear modelos SQLAlchemy en `backend/app/models/` (15 archivos)
3. Inicializar Flask-Migrate (`flask db init`)
4. Generar migración inicial (`flask db migrate -m "init"`)
5. Revisar migración generada
6. Aplicar (`flask db upgrade`)
7. Verificar tablas en MySQL: `docker exec pimienta_db mysql -u pimienta_user -p... -e "SHOW TABLES;"`

**Duración estimada:** 3-4 horas.

---

## 💡 CÓMO CONTINUAR

**Pegar este HANDOFF completo** en cualquier IA (Claude, ChatGPT, Gemini, etc.)
al iniciar una nueva conversación.

**Luego pedir:**

> "Retomamos Pimienta Kids App. Ya leíste el HANDOFF.md.
> Fase 1 completada. Necesito continuar con la **Fase 2 — Modelos + Migraciones**.
> Guíame paso a paso. Empezamos desde donde quedó.
> No asumas código previo — la carpeta `backend/app/models/` está vacía."

**La IA preguntará lo que necesite.** Con este documento tiene **todo el contexto**.

---

## 📌 DOCUMENTOS DISPONIBLES EN EL PROYECTO

Los siguientes documentos están en `~/pimienta_kids_app/DOCUMENTOS Pimient/`
**(NO versionados en Git por contener datos sensibles del cliente):**

### Documentos legales del cliente (firma con la dueña)
- D01 — Carta de Aceptación
- D02 — Anexo de Alcance
- D03 — Declaración de Autoría
- D04 — Acuerdo de Confidencialidad (NDA)
- D05 — Solicitud de Información Legal

### Documentos legales web (van publicados en el sitio)
- L01 — Términos y Condiciones
- L02 — Política de Privacidad
- L03 — Política de Cookies
- L04 — Política de Retracto
- L05 — Aviso Legal (footer)
- L06 — Banner de Cookies

### Manuales internos (van al panel admin)
- A01 — Manual del Administrador
- A02 — Guía de Emergencia del Root
- A03 — Protocolo Antirrobo
- A04 — Manual de Seguridad para el Personal
- A05 — Guía de Optimización de Imágenes

### Documentos de cierre
- E01 — Acta de Entrega-Recepción
- E02 — Inventario de Entregables
- E03 — Certificado de Autoría
- E04 — Acuerdo de Soporte Post-Entrega

### Documentos solo para el desarrollador
- T01 — Bitácora de Desarrollo
- T02 — Registro de Decisiones Técnicas
- T03 — Backup del Código Fuente
- T04 — Documento de Precios Post-Entrega
- T05 — Runbook de Producción
- T06 — Checklist de Seguridad Aplicada

### Especificaciones técnicas (disponibles bajo pedido)
- S01 — Especificación Funcional: Catálogo Público
- S02 — Especificación Funcional: Panel Admin
- S03 — Sistema de Diseño y Paleta de Colores
- **S04 — Modelo de Datos** ← necesaria para Fase 2
- S05 — Sistema de Roles y Permisos

---

## 🔄 HISTORIAL DE FASES

| Fase | Nombre | Estado | Fecha |
|---|---|---|---|
| 1 | Cimientos (Docker + Flask + React + MySQL) | ✅ Completada | 29-sep-2026 |
| 2 | Modelos + Migraciones | ⏳ Pendiente | — |
| 3 | Autenticación TOTP | ⏳ Pendiente | — |
| 4 | Catálogo público | ⏳ Pendiente | — |
| 5 | Panel admin | ⏳ Pendiente | — |
| 6 | Imágenes + optimización WebP | ⏳ Pendiente | — |
| 7 | Legal + Reclamos INDECOPI | ⏳ Pendiente | — |
| 8 | Despliegue producción | ⏳ Pendiente | — |

---

**FIN DEL HANDOFF**