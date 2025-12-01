from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/calculations/", response_model=schemas.CalculationRead)
def create_calculation(calc: schemas.CalculationCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_calculation(db, calc)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
