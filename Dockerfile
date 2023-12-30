FROM  python:3.11
ENV PYTHONDONTWRITENYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . /new
WORKDIR /new

RUN pip install -r requirements.txt