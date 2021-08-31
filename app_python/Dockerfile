# syntax=docker/dockerfile:1
FROM python:3.8-alpine AS app_deps

WORKDIR /myapp

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --no-cache build-base==0.4-r1 openssl-dev==1.1.1 libffi-dev==3.3-r2 \
    python3 -m venv /venv

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install --no-cache-dir poetry==1.1.8 && \
    poetry export -f requirements.txt | \
    /venv/bin/python3 -m pip install -r /dev/stdin

FROM python:3.8-alpine AS app

WORKDIR /myapp

COPY . .

RUN apk add --no-cache openssl==1.1.1 libffi==3.2.1-r2 \
    adduser --disabled-password app -h /myapp && \
    chown -R app /venv && \
    chown -R app /myapp

CMD ["poetry", "run", "python", "server.py"]
