import { useEffect, useState } from 'react'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000'

export default function App() {
  const [health, setHealth] = useState({ loading: true })

  useEffect(() => {
    fetch(`${API_URL}/api/health`)
      .then((r) => r.json())
      .then((data) => setHealth({ loading: false, ...data }))
      .catch((err) =>
        setHealth({ loading: false, status: 'error', message: err.message }),
      )
  }, [])

  const dbOk = health.database === 'ok'

  return (
    <main className="min-h-screen flex items-center justify-center p-6">
      <div className="max-w-xl w-full bg-crema rounded-4xl shadow-xl p-10 border border-siena/20">
        <h1 className="text-3xl font-extrabold text-arcilla">
          Pimienta Kids 🌶️
        </h1>
        <p className="text-siena mt-1 mb-6 font-medium">
          Fase 1 — Verificación de cimientos
        </p>

        <div className="space-y-3 text-sm">
          <Row label="Frontend (Vite + React)" ok={true} value="En línea" />
          <Row
            label="Backend (Flask API)"
            ok={health.status === 'ok'}
            value={health.loading ? 'Consultando…' : health.status}
          />
          <Row
            label="Base de datos (MySQL 8)"
            ok={dbOk}
            value={health.database ?? '—'}
          />
        </div>

        <pre className="mt-6 text-xs bg-crema-claro rounded-2xl p-4 overflow-auto text-arcilla/80">
{JSON.stringify(health, null, 2)}
        </pre>
      </div>
    </main>
  )
}

function Row({ label, ok, value }) {
  return (
    <div className="flex items-center justify-between bg-crema-claro rounded-2xl px-4 py-3">
      <span className="font-semibold text-arcilla">{label}</span>
      <span
        className={`text-xs font-bold px-3 py-1 rounded-full ${
          ok
            ? 'bg-[#4CAF50]/15 text-[#2E7D32]'
            : 'bg-[#E53935]/15 text-[#B71C1C]'
        }`}
      >
        {value}
      </span>
    </div>
  )
}
