MKDOCS_VERSION:=9.6.14
DOCKER_IMAGE:=mkdocs-golden:$(MKDOCS_VERSION)

docker-build:
	docker build -t $(DOCKER_IMAGE) --build-arg MKDOCS_VERSION=$(MKDOCS_VERSION) .