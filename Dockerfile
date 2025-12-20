FROM python:3.11-slim
WORKDIR /app

# 1. Copiar solo el archivo de dependencias primero (Mejor uso del caché de Docker)
COPY requirements.txt .
# 2. Instalar dependencias con versiones fijas
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copiar el resto del código de la aplicación
COPY . .

# 4. Documentar el puerto interno del contenedor (Buena práctica)
EXPOSE 8000

# 5. Comando de ejecución: Lanza la API de FastAPI con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
