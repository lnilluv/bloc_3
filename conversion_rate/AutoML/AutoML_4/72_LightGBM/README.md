# Summary of 72_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 63
- **learning_rate**: 0.2
- **feature_fraction**: 0.8
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 10
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

161.0 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0422283 |  nan        |
| auc       | 0.981892  |  nan        |
| f1        | 0.765571  |    0.491559 |
| accuracy  | 0.986303  |    0.491559 |
| precision | 0.846961  |    0.491559 |
| recall    | 1         |    0        |
| mcc       | 0.762325  |    0.491559 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0422283 |  nan        |
| auc       | 0.981892  |  nan        |
| f1        | 0.765571  |    0.491559 |
| accuracy  | 0.986303  |    0.491559 |
| precision | 0.846961  |    0.491559 |
| recall    | 0.698451  |    0.491559 |
| mcc       | 0.762325  |    0.491559 |


## Confusion matrix (at threshold=0.491559)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246886 |             1035 |
| Labeled as 1 |             2473 |             5728 |

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
