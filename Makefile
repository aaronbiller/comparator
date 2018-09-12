venv:
	python3 -m venv ./venv

hooks:
	bash bin/setup_hooks.sh

.PHONY: install
install:
	python3 setup.py install

.PHONY: test
test:
	python3 setup.py test

.PHONY: coveralls
coveralls:
	pytest -v --cov coveralls --cov-report term-missing

.PHONY: clean
clean:
	find . -iname '*.pyc' -delete