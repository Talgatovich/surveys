

# Surveys
#### Сервис прохождения опросов пользователями.
#### Пользователи получают определённое количество баллов за прохождение тестов.
#### Баллы можно тратить на перекрашивание цвета логина или фона в личном кабинете

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Talgatovich/surveys.git
```
``` 
cd surveys/
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Перейти в директорию с файлом manage.py:

```
cd surveys_project/
```

Выполнить миграции:

```
python3 manage.py migrate
```

Загрузить тесты:

```
python3 manage.py load_tests
```

Запустить проект:

```
python3 manage.py runserver
```

Автор: [Ибятов Раиль](https://github.com/Talgatovich)
