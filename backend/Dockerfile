# Receita para construir a imagem da API.
# Cada linha cria uma "camada"; o Docker reaproveita camadas que não mudaram.

FROM python:3.12-slim

WORKDIR /app

# Copia SÓ o requirements primeiro: se o código mudar mas as dependências
# não, o Docker pula a instalação (build bem mais rápido).
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

# Roda como usuário comum, não como root: se alguém explorar uma falha na
# API, ele não ganha poder total dentro do contêiner.
RUN useradd --create-home appuser
USER appuser

EXPOSE 8000

# 0.0.0.0 = aceita conexões de fora do contêiner (senão só ele mesmo alcança).
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
