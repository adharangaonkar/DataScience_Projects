
# Customer Churn in Banking


## Project Description
A well-known bank has been observing a lot of customers closing their accounts or switching to competitor banks over the past couple of quarters. This has caused a huge dent in their quarterly revenues and might drastically affect annual revenues for the ongoing financial year, causing stocks to plunge and market cap to reduce significantly. The idea is to be able to predict which customers are going to churn so that necessary actions/interventions can be taken by the bank to retain such customers.

In this machine learning churn prediction project, we are provided with customer data pertaining to his past transactions with the bank and some demographic information. We use this to establish relations/associations between data features and customer's propensity to churn and build a classification model to predict whether the customer will leave the bank or not. We also go about explaining model predictions through multiple visualizations and give insight into which factor(s) are responsible for the churn of the customers.

This project walks you through a complete end-to-end cycle of a data science project in the banking industry, right from the deliberations during formation of the problem statement to making the model deployment-ready.

## Getting Started

### Prerequisites

#### Create an environment <br>
Whatever you prefer (e.g. `conda` or `venv`)
```console
mkdir myproject
$ cd myproject
$ python3 -m venv venv
```

#### Activate it
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
```

#### Install Dependencies
 ```console
pip install numpy 
pip install pandas
pip install matplotlib
pip install scikit-learn
pip install seaborn
pip install xgboost
pip install lightgbm
pip install shap
 ```

#### Usage

Run

```console
"Churn Prediction Baseline Creation.ipynb"
```

This will generate baseline statistics which will further need improving







