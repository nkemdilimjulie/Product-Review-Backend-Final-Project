# Use this version of Python
FROM python:3.10

# Set the working directory inside the container
WORKDIR /usr/src/app

# Update package index files on system
RUN apt-get update
# Copy the requirements file into the working directory
COPY requirements.txt .  

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt  

# Copy the entire project to the container
COPY . . 

# Collect static files for production
RUN python manage.py collectstatic --noinput

# Install gunicorn
RUN pip install gunicorn

# Open port 8000 for the application
EXPOSE 8000

# Default command is overridden in docker-compose
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "django_project.wsgi:application"]