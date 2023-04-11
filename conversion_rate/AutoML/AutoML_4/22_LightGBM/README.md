# Summary of 22_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 95
- **learning_rate**: 0.05
- **feature_fraction**: 1.0
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

246.8 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0412156 | nan           |
| auc       | 0.984323  | nan           |
| f1        | 0.764087  |   0.486011    |
| accuracy  | 0.986171  |   0.486011    |
| precision | 0.84192   |   0.486011    |
| recall    | 1         |   6.73201e-06 |
| mcc       | 0.760481  |   0.486011    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0412156 |  nan        |
| auc       | 0.984323  |  nan        |
| f1        | 0.764087  |    0.486011 |
| accuracy  | 0.986171  |    0.486011 |
| precision | 0.84192   |    0.486011 |
| recall    | 0.699427  |    0.486011 |
| mcc       | 0.760481  |    0.486011 |


## Confusion matrix (at threshold=0.486011)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246844 |             1077 |
| Labeled as 1 |             2465 |             5736 |

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
