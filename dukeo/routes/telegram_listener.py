# dukeo/routes/telegram_listener.py
from fastapi import APIRouter

# ❗  no più `name=`
router = APIRouter()

@router.get("/start")
async def start():
    return {"message":"Bot in esecuzione. Usa /help"}

@router.get("/help")
async def help():
    return {"message":"Comandi disponibili: /start, /help"}
