from fastapi import FastAPI 
from routes import auth, courses, user 
#from schemas.user import User

app = FastAPI(include_in_schema_for_serialization={"schema"})

app = FastAPI()

@app.get("/")
async def root():
    return {"Name": "Fave"}

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(user.router)
#app.include_model(User)


