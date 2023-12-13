default:
	@cat makefile

#make the environment - if it exists, nothing will happen
#enter into the virtual environment and install requited packages
env:
	python3 -m venv env
	. env/bin/activate; pip install -r requirements.txt

#run the file in the bin folder
run:
	@. env/bin/activate; python3 bin/clockdeco_param.py

#make sure tests will always run even though there's a folder called tests
.PHONY: tests

tests:
	. env/bin/activate; pytest -vv tests

#lint perceptron file
lint:
	. env/bin/activate; pylint bin/perceptron.py
