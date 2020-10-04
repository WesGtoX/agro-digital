build:
	docker-compose build

bash:
	docker-compose run --rm project bash

run:
	docker-compose up

test:
	docker-compose run --rm project pytest

down:
	docker-compose down -v
