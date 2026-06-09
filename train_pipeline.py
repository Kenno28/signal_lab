from pathlib import Path
from app.models.train_models import train_models, save_model
from app.data.process_data import process_data
from app.util.utilities import load_data, load_config
from app.util.logging import AppLogger

logger = AppLogger(__name__)

config = load_config()
data_path = Path(config["data"]["path"])

def pipeline():
    """Main pipeline function to execute the data fetching, preprocessing, model training, and evaluation."""
    logger.info("Starting the pipeline.")
    
    # Step 1: Fetch NVIDIA stock data
    df= load_data(data_path)
    if df is None:
        logger.error("Failed to fetch NVIDIA stock data. Exiting pipeline.")
        return
    
    logger.info(f"df columns: {df.columns}")
    # Step 2: Preprocess the data
    train, validate, test = process_data(df)
    logger.info("Data preprocessing completed.")
    
    # Step 4: Split the data into features and target variable
    X_train = train.drop(columns=["target", "Date"])
    y_train = train["target"]
    # Validate will be implemnted in the furture
    X_validate = validate.drop(columns=["target", "Date"])
    y_validate = validate["target"]
    X_test = test.drop(columns=["target", "Date"])
    y_test = test["target"]

    # Step 5: Train models and evaluate performance
    models = train_models(X_train, y_train, X_test, y_test)
    
    # Step 6: Save the trained models
    for model_name, model in models.items():
        save_model(model, model_name)

    logger.info("Pipeline execution completed.")
    return models

if __name__ == "__main__":
    pipeline()