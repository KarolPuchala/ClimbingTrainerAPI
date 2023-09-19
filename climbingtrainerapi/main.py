from fastapi import FastAPI
from climbingtrainerapi.routers import users

app = FastAPI()
app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}