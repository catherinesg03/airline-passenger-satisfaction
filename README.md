# Airline Passenger Satisfaction Prediction

A Machine Learning project focused on predicting airline passenger satisfaction using classification algorithms. The project includes data preprocessing, model training, performance evaluation, and an interactive web application built with Streamlit.

## Live Demo

**Try the application:** [Airline Passenger Satisfaction – Live App](https://airline-passenger-satisfaction-4oxjvg9h2hy6ff6ktzkdik.streamlit.app/)

**Source Code:** [GitHub Repository](https://github.com/catherinesg03/airline-passenger-satisfaction)

## Project Overview

The objective of this project is to predict whether an airline passenger is satisfied or neutral/dissatisfied based on their travel experience and service ratings.

The dataset includes features such as:

- Gender and Customer Type
- Age and Type of Travel
- Travel Class and Flight Distance
- In-flight services and Seat Comfort
- Departure and Arrival Delays

## Machine Learning Models

I trained and evaluated the following classification algorithms:

- K-Nearest Neighbors (KNN)
- Gaussian Naive Bayes
- Bernoulli Naive Bayes
- Multinomial Naive Bayes
- Decision Tree
- Random Forest
- Logistic Regression
- XGBoost

**Best Performing Model:** XGBoost

**Test Accuracy:** 96.31%

## Streamlit Web Application

An interactive web interface was developed using Streamlit. Users can enter passenger details and receive a satisfaction prediction.

[Open Live Application](https://airline-passenger-satisfaction-4oxjvg9h2hy6ff6ktzkdik.streamlit.app/)

## Project Structure

| File | Description |
|---|---|
| `Airline_Passenger_Satisfaction.ipynb` | Data analysis, preprocessing and model training |
| `airline_passenger_satisfaction.csv` | Original dataset |
| `data_dictionary.csv` | Dataset column descriptions |
| `app.py` | Streamlit application |
| `airline_satisfaction_model.pkl` | Trained model and preprocessing information |
| `airport_background.png` | Application background image |
| `requirements.txt` | Required Python libraries |
| `README.md` | Project documentation |

## Run Locally

To run the application on your system:

**1. Clone the repository**

```bash
git clone https://github.com/catherinesg03/airline-passenger-satisfaction.git
```

**2. Navigate to the project folder**

```bash
cd airline-passenger-satisfaction
```

**3. Install the dependencies**

```bash
pip install -r requirements.txt
```

**4. Run the Streamlit application**

```bash
streamlit run app.py
```

The application will open in your browser at the local URL provided by Streamlit.

## Results

Among the classification models evaluated, XGBoost achieved the highest test accuracy of approximately **96.31%**.

Through this project, I gained practical experience in data preprocessing, classification algorithms, model evaluation, and deploying a Machine Learning application using Streamlit.
