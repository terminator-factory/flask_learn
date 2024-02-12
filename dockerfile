FROM python:3.10.13-slim

WORKDIR /app

COPY . /app

RUN apt-get update && \
    apt-get install -y gcc python3-dev &&\
    pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 9697

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0:9697", "predict:app"]