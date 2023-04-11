# Summary of 4_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

36.5 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.042063 | nan           |
| auc       | 0.985031 | nan           |
| f1        | 0.769054 |   0.312276    |
| accuracy  | 0.986085 |   0.377325    |
| precision | 0.833658 |   0.377325    |
| recall    | 1        |   6.07655e-09 |
| mcc       | 0.762493 |   0.312276    |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.042063 |  nan        |
| auc       | 0.985031 |  nan        |
| f1        | 0.764145 |    0.377325 |
| accuracy  | 0.986085 |    0.377325 |
| precision | 0.833658 |    0.377325 |
| recall    | 0.705333 |    0.377325 |
| mcc       | 0.759836 |    0.377325 |


## Confusion matrix (at threshold=0.377325)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |            54841 |              256 |
| Labeled as 1 |              536 |             1283 |

## Learning curves
![Learning curves](learning_curves.png)

## Permutation-based Importance
![Permutation-based Importance](permutation_importance.png)
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
