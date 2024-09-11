FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r grpcio grpcio-tools sqlite3

COPY . .

CMD ["python", "server.py"]