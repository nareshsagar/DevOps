from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Naresh! Your FastAPI CI/CD Pipeline is 2.0v"}

@app.get("/health")
def status():
    return {"status": "ok"}

