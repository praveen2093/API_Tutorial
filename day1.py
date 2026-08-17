from fastapi import FastAPI

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