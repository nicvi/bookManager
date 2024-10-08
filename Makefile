SHELL := /bin/bash

.PHONY: install run-test run-app

install:
	@echo "====================================Installing dependencies Performance================================="
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install flake8
	@echo "Completed!"

run-test:
	@echo "==============================================Lint with flake8=========================================="
	#flake8 ./app --show-source --statistics
	@echo "Completed flake8!"
	@echo "==============================================Running test=============================================="
	pytest -vv

run-app:
	@echo "====================================Running app================================="
	uvicorn app.main:app --host 127.0.0.1 --port 7000 --reload
