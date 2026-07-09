from fastapi import FastAPI

# Initialize the FastAPI application instance
app = FastAPI()

# Define a root path GET endpoint
@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI is initialized!"}