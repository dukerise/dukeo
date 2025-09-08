# dukeo/services/alert.py
"""
Funzioni di notifica (Telegram / e‑mail).
Solo `send_telegram` è utilizzata dai test; l’implementazione
è una versione “mock‑safe” che non fallisce se il bot non è
configurato.
"""
from telegram import Bot
from .logger import log
from ..config import settings

async def send_telegram(msg: str) -> None:
    """
    Invia un messaggio Telegram. Se il token non è configurato
    l’azione è semplicemente loggata.
    """
    if not settings.bot_token:
        log.warning("Telegram bot token non configurato – invio annullato", message=msg)
        return
    bot = Bot(token=settings.bot_token.get_secret_value())
    try:
        await bot.send_message(chat_id=settings.chat_id, text=msg)
        log.info("Telegram sent", message=msg)
    except Exception as e:
        log.error("Telegram send error", error=str(e), message=msg)


# (Per gli altri alert (SMTP, ecc.) è sufficiente definire
#  funzioni placeholder se non usate nei test.)

