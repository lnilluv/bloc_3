# Summary of 39_CatBoost

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
| logloss   | 0.0410716 | nan           |
| auc       | 0.985052  | nan           |
| f1        | 0.769862  |   0.419142    |
| accuracy  | 0.986173  |   0.496818    |
| precision | 0.849628  |   0.496818    |
| recall    | 1         |   1.74965e-06 |
| mcc       | 0.764241  |   0.419142    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0410716 |  nan        |
| auc       | 0.985052  |  nan        |
| f1        | 0.765425  |    0.496818 |
| accuracy  | 0.986173  |    0.496818 |
| precision | 0.849628  |    0.496818 |
| recall    | 0.696407  |    0.496818 |
| mcc       | 0.762356  |    0.496818 |


## Confusion matrix (at threshold=0.496818)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219380 |              909 |
| Labeled as 1 |             2239 |             5136 |

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
