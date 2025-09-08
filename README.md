# 🔒 dukeo

**Un bot di trading automatico** – unisce Telegram, TradingView e OctoBot con gestione del rischio, alert e monitoraggio in tempo reale.

## Prerequisiti

- Docker & Docker‑Compose
- (Opzionale) GitHub Actions per CI

## Come ottenere le chiavi

1. **Telegram** – BotFather → token → `BOT_TOKEN`; invia un messaggio al bot → `CHAT_ID`.
2. **TradingView** – `Webhook URL: https://<host>/tv_webhook`; `X‑API‑KEY: <secret>`.
3. **OctoBot** – URL + token (`OCTOBOT_URL`, `OCTOBOT_TOKEN`).

## Istruzioni di avvio

```bash
# Copia .env.example → .env e riempi con i tuoi valori
docker compose up -d
# Test webhook
curl -X POST http://localhost:8000/tv_webhook \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: <secret>" \
  -d '{"symbol":"BTCUSDT","side":"buy","entry_price":48000,"qty":0.01}'
