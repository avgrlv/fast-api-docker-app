from fastapi import FastAPI

from backend.database import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/user")
async def create_user(name: str, email: str):
    user = User(name=name, email=email)
    await User.objects.get_or_create(user)
    return {"id": user.id}


@app.get("/users")
async def get_users():
    users = await User.objects.all()
    return users
