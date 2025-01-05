# recipe-app-api

## Creating and Running Docker containers:
    - docker build .
    - docker-compose build

### To Run Tests
    - docker-compose run --rm app sh -c "python manage.py tests && flake8"

## Create Project in Docker
    - docker-compose run --rm app sh -c "django-admin startproject app ."

## To Run The Server:
    - docker-compose up
    - Then you can visit http://127.0.0.1:8100 or http://localhost:8100

## Migrations
    - Ensure that app is enabled in settings.py
    - then use Django CLI
     - python manage.py makemirations
     - python manage.py migrate
    
