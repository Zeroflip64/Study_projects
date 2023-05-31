## [Прогнозирование отказа от брони номера\Predicting the cancellation of a room reservation]()

### Цель\Goal

Построить модель машинного обучения для предсказания откажеться ли клиент от своей брони или нет.\Build a machine learning model to predict whether a customer will give up their reservation or not.

### Описание\Description

Необходимо построить модель, которая сможет предсказать откажеться ли клиент от брони в отеле или нет,так же провести анализ самых распространеных факторов клиентов склонных к таким действиям.\It is necessary to build a model that will be able to predict whether a client will refuse a hotel reservation or not, as well as analyze the most common factors of clients prone to such actions.

Необходимо \ Necessary
- Произвести анализ данных. \ Perform data analysis.
- Построить модели машиного обучения для предсказания и нс основании предсказания вычитать прибыль которую получит отель. \ Build machine learning models for prediction and, based on the prediction, deduct the profit that the hotel will receive.
- Провести анализ 'непостоянного клиента'. \ Conduct an analysis of a 'non-permanent client'.

### Используемые библиотеки \ Libraries used
- **`Scikit-learn`**
- **`Pandas`**
- **`NumPy`**
- **`Matplotlib`**
- **`Seaborn`**
- **`Catboost`**
### Результаты \ Results
С использованием кроссвалидации построены, обучены и протестированы разные модели машинного обучения. Выбрана модель которая предсказывает наименьшую потерю для отеля. / Various machine learning models have been built, trained and tested using cross validation. A model has been chosen that predicts the least loss for the hotel.
