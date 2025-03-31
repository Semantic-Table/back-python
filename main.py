# import fastapi and uvuicorn
from fastapi import Depends, FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated
import random

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
@app.get("/{sport}")
async def get_sport(sport: str):
    return {"message": sport + str(random.randint(1, 100))}