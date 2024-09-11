# Usa una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos requirements.txt (si los tienes) y server.py al contenedor
COPY requirements.txt requirements.txt

# Instalar las dependencias de Python (gRPC y cualquier otra que uses)
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto a la carpeta /app
COPY . .

# Exponer el puerto 50051 para gRPC
EXPOSE 50051

# Comando para ejecutar el servidor
CMD ["python", "server.py"]
