# Summary of 31_CatBoost

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

118.3 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0404245 | nan           |
| auc       | 0.985468  | nan           |
| f1        | 0.768256  |   0.486237    |
| accuracy  | 0.986432  |   0.486237    |
| precision | 0.847807  |   0.486237    |
| recall    | 1         |   2.51889e-06 |
| mcc       | 0.764911  |   0.486237    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0404245 |  nan        |
| auc       | 0.985468  |  nan        |
| f1        | 0.768256  |    0.486237 |
| accuracy  | 0.986432  |    0.486237 |
| precision | 0.847807  |    0.486237 |
| recall    | 0.702353  |    0.486237 |
| mcc       | 0.764911  |    0.486237 |


## Confusion matrix (at threshold=0.486237)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246887 |             1034 |
| Labeled as 1 |             2441 |             5760 |

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
