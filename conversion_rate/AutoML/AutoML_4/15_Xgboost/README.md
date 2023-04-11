# Summary of 15_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eta**: 0.1
- **max_depth**: 4
- **min_child_weight**: 25
- **subsample**: 0.7
- **colsample_bytree**: 0.7
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

265.9 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0402592 | nan           |
| auc       | 0.985852  | nan           |
| f1        | 0.766814  |   0.490785    |
| accuracy  | 0.986381  |   0.490785    |
| precision | 0.848749  |   0.490785    |
| recall    | 1         |   2.45086e-05 |
| mcc       | 0.76365   |   0.490785    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0402592 |  nan        |
| auc       | 0.985852  |  nan        |
| f1        | 0.766814  |    0.490785 |
| accuracy  | 0.986381  |    0.490785 |
| precision | 0.848749  |    0.490785 |
| recall    | 0.699305  |    0.490785 |
| mcc       | 0.76365   |    0.490785 |


## Confusion matrix (at threshold=0.490785)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246899 |             1022 |
| Labeled as 1 |             2466 |             5735 |

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
