# Summary of 1_DecisionTree

[<< Go back](../README.md)


## Decision Tree
- **n_jobs**: -1
- **criterion**: gini
- **max_depth**: 3
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

37.9 seconds

## Metric details
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0500671 | nan          |
| auc       | 0.955139  | nan          |
| f1        | 0.732919  |   0.348994   |
| accuracy  | 0.985058  |   0.348994   |
| precision | 0.856886  |   0.348994   |
| recall    | 1         |   0.00200945 |
| mcc       | 0.733559  |   0.348994   |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0500671 |  nan        |
| auc       | 0.955139  |  nan        |
| f1        | 0.732919  |    0.348994 |
| accuracy  | 0.985058  |    0.348994 |
| precision | 0.856886  |    0.348994 |
| recall    | 0.640288  |    0.348994 |
| mcc       | 0.733559  |    0.348994 |


## Confusion matrix (at threshold=0.348994)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           247044 |              877 |
| Labeled as 1 |             2950 |             5251 |

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
