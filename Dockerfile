FROM python:3.9.5-slim
RUN pip install pipenv

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy --ignore-pipfile --dev

COPY . ./
