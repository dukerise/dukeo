# ------------------------------------------------------------------
# dukeo/main.py – “FastAPI entry point” con metrics e health‑check
# ------------------------------------------------------------------
import uvicorn
from fastapi import FastAPI

# la libreria prometheus-fastapi-instrumentator è opzionale
# ma aggiunge la route /metrics per Prometheus
from prometheus_fastapi_instrumentator import Instrumentator

# Importiamo tutte le dipendenze che si basano su Settings
from .config import settings
from .routes import tv_webhook, telegram_listener
from .services.logger import log

# ---------------------------------------------------------------
# Creiamo la singola app FastAPI
# ---------------------------------------------------------------
app = FastAPI(title="dukeo Bot", version="0.1.0")

# Mount dei routes
app.include_router(tv_webhook.router, prefix="/tv_webhook")
app.include_router(telegram_listener.router, prefix="/telegram")

# Health‑check semplice
@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

# ---------------------------------------------------------------
# Aggiungiamo le metrics Prometheus
# ---------------------------------------------------------------
Instrumentator().instrument(app).expose(app)

# ---------------------------------------------------------------
# Uvicorn entry point (eseguito solo quando avvii il script)
# ---------------------------------------------------------------
if __name__ == "__main__":
    uvicorn.run("dukeo.main:app", host="0.0.0.0", port=8000, workers=2)
