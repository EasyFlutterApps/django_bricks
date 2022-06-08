<!-- # [Simple Django Starter](https://brickhub.dev/bricks/simple_django_starter/0.1.0+2) -->
<a href="https://brickhub.dev/bricks/simple_django_starter/0.1.0+2" style="color: #eeeeee; text-decoration: none;">
  <h1>Simple Django Starter<h1/>  
<a/>

<div align="center">
  <img width="400" src="https://raw.githubusercontent.com/EasyFlutterApps/django_bricks/main/assets/django-logo.svg" alt="Django logo">
</div>

This is ready to deploy Django Starter Template which set up all the basic requirements for a Django project.

[![Powered by Mason](https://img.shields.io/endpoint?url=https%3A%2F%2Ftinyurl.com%2Fmason-badge)](https://github.com/felangel/mason) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)


## 🚀 Features

- Django 4.0 & Python 3.8
- Ready to deploy on Heroku
- SMTP email support

## Usage 🚀

```
mason make simple_django_starter
```

## Variables ✨

| variable           | description                  | default | type      |
| ------------------ | ---------------------------- | ------- | --------- |
| `name`     | project name          | Simple Project   | `string`  |
| `email`     | email address         | example@mail.com   | `string`  |
| `password`     | email password          | Null   | `string`  |

## Prerequisites 💬

System Requirements:
- Python 3.8+
- Django 4.0+

## Virtual Environment ⚡️

### Windows

- Using Virtualenv: `pip install virtualenv`
```bash
virtualenv venv
cd venv/Scripts
activate
```

### Linux & MacOS
- Using Virtualenv: `pip install virtualenv`
```bash
virtualenv venv
source venv/bin/activate
```

## Installation 📦

### Install requirements

    pip install -r requirements.txt

### Migrations

    python manage.py makemigrations
    python manage.py migrate

### Static files

    python manage.py collectstatic

### Create superuser

    python manage.py createsuperuser

### SMTP email

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
    EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)
    EMAIL_PORT = os.getenv('EMAIL_PORT', 587)
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '<email-address>')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '<email-password>')

## Deployment 🚀

### Heroku

    heroku login
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>

## Run Locally 🏃

    python manage.py runserver
