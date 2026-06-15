# NVDA Daily Signal Lab

## Project Overview

NVDA Daily Signal Lab is a learning-focused machine learning engineering project that predicts next-day movement signals for Nvidia stock (`NVDA`).

The system uses historical daily OHLCV data to build technical features, train classification models, evaluate model performance, and expose predictions through a FastAPI API.

The project is not intended to be a real trading bot or financial advice system.  
The goal is to build a clean, understandable, testable, deployable, and extensible ML engineering project.

---

## Current Project Version

The project has completed an initial V1 prototype and is now moving into:

## V2 — Stabilization, Daily Data Pipeline Refactor and Docker Preparation

V2 focuses on improving the foundation of the project instead of adding many new features.

The main goal of V2 is to make the project more stable, maintainable, and reliable by improving:

- Code structure
- Daily data loading
- Data validation
- Data processing
- Error handling
- Logging
- Evaluation output
- Tests
- Documentation
- Docker readiness

V2 is not about building the most accurate trading model.  
V2 is about making the system cleaner, safer, easier to run, and easier to extend.

A major goal before adding RAG, LLM-based explanations, or more advanced features is to integrate Docker and make the application reproducible in a containerized environment.

---

## Main Goal

The system should predict whether NVDA is likely to move up, down, or stay neutral on the next trading day.

Initial label definition:

- `UP`: next-day closing price increases by more than a defined threshold
- `DOWN`: next-day closing price decreases by more than a defined threshold
- `NEUTRAL`: next-day price movement stays within the threshold range

The threshold is configurable and may be adjusted during experimentation.

---

## Learning Purpose

This project is intentionally built with minimal AI assistance.

The main purpose of this project is to improve my own understanding of:

- Machine Learning
- Feature Engineering
- Daily Time Series Classification
- Software Engineering
- API Design
- Testing
- CI/CD
- Docker
- Logging
- Error Handling
- Data Validation
- Clean Project Structure
- Model Evaluation
- Maintainable ML Pipelines
- Deployment Preparation

AI tools may be used for guidance, review, and debugging support, but the core implementation, architecture decisions, and learning process should be done manually as much as possible.

This project is meant to strengthen real engineering understanding instead of simply generating a finished application.

---

## V1 Summary

V1 built the first end-to-end version of the project.

V1 included:

- Loading historical NVDA market data
- Creating basic technical features
- Creating classification labels
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

V2 focuses on stabilizing and improving the existing system while switching the project goal from intraday prediction to daily prediction.

V2 includes:

- Refactor the V1 architecture
- Replace intraday-specific logic with daily prediction logic
- Define clearer module responsibilities
- Add centralized configuration
- Add custom exception classes
- Use a transparent file-based daily data source
- Improve the raw data loading logic
- Normalize the raw daily data schema
- Add a stronger data validation layer
- Improve missing value handling
- Refactor the feature engineering pipeline for daily data
- Improve the target builder for next-day prediction
- Add a dedicated data pipeline service
- Improve the training pipeline
- Improve model evaluation output
- Improve prediction service error handling
- Add FastAPI exception handlers
- Improve logging messages
- Add tests for data validation
- Add tests for feature engineering
- Add tests for API error cases
- Prepare the project for Docker integration
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

RAG and LLM-based explanations are intentionally postponed.  
The next major engineering priority before RAG is Docker integration and deployment preparation.

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

### V2 — Stabilization and Daily Data Pipeline Refactor

Goal: Improve project stability, maintainability, data quality, and error handling while switching to daily prediction.

Focus areas:

- Better architecture
- Cleaner daily data pipeline
- Improved data validation
- Better exception handling
- More useful logs
- More reliable tests
- Better documentation
- Docker preparation

### V3 — Docker and Deployment Foundation

Goal: Make the project reproducible and easier to run in a containerized environment before adding RAG or LLM features.

Possible additions:

- Dockerfile
- docker-compose setup
- Containerized FastAPI application
- Containerized training or prediction workflow
- Environment variable handling
- Health check support
- Improved local development setup
- CI adjustments for Docker builds
- Deployment preparation

### V4 — Explainability and Evaluation Improvements

Possible additions:

- SHAP-based model explanations
- Better evaluation reports
- More detailed model comparison
- Feature importance analysis
- Improved threshold experiments
- More robust validation strategy

### V5 — RAG-Based Context Layer

Possible additions:

- Add Nvidia-related knowledge documents
- Add market analysis notes
- Retrieve relevant context for explanations
- Generate structured explanations based on model output and retrieved context

### V6 — Monitoring and Production Improvements

Possible additions:

- Request monitoring
- Prediction latency tracking
- Prediction distribution tracking
- Error tracking
- Model confidence tracking
- Improved CI/CD pipeline
- Deployment improvements

---

## Data

The project uses NVDA daily OHLCV data.

Required internal schema:

- `timestamp`
- `open`
- `high`
- `low`
- `close`
- `volume`

Target timeframe:

- Daily candles

Prediction horizon:

- Next trading day

### Current Data Source

The project is moving away from `stooq` as the main data source.

The new goal is to use a transparent file-based daily data source, such as a downloaded CSV from Stooq or another provider. This allows the raw data to be inspected, stored, versioned, and processed manually inside the project.

The selected source should be documented with:

- Reason for selection
- Available historical period
- Supported timeframe
- File format
- Known limitations
- Data quality considerations
- Future improvement options

---

## Data Processing Goals for V2

V2 should make the data pipeline more reliable and predictable.

Main goals:

- Load raw daily CSV data
- Normalize all raw data into a consistent internal schema
- Handle timestamps consistently
- Validate required columns
- Detect empty datasets
- Detect missing values
- Detect duplicate timestamps
- Detect unsorted timestamps
- Detect invalid prices or volumes
- Separate raw-data missing values from feature-generated missing values
- Save processed data for later ML usage
- Make the data processing step reusable inside a pipeline

---

## Initial Models

The project currently focuses on simple classification models:

- Logistic Regression
- Random Forest Classifier

More advanced models such as XGBoost or LightGBM will be added later.

V2 does not focus on adding more models.
The priority is improving the data pipeline, error handling, evaluation, maintainability, and Docker readiness.

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

Returns the predicted next-day signal for NVDA.

Example response:

```json
{
  "ticker": "NVDA",
  "timeframe": "1d",
  "prediction_horizon": "next_trading_day",
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
- `ConfigLoadingError`
- `ModelNotFoundError`
- `PipelineExecutionError`

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

## Docker Goal Before RAG

Before adding RAG, LLM-based explanations, or more advanced AI components, the project should first become easier to run and deploy.

The next major engineering goal is Docker integration.

This means the project should eventually support:

- Running the FastAPI application inside a Docker container
- Installing dependencies inside a controlled environment
- Using environment variables for configuration
- Running health checks inside the container
- Preparing the project for later deployment
- Making the project easier to run on another machine

This step is important because RAG and LLM features would add more complexity.  
The base application should be containerized before that complexity is added.

---

## Project Structure

Planned V2 structure:

```text
nvda-daily-signal-lab/
  app/
    api/
      routes.py
      schemas.py
    config/
      settings.py
    data/
      raw_data_loader.py
      data_validator.py
      data_normalizer.py
      missing_value_handler.py
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
- Config loading
- Pipeline execution

---
## What I Have Learned So Far

During this project, I have already learned and reinforced several important software engineering and ML engineering concepts.  
I am still actively improving these concepts in my code.

- Custom exceptions are extremely useful for making errors more explicit, readable, and easier to handle.
- I used `pytest` for the first time and realized how important automated tests are for building reliable code.
- A central configuration file helps avoid hardcoded values and makes the project easier to maintain.
- Logging is essential for understanding what happens inside the application, especially in data pipelines and API workflows.
- Small, focused GitHub issues make the development process more structured and easier to manage.
- Error handling is not only about catching errors, but also about understanding which parts of the data flow can be controlled and which parts cannot.
- Utility modules help keep reusable helper functions separated from core business logic.
- Separation of concerns makes the codebase easier to understand, test, debug, and extend.

---

## Disclaimer

This project is for educational and portfolio purposes only.

It does not provide financial advice.  
It does not execute trades.  
It should not be used for real trading decisions without proper validation, risk management, and professional review.
