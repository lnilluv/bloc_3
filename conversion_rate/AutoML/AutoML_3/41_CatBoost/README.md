# Summary of 41_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 8
- **rsm**: 1
- **loss_function**: Logloss
- **eval_metric**: F1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

121.2 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0418696 | nan           |
| auc       | 0.983774  | nan           |
| f1        | 0.768557  |   0.406071    |
| accuracy  | 0.986177  |   0.494452    |
| precision | 0.850464  |   0.494452    |
| recall    | 1         |   1.08036e-06 |
| mcc       | 0.762686  |   0.406071    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0418696 |  nan        |
| auc       | 0.983774  |  nan        |
| f1        | 0.765272  |    0.494452 |
| accuracy  | 0.986177  |    0.494452 |
| precision | 0.850464  |    0.494452 |
| recall    | 0.695593  |    0.494452 |
| mcc       | 0.762293  |    0.494452 |


## Confusion matrix (at threshold=0.494452)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219387 |              902 |
| Labeled as 1 |             2245 |             5130 |

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
