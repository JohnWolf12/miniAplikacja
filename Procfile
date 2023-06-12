release: python manage.py migrate
web: gunicorn miniAplikacja.wsgi --log-file -
python manage.py collectstatic --noinput
