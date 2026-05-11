from contextlib import asynccontextmanager
from fastapi import FastAPI
from ..util.logging import AppLogger

logger = AppLogger("API")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}