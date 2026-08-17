# Importing FastAPI

from fastapi import FastAPI

# Initializing FastAPI to app
app = FastAPI()


# 1.  Define a GET endpoint for the root URL
@app.get("/")
def read_root():
    return {"message" : "Welcome to FastAPI"}


# 2. A parameterized endpoint to greet someone by name
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message" : f"Good Morning! {name}"}


# 3. Performing mathematical operations
@app.get("/Arithmetic Operations/{operations}")
def Operations(a: int, b: int):
    return {"Add" : a + b, 
            "Sub" : a - b,
            "Mul" : a *b,
            "div" : a / b,
            "Mod" : a % b,
            "Square" : a * a
            }


# 4. Performing multiplication table
@app.get("/multiplication/{a}")
def multiply(a: int):
    multiples = []

    for i in range(1, 11):
        multiple = a * i
        multiples.append(multiple)

    return {"Multiplication" : multiples}