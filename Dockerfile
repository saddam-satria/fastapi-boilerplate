FROM python:alpine3.12 as builder

WORKDIR /app/fastapi-boilerplate

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN apk --no-cache add \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    && pip install --no-cache-dir -r requirements.txt

COPY app ./app

COPY config ./config

COPY database ./database

COPY pkg ./pkg 

COPY public ./public

COPY middleware ./middleware

COPY main.py ./

CMD [ "uvicorn", "main:app", "--port", "5000" ]