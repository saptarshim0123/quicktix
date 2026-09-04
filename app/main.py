from fastapi import FastAPI
from app.database import engine
from sqlalchemy import text
from app.routes.events import router as EventRouter

app = FastAPI(
    title="QuickTix ticket booking API",
    description="This is a ticket booking API for QuickTix, a ticket booking service.",
    version="1.0.0",
)

app.include_router(EventRouter)

@app.get("/")
async def root():
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    return {"message": "Welcome to the QuickTix ticket booking API!"}

