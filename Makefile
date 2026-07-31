COMPOSE := docker compose
UV := uv

.PHONY: help up down logs lint test

help: 
	@echo "Comandos disponíveis:"
	@echo ""
	@echo "  make up      - Inicia a infraestrutura"
	@echo "  make down    - Encerra a infraestrutura"
	@echo "  make logs    - Exibe os logs do Docker"
	@echo "  make lint    - Executa a análise de código"
	@echo "  make test    - Executa os testes"

up: 
	$(COMPOSE) up -d

down: 
	$(COMPOSE) down

logs: 
	$(COMPOSE) logs -f

lint: 
	$(UV) run ruff check .
	$(UV) run ruff format --check .

test: 
	$(UV) run pytest