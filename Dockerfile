FROM python:3.9.0a5-alpine3.10
ENV PATH /usr/local/bin:$PATH
ENV LANG C.UTF-8
COPY . /srv/
RUN apk add build-base
RUN cd /srv/ && pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "1992"]