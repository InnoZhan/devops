# syntax=docker/dockerfile:1
FROM python:3.8-alpine AS app_deps

WORKDIR /myapp

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk add --no-cache build-base==0.4-r1 openssl-dev==1.1.1 libffi-dev==3.3-4

RUN python3 -m venv /venv

COPY pyproject.toml .
COPY poetry.lock .

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN pip install poetry==1.1.8 && \
  poetry export -f requirements.txt | \
  /venv/bin/python3 -m pip install -r /dev/stdin

FROM python:3.8-alpine AS app

WORKDIR /myapp

COPY --from=app_deps /venv /venv
COPY . .

RUN apk add --no-cache openssl==1.1.1 libffi==3.4.2

RUN adduser --disabled-password app -h /myapp && \
  chown -R app /venv && \
  chown -R app /myapp

CMD ["/venv/bin/python3", "server.py"]
