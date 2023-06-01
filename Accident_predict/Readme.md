## [Оценка риска ДТП по определенному маршруту/Project objective: Assessment of the risk of an accident along a certain route ]()

### Цель\Goal

Построить предсказаельную модель ,которая будет исходя из условий будет оценивать выдавать машину клиенту или нет./ To build a predictive model that will evaluate whether or not to issue a car to the client based on the conditions

### Описание проекта
Поступил заказ: нужно создать систему, которая могла бы оценить риск ДТП по выбранному маршруту движения.Под риском понимается вероятность ДТП с любым повреждением транспортного средства.Как только водитель выбрал автомобиль и загрузил маршрут  система должна поеределить опасность маршрута и состояние водителя.

### Project Description
An order has been received: it is necessary to create a system that could assess the risk of an accident along the selected route.Risk refers to the probability of an accident with any damage to the vehicle.As soon as the driver has selected the car and loaded the route, the system should determine the danger of the route and the driver's condition.

## Этапы / Necessary
- Подключиться к базе данных SQl / Connect to SQl database
- Провести первичный анализ / Conduct a primary analysis
- Закрепить задачи по исследовательскому анализу для команды аналитиков / Assign research analysis tasks to the analytics team.
- Создать датафрейм с необходимыми данными и провести их предобработку провести анализ какие факторы влияют сильнее / Create a dataframe with the necessary data and pre-process it, analyze which factors influence more
- Выбрать модель,провести обучение / Choose a model,conduct training
- Сделать вывод и предложить решения заказчику  / Make a conclusion and offer solutions to the customer

### Используемые библиотеки / Libraries used
- **`Scikit-learn`**
- **`Pandas`**
- **`NumPy`**
- **`Matplotlib`**
- **`Seaborn`**
- **`Catboost`**
- **`Sqlalchemy`**
- **`phik`**
### Результаты \ Results
Были выявленны основные факторы которые могут привести к дтп и виновности водителя,на основании полученных данных были предложены решения для того что бы снизить риски для компании и для водителя. / The main factors that can lead to an accident and the driver's guilt were identified, based on the data obtained, solutions were proposed in order to reduce the risks for the company and for the driver.
