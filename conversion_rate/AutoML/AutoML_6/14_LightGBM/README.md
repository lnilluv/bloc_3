# Summary of 14_LightGBM

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 63
- **learning_rate**: 0.2
- **feature_fraction**: 0.5
- **bagging_fraction**: 1.0
- **min_data_in_leaf**: 10
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

93.2 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0416448 | nan           |
| auc       | 0.984909  | nan           |
| f1        | 0.764316  |   0.373024    |
| accuracy  | 0.986053  |   0.495692    |
| precision | 0.847817  |   0.495692    |
| recall    | 1         |   2.53455e-07 |
| mcc       | 0.758956  |   0.495692    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0416448 |  nan        |
| auc       | 0.984909  |  nan        |
| f1        | 0.761922  |    0.495692 |
| accuracy  | 0.986053  |    0.495692 |
| precision | 0.847817  |    0.495692 |
| recall    | 0.69183   |    0.495692 |
| mcc       | 0.758956  |    0.495692 |


## Confusion matrix (at threshold=0.495692)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           274260 |             1140 |
| Labeled as 1 |             2829 |             6351 |

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
