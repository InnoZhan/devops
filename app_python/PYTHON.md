# Best practices for a Python web application

## Framework

[Flask](https://flask.palletsprojects.com/en/2.0.x/) framework was used to create web application.

It has all necessary functional, like request handling, easy response,
HTML page formatting.

## Package manager

Package manager helps to track, install, manage project dependencies.

In this project [Poetry](https://python-poetry.org/) package manager was used.

All the dependencies are listed in 'pyproject.toml' file

## Formatting tools

Formatting tools helps to reformat code for better style and make it
more readable.

In this project [Balck](https://deepsource.io/blog/python-code-formatters/) formatting tool was used, since it is one of
the most popular and conventional tools for code reformatting.

## Linters

Linter is a tool that analyzes source code to flag programming errors,
bugs, stylistic errors, and suspicious constructs.

As python linter was used [pylint](https://www.pylint.org/) to check for code errors
and following code style conventions.

For formatting markdown i have used <https://dlaa.me/markdownlint/>

[Darglint](https://github.com/terrencepreilly/darglint) was used to check docstring style.

## Create .gitignore

## Add license

For licensing [lice](https://github.com/licenses/lice) package was used

## Rules & Principles

Follow PEP 8 code style

Try to comment all parts of the code that could be difficult to understand

Use readable variable names

Use proper tabbing

Use blank lines
