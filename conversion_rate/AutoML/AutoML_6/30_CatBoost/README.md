# Summary of 30_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.025
- **depth**: 7
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

102.2 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.163273 | nan           |
| auc       | 0.937636 | nan           |
| f1        | 0.758514 |   0.496582    |
| accuracy  | 0.985772 |   0.496582    |
| precision | 0.838144 |   0.496582    |
| recall    | 1        |   1.62245e-05 |
| mcc       | 0.754876 |   0.496582    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.163273 |  nan        |
| auc       | 0.937636 |  nan        |
| f1        | 0.758514 |    0.496582 |
| accuracy  | 0.985772 |    0.496582 |
| precision | 0.838144 |    0.496582 |
| recall    | 0.692702 |    0.496582 |
| mcc       | 0.754876 |    0.496582 |


## Confusion matrix (at threshold=0.496582)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           274172 |             1228 |
| Labeled as 1 |             2821 |             6359 |

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
