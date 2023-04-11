# Summary of Ensemble_Stacked

[<< Go back](../README.md)


## Ensemble structure
| Model                              |   Weight |
|:-----------------------------------|---------:|
| 36_CatBoost_GoldenFeatures_Stacked |       23 |
| 38_CatBoost                        |        1 |

## Metric details
|           |     score |     threshold |
|:----------|----------:|--------------:|
| logloss   | 0.0751947 | nan           |
| auc       | 0.962094  | nan           |
| f1        | 0.768558  |   0.397922    |
| accuracy  | 0.986155  |   0.485092    |
| precision | 0.840729  |   0.485092    |
| recall    | 1         |   1.46915e-05 |
| mcc       | 0.763738  |   0.485092    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.0751947 |  nan        |
| auc       | 0.962094  |  nan        |
| f1        | 0.767757  |    0.485092 |
| accuracy  | 0.986155  |    0.485092 |
| precision | 0.840729  |    0.485092 |
| recall    | 0.706441  |    0.485092 |
| mcc       | 0.763738  |    0.485092 |


## Confusion matrix (at threshold=0.485092)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |           219302 |              987 |
| Labeled as 1 |             2165 |             5210 |

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
