class FeatureExtractionError(Exception):
    """Custom exception for errors during feature extraction."""
    pass

class FeatureEngineeringError(Exception):
    """Custom exception for errors during feature engineering."""
    pass

class ModelTrainingError(Exception):
    """Custom exception for errors during model training."""
    pass

class ModelPredictionError(Exception):
    """Custom exception for errors during model prediction."""
    pass

class DataLoadingError(Exception):
    """Custom exception for errors during data loading."""
    pass

class ConfigLoadingError(Exception):    
    """Custom exception for errors during configuration loading."""
    pass

class ModelNotFoundError(Exception):
    """Custom exception for when a model file is not found."""
    pass

class PipelineExecutionError(Exception):
    """Custom exception for errors during pipeline execution."""
    pass

class InvalidInputError(Exception):
    """Custom exception for invalid input data."""
    pass