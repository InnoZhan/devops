# Moscow-time

Moscow-time is a Python web application for that provides current time in Moscow.

## Installation

Clone the repository

Use the Poetry package manager [Poetry](https://python-poetry.org/) to install Moscow-time.

```bash
pip install poetry
cd app_python
poetry install
```

## Usage

To start application we need to run it from poetry package manager

```bash
poetry run python server.py
```

Now app runs on port 5000 on localhost

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Docker image download

To clone docker image use
```bash
sudo docker pull zhandos1609/moscow-time
```

## Docker image run image

To start application

```bash
sudo docker run -p 5000:5000 zhandos1609/moscow-time
```
