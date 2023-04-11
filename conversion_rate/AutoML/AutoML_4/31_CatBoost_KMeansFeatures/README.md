# Summary of 31_CatBoost_KMeansFeatures

[<< Go back](../README.md)


## CatBoost
- **n_jobs**: -1
- **learning_rate**: 0.2
- **depth**: 8
- **rsm**: 1.0
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

151.4 seconds

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0409304 | nan           |
| auc       | 0.98457   | nan           |
| f1        | 0.768277  |   0.485354    |
| accuracy  | 0.986424  |   0.485354    |
| precision | 0.847149  |   0.485354    |
| recall    | 1         |   6.77567e-07 |
| mcc       | 0.764871  |   0.485354    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0409304 |  nan        |
| auc       | 0.98457   |  nan        |
| f1        | 0.768277  |    0.485354 |
| accuracy  | 0.986424  |    0.485354 |
| precision | 0.847149  |    0.485354 |
| recall    | 0.702841  |    0.485354 |
| mcc       | 0.764871  |    0.485354 |


## Confusion matrix (at threshold=0.485354)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           246881 |             1040 |
| Labeled as 1 |             2437 |             5764 |

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
