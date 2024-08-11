include .env

build:
	docker-compose --profile "*" build

start:
	docker-compose --profile app up -d

stop:
	docker-compose --profile "*" stop

ocr-dev:
	docker-compose --profile ocr-dev up -d

log:
	docker-compose --profile "*" logs -f --tail=5


