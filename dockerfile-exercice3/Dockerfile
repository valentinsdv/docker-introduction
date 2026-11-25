FROM python:3.12-alpine

WORKDIR /app

COPY *.py *.txt ./
COPY templates/ ./templates/

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]