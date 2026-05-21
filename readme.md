# NVDA Intraday Signal Lab

## Project Overview

NVDA Intraday Signal Lab is a learning-focused machine learning engineering project that predicts short-term intraday movement signals for Nvidia stock (`NVDA`).

The system uses historical intraday OHLCV data to build technical features, train classification models, evaluate model performance, and expose predictions through a FastAPI API.

The project is not intended to be a real trading bot or financial advice system.  
The goal is to build a clean, understandable, testable, and extensible ML engineering project.

---

## Current Project Version

The project has completed an initial V1 prototype and is now moving into:

## V2 — Stabilization and Data Pipeline Refactor

V2 focuses on improving the foundation of the project instead of adding many new features.

The main goal of V2 is to make the project more stable, maintainable, and reliable by improving:

- Code structure
- Data loading
- Data validation
- Data processing
- Error handling
- Logging
- Evaluation output
- Tests
- Documentation

V2 is not about building the most accurate trading model.  
V2 is about making the system cleaner, safer, and easier to extend.

---

## Main Goal

The system should predict whether NVDA is likely to move up, down, or stay neutral within the next 5-minute interval.

Initial label definition:

- `UP`: price increases by more than a defined threshold
- `DOWN`: price decreases by more than a defined threshold
- `NEUTRAL`: price movement stays within the threshold range

The threshold is configurable and may be adjusted during experimentation.

---

## Learning Purpose

This project is intentionally built with minimal AI assistance.

The main purpose of this project is to improve my own understanding of:

- Machine Learning
- Feature Engineering
- Time Series Classification
- Software Engineering
- API Design
- Testing
- CI/CD
- Logging
- Error Handling
- Data Validation
- Clean Project Structure
- Model Evaluation
- Maintainable ML Pipelines

AI tools may be used for guidance, review, and debugging support, but the core implementation, architecture decisions, and learning process should be done manually as much as possible.

This project is meant to strengthen real engineering understanding instead of simply generating a finished application.

---

## V1 Summary

V1 built the first end-to-end version of the project.

V1 included:

- Loading historical NVDA intraday OHLCV data
- Creating basic technical features
- Creating classification labels for the next 5-minute interval
- Training simple classification models
- Evaluating model performance
- Saving and loading trained models
- Exposing predictions through a FastAPI endpoint
- Adding basic logging
- Adding basic tests
- Adding a simple CI pipeline

V1 proved that the basic ML pipeline can run from data loading to API prediction.

---

## V2 Scope

V2 focuses on stabilizing and improving the existing system.

V2 includes:

- Review and refactor the V1 architecture
- Define clearer module responsibilities
- Add centralized configuration
- Add custom exception classes
- Re-evaluate and document the data source decision
- Improve the `PriceLoader`
- Normalize the raw data schema
- Add a stronger data validation layer
- Improve missing value handling
- Refactor the feature engineering pipeline
- Improve the target builder
- Add a dedicated data pipeline service
- Improve the training pipeline
- Improve model evaluation output
- Improve prediction service error handling
- Add FastAPI exception handlers
- Improve logging messages
- Add tests for data validation
- Add tests for feature engineering
- Add tests for API error cases
- Update documentation

---

## Not Part of V2

The following features are intentionally excluded from V2:

- No Reinforcement Learning
- No RAG
- No LLM-based prediction
- No live trading
- No broker integration
- No real money execution
- No dashboard
- No complex monitoring stack
- No continuous deployment

These features may be considered in later versions after the foundation is stable.

---

## Planned Version Roadmap

### V1 — Minimal ML Core

Goal: Build the first working end-to-end ML pipeline.

Included:

- Load data
- Create features
- Build targets
- Train models
- Evaluate results
- Save/load model
- Serve predictions through FastAPI
- Add basic logging, tests, and CI

### V2 — Stabilization and Data Pipeline Refactor

Goal: Improve project stability, maintainability, data quality, and error handling.

Focus areas:

- Better architecture
- Cleaner data pipeline
- Improved data validation
- Better exception handling
- More useful logs
- More reliable tests
- Better documentation

### V3 — Explainability and Evaluation Improvements

Possible additions:

- SHAP-based model explanations
- Better evaluation reports
- More detailed model comparison
- Feature importance analysis
- Improved threshold experiments
- More robust validation strategy

### V4 — RAG-Based Context Layer

Possible additions:

- Add Nvidia-related knowledge documents
- Add market analysis notes
- Retrieve relevant context for explanations
- Generate structured explanations based on model output and retrieved context

### V5 — Monitoring and Production Improvements

Possible additions:

- Request monitoring
- Prediction latency tracking
- Prediction distribution tracking
- Error tracking
- Model confidence tracking
- Docker setup
- Improved CI/CD pipeline
- Deployment preparation

---

## Data

The project uses NVDA intraday OHLCV data.

Required internal schema:

- `timestamp`
- `open`
- `high`
- `low`
- `close`
- `volume`

Target timeframe:

- 5-minute candles

Prediction horizon:

- Next 5-minute candle

### Current Data Source

The V1 prototype used `yfinance` as a simple development data source.

In V2, the data source decision will be reviewed and documented more carefully.

Potential sources to evaluate:

- `yfinance`
- Alpha Vantage
- Polygon / Massive
- Twelve Data
- Other financial market data APIs

The selected source should be documented with:

- Reason for selection
- Available historical period
- Supported interval
- API limitations
- Cost considerations
- Known data quality limitations

---

## Data Processing Goals for V2

V2 should make the data pipeline more reliable and predictable.

Main goals:

- Normalize all raw data into a consistent schema
- Handle timestamps consistently
- Remove source-specific column issues, such as MultiIndex columns
- Validate required columns
- Detect empty datasets
- Detect missing values
- Detect duplicate timestamps
- Detect unsorted timestamps
- Detect invalid prices or volumes
- Separate raw-data missing values from feature-generated missing values

---

## Initial Features

Current planned base features:

- `return_1`
- `return_3`
- `moving_average_5`
- `moving_average_20`
- `volatility_5`
- `volume_change`

V2 should refactor feature creation into a cleaner and more maintainable feature engineering pipeline.

More features may be added later, but V2 should focus on correctness and structure first.

---

## Initial Models

The project currently focuses on simple classification models:

- Logistic Regression
- Random Forest Classifier

More advanced models such as XGBoost or LightGBM may be added later.

V2 does not focus on adding more models.  
The priority is improving the data pipeline, error handling, evaluation, and maintainability.

---

## API Endpoints

### `GET /health`

Returns the current API status.

Example response:

```json
{
  "status": "ok"
}
```

### `POST /predict`

Returns the predicted signal for NVDA.

Example response:

```json
{
  "ticker": "NVDA",
  "timeframe": "5m",
  "prediction_horizon": "next_5_minutes",
  "signal": "UP",
  "confidence": 0.62,
  "model": "RandomForestClassifier"
}
```

---

## Error Handling Goals for V2

V2 should introduce clearer and more controlled error handling.

Planned custom exceptions:

- `DataLoadingError`
- `DataValidationError`
- `FeatureEngineeringError`
- `ModelTrainingError`
- `PredictionError`

The API should return clean JSON error responses instead of uncontrolled crashes.

Example error response:

```json
{
  "error": "DataValidationError",
  "message": "Missing required columns: close, volume"
}
```

---

## Logging Goals for V2

V2 should improve logs so the pipeline can be debugged more easily.

Logs should include:

- Start and end of important pipeline steps
- DataFrame shapes
- Missing value counts
- Target distribution
- Selected model name
- Evaluation results
- Prediction results
- Relevant exception details

---

## Project Structure

Planned V2 structure:

```text
nvda-intraday-signal-lab/
  app/
    api/
      routes.py
      schemas.py
    config/
      settings.py
    data/
      price_loader.py
      data_validator.py
      data_normalizer.py
    features/
      feature_engineer.py
      target_builder.py
    models/
      trainer.py
      predictor.py
      evaluator.py
      registry.py
    services/
      data_pipeline_service.py
      training_service.py
      prediction_service.py
    exceptions/
      custom_exceptions.py
    monitoring/
      logging.py
    utils/
  data/
    raw/
    processed/
  models/
    saved/
  docs/
    data_source.md
  tests/
  README.md
  requirements.txt
```

The exact structure may change during V2, but the goal is to keep responsibilities clearly separated.

---

## Testing Goals for V2

V2 should improve the test coverage around stability and error cases.

Planned test areas:

- Data validation
- Feature engineering
- Target building
- API health endpoint
- API prediction endpoint
- API error cases
- Missing model handling
- Data loading failure handling

---

## Disclaimer

This project is for educational and portfolio purposes only.

It does not provide financial advice.  
It does not execute trades.  
It should not be used for real trading decisions without proper validation, risk management, and professional review.
