## Error for 80_CatBoost

bad allocation
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 233, in train
    learner.fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\catboost\core.py", line 5128, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\catboost\core.py", line 2355, in _fit
    self._train(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\catboost\core.py", line 1759, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 4623, in _catboost._CatBoost._train
  File "_catboost.pyx", line 4672, in _catboost._CatBoost._train
_catboost.CatBoostError: bad allocation


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 81_CatBoost

bad allocation
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 233, in train
    learner.fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\algorithms\catboost.py", line 225, in fit
    self.model.fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\catboost\core.py", line 5128, in fit
    self._fit(X, y, cat_features, text_features, embedding_features, None, sample_weight, None, None, None, None, baseline, use_best_model,
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\catboost\core.py", line 2355, in _fit
    self._train(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\catboost\core.py", line 1759, in _train
    self._object._train(train_pool, test_pool, params, allow_clear_pool, init_model._object if init_model else None)
  File "_catboost.pyx", line 4623, in _catboost._CatBoost._train
  File "_catboost.pyx", line 4672, in _catboost._CatBoost._train
_catboost.CatBoostError: bad allocation


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 83_LightGBM

Unable to allocate 3.52 MiB for an array with shape (461018,) and data type float64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 233, in train
    learner.fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\algorithms\lightgbm.py", line 237, in fit
    self.model = lgb.train(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\lightgbm\engine.py", line 298, in train
    evaluation_result_list.extend(booster.eval_train(feval))
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\lightgbm\basic.py", line 3238, in eval_train
    return self.__inner_eval(self._train_data_name, 0, feval)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\lightgbm\basic.py", line 3809, in __inner_eval
    feval_ret = eval_function(self.__inner_predict(data_idx), cur_data)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\metric.py", line 208, in lightgbm_eval_metric_f1
    return "f1", -negative_f1(target, preds, weight), True
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\metric.py", line 67, in negative_f1
    val = f1_score(y_true, y_predicted, sample_weight=sample_weight, average=average)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\metrics\_classification.py", line 1136, in f1_score
    return fbeta_score(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\metrics\_classification.py", line 1277, in fbeta_score
    _, _, f, _ = precision_recall_fscore_support(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\metrics\_classification.py", line 1567, in precision_recall_fscore_support
    MCM = multilabel_confusion_matrix(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\metrics\_classification.py", line 479, in multilabel_confusion_matrix
    y_type, y_true, y_pred = _check_targets(y_true, y_pred)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\metrics\_classification.py", line 111, in _check_targets
    unique_values = np.union1d(y_true, y_pred)
  File "<__array_function__ internals>", line 180, in union1d
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\numpy\lib\arraysetops.py", line 781, in union1d
    return unique(np.concatenate((ar1, ar2), axis=None))
  File "<__array_function__ internals>", line 180, in unique
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\numpy\lib\arraysetops.py", line 274, in unique
    ret = _unique1d(ar, return_index, return_inverse, return_counts,
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\numpy\lib\arraysetops.py", line 328, in _unique1d
    ar = np.asanyarray(ar).flatten()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.52 MiB for an array with shape (461018,) and data type float64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 84_LightGBM

Unable to allocate 1.76 MiB for an array with shape (230509,) and data type float64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1239, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1432, in _get_listlike_indexer
    keyarr, indexer = ax._get_indexer_strict(key, axis_name)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6106, in _get_indexer_strict
    indexer = self.get_indexer_for(keyarr)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6093, in get_indexer_for
    return self.get_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 3974, in get_indexer
    return self._get_indexer(target, method, limit, tolerance)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\range.py", line 421, in _get_indexer
    locs[valid] = locs[valid] / step
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.76 MiB for an array with shape (230509,) and data type float64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 85_RandomForest

Unable to allocate 1.76 MiB for an array with shape (230509,) and data type float64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1239, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1432, in _get_listlike_indexer
    keyarr, indexer = ax._get_indexer_strict(key, axis_name)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6106, in _get_indexer_strict
    indexer = self.get_indexer_for(keyarr)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6093, in get_indexer_for
    return self.get_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 3974, in get_indexer
    return self._get_indexer(target, method, limit, tolerance)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\range.py", line 421, in _get_indexer
    locs[valid] = locs[valid] / step
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.76 MiB for an array with shape (230509,) and data type float64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 86_RandomForest

Unable to allocate 1.76 MiB for an array with shape (230509,) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1239, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1432, in _get_listlike_indexer
    keyarr, indexer = ax._get_indexer_strict(key, axis_name)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6106, in _get_indexer_strict
    indexer = self.get_indexer_for(keyarr)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6093, in get_indexer_for
    return self.get_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 3974, in get_indexer
    return self._get_indexer(target, method, limit, tolerance)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\range.py", line 418, in _get_indexer
    locs = target_array - start
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.76 MiB for an array with shape (230509,) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 87_RandomForest

Unable to allocate 1.76 MiB for an array with shape (230509,) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1239, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1432, in _get_listlike_indexer
    keyarr, indexer = ax._get_indexer_strict(key, axis_name)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6106, in _get_indexer_strict
    indexer = self.get_indexer_for(keyarr)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6093, in get_indexer_for
    return self.get_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 3900, in get_indexer
    target = self._maybe_cast_listlike_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6621, in _maybe_cast_listlike_indexer
    return ensure_index(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 7374, in ensure_index
    return Index._with_infer(index_like, copy=copy)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 717, in _with_infer
    result = cls(*args, **kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 541, in __new__
    arr = klass._ensure_array(arr, dtype, copy)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\numeric.py", line 166, in _ensure_array
    subarr = np.array(data, dtype=dtype, copy=copy)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.76 MiB for an array with shape (230509,) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 88_Xgboost

Unable to allocate 1.76 MiB for an array with shape (230509,) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1239, in _getitem_iterable
    keyarr, indexer = self._get_listlike_indexer(key, axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1432, in _get_listlike_indexer
    keyarr, indexer = ax._get_indexer_strict(key, axis_name)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6106, in _get_indexer_strict
    indexer = self.get_indexer_for(keyarr)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6093, in get_indexer_for
    return self.get_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 3900, in get_indexer
    target = self._maybe_cast_listlike_indexer(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 6621, in _maybe_cast_listlike_indexer
    return ensure_index(target)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 7374, in ensure_index
    return Index._with_infer(index_like, copy=copy)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 717, in _with_infer
    result = cls(*args, **kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\base.py", line 541, in __new__
    arr = klass._ensure_array(arr, dtype, copy)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexes\numeric.py", line 166, in _ensure_array
    subarr = np.array(data, dtype=dtype, copy=copy)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.76 MiB for an array with shape (230509,) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 89_Xgboost

Unable to allocate 5.86 MiB for an array with shape (3, 256122) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 5.86 MiB for an array with shape (3, 256122) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 90_Xgboost

Unable to allocate 5.86 MiB for an array with shape (3, 256122) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 5.86 MiB for an array with shape (3, 256122) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 91_Xgboost

Unable to allocate 5.86 MiB for an array with shape (3, 256122) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 5.86 MiB for an array with shape (3, 256122) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 92_Xgboost

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 93_Xgboost

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 94_NeuralNetwork

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 95_NeuralNetwork

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 96_NeuralNetwork

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 97_NeuralNetwork

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 98_NeuralNetwork

Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 124, in get_split
    X = load_data(self._X_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 27, in load_data
    return store.get(file_path)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\utils\utils.py", line 13, in get
    return copy.deepcopy(Store.data[key])
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\copy.py", line 153, in deepcopy
    y = copier(memo)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6384, in __deepcopy__
    return self.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 3.91 MiB for an array with shape (2, 256122) and data type object


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 99_ExtraTrees

Unable to allocate 1.76 MiB for an array with shape (230509,) and data type float64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 233, in train
    learner.fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\algorithms\sklearn.py", line 119, in fit
    self.model.fit(X, np.ravel(y), sample_weight=sample_weight)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\ensemble\_forest.py", line 476, in fit
    trees = Parallel(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\joblib\parallel.py", line 1098, in __call__
    self.retrieve()
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\joblib\parallel.py", line 975, in retrieve
    self._output.extend(job.get(timeout=self.timeout))
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\multiprocessing\pool.py", line 774, in get
    raise self._value
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\multiprocessing\pool.py", line 125, in worker
    result = (True, func(*args, **kwds))
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\joblib\_parallel_backends.py", line 620, in __call__
    return self.func(*args, **kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\joblib\parallel.py", line 288, in __call__
    return [func(*args, **kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\joblib\parallel.py", line 288, in <listcomp>
    return [func(*args, **kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\utils\fixes.py", line 117, in __call__
    return self.function(*args, **kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\ensemble\_forest.py", line 191, in _parallel_build_trees
    tree.fit(X, y, sample_weight=sample_weight, check_input=False)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\tree\_classes.py", line 969, in fit
    super().fit(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\sklearn\tree\_classes.py", line 221, in fit
    classes_k, y_encoded[:, k] = np.unique(y[:, k], return_inverse=True)
  File "<__array_function__ internals>", line 180, in unique
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\numpy\lib\arraysetops.py", line 274, in unique
    ret = _unique1d(ar, return_index, return_inverse, return_counts,
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\numpy\lib\arraysetops.py", line 328, in _unique1d
    ar = np.asanyarray(ar).flatten()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.76 MiB for an array with shape (230509,) and data type float64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 100_ExtraTrees

Unable to allocate 5.28 MiB for an array with shape (3, 230509) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1240, in _getitem_iterable
    return self.obj._reindex_with_indexers(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 5355, in _reindex_with_indexers
    new_data = new_data.reindex_indexer(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 742, in reindex_indexer
    new_blocks = [
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 743, in <listcomp>
    blk.take_nd(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 878, in take_nd
    new_values = algos.take_nd(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\array_algos\take.py", line 117, in take_nd
    return _take_nd_ndarray(arr, indexer, axis, fill_value, allow_fill)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\array_algos\take.py", line 158, in _take_nd_ndarray
    out = np.empty(out_shape, dtype=dtype)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 5.28 MiB for an array with shape (3, 230509) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 101_ExtraTrees

Unable to allocate 5.28 MiB for an array with shape (3, 230509) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1240, in _getitem_iterable
    return self.obj._reindex_with_indexers(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 5355, in _reindex_with_indexers
    new_data = new_data.reindex_indexer(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 742, in reindex_indexer
    new_blocks = [
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 743, in <listcomp>
    blk.take_nd(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 878, in take_nd
    new_values = algos.take_nd(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\array_algos\take.py", line 117, in take_nd
    return _take_nd_ndarray(arr, indexer, axis, fill_value, allow_fill)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\array_algos\take.py", line 158, in _take_nd_ndarray
    out = np.empty(out_shape, dtype=dtype)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 5.28 MiB for an array with shape (3, 230509) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for 102_DecisionTree

Unable to allocate 5.28 MiB for an array with shape (3, 230509) and data type int64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 165, in train
    train_data, validation_data = self.validation.get_split(k_fold, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validation_step.py", line 30, in get_split
    return self.validator.get_split(k, repeat)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\validation\validator_kfold.py", line 133, in get_split
    train_data = {"X": X.loc[train_index], "y": y.loc[train_index]}
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1073, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1301, in _getitem_axis
    return self._getitem_iterable(key, axis=axis)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\indexing.py", line 1240, in _getitem_iterable
    return self.obj._reindex_with_indexers(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 5355, in _reindex_with_indexers
    new_data = new_data.reindex_indexer(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 742, in reindex_indexer
    new_blocks = [
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 743, in <listcomp>
    blk.take_nd(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 878, in take_nd
    new_values = algos.take_nd(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\array_algos\take.py", line 117, in take_nd
    return _take_nd_ndarray(arr, indexer, axis, fill_value, allow_fill)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\array_algos\take.py", line 158, in _take_nd_ndarray
    out = np.empty(out_shape, dtype=dtype)
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 5.28 MiB for an array with shape (3, 230509) and data type int64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

## Error for Ensemble

Unable to allocate 1.95 MiB for an array with shape (1, 256122) and data type float64
Traceback (most recent call last):
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 1083, in _fit
    trained = self.ensemble_step(
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\base_automl.py", line 400, in ensemble_step
    oofs, target, sample_weight = self.ensemble.get_oof_matrix(self._models)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\ensemble.py", line 166, in get_oof_matrix
    oof = m.get_out_of_folds()
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\supervised\model_framework.py", line 344, in get_out_of_folds
    return self.oof_predictions.copy(deep=True)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\generic.py", line 6368, in copy
    data = self._mgr.copy(deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 644, in copy
    res = self.apply("copy", deep=deep)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\managers.py", line 347, in apply
    applied = getattr(b, f)(**kwargs)
  File "C:\Users\laure\anaconda3\envs\pythonProject\lib\site-packages\pandas\core\internals\blocks.py", line 549, in copy
    values = values.copy()
numpy.core._exceptions._ArrayMemoryError: Unable to allocate 1.95 MiB for an array with shape (1, 256122) and data type float64


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

