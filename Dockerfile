FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

ENV FLASK_APP=index.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
