from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    # We keep the cleanest version of your message
    return {"message": "Hello Naresh! Your FastAPI CI/CD Pipeline is 2.0V"}

@app.get("/health")
def status():
    return {"status": "ok"}
  
  