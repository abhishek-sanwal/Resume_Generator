FROM python:3.10-slim
ENV PYTHONBUFFERED 1
WORKDIR /project

COPY requirments.txt /project/requirments.txt

RUN pip install -r requirments.txt

COPY . /project
