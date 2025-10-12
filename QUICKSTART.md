# 🚀 Быстрый старт

Краткое руководство по запуску проекта для разработки.

## Минимальные требования

- Python 3.10+
- pip
- 5 минут времени

## Запуск за 5 шагов

### 1️⃣ Создайте виртуальное окружение

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2️⃣ Установите зависимости

```bash
pip install -r requirements.txt
```

### 3️⃣ Примените миграции

```bash
python manage.py migrate
```

### 4️⃣ Создайте суперпользователя

```bash
python manage.py createsuperuser
```

Введите:
- Username: `admin`
- Email: `admin@example.com`
- Password: (ваш пароль)

### 5️⃣ Запустите сервер

```bash
python manage.py runserver
```

## ✅ Готово!

Откройте в браузере:
- 🌐 Сайт: http://127.0.0.1:8000
- 🔧 Админка: http://127.0.0.1:8000/admin

## 📝 Первые шаги

### Вариант A: Быстро заполнить демо-данными (рекомендуется)

Заполните сайт тестовыми данными одной командой:

```bash
python manage.py populate_demo_data
```

Эта команда создаст:
- ✅ Профиль социолога
- ✅ 6 услуг
- ✅ 3 публикации
- ✅ 2 проекта
- ✅ 2 статьи блога
- ✅ 2 достижения
- ✅ 3 отзыва

Теперь можно сразу открыть сайт и увидеть его в действии!

### Вариант B: Заполнить вручную

#### Заполните профиль

1. Войдите в админку
2. Перейдите в "Профили"
3. Нажмите "Добавить профиль"
4. Заполните информацию о социологе
5. Сохраните

### Добавьте услугу

1. В админке откройте "Услуги"
2. Нажмите "Добавить услугу"
3. Заполните название, описание, цену
4. Выберите иконку (например: `fas fa-chart-bar`)
5. Сохраните

### Создайте публикацию

1. Откройте "Публикации"
2. Нажмите "Добавить публикацию"
3. Заполните библиографические данные
4. Сохраните

### Напишите статью в блог

1. Перейдите в "Статьи блога"
2. Создайте новую статью
3. Slug сгенерируется автоматически
4. Отметьте "Опубликовано"
5. Сохраните

## 🎨 Иконки для услуг

Font Awesome классы для разных услуг:

- Исследования: `fas fa-search`
- Консультации: `fas fa-user-tie`
- Аналитика: `fas fa-chart-line`
- Опросы: `fas fa-clipboard-list`
- Обучение: `fas fa-graduation-cap`
- Экспертиза: `fas fa-certificate`
- Статистика: `fas fa-chart-bar`
- Документы: `fas fa-file-alt`

Полный список: https://fontawesome.com/icons

## 🛠 Полезные команды

```bash
# Создать миграции
python manage.py makemigrations

# Применить миграции
python manage.py migrate

# Собрать статику
python manage.py collectstatic

# Создать суперпользователя
python manage.py createsuperuser

# Заполнить демо-данными (новое!)
python manage.py populate_demo_data

# Запустить тесты
python manage.py test

# Запустить тесты с подробным выводом
python manage.py test --verbosity=2

# Очистить базу данных
python manage.py flush

# Запустить в другом порту
python manage.py runserver 8080

# Проверить проект на ошибки
python manage.py check
```

## 📚 Дополнительная информация

- Полная документация: [README.md](README.md)
- Инструкция по деплою: [DEPLOYMENT.md](DEPLOYMENT.md)
- Создание статьи в Wikipedia: [WIKIPEDIA_GUIDE.md](WIKIPEDIA_GUIDE.md)

## ❓ Проблемы?

### Ошибка импорта decouple

```bash
pip install python-decouple
```

### Ошибка с Pillow

```bash
pip install Pillow
```

### База данных заблокирована

Закройте все процессы использующие БД и перезапустите сервер.

### Статические файлы не загружаются

```bash
python manage.py collectstatic --noinput
```

## 💡 Совет

Создайте файл `.env` для настроек (см. `.env.example`):

```bash
cp .env.example .env
nano .env  # или откройте в редакторе
```

---

**Приятной работы!** 🎉

Если нужна помощь, создайте issue в репозитории.

