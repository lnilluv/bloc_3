# Summary of 38_RandomForest

[<< Go back](../README.md)


## Random Forest
- **n_jobs**: -1
- **criterion**: gini
- **max_features**: 0.7
- **min_samples_split**: 30
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

121.3 seconds

## Metric details
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0410439 |  nan        |
| auc       | 0.984633  |  nan        |
| f1        | 0.766869  |    0.485768 |
| accuracy  | 0.986362  |    0.485768 |
| precision | 0.847095  |    0.485768 |
| recall    | 0.999878  |    0        |
| mcc       | 0.76355   |    0.485768 |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0410439 |  nan        |
| auc       | 0.984633  |  nan        |
| f1        | 0.766869  |    0.485768 |
| accuracy  | 0.986362  |    0.485768 |
| precision | 0.847095  |    0.485768 |
| recall    | 0.700524  |    0.485768 |
| mcc       | 0.76355   |    0.485768 |


## Confusion matrix (at threshold=0.485768)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246884 |             1037 |
| Labeled as 1 |             2456 |             5745 |

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
