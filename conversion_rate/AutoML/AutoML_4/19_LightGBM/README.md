# Summary of 19_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 15
- **learning_rate**: 0.05
- **feature_fraction**: 0.8
- **bagging_fraction**: 0.5
- **min_data_in_leaf**: 50
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

256.1 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0408117 | nan           |
| auc       | 0.985507  | nan           |
| f1        | 0.768496  |   0.46577     |
| accuracy  | 0.986366  |   0.46577     |
| precision | 0.842075  |   0.46577     |
| recall    | 1         |   4.62411e-06 |
| mcc       | 0.764631  |   0.46577     |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0408117 |   nan       |
| auc       | 0.985507  |   nan       |
| f1        | 0.768496  |     0.46577 |
| accuracy  | 0.986366  |     0.46577 |
| precision | 0.842075  |     0.46577 |
| recall    | 0.706743  |     0.46577 |
| mcc       | 0.764631  |     0.46577 |


## Confusion matrix (at threshold=0.46577)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246834 |             1087 |
| Labeled as 1 |             2405 |             5796 |

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
