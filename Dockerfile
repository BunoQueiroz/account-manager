ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-alpine as base

WORKDIR /application/
COPY requirements.txt /application/
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
