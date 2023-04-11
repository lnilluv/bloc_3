# Summary of 6_Default_CatBoost_GoldenFeatures

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

140.7 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0416281 | nan           |
| auc       | 0.983868  | nan           |
| f1        | 0.769905  |   0.413661    |
| accuracy  | 0.986111  |   0.459596    |
| precision | 0.837959  |   0.459596    |
| recall    | 1         |   2.67721e-06 |
| mcc       | 0.764083  |   0.413661    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0416281 |  nan        |
| auc       | 0.983868  |  nan        |
| f1        | 0.767637  |    0.459596 |
| accuracy  | 0.986111  |    0.459596 |
| precision | 0.837959  |    0.459596 |
| recall    | 0.708203  |    0.459596 |
| mcc       | 0.763391  |    0.459596 |


## Confusion matrix (at threshold=0.459596)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219279 |             1010 |
| Labeled as 1 |             2152 |             5223 |

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
