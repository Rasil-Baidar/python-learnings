# Python Lesson 1

This project contains introductory Python lessons covering numbers, booleans, and comparison operators.

## Requirements

- Python 3.14
- Optional: Pipenv for managing the virtual environment

Check that Python is installed:

```bash
python3 --version
```

## Run with Python

From the repository workspace, change into the lesson directory and run the application:

```bash
cd learn-python/lesson-1
python3 app.py
```

The lessons only use Python's standard library, so no third-party packages need to be installed.

## Run with Pipenv

If Pipenv is installed, create the environment described by the `Pipfile` and run the application:

```bash
cd learn-python/lesson-1
pipenv install
pipenv run python app.py
```

If Pipenv is not installed:

```bash
python3 -m pip install --user pipenv
```

## Project structure

```text
lesson-1/
├── app.py
├── Pipfile
└── lessons/
    └── dataTypes/
        ├── lessonBoolean.py
        └── lessonNumbers.py
```

`app.py` imports and executes each lesson, printing its examples and results to the terminal.

## Troubleshooting

- Run the command from the `lesson-1` directory so Python can resolve the `lessons` imports.
- If `python3` is unavailable, install Python 3.14 or use a compatible Python 3 installation.
- If Pipenv cannot find Python 3.14, install that version or run the project directly with `python3 app.py`.
