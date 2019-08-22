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
