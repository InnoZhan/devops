# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
COPY . .

RUN pip install poetry==1.1.8
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["poetry", "run", "python3", "server.py"]
