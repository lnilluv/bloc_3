# Summary of 42_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 1.0
- **min_samples_split**: 40
- **max_depth**: 7
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

148.0 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0414838 |   nan       |
| auc       | 0.983205  |   nan       |
| f1        | 0.768005  |     0.48905 |
| accuracy  | 0.986354  |     0.48905 |
| precision | 0.842803  |     0.48905 |
| recall    | 0.998537  |     0       |
| mcc       | 0.764233  |     0.48905 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0414838 |   nan       |
| auc       | 0.983205  |   nan       |
| f1        | 0.768005  |     0.48905 |
| accuracy  | 0.986354  |     0.48905 |
| precision | 0.842803  |     0.48905 |
| recall    | 0.705402  |     0.48905 |
| mcc       | 0.764233  |     0.48905 |


## Confusion matrix (at threshold=0.48905)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246842 |             1079 |
| Labeled as 1 |             2416 |             5785 |

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
