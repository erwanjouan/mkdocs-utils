GO_HTTP_SERVER:=docus-perso-mac
BIN_FOLDER:=.venv/bin

.ONESHELL:

activate:
	python3 -m venv .venv && \
	source $(BIN_FOLDER)/activate

install: activate
	$(BIN_FOLDER)/python3 -m pip install -r mkdocs-macros/requirements.txt && \
	mkdir -p docs/_utils && \
	curl -q https://raw.githubusercontent.com/erwanjouan/mkdocs-utils/refs/heads/main/js/secrets.js > docs/_utils/secrets.js  && \
	curl -q https://raw.githubusercontent.com/erwanjouan/mkdocs-utils/refs/heads/main/js/mermaid.min.js > docs/_utils/mermaid.min.js && \
	curl -q https://raw.githubusercontent.com/erwanjouan/mkdocs-utils/refs/heads/main/py/macros.py > docs/_utils/macros.py

init: install
	$(BIN_FOLDER)/python3 -m mkdocs new .

serve: activate
	$(BIN_FOLDER)/python3 -m mkdocs serve

site-build: activate
	$(BIN_FOLDER)/python3 -m mkdocs build

run: site-build
	docker run -v $$(pwd)/site:/usr/share/nginx/html:ro -p8080:80 nginx

docker_build:
	docker build -t some-content-nginx .

docker_run: docker_build
	docker run --name some-nginx -d -p 8080:80 some-content-nginx

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

pptx-convert: activate
	$(BIN_FOLDER)/python3 mkdocs-macros/pptx_to_reveal.py --root .
