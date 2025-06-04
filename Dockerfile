FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install /app/requirements.txt
COPY . /app
CMD ["python3", "app.py"]

