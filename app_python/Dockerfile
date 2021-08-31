# syntax=docker/dockerfile:1
FROM python:3.8-alpine AS app

WORKDIR /myapp

COPY . .

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

RUN adduser --disabled-password app -h /myapp && \
    chown -R app /myapp

CMD ["poetry", "run", "python", "server.py"]
