# ------------------------------------------------------------------
# dukeo/config.py – pydantic‑based Settings con valori di fallback
# ------------------------------------------------------------------
from pydantic_settings import BaseSettings
from pydantic import SecretStr
# (non usiamo `os` ma l’import è comune per la lettura di env)
import os

class Settings(BaseSettings):
    # ----- Telegram --------------------------------------------------
    bot_token: SecretStr          = SecretStr("dummy_token")   # placeholder
    chat_id: int                  = 0                           # placeholder
    tv_secret: SecretStr | None   = None

    # ----- OctoBot -------------------------------------------------------
    octobot_url: str              = "http://localhost:5000"     # placeholder
    octobot_token: SecretStr | None = SecretStr("dummy_token")

    # ----- Risk -------------------------------------------------------
    sl_atr_mult: float = 1.5
    tp_atr_mult: float = 3.0
    max_dd: float = 0.20
    small_dd: float = 0.05

    # ----- SMTP ---------------------------------------------------------
    smtp_host: str | None = None
    smtp_port: int | None = None
    smtp_user: SecretStr | None = None
    smtp_pass: SecretStr | None = None

    # ----- Capital & per‑trade ------------------------------------------
    balance: float = 10_000
    risk_per_trade: float = 0.02

    class Config:
        # Caricamento da `.env` – se non presente basta i fallback
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"

# ------------------------------------------------------------------
# Instanzio Settings (tutti i moduli lo importano)
# ------------------------------------------------------------------
settings = Settings()
