# Usar imagen base Python 3.8
FROM python:3.8-slim

# Establecer directorio de trabajo
WORKDIR /app

# Actualizar pip
RUN pip install --upgrade pip

# Copiar requirements.txt primero (para aprovechar el cache de Docker)
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Railway asigna el puerto dinámicamente
EXPOSE $PORT

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Comando por defecto para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:$PORT", "portfolio.wsgi:application" ]