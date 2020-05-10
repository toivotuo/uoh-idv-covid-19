FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY ./resources/world-countries.json /tmp/world-countries.json
COPY ./resources/capitals.csv /tmp/capitals.csv

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8080" ]
