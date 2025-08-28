#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install system dependencies for Pillow (if needed)
# apt-get update && apt-get install -y python3-dev python3-setuptools python3-pip python3-venv libpq-dev

# Collect static files
echo "Collecting static files..."
python portfolio/manage.py collectstatic --no-input --clear

# Apply database migrations
echo "Applying database migrations..."
python portfolio/manage.py migrate --no-input

# Create superuser (uncomment and modify if needed)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password') if not User.objects.filter(username='admin').exists() else None" | python portfolio/manage.py shell