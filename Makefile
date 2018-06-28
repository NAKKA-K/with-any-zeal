.DEFAULT_GOAL := help

.PHONY: help install run test migrate clean

PYTHON   = python3
PIP      = pip3
MANAGE   = manage.py


help: Makefile
	@cat Makefile

install:
	$(PIP) install -r requirements.txt

run: $(DATABASE)
	$(PYTHON) $(MANAGE) runserver 0.0.0.0:8000

test:
	$(PYTHON) -W default $(MANAGE) test

makemigrations:
	$(PYTHON) $(MANAGE) makemigrations

migrate:
	$(PYTHON) $(MANAGE) migrate

clean:
	-@rm $(DATABASE)
