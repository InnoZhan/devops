# syntax=docker/dockerfile:1
FROM python:3.8-alpine AS app

WORKDIR /myapp

COPY . .

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
    poetry config virtualenvs.create false
    poetry install
    adduser --disabled-password app -h /myapp && \
    chown -R app /myapp

CMD ["poetry", "run", "python", "server.py"]
