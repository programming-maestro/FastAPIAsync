from fastapi import FastAPI
from app.api.vi.routes_quote import router as quote_router

app = FastAPI(title="Async Trading API")
app.include_router(quote_router, prefix="/v1")


# http://127.0.0.1:8000/v1/quote/zerodha
# http://127.0.0.1:8000/v1/quote/alpaca
# http://127.0.0.1:8000/v1/quote/fyers


'''
1..5 | ForEach-Object -Parallel {
    curl -s http://127.0.0.1:8000/v1/quote/zerodha
}
'''