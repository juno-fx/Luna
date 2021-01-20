BROWSER := xdg-open

ifeq ($(OS),Windows_NT)
    BROWSER := start
endif

.PHONY: docs

# local devel workflow
setup:
	@pre-commit install -c ./.githooks/.pre-commit-config.yaml

build:
	@docker-compose build

clean:
	@rm -rf docs/_build htmlcov/*

clean-docker:
	@docker-compose down -v --remove-orphans --rmi local
	@docker network prune -f
	@docker volume prune -f

dev:
	@docker-compose up
	@make clean-docker

docs: clean
	@docker-compose run luna sh -c "sphinx-build -b html docs docs/_build"
	@make clean-docker

lint:
	@docker-compose run luna pylint ./luna --fail-under=9
	@make clean-docker

test: clean
	@docker-compose up -d workstation
	@docker-compose run luna sh -c "coverage run -m unittest discover -s ./tests -p '*_test.py' && coverage html && coverage report --fail-under=90"
	@make clean-docker
