.DEFAULT_GOAL := help

.PHONY: help install run test migrate clean

PYTHON   = python3
PIP      = pip3
MANAGE   = manage.py
COLLECT_DIR = asset/


help: Makefile
	@cat Makefile

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MANAGE) runserver 0.0.0.0:8000

test:
	$(PYTHON) -W default $(MANAGE) test

makemigrations:
	$(PYTHON) $(MANAGE) makemigrations

migrate:
	$(PYTHON) $(MANAGE) migrate

collect: $(COLLECT_DIR)
	$(PYTHON) $(MANAGE) collectstatic

clean:
	-@rm -r $(COLLECT_DIR)

