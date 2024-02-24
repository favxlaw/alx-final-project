from fastapi import FastAPI 
from routes import auth, courses, user 
from fastapi.middleware.cors import CORSMiddleware

#from schemas.user import User

app = FastAPI(include_in_schema_for_serialization={"schema"})

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:9000"
]

app.add_middleware(CORSMiddleware, allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   allow_origins=origins)

@app.get("/")
async def root():
    return {"Name": "Fave"}

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(user.router)
#app.include_model(User)


