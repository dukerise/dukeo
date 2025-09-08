import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from .config import settings
from .routes import tv_webhook, telegram_listener
from .services.logger import log

app = FastAPI(title="dukeo Bot", version="0.1.0")
app.include_router(tv_webhook.router, prefix="/tv_webhook")
app.include_router(telegram_listener.router, prefix="/telegram")

@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}

Instrumentator().instrument(app).expose(app)

if __name__ == "__main__":
    uvicorn.run("dukeo.main:app", host="0.0.0.0", port=8000, workers=2)

