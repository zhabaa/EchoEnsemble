# EchoEnsemble
______
#### Добро пожаловать в мир EchoEnsemble.
#### EchoEnsemble - ваш путеводитель в мир музыкальных эмоций и вдохновения. 
#### На сайте вы найдете широкий выбор музыкальных произведений различных жанров, созданных талантливыми музыкантами со всего мира.

## Техническое задание для проекта "EchoEnsemble":

1. Создание базы данных с таблицами:
    - Таблица "Пользователи" для хранения информации о зарегистрированных пользователях (ID, имя, электронная почта, пароль, создатель).
    - Таблица "Музыкальные произведения" для хранения информации о музыкальных композициях (ID, название, исполнитель, аудиофайл, изображение, уникальный ключ).

2. Регистрация и авторизация пользователя:
   - Форма регистрации/авторизации
   - Проверка на уникальность электронной почты.
   - Хэширование пароля перед сохранением в базе данных.
   - Проверка соответствия введенных данных данным из базы.

3. Функционал:
    - Просмотр списка музыкальных произведений
    - Воспроизведение аудио
    - Поиск музыкальных композиций по названию или исполнителю
    - Добавление и удаление композиций (Создатель):
    - Административный доступ (Разграничение между создателями и пользователями)

Этот функционал позволит пользователям сайта "EchoEnsemble" наслаждаться музыкой, искать новые исполнителей, а также создавать собственные списки треков.

### Пояснительная записка
______
Идея проекта EchoEnsemble заключается в создании сайта, где любители музыки смогут слушать свои любимые песни. Сайт предлагает пользователям возможность прослушивания и загрузки музыки. Кроме того, EchoEnsemble предоставляет возможность музыкальным исполнителям и группам загружать свои композиции на платформу, чтобы расширить свою аудиторию и получить обратную связь от слушателей, например, в социальных сетях. Целью проекта EchoEnsemble является создание удобного и вдохновляющего пространства для всех ценителей музыки.


### Реализация 
_______
Для реализации сайта EchoEnsemble на Python с использованием Flask были созданы следующие основные классы: [User]? для представления пользователей ...

Для производительности и безопасности сайта, были использованы следующие приемы:

1. Реализация аутентификации и авторизации пользователей с помощью Flask-Login для защиты конфиденциальной информации и контроля доступа к функционалу сайта.
2. Использование ORM (Object-Relational Mapping) библиотеки SQLAlchemy для удобного взаимодействия с базой данных и уменьшения объема кода. (😭)

Приемы для написания сайта на Python с использованием Flask:
- Использование виртуального окружения для изоляции зависимостей
- Разделение кода на модули для удобного масштабирования и поддержки
- Тестирование функционала с помощью фреймворка pytest для обеспечения корректной работы сайта и выявления возможных ошибок.


### Презентация и скриншоты
_______
[Презентация проекта](https://clck.ru/3AFvZP)

Скриншот №1

Скриншот №2

Скриншот №3

Скриншот №4

