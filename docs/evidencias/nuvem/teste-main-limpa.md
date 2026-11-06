# Teste da `main` com clone limpo

> Preencher. A ideia é simular um computador novo. Se o teste anterior foi feito há algum tempo, repita e tire print: sem print, não é evidência.

| Item | Valor |
|---|---|
| Data do teste | |
| Quem executou | (de preferência alguém que **não** escreveu o README) |
| Commit testado (`git rev-parse --short HEAD`) | |
| É o mesmo commit que receberá a tag? | sim / não |

## Comandos e resultado

```bash
git clone <URL-DO-REPO> teste-limpo && cd teste-limpo
cp .env.example .env
docker compose up --build -d
docker compose ps                       # todos "running"?
curl -i http://localhost:8000/health    # primeira linha: HTTP/1.1 200 OK?
docker compose down -v
```

| Passo | Resultado | Print |
|---|---|---|
| `docker compose up` | | `prints/` |
| `docker compose ps` | | `prints/` |
| `curl -i .../health` | | `prints/` |

## Verificação de arquivos indevidos

```bash
git ls-files | grep -E "\.env$|\.pt$|\.onnx$"   # não pode imprimir nada
```

Resultado: ___

## Checklist

- [ ] Rodou do zero seguindo só o README
- [ ] `.env.example` existe, sem valores reais
- [ ] Nenhum commit direto na `main` e branch protegida
- [ ] `docs/adr/` e C4 na `main`
- [ ] Testes automáticos passam (se existirem)

**Observações / problemas encontrados:**
