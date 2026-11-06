"""API do Projeto 6 (Ovitrampas / GEVACZ) - versão mínima.

Por enquanto só responde "estou vivo" (/health) e "meus vizinhos estão vivos"
(/health/ready). Os módulos do monólito (acesso, registro, contagens,
indicadores, notificação) entram aqui depois, cada um na sua pasta.
"""
import logging
import os

import psycopg  # conversa com o PostgreSQL
import redis    # conversa com o Redis
from fastapi import FastAPI, Response

log = logging.getLogger("api")
logging.basicConfig(level=logging.INFO)

# O objeto "app" é o programa inteiro. O uvicorn recebe os pedidos HTTP da
# rede e entrega cada um para ele.
app = FastAPI(title="Ovitrampas API")


@app.get("/health")
def health():
    """Liveness: 'o processo da API está de pé?'. Não consulta ninguém."""
    # O FastAPI converte este dicionário Python em JSON: {"status":"ok"}
    return {"status": "ok"}


@app.get("/health/ready")
def ready(response: Response):
    """Readiness: 'a API consegue falar com o banco e com a fila?'."""
    checks = {}

    try:
        # Os dados de conexão vêm de variáveis de ambiente (nunca no código).
        with psycopg.connect(
            host=os.environ["POSTGRES_HOST"],
            port=os.environ.get("POSTGRES_PORT", "5432"),
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            dbname=os.environ["POSTGRES_DB"],
            connect_timeout=3,
        ) as conn:
            conn.execute("SELECT 1")  # pergunta mais simples possível
        checks["db"] = "ok"
    except Exception:
        # O detalhe do erro vai para o log, não para quem chamou
        # (mensagens de erro podem revelar host, usuário, etc.).
        log.exception("falha ao conectar no PostgreSQL")
        checks["db"] = "erro"

    try:
        r = redis.Redis(
            host=os.environ["REDIS_HOST"],
            port=int(os.environ.get("REDIS_PORT", "6379")),
            password=os.environ["REDIS_PASSWORD"],
            socket_connect_timeout=3,
        )
        r.ping()  # o Redis responde PONG
        checks["redis"] = "ok"
    except Exception:
        log.exception("falha ao conectar no Redis")
        checks["redis"] = "erro"

    if "erro" in checks.values():
        response.status_code = 503  # "serviço indisponível"
    return checks
