FROM python:3.13-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
