#!/bin/bash
# Quick start script for Django development server

echo "🚀 Starting Axmedova Portfolio Website..."
echo "================================"

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "✓ Virtual environment activated"
else
    echo "❌ Virtual environment not found. Please run: python3 -m venv venv"
    exit 1
fi

# Check if migrations are applied
echo "Checking database..."
python manage.py migrate --check 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠ Migrations needed. Applying..."
    python manage.py migrate
fi

# Start server
echo "================================"
echo "✅ Starting server at http://127.0.0.1:8000"
echo "Press Ctrl+C to stop"
echo "================================"
python manage.py runserver

