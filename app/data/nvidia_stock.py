import yfinance as yf
from pandas import DataFrame
import numpy as np
from ..util.logging import AppLogger
from ..util.utilities import normalize_yfinance_columns
logger = AppLogger("Stock_Data")


def validate_nvidia_stock_data(df: DataFrame) -> bool:
    """Validates the NVIDIA stock data."""
    
    if df.empty:
        logger.error("NVIDIA stock data is empty")
        return False

    required_columns = {"Open", "High", "Low", "Close", "Volume"}
    if not required_columns.issubset(df.columns):
        logger.debug(f"DataFrame columns: {df.columns}")
        logger.error("NVIDIA stock data is missing required columns")
        return False
    
    return True

def get_nvidia_stock_data() -> DataFrame | None:
    """Fetches NVIDIA stock data for the last 60 days at 5-minute intervals."""
    
    logger.info("Downloading NVIDIA stock data")
    df = yf.download(
        tickers="NVDA",
        period="60d",
        interval="5m"
    )

    if df is None or df.empty:
        logger.error("No data downloaded for NVIDIA stock")
        return None
    
    df = normalize_yfinance_columns(df)

    if isinstance(df, DataFrame) and validate_nvidia_stock_data(df):
        df = target_builder_nvidia_stock_data(df)

        return feature_engineer_nvidia_stock_data(df)
    else:
        logger.error("Failed to download NVIDIA stock data")
        return None

def feature_engineer_nvidia_stock_data(df: DataFrame) -> DataFrame:
    """Performs feature engineering on NVIDIA stock data."""
    
    df = df.copy()

    # Return features
    df["return_1"] = df["Close"].pct_change(1)
    df["return_3"] = df["Close"].pct_change(3)

    # Moving averages
    df["moving_average_5"] = df["Close"].rolling(window=5).mean()
    df["moving_average_20"] = df["Close"].rolling(window=20).mean()

    # Volatility based on recent returns
    df["volatility_5"] = df["return_1"].rolling(window=5).std()

    # Volume change
    df["volume_change"] = df["Volume"].pct_change(1)

    # Order DF by datetime index
    df = df.sort_index()

    # Remove rows with NaN values caused by pct_change / rolling
    df = df.dropna()

    return df

def target_builder_nvidia_stock_data(df: DataFrame, threshold: float = 0.001) -> DataFrame:
    """Builds the target variable for NVIDIA stock data."""
    
    # Calculate future return for the next 5-minute candle
    df["future_return"] = df["Close"].shift(-1) / df["Close"] - 1

    # Remove rows without valid future target
    df = df.dropna(subset=["future_return"])

    # Create single target label
    conditions = [
        df["future_return"] > threshold,
        df["future_return"] < -threshold
    ]

    choices = ["UP", "DOWN"]

    df["target"] = np.select(
        conditions,
        choices,
        default="NEUTRAL"
    )
    logger.info(f"Target variable created with distribution: {df['target'].value_counts().to_dict()}")
    return df