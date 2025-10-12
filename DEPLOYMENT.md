# Инструкция по деплою на cPanel

Подробное руководство по развертыванию Django-проекта на хостинге с cPanel.

## 📋 Предварительные требования

1. **Хостинг с cPanel** и поддержкой:
   - Python 3.9+
   - Passenger (mod_wsgi альтернатива)
   - SSH доступ (рекомендуется)
   - Возможность создания виртуального окружения

2. **Доменное имя** настроенное на ваш хостинг

3. **База данных** PostgreSQL или MySQL (опционально, можно использовать SQLite)

## 🚀 Пошаговая инструкция

### Шаг 1: Загрузка проекта на сервер

#### Вариант A: Через SSH (рекомендуется)

```bash
# Подключитесь к серверу
ssh username@your-domain.com

# Перейдите в директорию public_html или нужную папку
cd ~/public_html

# Клонируйте репозиторий или загрузите архив
# Если у вас git:
git clone https://github.com/yourusername/axmedova.git

# Или распакуйте архив:
unzip axmedova.zip
cd axmedova
```

#### Вариант B: Через File Manager в cPanel

1. Войдите в cPanel
2. Откройте File Manager
3. Перейдите в `public_html`
4. Загрузите архив проекта и распакуйте его

### Шаг 2: Создание виртуального окружения

```bash
# Находясь в директории проекта
cd ~/public_html/axmedova

# Создайте виртуальное окружение
python3.9 -m venv venv

# Активируйте его
source venv/bin/activate

# Обновите pip
pip install --upgrade pip
```

### Шаг 3: Установка зависимостей

```bash
# Установите все необходимые пакеты
pip install -r requirements.txt
```

### Шаг 4: Настройка базы данных (опционально)

#### Если используете PostgreSQL:

1. В cPanel создайте новую PostgreSQL базу данных:
   - Database name: `axmedova_db`
   - Database user: создайте пользователя с паролем
   - Предоставьте все права пользователю

2. Запишите данные подключения

#### Если используете MySQL:

1. В cPanel создайте MySQL базу данных
2. Создайте пользователя
3. Привяжите пользователя к базе

### Шаг 5: Настройка переменных окружения

Создайте файл `.env` в корне проекта:

```bash
nano .env
```

Добавьте следующее содержимое:

```env
# Django Settings
SECRET_KEY=your-very-secret-and-long-random-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# CSRF Trusted Origins (for HTTPS in production)
CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com

# Database Settings (для PostgreSQL)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=axmedova_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

# Или для MySQL
# DB_ENGINE=django.db.backends.mysql
# DB_NAME=your_db_name
# DB_USER=your_db_user
# DB_PASSWORD=your_db_password
# DB_HOST=localhost
# DB_PORT=3306

# Email Settings
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
ADMIN_EMAIL=admin@yourdomain.com
```

Сохраните файл (Ctrl+O, Enter, Ctrl+X).

### Шаг 6: Настройка passenger_wsgi.py

Отредактируйте `passenger_wsgi.py` и замените пути:

```bash
nano passenger_wsgi.py
```

Обновите пути в соответствии с вашим сервером:

```python
import os
import sys

# ЗАМЕНИТЕ username НА ВАШЕ ИМЯ ПОЛЬЗОВАТЕЛЯ
INTERP = os.path.expanduser("~/public_html/axmedova/venv/bin/python")
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

sys.path.insert(0, os.path.expanduser('~/public_html/axmedova'))
sys.path.insert(0, os.path.expanduser('~/public_html/axmedova/venv/lib/python3.9/site-packages'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'axmedova_project.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### Шаг 7: Настройка .htaccess

Отредактируйте `.htaccess`:

```bash
nano .htaccess
```

Обновите пути:

```apache
PassengerEnabled On
PassengerAppRoot /home/username/public_html/axmedova

# ЗАМЕНИТЕ username И путь к python
PassengerPython /home/username/public_html/axmedova/venv/bin/python

PassengerStartupFile passenger_wsgi.py
PassengerAppEnv production

# Остальное оставьте без изменений
```

### Шаг 8: Применение миграций Django

```bash
# Убедитесь, что виртуальное окружение активно
source venv/bin/activate

# Примените миграции
python manage.py migrate

# Создайте суперпользователя
python manage.py createsuperuser

# Соберите статические файлы
python manage.py collectstatic --noinput
```

### Шаг 9: Настройка прав доступа

```bash
# Дайте права на запись для директорий медиа и статики
chmod -R 755 ~/public_html/axmedova/media
chmod -R 755 ~/public_html/axmedova/staticfiles

# Права на базу данных SQLite (если используется)
chmod 664 ~/public_html/axmedova/db.sqlite3
```

### Шаг 10: Настройка домена в cPanel

1. Войдите в cPanel
2. Перейдите в раздел "Domains" или "Addon Domains"
3. Настройте домен на директорию:
   - Document Root: `/home/username/public_html/axmedova`

### Шаг 11: Перезапуск приложения

```bash
# Создайте файл tmp/restart.txt для перезапуска Passenger
mkdir -p tmp
touch tmp/restart.txt

# Или перезапустите через cPanel в разделе "Setup Python App"
```

### Шаг 12: Проверка работы

1. Откройте ваш домен в браузере: `https://yourdomain.com`
2. Проверьте главную страницу
3. Войдите в админ-панель: `https://yourdomain.com/admin`
4. Проверьте все страницы сайта

## 🔧 Настройка через cPanel Python App (альтернативный способ)

Если ваш хостинг поддерживает "Setup Python App":

1. В cPanel найдите "Setup Python App"
2. Нажмите "Create Application"
3. Заполните форму:
   - Python version: 3.9 или выше
   - Application root: `/home/username/public_html/axmedova`
   - Application URL: ваш домен
   - Application startup file: `passenger_wsgi.py`
   - Application Entry point: `application`

4. После создания приложения:
   - Активируйте виртуальное окружение (команда будет показана)
   - Установите зависимости: `pip install -r requirements.txt`
   - Примените миграции
   - Перезапустите приложение

## 🔐 Настройка SSL (HTTPS)

### Через Let's Encrypt в cPanel:

1. В cPanel найдите "SSL/TLS Status" или "Let's Encrypt SSL"
2. Выберите ваш домен
3. Нажмите "Install" или "Issue"
4. Дождитесь установки сертификата

### Принудительное перенаправление на HTTPS:

В `.htaccess` раскомментируйте строки:

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

## 📧 Настройка Email

### Для Gmail:

1. Включите 2-факторную аутентификацию
2. Создайте App Password: https://myaccount.google.com/apppasswords
3. Используйте полученный пароль в `.env`

### Для SMTP хостинга:

Спросите у вашего хостинг-провайдера параметры SMTP и обновите `.env`.

## 🔄 Обновление проекта

Для обновления проекта на сервере:

```bash
# Подключитесь по SSH
ssh username@your-domain.com
cd ~/public_html/axmedova

# Активируйте окружение
source venv/bin/activate

# Получите последние изменения
git pull origin main

# Установите новые зависимости (если есть)
pip install -r requirements.txt

# Примените новые миграции
python manage.py migrate

# Соберите статику
python manage.py collectstatic --noinput

# Перезапустите приложение
touch tmp/restart.txt
```

## 🐛 Устранение неполадок

### Passenger Error #2 - Permission Denied
**Ошибка**: `Permission denied (errno=13)` при доступе к `Passengerfile.json`

**Решение**:
1. Загрузите файл `Passengerfile.json` в корень сайта
2. Установите права доступа:
   ```bash
   # В Terminal cPanel
   cd /home/axmedova/website
   chmod 644 Passengerfile.json
   chown axmedova:nobody Passengerfile.json
   ```
3. Или запустите готовый скрипт:
   ```bash
   bash fix_permissions.sh
   ```
4. Перезапустите Passenger:
   ```bash
   touch .restart.txt
   ```

### Ошибка 500 Internal Server Error

1. Проверьте логи ошибок:
   - cPanel: "Errors" в разделе "Metrics"
   - SSH: `tail -f ~/logs/error_log`

2. Проверьте права на файлы и директории

3. Убедитесь, что `DEBUG=False`, `ALLOWED_HOSTS` и `CSRF_TRUSTED_ORIGINS` настроены правильно

### Статические файлы не загружаются

1. Проверьте пути в `.htaccess`
2. Убедитесь, что `collectstatic` был выполнен

### CSRF ошибки (403 Forbidden)

Если получаете ошибки CSRF при отправке форм:

1. **Проверьте CSRF_TRUSTED_ORIGINS** в `.env` файле:
   ```env
   CSRF_TRUSTED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
   ```

2. **Убедитесь, что домены точно совпадают** (с https:// и без слеша в конце)

3. **Перезапустите приложение** после изменения `.env`:
   ```bash
   touch .restart.txt
   ```
3. Проверьте права доступа к директории `staticfiles`

### База данных не подключается

1. Проверьте параметры подключения в `.env`
2. Убедитесь, что база данных создана в cPanel
3. Проверьте, что пользователь имеет права на базу

### Passenger не запускается

1. Проверьте пути в `passenger_wsgi.py`
2. Убедитесь, что Python версия совпадает
3. Проверьте логи Passenger

## 📊 Мониторинг и поддержка

### Логи приложения

```bash
# Просмотр логов через SSH
tail -f ~/logs/error_log
tail -f ~/logs/access_log
```

### Резервное копирование

Регулярно создавайте бэкапы:

```bash
# Бэкап базы данных
python manage.py dumpdata > backup_$(date +%Y%m%d).json

# Бэкап медиа файлов
tar -czf media_backup_$(date +%Y%m%d).tar.gz media/

# Через cPanel используйте встроенный инструмент Backup
```

## ✅ Чеклист после деплоя

- [ ] Сайт открывается по домену
- [ ] HTTPS работает корректно
- [ ] Админ-панель доступна
- [ ] Статические файлы загружаются
- [ ] Медиа файлы загружаются
- [ ] Формы отправляются корректно
- [ ] Email уведомления работают
- [ ] Sitemap доступен
- [ ] robots.txt настроен
- [ ] Google Analytics подключен (опционально)
- [ ] Настроены регулярные бэкапы

## 📞 Поддержка

Если у вас возникли проблемы:
1. Проверьте логи ошибок
2. Обратитесь в поддержку хостинг-провайдера
3. Создайте issue в репозитории проекта

---

**Поздравляем! Ваш сайт успешно развернут на cPanel!** 🎉

