from fastapi import FastAPI
from app.endpoints import shortener

app = FastAPI()

app.include_router(shortener.router)