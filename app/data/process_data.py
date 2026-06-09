import pandas as pd
from pandas.core.frame import DataFrame
from ..util.logging import AppLogger
from ..util.utilities import load_data

logger = AppLogger(__name__)


def process_data(file: DataFrame) -> tuple[DataFrame, DataFrame, DataFrame]:
    """
    Process the input data by normalizing column names and ensuring all required features are present.

    Parameters:
    file (DataFrame): The input data as a DataFrame.

    Returns:
    tuple[DataFrame, DataFrame, DataFrame]: A tuple containing the processed train, validate, and test DataFrames.
    """

    if file is None:
        logger.error("No data to process. The input file is None.")
        raise ValueError("Input file cannot be None.")

    # Ensure all required features are present
    required_features = ["Close", "High", "Low", "Open", "Volume", "Date"]

    missing_features = [feature for feature in required_features if feature not in file.columns]

    if missing_features:
        logger.error(f"Missing required features: {missing_features}")
        raise ValueError(f"Missing required features: {missing_features}")
    
    try :
        # Convert 'Date' column to datetime format
        file["Date"] = pd.to_datetime(file["Date"], errors="coerce")
        # check for any NaT values after conversion
        if file["Date"].isnull().any():
            logger.warning("Some dates could not be converted and will be set to NaT.")
        
        # now check for any NaT values and raise an error if found
        if file.isnull().any().any():
            logger.error("Data contains NaN values after processing.")
            raise ValueError("Data contains NaN values after processing.")
        
        # add target variable for model training

        file["target"] = file["Close"].shift(-1) - file["Close"]
        file = file.dropna()
        file["target"] = file["target"].apply(lambda x: "UP" if x > 0 else "DOWN" if x < 0 else "NEUTRAL")


        # now split the date into train, validate and test sets based on a specific date
        file = file.sort_values("Date") 
        train = file[file["Date"] < "2023-01-01"]
        validate = file[(file["Date"] >= "2023-01-01") & (file["Date"] < "2023-06-01")]
        test = file[file["Date"] >= "2023-06-01"]

        return train, validate, test

    except ValueError as e:
        logger.error(f"Error occurred while processing dates: {e}")
        raise