# Installation notes

For virtual environment

```
pip install pipenv
```

For starting virtual environment
``pip shell``

For creating requirements.txt
``pip freeze > requirements.txt``

For installing pipfile
``pip install -r requirements.txt``

Or for installing Pipfile
``pipenv install``

To run in a development environment

```
gunicorn -b ip_address:8050 index:server
```
