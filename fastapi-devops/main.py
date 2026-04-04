from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
<<<<<<< HEAD
    return {"message": "Hello Naresh! Your FastAPI CI/CD Pipeline is 2.0v"}
=======
    return {"message": "Hello Naresh! Your FastAPI CI/CD Pipeline is 2.0V"}
>>>>>>> aadbce22f835cbf40e7ef5832b318b5337a3d7b1

@app.get("/health")
def status():
    return {"status": "ok"}

