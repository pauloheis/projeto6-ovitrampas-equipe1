# Evidências — Sprint 3 (07/11/2026)

Grupo 1 · Projeto 6 (GEVACZ). Esta pasta reúne as evidências por disciplina. Legenda: ✅ pronto · 🟡 parcial · ⬜ falta.

> Os **prints originais** devem ser salvos nas subpastas `prints/` de cada disciplina, com o nome indicado abaixo. Os arquivos `.md` desta pasta transcrevem os resultados em texto, mas não substituem o print.

## Machine Learning

| Evidência | Status | Onde |
|---|---|---|
| Tempos de inferência (CPU e GPU), com condições do teste | ✅ | `ml/tempos-inferencia.md` |
| Print da saída dos tempos na CPU (1ª rodada) | ✅ | `ml/prints/tempos-cpu.png` |
| Print da CPU com tempos + `torch.cuda.is_available()` = `False` | ✅ | `ml/prints/tempos-cpu-cuda-false.png` |
| Print da GPU com tempos + `torch.cuda.is_available()` = `True` | ✅ | `ml/prints/tempos-gpu-cuda-true.png` |
| Print com as 2 rodadas de CPU e de GPU + tamanho da imagem | ✅ (é uma anotação do grupo; ideal: print da saída real da GPU) | `ml/prints/resumo-rodadas-cpu-gpu.png` |
| Print do `nvidia-smi` (Tesla T4) | ✅ | `ml/prints/nvidia-smi-t4.png` |
| Registro de validação (go/no-go) | ✅ | ADR-005 em `docs/adr/` |
| Teste do baseline clássico (T10) em 1 foto provisória | 🟡 preencher | `ml/baseline-t10.md` |
| Notebook do baseline clássico (T10) | ⬜ commitar | `notebooks/` no repositório |
| Custo de rotulagem (minutos por ovo) | ⬜ medir | `ml/custo-rotulagem.md` |
| Lista de datasets públicos com licença (T3) | ⬜ anexar | `ml/datasets-publicos.md` (ou link para o arquivo da T3) |

## Arquitetura Nativa em Nuvem

| Evidência | Status | Onde |
|---|---|---|
| ADRs 001 a 005 | ✅ | `docs/adr/` |
| C4 níveis 1 e 2 (T2) | ⬜ anexar | `docs/c4/` |
| Teste da `main` com clone limpo (`docker compose up` + `/health`) | ⬜ registrar | `nuvem/teste-main-limpa.md` + `nuvem/prints/` |
| Pesquisa comparativa de nuvem gratuita/acadêmica (T12) | ⬜ anexar | link para o arquivo da T12 |
| Tag `v0.3.0` no GitHub | ⬜ criar | print da página de Releases/Tags em `nuvem/prints/tag-v030.png` |

## Segurança da Informação

| Evidência | Status | Onde |
|---|---|---|
| Tabela de ativos, riscos, perfis de acesso e dados LGPD (T6) | ⬜ anexar | `docs/seguranca/` |
| Regras de segredos (`.env.example`, `.gitignore`, secret scanning) | ⬜ print | `seguranca/prints/` |

## Projeto

| Evidência | Status | Onde |
|---|---|---|
| Wireframes (T8) | ⬜ anexar | link ou imagens |
| Modelo de dados ER + migração (T7) | ⬜ anexar | `docs/` |
| Contato com o GEVACZ (pedido de fotos, data, resposta) | ⬜ preencher | `projeto/contato-gevacz.md` |
| Quadro Scrum com as tarefas da semana 1 concluídas | ⬜ print | `projeto/prints/quadro-scrum.png` |

## Estrutura da pasta

```
docs/evidencias/
├── README.md
├── ml/            tempos-inferencia.md · baseline-t10.md · custo-rotulagem.md · prints/
├── nuvem/         teste-main-limpa.md · prints/
├── seguranca/     prints/
└── projeto/       contato-gevacz.md · prints/
```

## Uso de IA

Parte da estrutura e dos modelos desta pasta foi gerada com apoio de IA (Claude). Os resultados e medidas são do grupo.
