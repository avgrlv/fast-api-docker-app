from fastapi import FastAPI
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

app = FastAPI()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/user/")
def create_user(name: str, email: str):
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    return {"id": user.id}


@app.get("/users/")
def get_users():
    users = session.query(User).all()
    return users
