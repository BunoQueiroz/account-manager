ARG PYTHON_VERSION=3.12.2
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
COPY --from=base /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
RUN python -m pip install --upgrade pip
COPY . .
RUN crontab -l | { cat; echo "0 * * * * /bin/sh /application/scripts/backup.sh"; } | crontab -
EXPOSE 8000
CMD [ "python", "-m", "gunicorn", "config.wsgi" ]
