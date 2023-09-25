FROM python:3.10

RUN mkdir /ClimbingTrainerAPI

COPY /ClimbingTrainerAPI /ClimbingTrainerAPI
RUN apt-get update
RUN apt-get install -y postgresql-client

WORKDIR /ClimbingTrainerAPI
ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD ["./docker-entrypoint.sh"]
