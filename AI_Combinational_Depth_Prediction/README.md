# AI-Based Combinational Depth Prediction

## Overview
This project predicts the combinational logic depth of RTL signals using machine learning, avoiding full synthesis.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Place RTL files in `dataset/`
3. Run feature extraction: `python src/feature_extraction.py`
4. Train model: `python src/train_model.py`
5. Predict depth: `python src/predict_depth.py`

## Folder Structure
- `dataset/` : Contains RTL input files
- `src/` : Feature extraction, training, and prediction scripts
- `models/` : Saved trained models
- `results/` : Model evaluation outputs

## Next Steps
- Improve feature engineering
- Test different ML models
- Optimize inference speed
