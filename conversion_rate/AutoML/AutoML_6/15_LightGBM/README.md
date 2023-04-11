# Summary of 15_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 63
- **learning_rate**: 0.05
- **feature_fraction**: 0.9
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 20
- **metric**: custom
- **custom_eval_metric_name**: f1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **k_folds**: 4
 - **shuffle**: False
 - **stratify**: True

## Optimized metric
f1

## Training time

138.3 seconds

## Metric details
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0414413 | nan          |
| auc       | 0.984669  | nan          |
| f1        | 0.766801  |   0.373993   |
| accuracy  | 0.986067  |   0.498231   |
| precision | 0.846052  |   0.498231   |
| recall    | 1         |   3.8106e-06 |
| mcc       | 0.759974  |   0.373993   |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0414413 |  nan        |
| auc       | 0.984669  |  nan        |
| f1        | 0.762788  |    0.498231 |
| accuracy  | 0.986067  |    0.498231 |
| precision | 0.846052  |    0.498231 |
| recall    | 0.694444  |    0.498231 |
| mcc       | 0.759595  |    0.498231 |


## Confusion matrix (at threshold=0.498231)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           274240 |             1160 |
| Labeled as 1 |             2805 |             6375 |

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
