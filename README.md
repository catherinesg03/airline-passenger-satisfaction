# Airline Passenger Satisfaction - Streamlit App

## Files
- `app.py` — Streamlit user interface
- `airline_satisfaction_model.pkl` — trained XGBoost model, MinMaxScaler and feature-column metadata
- `requirements.txt` — Python dependencies

## Run locally
1. Keep all three project files in the same folder.
2. Open a terminal in that folder.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the application:
   ```bash
   streamlit run app.py
   ```
5. Streamlit will open the app in your browser (usually at http://localhost:8501).

The model follows the notebook's preprocessing: fill missing `Arrival Delay` values with the training median, remove `ID`, one-hot encode categorical predictors with `drop_first=True`, apply `MinMaxScaler`, and predict with XGBoost.

The reported test accuracy is approximately 96.3%. This is the notebook's held-out test accuracy, not a guarantee for individual predictions.
