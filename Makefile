default: build-images

build-images:
	@docker build . --target=prod_img -t api-server

rebuild-images:
	@docker build . --target=prod_img -t api-server --no-cache

run-local:
	@clear
	@docker-compose up api_server postgres

lint:
	@flake8 . --ignore=W503

create-migration:
	# To use run: make create-migration NAME="migration name"
	@alembic revision -m $(NAME)
