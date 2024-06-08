# Use a base image com Python
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py

# Expõe a porta que o Flask usa
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app:app"]
