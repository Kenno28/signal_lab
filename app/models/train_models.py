from app.models.logistic_regression import train_logistic_regression
from app.models.random_forest import train_random_forest
import joblib
from app.util.logging import AppLogger

logger = AppLogger(__name__)


def train_models(X_train, y_train, X_test, y_test):
    """Train multiple models and return their performance metrics."""
    logger.info("Starting model training.")
    lr_model, lr_acc, lr_conf_matrix, lr_recall, lr_precision, lr_f1 = train_logistic_regression(X_train, y_train, X_test, y_test)
    rf_model, rf_acc, rf_conf_matrix, rf_recall, rf_precision, rf_f1 = train_random_forest(X_train, y_train, X_test, y_test)

    comparison = compare_models({
        "Logistic Regression": {
            "accuracy": lr_acc,
            "confusion_matrix": lr_conf_matrix,
            "recall": lr_recall,
            "precision": lr_precision,
            "f1_score": lr_f1
        },
        "Random Forest": {
            "accuracy": rf_acc,
            "confusion_matrix": rf_conf_matrix,
            "recall": rf_recall,
            "precision": rf_precision,
            "f1_score": rf_f1
        }
    })
    logger.info(f"Comparison: {comparison}")
    logger.info("Model comparison completed.")
    return {
        "Logistic Regression": lr_model,
        "Random Forest": rf_model
    }


def compare_models(metrics):
    """Compare the performance of different models based on their metrics."""

    for model_name, model_metrics in metrics.items():
        print(f"Model: {model_name}")
        print(f"Accuracy: {model_metrics['accuracy']}")
        print(f"Confusion Matrix: \n{model_metrics['confusion_matrix']}")
        print(f"Recall: {model_metrics['recall']}")
        print(f"Precision: {model_metrics['precision']}")
        print(f"F1 Score: {model_metrics['f1_score']}\n")


def save_model(model, model_name):
    """Save the trained model to disk."""
    joblib.dump(model, f"{model_name}.joblib")
    logger.info(f"Model {model_name} saved to disk.")