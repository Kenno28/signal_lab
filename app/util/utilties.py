from pandas import DataFrame
import pandas as pd


def normalize_yfinance_columns(df: DataFrame) -> DataFrame:
    """Normalizes the column names of a DataFrame downloaded from yfinance."""
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df