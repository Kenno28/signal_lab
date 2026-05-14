import joblib, os, glob
import numpy as np
from pandas.api.types import is_numeric_dtype

from util.logging import AppLogger
logger = AppLogger(__name__)

class ModelService:
    """Service class to manage loading and using machine learning models for predictions."""

    REQUIRED_FEATURES = (
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "return_1",
        "return_3",
        "moving_average_5",
        "moving_average_20",
        "volatility_5",
        "volume_change",
    )
    OPTIONAL_NUMERIC_FEATURES = ("future_return",)
    FORBIDDEN_FEATURES = ("target",)

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

    def validate_input(self, X) -> bool:
        """Validates the input data for predictions."""
        if X is None:
            logger.error("Input data is None")
            return False
        
        if not hasattr(X, "shape"):
            logger.error("Input data does not have a shape attribute")
            return False
        
        if X.shape[0] == 0:
            logger.error("Input data has zero rows")
            return False
        
        if not hasattr(X, "columns"):
            logger.error("Input data must be a DataFrame with named NVDA feature columns")
            return False

        missing_features = [column for column in self.REQUIRED_FEATURES if column not in X.columns]
        if missing_features:
            logger.error(f"Input data is missing required feature columns: {missing_features}")
            return False

        forbidden_features = [column for column in self.FORBIDDEN_FEATURES if column in X.columns]
        if forbidden_features:
            logger.error(f"Input data contains non-feature columns: {forbidden_features}")
            return False

        numeric_features = [
            column
            for column in (*self.REQUIRED_FEATURES, *self.OPTIONAL_NUMERIC_FEATURES)
            if column in X.columns
        ]
        non_numeric_features = [
            column for column in numeric_features if not is_numeric_dtype(X[column])
        ]
        if non_numeric_features:
            logger.error(f"Input data has non-numeric feature columns: {non_numeric_features}")
            return False

        feature_values = X[numeric_features].to_numpy()
        if not np.isfinite(feature_values).all():
            logger.error("Input data contains NaN or infinite feature values")
            return False

        if (X[["Open", "High", "Low", "Close"]] <= 0).any().any():
            logger.error("Input data contains non-positive OHLC prices")
            return False

        if (X["Volume"] < 0).any():
            logger.error("Input data contains negative volume values")
            return False

        if (
            (X["High"] < X[["Open", "Low", "Close"]].max(axis=1)).any()
            or (X["Low"] > X[["Open", "High", "Close"]].min(axis=1)).any()
        ):
            logger.error("Input data contains invalid OHLC price relationships")
            return False

        return True

    def predict(self, X) -> dict | None:
        """Generates predictions from the loaded models given input data X."""

        if not self.models:
            raise ValueError("No models loaded. Call load_models() first.")

        if not self.validate_input(X):
            return None
        
        model_predictions = {}

        try:
            for model in self.models:
                if hasattr(model, "predict"):
                    model_predictions[type(model).__name__] = model.predict(X)
        except AttributeError as e:
            logger.error(f"Model does not have a predict method: {e}")
            return None
            
        return model_predictions