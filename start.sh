#!/bin/bash

# Exit on any error
set -e

echo "Starting Django Portfolio Application..."

# Wait for database to be ready (if using external database)
echo "Waiting for database..."
python manage.py wait_for_db

# Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser if it doesn't exist (optional)
echo "Checking for superuser..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

# Start the application
echo "Starting Gunicorn..."
PORT=${PORT:-8000}
exec gunicorn --bind 0.0.0.0:$PORT --workers 3 --timeout 120 portfolio_project.wsgi:application 