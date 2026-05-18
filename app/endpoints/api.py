from contextlib import asynccontextmanager
from fastapi import FastAPI
import pandas as pd
from fastapi.responses import JSONResponse
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
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok"
        }
        )

@app.post("/predict")
def predict(data: dict):

    if not data:
        logger.error("No data provided in the request")
        return JSONResponse(
        status_code=400,
        content={
            "error": "No data provided"
        }
        )

    logger.info(f"Predict endpoint called with data: {data}")

    
    try:
        input_df = pd.DataFrame([data])
        model_predictions = models.predict(input_df)
    except ValueError as e:
        logger.error(f"Prediction failed due to invalid input: {e}")
        return JSONResponse(
        status_code=400,
        content={
            "error": str(e),
        }
        )
   
    except FileNotFoundError as e:
        logger.error(f"Prediction failed due to missing models: {e}")
        return JSONResponse(
        status_code=500,
        content={
            "error": "Model files not found. Ensure models are properly loaded."
        }
        )

    if model_predictions is None:
        logger.error("Prediction failed due to invalid input or model error")
        return JSONResponse(
        status_code=500,
        content={
            "error": "Prediction failed. Check logs for details.",
        }
        )

    return JSONResponse(
        status_code=200,
        content={
            "signal": model_predictions["signal"],
            "confidence": model_predictions["confidence"]
        }
    )


# Catch any unwanted routes and return a 404 error
@app.get("/{full_path:path}")
async def fallback(full_path: str):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Unknown route",
            "path": full_path,
            "message": "This endpoint does not exist."
    },
    )