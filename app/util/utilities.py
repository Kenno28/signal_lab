from pandas import DataFrame
import pandas as pd
from app.util.logging import AppLogger

logger = AppLogger(__name__)

def create_valid_nvda_test_data() -> pd.DataFrame:
    """Creates valid NVDA test data with all required features."""

    data = {
        "Close": [101.0, 102.0, 103.0, 104.0, 105.0],
        "High": [102.0, 103.0, 104.0, 105.0, 106.0],
        "Low": [99.0, 100.0, 101.0, 102.0, 103.0],
        "Open": [100.0, 101.0, 102.0, 103.0, 104.0],
        "Volume": [1_000_000, 1_050_000, 1_100_000, 1_080_000, 1_120_000],

        "future_return": [0.0099, 0.0098, 0.0097, 0.0096, 0.0],

        "return_1": [0.01, 0.0099, 0.0098, 0.0097, 0.0096],
        "return_3": [0.03, 0.029, 0.028, 0.027, 0.026],
        "moving_average_5": [101.0, 101.5, 102.0, 102.5, 103.0],
        "moving_average_20": [100.5, 101.0, 101.5, 102.0, 102.5],
        "volatility_5": [0.01, 0.011, 0.012, 0.013, 0.014],
        "volume_change": [0.0, 0.05, 0.0476, -0.0182, 0.0370],
    }

    return pd.DataFrame(data)


def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        return None
    

def load_config(config_path = "config.yaml") -> dict:
    """Load configuration from a YAML file."""
    import yaml

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Config loaded successfully from {config_path}")
        return config
    except Exception as e:
        logger.error(f"Error loading config: {e}")
        # Raise an exception because the config is essential for the application to run
        raise ValueError(f"Failed to load config from {config_path}")