from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text

app = FastAPI(
    title="QuickTix ticket booking API",
    description="This is a ticket booking API for QuickTix, a ticket booking service.",
    version="1.0.0",
    # lifespan=lifespan
)

@app.get("/")
async def root():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"message": "Welcome to the QuickTix ticket booking API!"}