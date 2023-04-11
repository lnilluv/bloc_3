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

33.1 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0469401 | nan           |
| auc       | 0.96922   | nan           |
| f1        | 0.741575  |   0.369219    |
| accuracy  | 0.985189  |   0.411067    |
| precision | 0.866911  |   0.411067    |
| recall    | 1         |   0.000823384 |
| mcc       | 0.738531  |   0.411067    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0469401 |  nan        |
| auc       | 0.96922   |  nan        |
| f1        | 0.737178  |    0.411067 |
| accuracy  | 0.985189  |    0.411067 |
| precision | 0.866911  |    0.411067 |
| recall    | 0.64122   |    0.411067 |
| mcc       | 0.738531  |    0.411067 |


## Confusion matrix (at threshold=0.411067)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219563 |              726 |
| Labeled as 1 |             2646 |             4729 |

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
