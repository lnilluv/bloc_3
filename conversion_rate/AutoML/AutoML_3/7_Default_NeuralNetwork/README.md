# Summary of 7_Default_NeuralNetwork

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

427.3 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0426755 | nan           |
| auc       | 0.983105  | nan           |
| f1        | 0.767627  |   0.427937    |
| accuracy  | 0.985979  |   0.545938    |
| precision | 0.854071  |   0.545938    |
| recall    | 1         |   1.50782e-11 |
| mcc       | 0.761085  |   0.427937    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0426755 |  nan        |
| auc       | 0.983105  |  nan        |
| f1        | 0.759675  |    0.545938 |
| accuracy  | 0.985979  |    0.545938 |
| precision | 0.854071  |    0.545938 |
| recall    | 0.684068  |    0.545938 |
| mcc       | 0.757466  |    0.545938 |


## Confusion matrix (at threshold=0.545938)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219427 |              862 |
| Labeled as 1 |             2330 |             5045 |

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
