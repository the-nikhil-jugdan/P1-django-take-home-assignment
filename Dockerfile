FROM python:3.12-alpine
LABEL authors="the-nikhil-jugdan"

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Copying requirements
COPY ./rakt_food_app/ .

RUN apk add ca-certificates gcc postgresql-dev \
    linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev \
    gdal-dev g++

RUN pip install -r requirements.txt
