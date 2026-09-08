# Use a imagem oficial do Python 3.11-slim como base
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências do requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do projeto para o diretório de trabalho
COPY . .

# Exponha a porta 8000
EXPOSE 8000

# Comando para iniciar o aplicativo Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
