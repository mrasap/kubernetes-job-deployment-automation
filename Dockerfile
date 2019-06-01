FROM python:alpine

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /app /app

WORKDIR /app

CMD ["python", "deploy.py"]