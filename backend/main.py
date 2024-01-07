from fastapi import FastAPI 
from routes import auth, courses

app = FastAPI()

@app.get("/")
async def root():
    return {"Name": "Fave"}

app.include_router(auth.router)
app.include_router(courses.router)

