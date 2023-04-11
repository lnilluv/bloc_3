# Summary of 32_CatBoost

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
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

116.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0406325 | nan           |
| auc       | 0.984888  | nan           |
| f1        | 0.767312  |   0.490686    |
| accuracy  | 0.986448  |   0.490686    |
| precision | 0.852144  |   0.490686    |
| recall    | 1         |   3.42192e-06 |
| mcc       | 0.764431  |   0.490686    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0406325 |  nan        |
| auc       | 0.984888  |  nan        |
| f1        | 0.767312  |    0.490686 |
| accuracy  | 0.986448  |    0.490686 |
| precision | 0.852144  |    0.490686 |
| recall    | 0.697842  |    0.490686 |
| mcc       | 0.764431  |    0.490686 |


## Confusion matrix (at threshold=0.490686)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246928 |              993 |
| Labeled as 1 |             2478 |             5723 |

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
