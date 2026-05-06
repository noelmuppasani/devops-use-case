from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/info")
def info():
    return {
        "app": "DevOps Use Case API",
        "version": "1.0.0",
        "stack": "FastAPI + AKS"
    }