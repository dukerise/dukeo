import pytest, httpx
from dukeo.services import octobot

@pytest.mark.asyncio
async def test_place(monkeypatch):
    async def dummy(cls, *_, **__):
        class R:
            status_code = 200
            def raise_for_status(self): pass
            def json(self): return {"order_id":"A"}
        return R()
    monkeypatch.setattr(httpx.AsyncClient, "post", dummy)
    resp = await octobot.place_order("BTC", "buy", 0.01, 48000)
    assert resp["order_id"] == "A"
