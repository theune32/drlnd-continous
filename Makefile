VIRTUAL_ENV=venv
ENVIRONMENT_URL=https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip
EXAMPLE_NOTEBOOK=https://raw.githubusercontent.com/udacity/deep-reinforcement-learning/master/p2_continuous-control/Continuous_Control.ipynb

${VIRTUAL_ENV}:
	virtualenv ${VIRTUAL_ENV} -p python3.6
	(source ${VIRTUAL_ENV}/bin/activate; pip install -r requirements.txt;)

.PHONY: virtualenv
virtualenv: ${VIRTUAL_ENV}

.PHONY: freeze
freeze:
	(source ${VIRTUAL_ENV}/bin/activate; pip freeze > requirements.txt; )

.PHONY: clean
clean:
	rm -rf ${VIRTUAL_ENV}
	rm -rf files/

files/Reacher.app.zip:
	mkdir -p files/
	wget -O $@ ${ENVIRONMENT_URL}

files/Reacher.app: files/Reacher.app.zip
	unzip -d files $@.zip

files/Continous_Control.ipynb:
	mkdir -p files/
	wget -O $@ ${EXAMPLE_NOTEBOOK}

.PHONY: setup
setup: files/Continous_Control.ipynb files/Reacher.app virtualenv