.DEFAULT_GOAL = help

install:
	pipenv install

venv:
	pipenv shell

run:
	pipenv run python main.py

test:
	pipenv run pytest tests.py
	pipenv run coverage report

help:
	@echo "install"
	@echo "    Install the virtual environment"
	@echo "venv"
	@echo "    Access to the virtual environment"
	@echo "run"
	@echo "    Execute folder organizer"
	@echo "test"
	@echo "    Run the tests for this project"