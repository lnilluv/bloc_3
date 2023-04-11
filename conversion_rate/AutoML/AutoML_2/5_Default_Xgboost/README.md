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
- **eval_metric**: logloss
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
logloss

## Training time

50.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0405873 | nan           |
| auc       | 0.985585  | nan           |
| f1        | 0.769274  |   0.360761    |
| accuracy  | 0.986269  |   0.499154    |
| precision | 0.85474   |   0.504407    |
| recall    | 1         |   1.68796e-05 |
| mcc       | 0.763247  |   0.412507    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0405873 |  nan        |
| auc       | 0.985585  |  nan        |
| f1        | 0.763218  |    0.499154 |
| accuracy  | 0.986269  |    0.499154 |
| precision | 0.854043  |    0.499154 |
| recall    | 0.689853  |    0.499154 |
| mcc       | 0.760803  |    0.499154 |


## Confusion matrix (at threshold=0.499154)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219500 |              861 |
| Labeled as 1 |             2265 |             5038 |

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
