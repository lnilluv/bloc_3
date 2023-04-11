# Summary of 29_CatBoost

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
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

147.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.040383 | nan           |
| auc       | 0.985623 | nan           |
| f1        | 0.767534 |   0.486996    |
| accuracy  | 0.986424 |   0.486996    |
| precision | 0.849615 |   0.486996    |
| recall    | 1        |   1.85471e-06 |
| mcc       | 0.764401 |   0.486996    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.040383 |  nan        |
| auc       | 0.985623 |  nan        |
| f1        | 0.767534 |    0.486996 |
| accuracy  | 0.986424 |    0.486996 |
| precision | 0.849615 |    0.486996 |
| recall    | 0.699915 |    0.486996 |
| mcc       | 0.764401 |    0.486996 |


## Confusion matrix (at threshold=0.486996)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246905 |             1016 |
| Labeled as 1 |             2461 |             5740 |

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
