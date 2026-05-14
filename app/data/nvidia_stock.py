import yfinance as yf
from pandas import DataFrame
from ..util.logging import AppLogger
from ..util.utilties import normalize_yfinance_columns
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

    # Remove rows with NaN values caused by pct_change / rolling
    df = df.dropna()

    return df