cd space
sleep 120
python3 manage.py makemigrations space
python3 manage.py migrate space
python3 manage.py migrate
python3 manage.py collectstatic --noinput
python3 manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
python3 manage.py search_index --rebuild -f
python3 manage.py runsslserver --certificate /usr/share/nginx/certbot/space.automateyournetwork.ca/fullchain1.pem --key /usr/share/nginx/certbot/space.automateyournetwork.ca/privkey1.pem 0.0.0.0:8000
#python3 manage.py runserver 0.0.0.0:8000