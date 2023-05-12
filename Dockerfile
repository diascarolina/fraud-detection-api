FROM python:3.9-slim-buster

RUN mkdir /home/project/

COPY . /home/project/

WORKDIR /home/project/

ENV SYSTEM_VERSION_COMPAT=1

RUN apt-get clean \
    && apt-get update \
    && apt-get install -y curl \
    && pip install --no-cache-dir --upgrade pip

RUN pip install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-root \
    && poetry run pytest

EXPOSE 8000

ENTRYPOINT [ "sh", "init.sh" ]