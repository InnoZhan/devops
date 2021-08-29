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


## Unit tests

With pytest framework we can ran unit tests in tests directory.

test_connection.py checks wether connection with application is available and if application responses correctly.
test_time.py checks time difference in Moscow and time from response is less than second.

Tests Should Be Fast - less time it takes to test application more it will be tested
Tests Should Be Simple - simpler tests provides more confidence in their results
Test Shouldn’t Duplicate Implementation Logic - less chance that bug from tested code will be repeated
Tests Should Be Readable - so developer could easily track the bug from test results
Tests Should Be Deterministic - test should not change result if tested code is not changed
Adopt a Sound Naming Convention for Your Tests - tests should present which part of the application they test
