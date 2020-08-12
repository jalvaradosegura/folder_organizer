install:
	pipenv install

venv:
	pipenv shell

run:
	python main.py

test:
	pytest tests.py