# Backend for Bookstore app

Django-based project. Frontend is built on React.js and can be found in the separate repo.

## Configuration

Configuration is stored in ```src/core/.env```, for examples see ```src/app/.sample.env```

## Installing on a local machine

This project requires python 3.9. Deps are managed by the package manager [pip](https://pip.pypa.io/en/stable/).

Step 1: Create a new virtualenv and install requirements:

```bash 
pip install -r dev-requirements.txt
```

Step 2: Rename .sample.env to .env:

```bash
mv .sample.env .env
```

Step 3 : Run server:

```bash
$ python src/manage.py migrate --settings=app.settings.development
```
```bash
$ python src/manage.py createsuperuser --settings=app.settings.development
```
```bash
$ python src/manage.py runserver --settings=app.settings.development
```


Or you can ```run server``` by simply:

```bash
make server
```
Testing:

```bash
# run lint
make lint

# run unit tests
make test
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Backend Code requirements

Obey django's style guide.

Configure your IDE to use flake8 for checking your python code. 

For running flake8 manualy, do cd src && flake8

Prefer English over your native language in comments and commit messages.




## License

[MIT](https://choosealicense.com/licenses/mit/)
