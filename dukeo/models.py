# dukeo/models.py
from pydantic import BaseModel
from typing import Literal

class TVSignal(BaseModel):
    symbol: str
    side: Literal["buy", "sell"]
    entry_price: float
    qty: float

class OrderResponse(BaseModel):
    order_id: str
    status: str

