## Поект спринт: новые записи

Все как в проекте https://github.com/Alexander28-31/hw02_community.git

Теперь добавлен новый функционал：
- Добавлена форма для публикации новых записей
- Добавлена страница для редактирования записей

## Инструкция по запуске проекта

Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/Alexander28-31/hw03_forms.git
```
```
cd hw02_community 
```

Создайте виртуальное окружение и активируйте его
```
python -m venv venv
```
```
source venv/Scripts/activate
```

Установите зависимости из файла 
```
pip install -r requirements.txt
```

Создайте миграции и запустите их
```
python manage.py makemigrations
```
```
python manage.py migrate
```

Есть возможность создать суперпользователя
```
python manage.py createsuperuser 
```

Запустите проект
```
python manage.py runserver
```
