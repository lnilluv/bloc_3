# Summary of 5_Default_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eta**: 0.075
- **max_depth**: 6
- **min_child_weight**: 1
- **subsample**: 1.0
- **colsample_bytree**: 1.0
- **eval_metric**: f1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

182.9 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0499869 | nan           |
| auc       | 0.973869  | nan           |
| f1        | 0.769297  |   0.396124    |
| accuracy  | 0.986028  |   0.460798    |
| precision | 0.83477   |   0.460798    |
| recall    | 1         |   0.000154792 |
| mcc       | 0.763249  |   0.396124    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0499869 |  nan        |
| auc       | 0.973869  |  nan        |
| f1        | 0.766772  |    0.460798 |
| accuracy  | 0.986028  |    0.460798 |
| precision | 0.83477   |    0.460798 |
| recall    | 0.709017  |    0.460798 |
| mcc       | 0.76231   |    0.460798 |


## Confusion matrix (at threshold=0.460798)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219254 |             1035 |
| Labeled as 1 |             2146 |             5229 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
