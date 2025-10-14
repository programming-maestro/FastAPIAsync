import asyncio
import time
import httpx
import requests
from fastapi import FastAPI

app = FastAPI()

# -----------------------
# Constants
# -----------------------
QUOTE_URL = "https://postman-echo.com/delay/3"

# -----------------------
# Non-API functions
# -----------------------

def fetch_sync(repetitions: int = 10):
    """Make repeated synchronous HTTP requests."""
    start_time = time.perf_counter()
    for _ in range(repetitions):
        requests.get(QUOTE_URL)
    elapsed_ms = (time.perf_counter() - start_time) * 1000
    return round(elapsed_ms, 2)

async def fetch_async(repetitions: int = 10):
    """Make repeated asynchronous HTTP requests."""
    start_time = time.perf_counter()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(QUOTE_URL) for _ in range(repetitions)]
        await asyncio.gather(*tasks)
    elapsed_ms = (time.perf_counter() - start_time) * 1000
    return round(elapsed_ms, 2)

# -----------------------
# API endpoints
# -----------------------

@app.get("/quote/async")
async def get_quote_async(repetitions: int = 10):
    elapsed_ms = await fetch_async(repetitions)
    return {
        "mode": "async",
        "repetitions": repetitions,
        "elapsed_milliseconds": elapsed_ms
    }

@app.get("/quote/sync")
def get_quote_sync(repetitions: int = 10):
    elapsed_ms = fetch_sync(repetitions)
    return {
        "mode": "sync",
        "repetitions": repetitions,
        "elapsed_milliseconds": elapsed_ms
    }

'''
GET /quote/async?repetitions=10     --> {"mode":"sync","repetitions":10,"elapsed_milliseconds":     37702.3}
GET /quote/sync?repetitions=10      --> {"mode":"async","repetitions":10,"elapsed_milliseconds":    4980.21}
'''