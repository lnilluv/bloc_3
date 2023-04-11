# Summary of 30_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
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

137.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0403753 | nan           |
| auc       | 0.985552  | nan           |
| f1        | 0.767503  |   0.489271    |
| accuracy  | 0.986424  |   0.489271    |
| precision | 0.849719  |   0.489271    |
| recall    | 1         |   7.97636e-07 |
| mcc       | 0.764382  |   0.489271    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0403753 |  nan        |
| auc       | 0.985552  |  nan        |
| f1        | 0.767503  |    0.489271 |
| accuracy  | 0.986424  |    0.489271 |
| precision | 0.849719  |    0.489271 |
| recall    | 0.699793  |    0.489271 |
| mcc       | 0.764382  |    0.489271 |


## Confusion matrix (at threshold=0.489271)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246906 |             1015 |
| Labeled as 1 |             2462 |             5739 |

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
