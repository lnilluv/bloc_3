# Summary of 23_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 8
- **rsm**: 1.0
- **loss_function**: Logloss
- **eval_metric**: F1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **k_folds**: 4
 - **shuffle**: False
 - **stratify**: True

## Optimized metric
f1

## Training time

80.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0412137 | nan           |
| auc       | 0.984479  | nan           |
| f1        | 0.768195  |   0.370272    |
| accuracy  | 0.986162  |   0.496642    |
| precision | 0.852285  |   0.496642    |
| recall    | 1         |   1.50395e-06 |
| mcc       | 0.761368  |   0.370272    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0412137 |  nan        |
| auc       | 0.984479  |  nan        |
| f1        | 0.763057  |    0.496642 |
| accuracy  | 0.986162  |    0.496642 |
| precision | 0.852285  |    0.496642 |
| recall    | 0.690741  |    0.496642 |
| mcc       | 0.760442  |    0.496642 |


## Confusion matrix (at threshold=0.496642)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           274301 |             1099 |
| Labeled as 1 |             2839 |             6341 |

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
