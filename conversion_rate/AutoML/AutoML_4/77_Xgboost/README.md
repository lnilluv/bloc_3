# Summary of 77_Xgboost

[<< Go back](../README.md)


## Extreme Gradient Boosting (Xgboost)
- **n_jobs**: -1
- **objective**: binary:logistic
- **eta**: 0.075
- **max_depth**: 8
- **min_child_weight**: 10
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

228.4 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0471518 | nan           |
| auc       | 0.975642  | nan           |
| f1        | 0.767542  |   0.491245    |
| accuracy  | 0.986354  |   0.491245    |
| precision | 0.844308  |   0.491245    |
| recall    | 1         |   2.41283e-05 |
| mcc       | 0.76393   |   0.491245    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0471518 |  nan        |
| auc       | 0.975642  |  nan        |
| f1        | 0.767542  |    0.491245 |
| accuracy  | 0.986354  |    0.491245 |
| precision | 0.844308  |    0.491245 |
| recall    | 0.703573  |    0.491245 |
| mcc       | 0.76393   |    0.491245 |


## Confusion matrix (at threshold=0.491245)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246857 |             1064 |
| Labeled as 1 |             2431 |             5770 |

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
