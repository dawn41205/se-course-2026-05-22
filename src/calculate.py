from fastapi import FastAPI

app = FastAPI()


def add_func(a: float, b: float) -> float:
    return a + b


def sub_func(a, b):
    # temp = 123
    return a - b


def mul_func(a: float, b: float) -> float:
    # return "123"
    return a * b


@app.get("/")
def home():
    return {"status": "Online", "message": "這是簡易計算機API"}


@app.get("/add")
def calculate_add(a: float, b: float):
    result = add_func(a, b)
    return {"Operatino": "addition", "a": a, "b": b, "result": result}
