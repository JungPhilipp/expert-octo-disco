FROM python:3.8

WORKDIR /src
# Avoid console interaction
ARG DEBIAN_FRONTEND=noninteractive

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt


ENTRYPOINT ["python", "example_postgresql.py"]