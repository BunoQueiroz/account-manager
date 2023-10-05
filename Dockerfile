ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-alpine as base
RUN apk update
RUN apk add postgresql-dev gcc musl-dev
WORKDIR /application/
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

FROM python:${PYTHON_VERSION}-alpine
WORKDIR /application/
RUN apk update
RUN apk add libpq-dev
COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
RUN python -m pip install --upgrade pip
COPY . .
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
