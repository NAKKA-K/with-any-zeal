.DEFAULT_GOAL := help

.PHONY: help install run test migrate clean

PYTHON   = python3
PIP      = pip3
MANAGE   = manage.py
DATABASE = aetam.sqlite3


help: Makefile
	@cat Makefile

install:
	$(PIP) install -r requirements.txt

run: $(DATABASE)
	$(PYTHON) $(MANAGE) runserver

test:
	$(PYTHON) -Wall $(MANAGE) test

migrate: $(DATABASE)
$(DATABASE):
	$(PYTHON) $(MANAGE) migrate

clean:
	-@rm $(DATABASE)
