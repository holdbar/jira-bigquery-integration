FROM python:3.7.4-alpine

COPY ./ /app

WORKDIR /app

RUN pip install -r requirements.txt && rm -rf ~/.cache/pip/*

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["/bin/sh"]
