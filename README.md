# mirgovorit_test_task

# Стек

- Python 3.11.1
- Django 5.0.1

# Запуск

Первоочередно, конечно, необходимо создать и активировать виртуальное окружение, а затем установить зависимости:

Виртуальное окружение:

Windows:

```bash
py -3 -m venv env
```

```bash
. venv/Scripts/activate 
```

macOS/Linux:

```bash
python3 -m venv .venv
```

```bash
source env/bin/activate
```

Зависимости:

```bash
pip install -r requirements.txt
```

Вторым шагам следует осуществить миграции:

Windows: 

```bash
py manage.py makemigrations
```

```bash
py manage.py migrate
```

macOS/Linux:

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

Сам проект запускается стандартно с помощью команды:

Windows:

```bash
py manage.py runserver
```
Linux/MacOS

```bash
python3 manage.py runserver
```

Также для удобства добавлен набор продуктов для предзаполнения БД, работает с помощью встроенной команды Django:

Windows:

```bash
py manage.py loaddata <название файла>
```
Linux/MacOS

```bash
python3 manage.py loaddata <название файла>
```

Наименования файла - products.json
