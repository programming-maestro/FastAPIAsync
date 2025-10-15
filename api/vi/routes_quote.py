from fastapi import APIRouter
from app.utils.http_client import async_get
from app.contants.exchanges import BROKER_URLS
import httpx

router = APIRouter()

@router.get("/quote/{broker}")
async def get_quote(broker: str):
    url = BROKER_URLS.get(broker, "https://postman-echo.com/delay/2")
    try:
        data = await async_get(url)
        return {"broker": broker, "data": data}
    except httpx.RequestError as e:
        return {"error": f"Failed to connect to {url}", "details": str(e)}
