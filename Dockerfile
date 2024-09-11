FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r grpcio grpcio-tools

COPY . .
EXPOSE 50051

CMD ["python", "server.py"]