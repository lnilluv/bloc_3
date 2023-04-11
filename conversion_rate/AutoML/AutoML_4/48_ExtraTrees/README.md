# Summary of 48_ExtraTrees

[<< Go back](../README.md)


## Extra Trees Classifier (Extra Trees)
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
- **min_samples_split**: 40
- **max_depth**: 3
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

96.2 seconds

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.057602 | nan          |
| auc       | 0.981288 | nan          |
| f1        | 0.711885 |   0.148233   |
| accuracy  | 0.984101 |   0.320678   |
| precision | 0.889896 |   0.320678   |
| recall    | 1        |   0.00030002 |
| mcc       | 0.70799  |   0.320678   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.057602 |  nan        |
| auc       | 0.981288 |  nan        |
| f1        | 0.698281 |    0.320678 |
| accuracy  | 0.984101 |    0.320678 |
| precision | 0.889896 |    0.320678 |
| recall    | 0.574564 |    0.320678 |
| mcc       | 0.70799  |    0.320678 |


## Confusion matrix (at threshold=0.320678)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           247338 |              583 |
| Labeled as 1 |             3489 |             4712 |

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
