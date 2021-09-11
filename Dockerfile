FROM python3.9-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /source
COPY requirements.txt /source/

COPY vendor /source/vendor/

RUN pip3 install -r requirements.txt

WORKDIR /source

COPY . /source/

WORKDIR /source/backend

EXPOSE 8000