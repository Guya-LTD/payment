DOCKER_COMPOSE_DIR=./.docker
DOCKER_COMPOSE_FILE=$(DOCKER_COMPOSE_DIR)/docker-compose.yml
DOCKER_COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE) --project-directory $(DOCKER_COMPOSE_DIR)

DEFAULT_GOAL := help
help:
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-27s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ [Docker] Build / Infrastructure
.docker/.env:
	cp $(DOCKER_COMPOSE_DIR)/.env.example $(DOCKER_COMPOSE_DIR)/.env

.PHONY: init
init: .docker/.env ## Make sure the .env file exists for docker

.PHONY: clean
clean: ## Remove the .env file for docker
	rm -f $(DOCKER_COMPOSE_DIR)/.env

.PHONY: test
test:

.PHONY: build 
build: clean init ## Build all docker images from scratch, without cache etc. Build a specific image by providing the service name via: make build CONTAINER=<service>s
	$(DOCKER_COMPOSE) rm -fs $(CONTAINER)
	$(DOCKER_COMPOSE) build --no-cache --parallel $(CONTAINER)

.PHONY: re-build
re-build: init ## Build all docker images. Build a specific image by providing the service name via: make docker-build CONTAINER=<service>
	$(DOCKER_COMPOSE) build --parallel $(CONTAINER)

.PHONY: run
run: ## Start all docker containers. To only start one container, use CONTAINER=<service>
	$(DOCKER_COMPOSE) up -d --force-recreate $(CONTAINER)
	#$(DOCKER_COMPOSE) up -d $(CONTAINER)

.PHONY: stop
stop: ## Stop all docker containers. To only stop one container, use CONTAINER=<service>
	$(DOCKER_COMPOSE) down $(CONTAINER)

.PHONY: all
all: build run # Build from scratch, no cache, and run 
