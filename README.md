# Airline Passenger Satisfaction Prediction

This is a Machine Learning project that I worked on to predict whether an airline passenger is satisfied with their travel experience.

I explored the dataset, performed preprocessing, trained different classification models, and compared their performance to find the best-performing model. I also created a simple web interface using Streamlit to make predictions easier.

## About the Project

The main objective is to predict passenger satisfaction based on details such as:

- Gender
- Customer Type
- Age
- Type of Travel
- Class
- Flight distance
- In-flight services
- Seat comfort
- Departure and arrival delays

## Machine Learning Models Used

I trained and evaluated the following models:

- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Bernoulli Naive Bayes
- Multinomial Naive Bayes
- Decision Tree
- Random Forest
- Logistic Regression
- XGBoost

**Best Model:** XGBoost

**Accuracy:** 96.31%

## Streamlit Application

I used Streamlit to build an interactive interface where users can enter passenger details and get a satisfaction prediction.

## Project Files

- `Airline_Passenger_Satisfaction.ipynb` – Notebook containing the data analysis, preprocessing and model training.
- `airline_passenger_satisfaction.csv` – Dataset used for the project.
- `data_dictionary.csv` – Description of the dataset columns.
- `app.py` – Streamlit application.
- `airline_satisfaction_model.pkl` – Saved trained model and preprocessing information.
- `airport_background.png` – Background image used in the application.
- `requirements.txt` – Required Python libraries.

## Run the Project Locally

1. Clone this repository:

   `git clone https://github.com/catherinesg03/airline-passenger-satisfaction.git`

2. Open the project folder.

3. Install the required libraries:

   `pip install -r requirements.txt`

4. Run the Streamlit application:

   `streamlit run app.py`

5. Open the local URL displayed in your terminal.

## Result

Among the models I tested, XGBoost achieved the highest accuracy of approximately 96.31% on the test dataset.

This project helped me understand the process of building, evaluating and deploying a Machine Learning classification model.
