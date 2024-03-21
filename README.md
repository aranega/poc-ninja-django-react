# poc-ninja-django-react

Simple PoC using ninja django, react and generation of the client API.


Tested with Python 3.12 (will probably work with 3.9 < Python <= 3.12), and Node 21.

## How to run it all

### Install dependencies for python and typescript

Create a venv for python/django and install the following dependencies:

```bash
# Do it inside your venv
pip install django django-cors-header django-ninja uvicorn
```

Then install dependencies for the frontend

```bash
# from the repo root
cd frontend
npm install
```

### Migrate/create the sqlite db and generate the openapi json schema

```bash
# from the repo root
cd backend

python manage.py migrate
python manage.py makemigrations myapp
python manage.py migrate myapp
```

### Generate the client API typescript binding and openapi json schema

```bash
# from the repo root
bash generate-binding.bash
```


### Start the client and the server

Client:

```bash
# from the repo root
cd frontend
npm start
```

Server:

```bash
# from the repo root
cd backend
uvicorn api.asgi:application

# or, for dev purpose
uvicorn api.asgi:application --reload
```


### Populate the DB

There is a special endpoint to populate the DB with dummy values.
Go to `http://127.0.0.1:3000/api/docs` and try the `/generate` endpoint.