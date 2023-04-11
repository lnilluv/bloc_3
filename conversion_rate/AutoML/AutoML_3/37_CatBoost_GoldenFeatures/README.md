# Summary of 37_CatBoost_GoldenFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 7
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

116.6 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0413209 | nan           |
| auc       | 0.984712  | nan           |
| f1        | 0.769109  |   0.420951    |
| accuracy  | 0.986058  |   0.468035    |
| precision | 0.838845  |   0.468035    |
| recall    | 1         |   7.10057e-07 |
| mcc       | 0.76353   |   0.420951    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0413209 |  nan        |
| auc       | 0.984712  |  nan        |
| f1        | 0.766171  |    0.468035 |
| accuracy  | 0.986058  |    0.468035 |
| precision | 0.838845  |    0.468035 |
| recall    | 0.705085  |    0.468035 |
| mcc       | 0.762084  |    0.468035 |


## Confusion matrix (at threshold=0.468035)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219290 |              999 |
| Labeled as 1 |             2175 |             5200 |

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
