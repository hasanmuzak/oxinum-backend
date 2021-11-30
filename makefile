run-test: ## backend unit test 
	clear; alembic downgrade base;alembic upgrade head;pytest