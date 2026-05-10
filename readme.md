# NVDA Intraday Signal Lab

## Project Overview

NVDA Intraday Signal Lab is a learning-focused machine learning project that aims to predict short-term intraday movement signals for Nvidia stock (`NVDA`).

The system will use historical intraday OHLCV data to generate technical features, train classification models, and expose predictions through a simple FastAPI endpoint.

The goal is not to build a real trading bot or financial advice system.  
The goal is to build a clean, understandable, and extensible ML engineering project.

---

## Main Goal

The system should predict whether NVDA is likely to move up, down, or stay neutral within the next 5-minute interval.

Initial label definition:

- `UP`: price increases by more than a defined threshold
- `DOWN`: price decreases by more than a defined threshold
- `NEUTRAL`: price movement stays within the threshold range

The exact threshold will be tested and adjusted during development.

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
- Monitoring
- Clean Project Structure
- Model Evaluation

AI tools may be used for guidance, review, and debugging support, but the core implementation, architecture decisions, and learning process should be done manually as much as possible.

This project is meant to strengthen real engineering understanding instead of simply generating a finished application.

---

## V1 Scope

The first version should stay minimal and focused.

V1 includes:

- Load historical NVDA intraday OHLCV data
- Build basic technical features
- Create classification labels for the next 5-minute interval
- Train simple classification models
- Evaluate model performance
- Save and load trained models
- Expose predictions through a FastAPI endpoint
- Add basic logging
- Add simple tests
- Add a simple CI pipeline

---

## Not Part of V1

The following features are intentionally excluded from V1:

- No Reinforcement Learning
- No RAG
- No LLM-based prediction
- No live trading
- No broker integration
- No real money execution
- No dashboard
- No complex monitoring stack
- No continuous deployment
- No complicated error handling

These topics may be added in later versions after the ML core is stable.

---

## Planned Versions

### V1 — Minimal ML Core

Build the basic ML pipeline:

- Load data
- Create features
- Train models
- Evaluate results
- Serve predictions through an API

### V2 — Explainability and Better Evaluation

Possible additions:

- SHAP-based model explanations
- Better metrics
- Better validation strategy
- Improved feature analysis

### V3 — RAG-Based Context Layer

Possible additions:

- Add Nvidia-related knowledge documents
- Add market analysis notes
- Retrieve relevant context for explanations
- Generate structured explanations based on model output and retrieved context

### V4 — Monitoring and Production Improvements

Possible additions:

- Request monitoring
- Prediction latency tracking
- Prediction distribution tracking
- Error tracking
- Model confidence tracking
- Docker setup
- Improved CI/CD pipeline

---

## Data

The project will use NVDA intraday OHLCV data.

Required columns:

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

---

## Initial Features

Planned V1 features:

- `return_1`
- `return_3`
- `moving_average_5`
- `moving_average_20`
- `volatility_5`
- `volume_change`

More features may be added later after the baseline models are working.

---

## Initial Models

V1 will start with simple classification models:

- Logistic Regression
- Random Forest Classifier

More advanced models such as XGBoost or LightGBM may be added later.

---

## API Endpoints

Planned endpoints:

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

## Project Structure

Planned structure:

```text
nvda-intraday-signal-lab/
  app/
    api/
    data/
    features/
    models/
    services/
    monitoring/
  data/
    raw/
    processed/
  models/
    saved/
  tests/
  README.md
  requirements.txt
```

---

## Disclaimer

This project is for educational and portfolio purposes only.

It does not provide financial advice.  
It does not execute trades.  
It should not be used for real trading decisions without proper validation, risk management, and professional review.
