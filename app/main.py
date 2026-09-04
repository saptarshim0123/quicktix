from fastapi import FastAPI

app = FastAPI(
    title="QuickTix ticket booking API",
    description="This is a ticket booking API for QuickTix, a ticket booking service.",
    version="1.0.0",
    # lifespan=lifespan
)

@app.get("/")
async def root():
    return {"message": "Welcome to the QuickTix ticket booking API!"}