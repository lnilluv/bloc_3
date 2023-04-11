# Summary of 73_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.8
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 20
- **metric**: custom
- **custom_eval_metric_name**: f1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

263.9 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0411532 | nan           |
| auc       | 0.984646  | nan           |
| f1        | 0.766227  |   0.485571    |
| accuracy  | 0.986303  |   0.485571    |
| precision | 0.84482   |   0.485571    |
| recall    | 1         |   8.64293e-06 |
| mcc       | 0.762744  |   0.485571    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0411532 |  nan        |
| auc       | 0.984646  |  nan        |
| f1        | 0.766227  |    0.485571 |
| accuracy  | 0.986303  |    0.485571 |
| precision | 0.84482   |    0.485571 |
| recall    | 0.701012  |    0.485571 |
| mcc       | 0.762744  |    0.485571 |


## Confusion matrix (at threshold=0.485571)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246865 |             1056 |
| Labeled as 1 |             2452 |             5749 |

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
