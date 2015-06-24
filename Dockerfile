FROM python:3
MAINTAINER Aleksandr Vinokurov <aleksandr.vin@gmail.com>

RUN groupadd user && useradd --create-home --home-dir /code -g user user

WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code

USER user
CMD ["./run.py"]
