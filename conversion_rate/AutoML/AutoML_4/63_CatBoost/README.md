# Summary of 63_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
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

133.1 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0404595 | nan           |
| auc       | 0.985356  | nan           |
| f1        | 0.769118  |   0.487996    |
| accuracy  | 0.986526  |   0.487996    |
| precision | 0.85206   |   0.487996    |
| recall    | 1         |   1.25329e-06 |
| mcc       | 0.766104  |   0.487996    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0404595 |  nan        |
| auc       | 0.985356  |  nan        |
| f1        | 0.769118  |    0.487996 |
| accuracy  | 0.986526  |    0.487996 |
| precision | 0.85206   |    0.487996 |
| recall    | 0.70089   |    0.487996 |
| mcc       | 0.766104  |    0.487996 |


## Confusion matrix (at threshold=0.487996)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246923 |              998 |
| Labeled as 1 |             2453 |             5748 |

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
