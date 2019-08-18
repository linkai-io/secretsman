install:
	pip install .
	
venv: requirements.txt
	python3 -m venv .venv
	. ./.venv/bin/activate && \
	pip --quiet install --upgrade pip && \
	pip --quiet install -r requirements.txt
	pip --quiet install .

test: venv
	pytest tests/

buildexample:
	docker build -t service -f Dockerfile.service .
