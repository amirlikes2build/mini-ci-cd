from fastapi import FastAPI

from app.calculator import add, subtract

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

@app.get("/healthz")
def get_health():
    return {
        "status": "ok",
        "service": "mini-ci-cd",
    }
