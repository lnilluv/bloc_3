# Summary of 26_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 0.7
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

70.2 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0410815 | nan           |
| auc       | 0.984889  | nan           |
| f1        | 0.768213  |   0.362335    |
| accuracy  | 0.986183  |   0.496153    |
| precision | 0.852973  |   0.496153    |
| recall    | 1         |   8.03932e-06 |
| mcc       | 0.761057  |   0.362335    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0410815 |  nan        |
| auc       | 0.984889  |  nan        |
| f1        | 0.763332  |    0.496153 |
| accuracy  | 0.986183  |    0.496153 |
| precision | 0.852973  |    0.496153 |
| recall    | 0.690741  |    0.496153 |
| mcc       | 0.760765  |    0.496153 |


## Confusion matrix (at threshold=0.496153)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           274307 |             1093 |
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
