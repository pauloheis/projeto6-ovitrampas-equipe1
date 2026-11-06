# Tempo de inferência do YOLO (medido em 06/11/2026)

## Condições do teste

| Item | Valor |
|---|---|
| Modelo | `yolo11n` pré-treinado, **sem ajuste fino** |
| Biblioteca | Ultralytics 8.4.203 |
| Ambiente | Google Colab |
| Imagem de teste | `ovitrampa2.jpg`, **1608×1206 px** |
| Método | 1 execução de aquecimento descartada; depois média de 5 repetições por rodada |
| GPU | Tesla T4 (confirmada por `nvidia-smi`) |

## Resultados

| Hardware | Rodada | 640 px | 1280 px |
|---|---|---|---|
| CPU | 1ª | 0,18 s | 0,66 s |
| CPU | 2ª | 0,20 s | 0,72 s |
| GPU (T4) | 1ª | 0,04 s | 0,06 s |
| GPU (T4) | 2ª | 0,03 s | 0,05 s |
| CPU | 3ª (com `cuda.is_available()` = `False` no print) | 0,16 s | 0,56 s |
| GPU (T4) | 3ª (com `cuda.is_available()` = `True` no print) | 0,04 s | 0,06 s |

## Verificação do hardware (transcrição do `nvidia-smi`, rodada na GPU)

- Driver: 580.82.07 · CUDA: 13.0
- GPU 0: **Tesla T4**, 15360 MiB de memória, 315 MiB em uso
- Processo: `/usr/bin/python3`, 312 MiB
- Temperatura 60 °C, uso de GPU 0% no instante da captura

(Print original: `prints/nvidia-smi-t4.png`.)

## Leitura

- O tempo de inferência **não é gargalo**: menos de 1 s por foto na CPU, e o processamento é assíncrono (ADR-001).
- **CPU basta para servir o modelo** no MVP; a GPU é útil sobretudo para o treinamento.

## Limitações

- `yolo11n` é o menor modelo da família; modelos maiores são mais precisos e mais lentos.
- Fatiar a imagem (SAHI) multiplicaria o tempo; a estimativa de cerca de 5 s por foto (30 blocos de 640 px na CPU) é **grosseira e não foi medida**.
- A imagem de teste é menor que uma foto real de celular.
- Medido no Colab, não no servidor final; valores da GPU no limite da precisão (duas casas decimais), devem ser lidos como faixa.
- Este teste mede **velocidade**, não se o modelo detecta ovos: isso depende de fotos reais e do ajuste fino.
