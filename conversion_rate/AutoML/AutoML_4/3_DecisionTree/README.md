# Summary of 3_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 4
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

37.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0460664 | nan           |
| auc       | 0.969676  | nan           |
| f1        | 0.73861   |   0.195836    |
| accuracy  | 0.98548   |   0.478417    |
| precision | 0.872754  |   0.478417    |
| recall    | 1         |   0.000763399 |
| mcc       | 0.740389  |   0.478417    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0460664 |  nan        |
| auc       | 0.969676  |  nan        |
| f1        | 0.738338  |    0.478417 |
| accuracy  | 0.98548   |    0.478417 |
| precision | 0.872754  |    0.478417 |
| recall    | 0.6398    |    0.478417 |
| mcc       | 0.740389  |    0.478417 |


## Confusion matrix (at threshold=0.478417)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           247156 |              765 |
| Labeled as 1 |             2954 |             5247 |

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
