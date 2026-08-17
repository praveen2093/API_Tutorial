from fastapi import FastAPI
import math

# 1. Initialize the FastAPI app instance
app = FastAPI()

# 2. Define a GET endpoint for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 3. Optional: A parameterized endpoint to greet someone by name
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/age/{age}")
def get_age(age: int):
    return {"message": f"Hello, you are {age} years old!"}

# 5. Addition
@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}

# 6. Multiplication
@app.get("/multiplication/{a}/{b}")
def multiplication(a: int, b: int):
    return {"result": a * b}

# 7. Square root
@app.get("/sqrt/{number}")
def sqrt(number: float):
    return {"result": math.sqrt(number)}

@app.get("/table/{number}")
def multiplication_table(number: int):
    table = []

    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")

    return {"table": table}

# Division
@app.get("/division/{a}/{b}")
def division(a: float, b: float):
    return {"result": a / b}


# Subtraction
@app.get("/sub/{a}/{b}")
def sub(a: float, b: float):
    return {"result": a - b}