#!/usr/bin/env bash
# Build script for Render

set -o errexit  # Exit on error

# Install dependencies
pip install -r requirements.txt

# Create .env file with dummy values
echo "Creating .env file with sample values"
echo "SECRET_KEY=your-secret-key-here" > .env

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate 