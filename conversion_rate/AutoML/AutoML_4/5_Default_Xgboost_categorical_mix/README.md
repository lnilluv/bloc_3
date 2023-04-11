# Summary of 5_Default_Xgboost_categorical_mix

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

219.5 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0608684 | nan           |
| auc       | 0.967081  | nan           |
| f1        | 0.758852  |   0.283535    |
| accuracy  | 0.986116  |   0.541039    |
| precision | 0.862494  |   0.541039    |
| recall    | 1         |   2.88216e-06 |
| mcc       | 0.755593  |   0.541039    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0608684 |  nan        |
| auc       | 0.967081  |  nan        |
| f1        | 0.756572  |    0.541039 |
| accuracy  | 0.986116  |    0.541039 |
| precision | 0.862494  |    0.541039 |
| recall    | 0.67382   |    0.541039 |
| mcc       | 0.755593  |    0.541039 |


## Confusion matrix (at threshold=0.541039)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           247040 |              881 |
| Labeled as 1 |             2675 |             5526 |

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
