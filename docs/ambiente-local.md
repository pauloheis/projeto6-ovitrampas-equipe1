# Infra local do Projeto 6 (Ovitrampas / GEVACZ)

Sobe o banco PostgreSQL e uma tela web (Adminer) para ver as tabelas, com um comando.

## Pré-requisitos
- Docker Desktop instalado e **aberto** (Windows/Mac) ou Docker Engine + plugin compose (Linux).
- Teste: `docker compose version` deve mostrar uma versão.

## Como rodar (primeira vez)
1. Copie o arquivo de variáveis e troque a senha:
   - Linux/Mac: `cp .env.example .env`
   - Windows (PowerShell): `Copy-Item .env.example .env`
   - Abra o `.env` e troque `POSTGRES_PASSWORD` por uma senha sua.
2. Suba tudo: `docker compose up -d`
3. Veja se está saudável: `docker compose ps` (o `db` deve aparecer como `healthy`).
4. Abra http://localhost:8080 e entre com:
   - Sistema: PostgreSQL | Servidor: `db` | Usuário/Senha/Base: os valores do seu `.env`.
   - Deve existir a tabela `teste_compose` (criada pelo script em `db/init/`).

## Comandos do dia a dia
| Comando | O que faz |
|---|---|
| `docker compose up -d` | liga tudo em segundo plano |
| `docker compose logs -f db` | acompanha o log do banco (Ctrl+C sai) |
| `docker compose down` | desliga (dados do banco continuam) |
| `docker compose down -v` | desliga e **apaga os dados** |

## Atenção
- `.env` nunca vai para o Git (já está no `.gitignore`).
- Scripts em `db/init/` só rodam quando o banco é criado do zero. Se mudar um script e quiser reaplicar: `docker compose down -v` e `docker compose up -d`.
- Armazenamento das fotos das palhetas: ainda NÃO incluído (decisão pendente do grupo).
