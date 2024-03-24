install-deps:
	pip-sync requirements.txt

deps:
	pip install --upgrade pip pip-tools

shell:
	cd src && ./manage.py shell --settings=app.settings.development

mg1:
	cd src && ./manage.py makemigrations --settings=app.settings.development

mg2:
	cd src && ./manage.py migrate --settings=app.settings.development

serv:
	cd src && ./manage.py runserver --settings=app.settings.development

server:
	cd src && ./manage.py migrate --settings=app.settings.development && ./manage.py runserver --settings=app.settings.development

lint:
	-cd src && ./manage.py makemigrations --settings=app.settings.development --check --no-input --dry-run
	-cd src && isort .
	-cd src && black .
	-flake8 src; mypy src

test:
	-cd src/products/tests && pytest -s

static:
	-cd src && ./manage.py collectstatic --settings=app.settings.development
