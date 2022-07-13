env:
	source virtual/Scripts/activate

run:
	python manage.py runserver localhost:8000

make:
	python manage.py makemigrations my_profile

migrate:
	python manage.py migrate

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

test:
	python manage.py test

drop:
	dropdb portfolio

create:
	createdb portfolio

live:
	python manage.py livereload

set:
	set PGUSER=postgres

admin:
	python manage.py createsuperuser --username admin --email admin@admin.com

hadmin:
	heroku run python manage.py createsuperuser --username admin --email admin@admin.com

hmake:
	heroku run python manage.py makemigrations

hmigrate:
	heroku run python manage.py migrate

pushdb:
	heroku pg:push api DATABASE_URL

reset:
	heroku pg:reset DATABASE

addon:
	heroku addons:create heroku-postgresql:hobby-dev
