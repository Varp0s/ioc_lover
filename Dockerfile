FROM python:3.11

WORKDIR /ioc_lover

COPY pyproject.toml poetry.lock ./
COPY envs / 
RUN apt-get update \
    && apt-get install -y curl \
    && apt-get install -y build-essential \
    && apt-get install -y python3-dev

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev

COPY ./ioc_lover /ioc_lover


CMD ["poetry", "run", "python", "main.py"]
