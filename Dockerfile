FROM python:3.9.0a5-alpine3.10 as encryption_api
ENV LANG C.UTF-8
WORKDIR /srv/
COPY . .
RUN apk add build-base
RUN cd /srv/ && pip install -r requirements.txt
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "1992"]