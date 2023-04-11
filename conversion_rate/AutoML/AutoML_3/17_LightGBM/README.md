# Summary of 17_LightGBM

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

256.8 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0415476 | nan           |
| auc       | 0.984371  | nan           |
| f1        | 0.768571  |   0.394415    |
| accuracy  | 0.986045  |   0.457321    |
| precision | 0.833069  |   0.457321    |
| recall    | 1         |   3.65313e-06 |
| mcc       | 0.763063  |   0.457321    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0415476 |  nan        |
| auc       | 0.984371  |  nan        |
| f1        | 0.767712  |    0.457321 |
| accuracy  | 0.986045  |    0.457321 |
| precision | 0.833069  |    0.457321 |
| recall    | 0.711864  |    0.457321 |
| mcc       | 0.763063  |    0.457321 |


## Confusion matrix (at threshold=0.457321)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219237 |             1052 |
| Labeled as 1 |             2125 |             5250 |

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
