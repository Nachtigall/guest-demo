FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD . /opt/app
WORKDIR /opt/app

RUN apt-get update && apt-get install -y \
  libpq-dev \
  gcc \
  netcat \
  && apt-get clean

RUN pip install pipenv
RUN pipenv install --system --deploy

EXPOSE 8001
