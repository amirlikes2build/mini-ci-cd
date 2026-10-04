from fastapi import FastAPI, HTTPException, status

from app.calculator import add, subtract
from app.signals import all_signals, search_signal

app = FastAPI()

@app.get('/')
def get_status():
    return {"message": "mini-ci-cd is running"}


@app.get('/add')
def get_addition(a: float, b: float):
    return {"result" : add(a, b)}

@app.get('/subtract')
def get_subtraction(a: float, b: float):
    return  {"result" : subtract(a, b)}

@app.get('/healthz')
def get_health():
    return {
        "status": "ok",
        "service": "mini-ci-cd",
    }

@app.get('/signals')
def get_signals():
    return all_signals()

@app.get('/signals/{symbol}')
def get_signal(symbol: str):
    symbol_upper = symbol.upper()
    search = search_signal(symbol_upper)

    if search is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Signal not found for symbol: {symbol_upper}")
    return search
