FROM python:3.11.4-slim-buster

WORKDIR /app

RUN apt-get update && apt-get install -y

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]