# Summary of 39_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.8
- **min_samples_split**: 40
- **max_depth**: 3
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

100.2 seconds

## Metric details
|           |     score |    threshold |
|:----------|----------:|-------------:|
| logloss   | 0.0501237 | nan          |
| auc       | 0.960507  | nan          |
| f1        | 0.756795  |   0.443986   |
| accuracy  | 0.985116  |   0.443986   |
| precision | 0.793657  |   0.443986   |
| recall    | 1         |   0.00128037 |
| mcc       | 0.749996  |   0.443986   |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0501237 |  nan        |
| auc       | 0.960507  |  nan        |
| f1        | 0.756795  |    0.443986 |
| accuracy  | 0.985116  |    0.443986 |
| precision | 0.793657  |    0.443986 |
| recall    | 0.723204  |    0.443986 |
| mcc       | 0.749996  |    0.443986 |


## Confusion matrix (at threshold=0.443986)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246379 |             1542 |
| Labeled as 1 |             2270 |             5931 |

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
