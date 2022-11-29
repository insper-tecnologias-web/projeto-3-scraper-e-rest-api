release: python manage.py migrate $$ python manage.py loaddata src\data\data.json
web: gunicorn gameboardapi.wsgi