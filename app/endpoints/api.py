from contextlib import asynccontextmanager
from fastapi import FastAPI
from ..util.logging import AppLogger
from ..service.model_service import ModelService

logger = AppLogger("API")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup")
    global models
    models = ModelService()
    models.load_models()
    yield
    logger.info("Application shutdown")

app = FastAPI(lifespan=lifespan)

@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}

@app.post("/predict")
def predict(data: dict):
    logger.info(f"Predict endpoint called with data: {data}")
    model_predictions = models.predict(data)
    if model_predictions is None:
        logger.error("Prediction failed due to invalid input or model error")
        return {"error": "Prediction failed. Check logs for details.", "code": 500 }
    
    return {"predictions": model_predictions, "code": 200}


# Catch any unwanted routes and return a 404 error
@app.get("/{full_path:path}")
async def fallback(full_path: str):
    return {
        "error": "Unknown route",
        "path": full_path,
        "message": "This endpoint does not exist.",
        "code": 404
    }