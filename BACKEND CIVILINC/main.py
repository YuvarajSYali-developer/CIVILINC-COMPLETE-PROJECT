from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def read_root():
    return {"message": "Welcome to the Civilinc Backend API!"} 