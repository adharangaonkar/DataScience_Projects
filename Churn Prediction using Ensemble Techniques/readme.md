
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

```console
"Churn Prediction Ensembles.ipynb"
```

This notebook contains all the enhanced models as well as hyperparameter tuning.

## Project Workflow

- Structuring and framing a business need into a Machine Learning problem statement
- Defining relevant metrics and setting the right expectations with business teams
- Exploratory Data Analysis - Univariate, Bivariate analysis
- Missing value and outlier treatment
- Label Encoder/One Hot Encoder and handling new categorical levels in test/production data
- Target encoding and avoiding data leakage
- Feature transforms (scaling and normalization)
- Feature engineering and Feature selection (RFE)
- Solving class imbalance
- Model explainability and interpretability through Tree visualizations and SHAP
- Hyperparameter tuning using RandomSearch and GridSearch
- Ensembling multiple models
- Error analysis
- Wrapping up code using Pipelines for production run

## Result Metrics

### Best Performing Stacked Model

#### Validation Metrics

Class/Metric | precision | recall | f1-score | support 
--- | --- | --- | --- |--- 
0 | 0.90 | 0.88 | 0.89 | 842 
1 | 0.61 | 0.66 | 0.63 | 238 
accuracy |  |  | 0.83 | 1000 
macro avg | 0.76 | 0.77 | 0.76 | 1000
weighted avg | 0.84 | 0.83 | 0.83 | 1000 

### LightGBM Best Performing model

#### Training Metrics

Class/Metric | precision | recall | f1-score | support 
--- | --- | --- | --- |--- 
0 | 0.93 | 0.84 | 0.89 | 809 
1 | 0.53 | 0.75 | 0.62 | 191 
accuracy |  |  | 0.83 | 1000 
macro avg | 0.73 | 0.80 | 0.75 | 1000
weighted avg | 0.86 | 0.83 | 0.84 | 1000 


#### Validation Metrics

Class/Metric | precision | recall | f1-score | support 
--- | --- | --- | --- |--- 
0 | 0.91 | 0.85 | 0.88 | 842 
1 | 0.56 | 0.70 | 0.62 | 238 
accuracy |  |  | 0.81 | 1000 
macro avg | 0.74 | 0.77 | 0.75 | 1000
weighted avg | 0.83 | 0.81 |  0.82 | 1000 


#### Test Metrics

Class/Metric | precision | recall | f1-score | support 
--- | --- | --- | --- |--- 
0 | 0.93 | 0.84 | 0.89 | 809 
1 | 0.53 | 0.75 | 0.62 | 191
accuracy |  |  | 0.83 | 1000 
macro avg | 0.73 | 0.80 | 0.75 | 1000
weighted avg | 0.86 | 0.83 |  0.84 | 1000 
