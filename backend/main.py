from fastapi import FastAPI, HTTPException
from routes.identity import identity_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to Agent Evo!"}

app.include_router(identity_router)
