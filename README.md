# Crop Yield Predictor

A machine learning web app that predicts crop yield based on farming conditions.

## Live Demo
[Click here to try the app]([your_huggingface_space_link](https://muzakkir-cmd-crop-yield-predictor.hf.space/?__theme=system&deep_link=ULlCJjW7zDI))

## Problem
Farmers and agricultural planners need to estimate crop yield based on 
environmental conditions. This app predicts yield in hg/ha given country, 
crop type, rainfall, pesticide usage and temperature.

## Dataset
- Source: Kaggle — Crop Yield Prediction Dataset
- 28,242 records across 101 countries
- Years: 1990 to 2013

## Approach
- Exploratory data analysis to understand feature distributions
- Label encoding for categorical variables (Area, Item)
- Random Forest Regressor with 100 estimators
- 80/20 train-test split

## Results
- R2 Score: 0.9857
- Mean Absolute Error: 3752.48 hg/ha
- Most important feature: Crop type (60.8% importance)

## Key Finding
Crop type alone accounts for 60% of yield prediction. Environmental 
factors like pesticides, temperature and rainfall explain the remaining 30%.

## Technologies Used
- Python
- Scikit-learn
- Pandas
- Gradio
- Hugging Face Spaces
