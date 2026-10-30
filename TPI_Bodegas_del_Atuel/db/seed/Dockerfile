FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY seed.py .
COPY catalogos ./catalogos

ENV PYTHONUNBUFFERED=1

CMD ["python", "seed.py"]
