#!/bin/bash

# Скрипт для исправления прав доступа в cPanel
# Запустите в Terminal cPanel: bash fix_permissions.sh

echo "🔧 Исправление прав доступа для Django сайта..."

# Переходим в папку сайта
cd /home/axmedova/website

echo "📁 Установка прав на папки (755)..."
find . -type d -exec chmod 755 {} \;

echo "📄 Установка прав на файлы (644)..."
find . -type f -exec chmod 644 {} \;

echo "⚡ Установка исполняемых прав для Python файлов..."
chmod +x manage.py
chmod +x passenger_wsgi.py

echo "📋 Установка специальных прав для Passengerfile.json..."
chmod 644 Passengerfile.json

echo "👤 Установка владельца файлов..."
chown -R axmedova:nobody .

echo "✅ Права доступа установлены!"
echo ""
echo "📋 Проверка основных файлов:"
echo "Passengerfile.json: $(ls -la Passengerfile.json)"
echo "passenger_wsgi.py: $(ls -la passenger_wsgi.py)"
echo "manage.py: $(ls -la manage.py)"
echo ""
echo "🚀 Теперь перезапустите Passenger:"
echo "touch .restart.txt"
echo ""
echo "📞 Если проблема продолжается, обратитесь в поддержку хостинга"
