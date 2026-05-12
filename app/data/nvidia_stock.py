import yfinance as yf
from pandas import DataFrame
from ..util.logging import AppLogger

logger = AppLogger("API")



def get_nvidia_stock_data() -> DataFrame | None:
    """Fetches NVIDIA stock data for the last 60 days at 5-minute intervals."""
    
    logger.info("Downloading NVIDIA stock data")
    df = yf.download(
        tickers="NVDA",
        period="60d",
        interval="5m"
    )

    if isinstance(df, DataFrame):
        return df
    else:
        logger.error("Failed to download NVIDIA stock data")
        return None
