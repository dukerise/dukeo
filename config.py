import os
from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    # Telegram
    bot_token: SecretStr
    chat_id: int
    tv_secret: SecretStr | None = None

    # OctoBot
    octobot_url: str
    octobot_token: SecretStr | None = None

    # Risk
    sl_atr_mult: float = 1.5
    tp_atr_mult: float = 3.0
    max_dd: float = 0.20
    small_dd: float = 0.05

    # SMTP (opzionale)
    smtp_host: str | None = None
    smtp_port: int | None = None
    smtp_user: SecretStr | None = None
    smtp_pass: SecretStr | None = None

    # Capital & risk per trade
    balance: float = 10_000
    risk_per_trade: float = 0.02

    class Config:
        case_sensitive = False
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
