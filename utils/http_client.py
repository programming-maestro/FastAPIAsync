import httpx
import requests
import asyncio

# Async version
async def async_get(url: str):
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        return resp.json()

# Sync version
def sync_get(url: str):
    resp = requests.get(url)
    return resp.json()
