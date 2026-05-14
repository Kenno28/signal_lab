from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score, precision_score, f1_score
import numpy as np
from ..util.logging import AppLogger 

logger = AppLogger(__name__)


def train_logistic_regression(X_train, y_train, X_test, y_test):
    """Train a Logistic Regression model and evaluate its performance."""

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='macro')
    precision = precision_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')

    logger.info(f"Logistic Regression Accuracy: {acc}")
    logger.info(f"Logistic Regression Confusion Matrix: \n{conf_matrix}")
    logger.info(f"Logistic Regression Recall: {recall}")
    logger.info(f"Logistic Regression Precision: {precision}")
    logger.info(f"Logistic Regression F1 Score: {f1}")

    return model, acc, conf_matrix, recall, precision, f1