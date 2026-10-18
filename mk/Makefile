GO_HTTP_SERVER:=docus-perso-mac
DOCKER_IMAGE:=mkdocs-base-image
DOCKER_FILE_PATH:=docs/mkdocs-utils/docker/Dockerfile

.ONESHELL:

docker-build:
	docker build -t $(DOCKER_IMAGE) -f $(DOCKER_FILE_PATH) .

## serve: retrieve password from macOS Keychain, start mkdocs + coffre-fort via Docker Compose
serve:
	@COFFRE_FORT_PASSWORD="$$(security find-generic-password -s coffre-fort -a coffre-fort -w 2>/dev/null)" \
	docker compose -f docs/mkdocs-utils/docker/docker-compose.yml up

## serve-mkdocs-only: start only the mkdocs container (no coffre-fort)
serve-mkdocs-only:
	docker run --rm \
		-v $$(pwd):/docs \
		-p 8000:8000 \
		$(DOCKER_IMAGE) serve --dev-addr=0.0.0.0:8000

site-build:
	docker run --rm \
		-v $$(pwd):/docs \
		$(DOCKER_IMAGE) build

jupyter:
	docker run --rm -it \
		--entrypoint jupyter \
		-v $$(pwd):/docs \
		-p 8888:8888 \
		$(DOCKER_IMAGE) notebook --notebook-dir=docs

pptx-convert:
	docker run --rm \
		--entrypoint python \
		-v $$(pwd):/docs \
		$(DOCKER_IMAGE) docs/mkdocs-utils/py/pptx_to_reveal.py --root .

go-build-intel-mac: site-build
	mv site mkdocs-macros/go/ && \
	GOOS=darwin GOARCH=amd64 go build -o mkdocs-macros/go/$(GO_HTTP_SERVER)-intel mkdocs-macros/go/main.go && \
	rm -rf mkdocs-macros/go/site

go-build: site-build
	mv site mkdocs-macros/go/ && \
	go build -o mkdocs-macros/go/$(GO_HTTP_SERVER)-arm mkdocs-macros/go/main.go && \
	rm -rf mkdocs-macros/go/site

go-run: go-build
	/mkdocs-macros/go/$(GO_HTTP_SERVER)-arm
