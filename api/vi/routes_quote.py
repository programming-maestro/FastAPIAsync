from fastapi import APIRouter
from app.utils.http_client import async_get
from app.contants.exchanges import BROKER_URLS

router = APIRouter()

@router.get("/quote/{broker}")
async def get_quote(broker: str):
    url = BROKER_URLS.get(broker, "https://postman-echo.com/delay/2")
    data = await async_get(url)
    return {"broker": broker, "data": data}
