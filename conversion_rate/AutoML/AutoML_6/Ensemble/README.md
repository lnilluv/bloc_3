# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model              |   Weight |
|:-------------------|---------:|
| 27_CatBoost        |        1 |
| 29_CatBoost        |        1 |
| 3_Default_CatBoost |        7 |
| 5_Xgboost          |        1 |

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0413738 | nan           |
| auc       | 0.984294  | nan           |
| f1        | 0.767841  |   0.362213    |
| accuracy  | 0.986289  |   0.495048    |
| precision | 0.852525  |   0.495048    |
| recall    | 1         |   1.39368e-05 |
| mcc       | 0.763075  |   0.495048    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0413738 |  nan        |
| auc       | 0.984294  |  nan        |
| f1        | 0.765871  |    0.495048 |
| accuracy  | 0.986289  |    0.495048 |
| precision | 0.852525  |    0.495048 |
| recall    | 0.695207  |    0.495048 |
| mcc       | 0.763075  |    0.495048 |


## Confusion matrix (at threshold=0.495048)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           274296 |             1104 |
| Labeled as 1 |             2798 |             6382 |

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
