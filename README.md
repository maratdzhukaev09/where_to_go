# Where to go - Moscow with Artem's eyes

Site about the most interesting places in Moscow. Artem's project.

## Installation

Python 3 must be installed.

Download the code.

### [Virtual Environment](https://docs.python.org/3/library/venv.html)

You must be in repository directory.

Create virtual environment with shell command:
```bash
$ python -m venv venv
```
Use `python3` if there're conflicts with Python 2.

Activate it with command:
```bash
$ venv/Scripts/activate
```

### Requirements

Install requirements with command:
```bash
$ pip install -r requirements.txt
```
Use `pip3` if there're conflicts with Python 2.

## Running Code

Create SGLite database with command:
```bash
$ python manage.py migrate
```

Run development server with command:
```bash
$ python manage.py runserver
```
Use `python3` if there're conflicts with Python 2.

## Models

- `Place` - places
    - `title` - name, `CharField`
    - `short_description` - short description, `TextField`
    - `long_description` - long description, `HTMLField` ([more](https://github.com/aljosa/django-tinymce))
    - `lat` - latitude, `FloatField`
    - `lon` - longitude, `FloatField`
- `Image` - images
    - `image` - image itself, `ImageField`
    - `place` - place, `ForeignKey`
    - `number` - index number, `IntegerField`

## Environment Variables

Some of settings are taken from environment variables. To define them, create `.env` file on the same level with `manage.py` and write data there in this format:`VARIABLE=value`.

There're 2 variables:
- `SECRET-KEY` - project's secret key.
- `DEBUG` - (default:`False`) debug mode. Set `True` to turn it on.

## Created with

- [Django 3](https://www.djangoproject.com/) - framework.
- [KudaGo](https://kudago.com/) - places information.
- [Where to go frontend](https://github.com/devmanorg/where-to-go-frontend/) - site's frontend.
- [django-admin-sortable2](https://pypi.org/project/django-admin-sortable2/), [django-tinymce](https://github.com/aljosa/django-tinymce), [python-dotenv](https://pypi.org/project/python-dotenv/) - python libraries.

## Project's Purposes

The code is written for educational purposes - this is a lesson in Python and web-development course on the site [Devman](https://dvmn.org/).
