FROM python:3.9.0a5-alpine3.10
ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8
COPY . /srv/
RUN cd /srv/ && pip install -r requirements.txt
RUN apk add build-base
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "1992"]