# Summary of 42_LightGBM_Stacked

[<< Go back](../README.md)


## LightGBM
- **n_jobs**: -1
- **objective**: binary
- **num_leaves**: 31
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

230.0 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0419113 | nan           |
| auc       | 0.983301  | nan           |
| f1        | 0.768568  |   0.401469    |
| accuracy  | 0.986168  |   0.502444    |
| precision | 0.849141  |   0.502444    |
| recall    | 1         |   1.81968e-06 |
| mcc       | 0.762677  |   0.401469    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0419113 |  nan        |
| auc       | 0.983301  |  nan        |
| f1        | 0.765473  |    0.502444 |
| accuracy  | 0.986168  |    0.502444 |
| precision | 0.849141  |    0.502444 |
| recall    | 0.696814  |    0.502444 |
| mcc       | 0.762355  |    0.502444 |


## Confusion matrix (at threshold=0.502444)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219376 |              913 |
| Labeled as 1 |             2236 |             5139 |

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
