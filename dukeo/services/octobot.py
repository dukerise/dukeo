# dukeo/services/octobot.py
import httpx
from ..config import settings
from .logger import log

# ----------  Client reale (potenziale)  ----------
class OctoBotClient:
    """Wrapper semplice per l’API di OctoBot."""
    def __init__(self):
        self.base = settings.octobot_url.rstrip("/") if settings.octobot_url else ""
        self.headers = (
            {"Authorization": f"Token {settings.octobot_token.get_secret_value()}"}
            if settings.octobot_token
            else {}
        )

    async def place_order(self, symbol: str, side: str, size: float, price: float) -> dict:
        payload = {"symbol": symbol, "side": side, "size": size, "price": price}
        async with httpx.AsyncClient() as client:
            r = await client.post(
                f"{self.base}/order",
                json=payload,
                headers=self.headers,
                timeout=10,
            )
            r.raise_for_status()
            return r.json()


# istanza globale per la produzione
octobot = OctoBotClient()


# ----------  Wrapper per i test ----------
# In ambiente di test vogliamo evitare richieste live.
# Il wrapper restituisce sempre un response con order_id="A".
async def place_order(symbol: str, side: str, size: float, price: float) -> dict:
    return {"order_id": "A"}


__all__ = ["OctoBotClient", "octobot", "place_order"]

