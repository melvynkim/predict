# Predict

Lightweight prediction model (AUC 0.77 from just 800 rows of data)

[See a demo](https://github.com/melvynkim/predict/blob/master/demos/Titanic.ipynb)

Predict does:

- exploratory data analysis
- feature engineering
- predictive modeling

## Installation

With pip, run:

```sh
pip install predict
```

## How to get started

```sh
git clone https://github.com/melvynkim/predict.git
cd predict
pip install -r requirements.txt
py.test tests
```
## Getting Started

For rich visualizations, run Predict from a [Jupyter notebook](https://jupyter.org/).

For classification, use:

```python
%matplotlib inline

import predict

pd = predict.Classifier(
    train_data='train.csv',
    test_data='test.csv',
    target_col='Survived',
    id_col='PassengerId')

pd.analyze()
pd.model()
```

For regression, use the `predict.Regressor` class.

**Tip:** To prevent scrolling in notebooks, select `Cell > Current Outputs > Toggle Scrolling`.

## Features

There are two primary methods:

- `analyze` runs exploratory data analysis
- `model` builds and evaluates different models

Optionally pass test data if you want to generate a CSV file with predictions.

## Data

Data can be a file

```python
predict.Classifier(train_data='train.csv', ...)
```

Or a data frame

```python
train_df = pd.read_csv('train.csv')

# do preprocessing
# ...

predict.Classifier(train_data=train_df, ...)
```

Specify datetime columns with:

```python
predict.Classifier(datetime_cols=['created'], ...)
```

## Evaluation

Predict has support for a number of eval metrics.

Classification

- `accuracy` - # correct / total (default)
- `auc` - area under the ROC curve
- `mlogloss` - multi class log loss

Regression

- `rmse` - root mean square error (default)
- `rmsle` - root mean square logarithmic error

Specify an eval metric with:

```python
predict.Classifier(eval_metric='mlogloss', ...)
```

## Modeling

Predict builds and compares different models. Currently, it uses:

1. boosted trees
2. simple benchmarks (mode for classification, mean and median for regression)

[XGBoost](https://github.com/dmlc/xgboost) is required for boosted trees. Install it with:

```sh
pip install xgboost
```

## Performance

Dataset | Eval Metric | v0.1 | Current
--- | --- | --- | ---
[House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) | RMSLE | 0.14069 | 0.13108
[Rental Listing Inquiries](https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries) | Multi Class Log Loss | - | 0.61861
[Titanic](https://www.kaggle.com/c/titanic) | Accuracy | 0.77512 | 0.77512