from app.models.train_models import train_models, save_model
from app.data.nvidia_stock import get_nvidia_stock_data
from app.util.logging import AppLogger
from app.data.splitting import split_time_series_data

logger = AppLogger(__name__)

def pipeline():
    """Main pipeline function to execute the data fetching, preprocessing, model training, and evaluation."""
    logger.info("Starting the pipeline.")
    
    # Step 1: Fetch NVIDIA stock data
    df = get_nvidia_stock_data()
    if df is None:
        logger.error("Failed to fetch NVIDIA stock data. Exiting pipeline.")
        return
    
    # Step 2: Preprocess the data (this is a placeholder, implement as needed)
    X_train, y_train, X_test, y_test = split_time_series_data(df)
    
    # Step 3: Train models and evaluate performance
    models = train_models(X_train, y_train, X_test, y_test)
    
    # Step 4: Save the trained models
    for model_name, model in models.items():
        save_model(model, model_name)

    logger.info("Pipeline execution completed.")
    return models

if __name__ == "__main__":
    pipeline()