# Django Email User

<div align="center">
  <img width="400" src="https://raw.githubusercontent.com/EasyFlutterApps/django_bricks/main/assets/django-logo.svg" alt="Django logo">
</div>

This is ready to use django user app module which set up all the basic requirements.

[![Powered by Mason](https://img.shields.io/endpoint?url=https%3A%2F%2Ftinyurl.com%2Fmason-badge)](https://github.com/felangel/mason) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)


## 🚀 Features

- Email based user authentication

## Usage 🚀

```
mason make django_email_user
```

## Variables ✨

| variable           | description                  | default | type      |
| ------------------ | ---------------------------- | ------- | --------- |
| `name`     | project name          | Simple Project   | `string`  |

## Prerequisites 💬

System Requirements:
- Blank Django Project

## Installation 📦

### INSTALLED_APPS

    <- app-name ->

### Settings

    AUTH_USER_MODEL = '<- app-name ->.CustomUser'

### Create superuser

    python manage.py createsuperuser
