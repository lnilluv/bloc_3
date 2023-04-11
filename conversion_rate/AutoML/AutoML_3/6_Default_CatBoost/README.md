# Summary of 6_Default_CatBoost

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.1
- **depth**: 6
- **rsm**: 1
- **loss_function**: Logloss
- **eval_metric**: F1
- **explain_level**: 0

## Validation
 - **validation_type**: kfold
 - **shuffle**: True
 - **stratify**: True
 - **k_folds**: 10

## Optimized metric
f1

## Training time

112.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0413733 | nan           |
| auc       | 0.984219  | nan           |
| f1        | 0.769659  |   0.399281    |
| accuracy  | 0.986173  |   0.465313    |
| precision | 0.840612  |   0.465313    |
| recall    | 1         |   1.62315e-06 |
| mcc       | 0.764134  |   0.465313    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0413733 |  nan        |
| auc       | 0.984219  |  nan        |
| f1        | 0.768189  |    0.465313 |
| accuracy  | 0.986173  |    0.465313 |
| precision | 0.840612  |    0.465313 |
| recall    | 0.707254  |    0.465313 |
| mcc       | 0.764134  |    0.465313 |


## Confusion matrix (at threshold=0.465313)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219300 |              989 |
| Labeled as 1 |             2159 |             5216 |

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
