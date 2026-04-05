from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# This automatically adds a /metrics endpoint to your app yes
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello Naresh! Your FastAPI CI/CD Pipeline is 3.0V"}

@app.get("/health")
def status():
    return {"status": "ok"}
    
