# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files
COPY . /app/

# Collect static files (optional, if needed)
RUN python manage.py collectstatic --noinput

# Default: run Django using gunicorn
CMD ["gunicorn", "employee_project.wsgi:application", "--bind", "0.0.0.0:8000"]
