# Summary of 46_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.5
- **min_samples_split**: 20
- **max_depth**: 4
- **eval_metric_name**: f1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

88.6 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0842188 |  nan        |
| auc       | 0.842518  |  nan        |
| f1        | 0.622994  |    0.355931 |
| accuracy  | 0.978541  |    0.355931 |
| precision | 0.71209   |    0.355931 |
| recall    | 1         |    0        |
| mcc       | 0.617263  |    0.355931 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0842188 |  nan        |
| auc       | 0.842518  |  nan        |
| f1        | 0.622994  |    0.355931 |
| accuracy  | 0.978541  |    0.355931 |
| precision | 0.71209   |    0.355931 |
| recall    | 0.553713  |    0.355931 |
| mcc       | 0.617263  |    0.355931 |


## Confusion matrix (at threshold=0.355931)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246085 |             1836 |
| Labeled as 1 |             3660 |             4541 |

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
