# app/main.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from . import models

app = FastAPI()

# Create all tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Hello, Module12!"}

@app.post("/users/")
def create_user(name: str, db: Session = Depends(get_db)):
    new_user = models.User(name=name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/calculations/")
def create_calculation(value: str, user_id: int, db: Session = Depends(get_db)):
    calc = models.Calculation(value=value, user_id=user_id)
    db.add(calc)
    db.commit()
    db.refresh(calc)
    return calc

@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/calculations/")
def list_calculations(db: Session = Depends(get_db)):
    return db.query(models.Calculation).all()
