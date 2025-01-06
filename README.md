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
     - python manage.py makemigrations
     - python manage.py migrate

    - For future changes, when you made changes (eg. create a model) you need to use;
        - docker-compose down
        - docker-compose run --rm app sh -c "python manage.py makemigrations"
        - docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate" => If you get this error < Error response from daemon: remove recipe-app-api_dev-db-data: volume is in use - [af2ce4a780d0ff3d672b36dfa39a046f5ff]> use:
        - docker volume ls
        - docker volume rm recipe-app-api_dev-db-data (volume name, you can check it by using docker volume ls) => to  delete volume. Then
        - docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"

## Creating superuser for admin panel
    - docker-compose run --rm app sh -c "python manage.py createsuperuser"
    Then CLI will as you an email and passwordto create superuser. After creating superuser you can visit http://localhost:8100/admin and login as a admin!
    Don't forget to make modifications and configurations in admin.py file.
