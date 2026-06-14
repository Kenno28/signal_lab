import joblib, os, glob
from collections import Counter
from pathlib import Path
from ..util.logging import AppLogger
from ..core.exceptions import ModelNotFoundError, PredictionError
from ..util.utilities import load_config 

config = load_config()
logger = AppLogger(__name__)
threshold_high = config["thresholds"]["high"] 
threshold_low = config["thresholds"]["low"]

class ModelService:
    """Service class to manage loading and using machine learning models for predictions."""


    def __init__(self, models_folder_path: Path =  Path(__file__).resolve().parents[1] / "models" / "trained_models"):
        self.models_folder_path = models_folder_path
        self.models = [] 

        
    REQUIRED_FEATURES = (
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Date"
    )

    FORBIDDEN_FEATURES = (
        "target"
    )
        
    def load_models(self):

        if not os.path.exists(self.models_folder_path):
            raise ModelNotFoundError(f"Model folder not found at {self.models_folder_path}")
        
        model_paths = glob.glob(os.path.join(self.models_folder_path, '*.joblib'))

        if not model_paths:
            raise ModelNotFoundError(f"No model files found in {self.models_folder_path}")
        
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
            raise ModelNotFoundError("No models loaded. Call load_models() first.")

        if not self.validate_input(X):
            raise PredictionError("Invalid input data. Check logs for details.")
        
        model_predictions = []

        try:
            for model in self.models:
                if hasattr(model, "predict"):
                    model_predictions.append(model.predict(X)[0])
        except AttributeError as e:
            logger.error(f"Model does not have a predict method: {e}")
            return None
        
        vote_counts = Counter(model_predictions)
        final_signal = vote_counts.most_common(1)[0][0]
        confidence = vote_counts[final_signal] / len(model_predictions)
        # combine both model predictions into a singel prediction
        response = {}
        response["signal"] = final_signal
        response["confidence"] = confidence
        response["timeframe"] = "1d"
        response["next_signal"] = "UP" if confidence >= threshold_high else "DOWN" if confidence <= threshold_low else "NEUTRAL"
        logger.info(f"Model predictions: {model_predictions}, Final signal: {final_signal}, Confidence: {confidence:.2f}")
        return response