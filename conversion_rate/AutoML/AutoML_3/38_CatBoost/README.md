# Summary of 38_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 5
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

103.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0411708 | nan           |
| auc       | 0.98483   | nan           |
| f1        | 0.770498  |   0.417989    |
| accuracy  | 0.986129  |   0.482934    |
| precision | 0.846166  |   0.482934    |
| recall    | 1         |   5.38698e-06 |
| mcc       | 0.765082  |   0.417989    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0411708 |  nan        |
| auc       | 0.98483   |  nan        |
| f1        | 0.765483  |    0.482934 |
| accuracy  | 0.986129  |    0.482934 |
| precision | 0.846166  |    0.482934 |
| recall    | 0.698847  |    0.482934 |
| mcc       | 0.762089  |    0.482934 |


## Confusion matrix (at threshold=0.482934)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219352 |              937 |
| Labeled as 1 |             2221 |             5154 |

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
