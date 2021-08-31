# syntax=docker/dockerfile:1
FROM python:3.8-alpine AS app_deps

WORKDIR /myapp

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --no-cache build-base openssl-dev libffi-dev

RUN python3 -m venv /venv

COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry==1.1.8 && \
  poetry export -f requirements.txt | \
  /venv/bin/python3 -m pip install -r /dev/stdin

FROM python:3.8-alpine AS app

WORKDIR /myapp

COPY --from=app_deps /venv /venv
COPY . .

RUN apk add --no-cache openssl libffi

RUN adduser --disabled-password app -h /myapp && \
  chown -R app /venv && \
  chown -R app /myapp

CMD ["/venv/bin/python3", "server.py"]
