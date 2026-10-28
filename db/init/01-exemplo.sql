-- Este script roda automaticamente UMA vez, na primeira vez que o banco é criado vazio.
-- É só um exemplo para provar que o mecanismo funciona. O esquema real (tabelas de
-- ovitrampa, coleta, contagem) será definido pelo grupo no protótipo "banco + registro".
CREATE TABLE IF NOT EXISTS teste_compose (
    id SERIAL PRIMARY KEY,
    mensagem TEXT NOT NULL
);
INSERT INTO teste_compose (mensagem) VALUES ('o init rodou!');
