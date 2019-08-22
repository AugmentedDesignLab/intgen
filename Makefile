.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --prompt '|> intgen <| ' env
	python -m pip install --upgrade pip
	env/Scripts/pip install -r requirements-dev.txt
	env/Scripts/python setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/Scripts/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=intgen \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t intgen:latest .

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
