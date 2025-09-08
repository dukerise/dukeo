# dukeo/routes/tv_webhook.py
from fastapi import APIRouter, Request, HTTPException, status
from ..config import settings
from ..services import octobot, risk, alert
from ..models import TVSignal
from ..services.logger import log

# ❗  **no più `name=`** – FastAPI 0.109+ non lo riconosce
router = APIRouter()

@router.post("/", status_code=status.HTTP_200_OK)
async def endpoint(req: Request):
    # Validate secret (if set)
    if settings.tv_secret and req.headers.get("X-API-KEY") != settings.tv_secret.get_secret_value():
        raise HTTPException(status_code=403, detail="Invalid secret")

    payload = await req.json()
    signal = TVSignal(**payload)

    atr = risk.get_mock_atr()
    size = risk.calc_position_size(atr, settings.balance, settings.risk_per_trade)

    # Execute order via OctoBot
    order_resp = await octobot.place_order(
        signal.symbol, signal.side, size, signal.entry_price
    )

    # Notify via Telegram
    await alert.send_telegram(
        f"✅ Ordine ricevuto: {signal.symbol} {signal.side} {size:.4f}@{signal.entry_price}\nOrder ID: {order_resp['order_id']}"
    )

    log.info("Webhook processed", signal=signal.dict(), order=order_resp)
    return {"status": "received", "order_id": order_resp["order_id"]}
