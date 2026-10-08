from fastapi import FastAPI, HTTPException, status

from app.calculator import add, subtract
from app.get_signals import get_all_signals, get_signal_by_ticker

app = FastAPI()


@app.get("/")
def get_status():
    return {"message": "mini-ci-cd is running"}


@app.get("/add")
def get_addition(a: float, b: float):
    return {"result": add(a, b)}


@app.get("/subtract")
def get_subtraction(a: float, b: float):
    return {"result": subtract(a, b)}


@app.get("/healthz")
def get_health():
    return {
        "status": "ok",
        "service": "mini-ci-cd",
    }


@app.get("/signals")
def get_signals():
    return get_all_signals()


@app.get("/signals/{ticker}")
def get_signal(ticker: str):
    signal = get_signal_by_ticker(ticker)

    if signal is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Signal not found for ticker: {ticker.upper()}",
        )

    return signal
