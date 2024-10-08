SHELL := /bin/bash

.PHONY: install run-test

install:
	@echo "====================================Installing dependencies Performance================================="
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install flake8
	@echo "Completed!"

run-test:
	@echo "==============================================Lint with flake8=========================================="
	flake8 ./app --show-source --statistics
	@echo "Completed flake8!"
	@echo "==============================================Running test=============================================="
	./venv/bin/pytest
