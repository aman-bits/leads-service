#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the server
echo "Starting the server..."
exec python manage.py runserver 0.0.0.0:8000
