FROM python:3.10.4-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

RUN mkdir /recipes-app

WORKDIR /recipes-app

RUN apt update

RUN apt upgrade -y

RUN apt install curl -y

# Installing poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Adding poetry's bin to PATH
ENV PATH="${PATH}:/root/.poetry/bin"

COPY pyproject.toml .

COPY poetry.lock .

# Keeps poetry from creating virtual enviroments
RUN poetry config virtualenvs.create false

# Install dependencies with poetry ignoring dev dependencies such as black
RUN poetry install --no-dev --no-interaction

COPY docker-entrypoint.sh .

RUN chmod +x /recipes-app/docker-entrypoint.sh

EXPOSE 8000

COPY . .

ENTRYPOINT [ "sh", "/recipes-app/docker-entrypoint.sh" ]
