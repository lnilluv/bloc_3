# Summary of 14_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eta**: 0.1
- **max_depth**: 6
- **min_child_weight**: 50
- **subsample**: 0.9
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

269.1 seconds

## Metric details
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0404173 | nan          |
| auc       | 0.985754  | nan          |
| f1        | 0.765202  |   0.49382    |
| accuracy  | 0.986311  |   0.49382    |
| precision | 0.848759  |   0.49382    |
| recall    | 1         |   2.4246e-05 |
| mcc       | 0.762149  |   0.49382    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0404173 |   nan       |
| auc       | 0.985754  |   nan       |
| f1        | 0.765202  |     0.49382 |
| accuracy  | 0.986311  |     0.49382 |
| precision | 0.848759  |     0.49382 |
| recall    | 0.696622  |     0.49382 |
| mcc       | 0.762149  |     0.49382 |


## Confusion matrix (at threshold=0.49382)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246903 |             1018 |
| Labeled as 1 |             2488 |             5713 |

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
