PY = python3
VENV = venv
BIN=$(VENV)/bin

## make install; - install dependencies
.PHONY: install
install:
		@echo "Installing..."
		pip install -r requirements.txt

## make install; - install dependencies
.PHONY: run
run:
		@echo "Running the Server..."
		uvicorn main:app --reload
