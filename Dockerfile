FROM python:3.8-slim AS base

COPY . /app/
WORKDIR /app

ADD scripts /app/scripts

RUN pip install --upgrade pip

RUN set -ex \
    && apt-get update && apt-get install -y wget ca-certificates

RUN sh ./scripts/install_dependencies.sh

FROM base as prod_img
ENTRYPOINT ["sh", "-c", "./scripts/run.sh"]
