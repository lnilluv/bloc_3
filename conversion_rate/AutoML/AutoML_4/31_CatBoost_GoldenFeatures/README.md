# Summary of 31_CatBoost_GoldenFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
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

136.7 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.040656 | nan           |
| auc       | 0.984836 | nan           |
| f1        | 0.767723 |   0.484089    |
| accuracy  | 0.986401 |   0.484089    |
| precision | 0.847218 |   0.484089    |
| recall    | 1        |   7.62606e-07 |
| mcc       | 0.764359 |   0.484089    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.040656 |  nan        |
| auc       | 0.984836 |  nan        |
| f1        | 0.767723 |    0.484089 |
| accuracy  | 0.986401 |    0.484089 |
| precision | 0.847218 |    0.484089 |
| recall    | 0.701866 |    0.484089 |
| mcc       | 0.764359 |    0.484089 |


## Confusion matrix (at threshold=0.484089)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246883 |             1038 |
| Labeled as 1 |             2445 |             5756 |

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
