# Summary of 40_CatBoost_GoldenFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 4
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

102.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0419546 | nan           |
| auc       | 0.983444  | nan           |
| f1        | 0.770485  |   0.408912    |
| accuracy  | 0.986173  |   0.480562    |
| precision | 0.843379  |   0.480562    |
| recall    | 1         |   2.16955e-06 |
| mcc       | 0.764449  |   0.408912    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0419546 |  nan        |
| auc       | 0.983444  |  nan        |
| f1        | 0.767332  |    0.480562 |
| accuracy  | 0.986173  |    0.480562 |
| precision | 0.843379  |    0.480562 |
| recall    | 0.703864  |    0.480562 |
| mcc       | 0.763569  |    0.480562 |


## Confusion matrix (at threshold=0.480562)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219325 |              964 |
| Labeled as 1 |             2184 |             5191 |

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
