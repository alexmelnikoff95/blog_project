FROM python:3.10-buster

ENV PYTHONUNBUFFERED 1
ENV APP_HOST 0.0.0.0
ENV APP_PORT 8000
ENV APP_WORKERS 2
ENV APP_WORKER_TIMEOUT 120

RUN python -m pip install -U pip

RUN mkdir -p /app
WORKDIR /app
COPY compose/start.sh .

COPY requirements.txt .
RUN pip install -r /app/requirements.txt
COPY . /app/

RUN ["chmod", "+x", "/app/start.sh"]
CMD ["/app/start.sh"]