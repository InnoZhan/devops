# syntax=docker/dockerfile:1
FROM python:3.8-alpine AS app

WORKDIR /myapp

COPY . .

RUN apk add --no-cache openssl==1.1.1 libffi==3.2.1-r2 \
    adduser --disabled-password app -h /myapp && \
    chown -R app /venv && \
    chown -R app /myapp

CMD ["poetry", "run", "python", "server.py"]
