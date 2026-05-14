import joblib, os, glob
from util.logging import AppLogger
logger = AppLogger(__name__)

class ModelService:
    """Service class to manage loading and using machine learning models for predictions."""

    def __init__(self, models_folder_path: str = "../models/trained_models"):
        self.models_folder_path = models_folder_path
        self.models = []  # This will hold the loaded models

    def load_models(self):

        if not os.path.exists(self.models_folder_path):
            raise FileNotFoundError(f"Model folder not found at {self.models_folder_path}")
        
        model_paths = glob.glob(os.path.join(self.models_folder_path, '*.pkl'))

        if not model_paths:
            raise FileNotFoundError(f"No model files found in {self.models_folder_path}")
        
        for model_path in model_paths:
            model = joblib.load(model_path)
            self.models.append(model)

    def predict(self, X) -> dict | None:
        
        if not self.models:
            raise ValueError("No models loaded. Call load_models() first.")
        
        model_predictions = {}

        try:
            for model in self.models:
                if hasattr(model, "predict"):
                    model_predictions[type(model).__name__] = model.predict(X)
        except AttributeError as e:
            logger.error(f"Model does not have a predict method: {e}")
            return None
            
        return model_predictions