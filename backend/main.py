from fastapi import FastAPI 
from routes import auth

app = FastAPI()

@app.get("/")
async def root():
    return {"Name": "Fave"}

app.include_router(auth.router)

