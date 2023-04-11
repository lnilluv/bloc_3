# Summary of 40_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: entropy
- **max_features**: 0.6
- **min_samples_split**: 50
- **max_depth**: 6
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

116.7 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0416303 |   nan       |
| auc       | 0.984693  |   nan       |
| f1        | 0.764448  |     0.47929 |
| accuracy  | 0.986155  |     0.47929 |
| precision | 0.839632  |     0.47929 |
| recall    | 0.999878  |     0       |
| mcc       | 0.760617  |     0.47929 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0416303 |   nan       |
| auc       | 0.984693  |   nan       |
| f1        | 0.764448  |     0.47929 |
| accuracy  | 0.986155  |     0.47929 |
| precision | 0.839632  |     0.47929 |
| recall    | 0.701622  |     0.47929 |
| mcc       | 0.760617  |     0.47929 |


## Confusion matrix (at threshold=0.47929)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246822 |             1099 |
| Labeled as 1 |             2447 |             5754 |

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
