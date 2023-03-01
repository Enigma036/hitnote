# syntax=docker/dockerfile:1

FROM python:3.10-buster

WORKDIR /

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --system --deploy
RUN pip install flask==2.2.2
RUN pip install Flask-SQLAlchemy==3.0.3
RUN pip install Flask-Login==0.6.2

COPY . .

CMD ["./start.sh"]

