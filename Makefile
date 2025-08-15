run:
	docker-compose up
init_data:
	docker-compose down -v
	docker-compose run --rm api python manage.py migrate
	docker-compose run --rm api python manage.py create_initial_data
	docker-compose down
init: init_data run
install:
	docker compose exec api uv pip install --system --requirement pyproject.toml
