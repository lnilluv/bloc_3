# Summary of 67_CatBoost_GoldenFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
- **rsm**: 0.7
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

112.4 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0410607 | nan           |
| auc       | 0.984247  | nan           |
| f1        | 0.767732  |   0.477998    |
| accuracy  | 0.986409  |   0.477998    |
| precision | 0.847775  |   0.477998    |
| recall    | 1         |   1.35296e-05 |
| mcc       | 0.764418  |   0.477998    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0410607 |  nan        |
| auc       | 0.984247  |  nan        |
| f1        | 0.767732  |    0.477998 |
| accuracy  | 0.986409  |    0.477998 |
| precision | 0.847775  |    0.477998 |
| recall    | 0.7015    |    0.477998 |
| mcc       | 0.764418  |    0.477998 |


## Confusion matrix (at threshold=0.477998)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246888 |             1033 |
| Labeled as 1 |             2448 |             5753 |

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
