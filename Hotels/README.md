## [Прогнозирование отказа от брони номера\Predicting the cancellation of a room reservation]()

### Цель\Goal

Построить модель машинного обучения для предсказания откажеться ли клиент от своей брони или нет.\Build a machine learning model to predict whether a customer will give up their reservation or not.

### Описание проекта
Заказчик этого исследования — сеть отелей «Как в гостях». 
Чтобы привлечь клиентов, эта сеть отелей добавила на свой сайт возможность забронировать номер без предоплаты. Однако если клиент отменял бронирование, то компания терпела убытки. Сотрудники отеля могли, например, закупить продукты к приезду гостя или просто не успеть найти другого клиента.
Чтобы решить эту проблему, вам нужно разработать систему, которая предсказывает отказ от брони. Если модель покажет, что бронь будет отменена, то клиенту предлагается внести депозит. Размер депозита — 80% от стоимости номера за одни сутки и затрат на разовую уборку. Деньги будут списаны со счёта клиента, если он всё же отменит бронь.
### Бизнес-метрика и другие данные
Основная бизнес-метрика для любой сети отелей — её прибыль. Прибыль отеля — это разница между стоимостью номера за все ночи и затраты на обслуживание: как при подготовке номера, так и при проживании постояльца. 
В отеле есть несколько типов номеров. В зависимости от типа номера назначается стоимость за одну ночь. Есть также затраты на уборку. Если клиент снял номер надолго, то убираются каждые два дня. 
Стоимость номеров отеля:
категория A: за ночь — 1 000, разовое обслуживание — 400;
категория B: за ночь — 800, разовое обслуживание — 350;
категория C: за ночь — 600, разовое обслуживание — 350;
категория D: за ночь — 550, разовое обслуживание — 150;
категория E: за ночь — 500, разовое обслуживание — 150;
категория F: за ночь — 450, разовое обслуживание — 150;
категория G: за ночь — 350, разовое обслуживание — 150.
В ценовой политике отеля используются сезонные коэффициенты: весной и осенью цены повышаются на 20%, летом — на 40%.
Убытки отеля в случае отмены брони номера — это стоимость одной уборки и одной ночи с учётом сезонного коэффициента.
На разработку системы прогнозирования заложен бюджет — 400 000. При этом необходимо учесть, что внедрение модели должно окупиться за тестовый период. Затраты на разработку должны быть меньше той выручки, которую система принесёт компании.

ENG:
### Project Description
The customer of this study is the hotel chain "As a guest".
To attract customers, this hotel chain has added to its website the ability to book a room without prepayment. However, if the customer cancelled the booking, the company suffered losses. The hotel staff could, for example, buy groceries for the arrival of a guest or simply not have time to find another client.
To solve this problem, you need to develop a system that predicts the rejection of the reservation. If the model shows that the reservation will be canceled, the client is invited to make a deposit. The deposit amount is 80% of the room rate for one day and the cost of a one—time cleaning. The money will be debited from the client's account if he still cancels the reservation.
### Business metrics and other data
The main business metric for any hotel chain is its profit. The profit of the hotel is the difference between the cost of a room for all nights and the cost of service: both during the preparation of the room and during the stay of the guest.
The hotel has several types of rooms. Depending on the type of room, the cost per night is assigned. There are also cleaning costs. If the client has rented a room for a long time, then they are cleaned every two days.
The cost of hotel rooms:
category A: per night — 1,000, one—time service - 400;
category B: per night — 800, one—time service - 350;
category C: per night — 600, one—time service - 350;
category D: per night — 550, one—time service - 150;
Category E: 500 per night, one—time service - 150;
category F: per night — 450, one—time service - 150;
category G: per night — 350, one—time service - 150.
The hotel's pricing policy uses seasonal coefficients: in spring and autumn prices increase by 20%, in summer — by 40%.
The hotel's losses in case of cancellation of the room reservation are the cost of one cleaning and one night, taking into account the seasonal coefficient.
The budget for the development of the forecasting system is 400,000. At the same time, it should be taken into account that the implementation of the model should pay off during the test period. Development costs should be less than the revenue that the system will bring to the company.

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
