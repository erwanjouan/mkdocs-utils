ARG MKDOCS_VERSION=9.6.14
FROM squidfunk/mkdocs-material:${MKDOCS_VERSION}

COPY py/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt