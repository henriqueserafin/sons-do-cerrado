# Detecção Facial e Áudio de Pássaros

Este projeto é um script em Python que detecta pontos faciais usando o MediaPipe, calcula os valores EAR (Eye Aspect Ratio) e MAR (Mouth Aspect Ratio) e reproduz sons de pássaros aleatoriamente. A aplicação utiliza o OpenCV para manipulação da câmera e o Pygame para reprodução de áudio.

## Funcionalidades

- **Detecção de Pontos Faciais**: Detecta posições dos olhos e boca usando o FaceMesh do MediaPipe.
- **Cálculo de EAR e MAR**: Calcula EAR e MAR para determinar os estados dos olhos e boca.
- **Reprodução de Áudio Aleatória**: Reproduz sons de pássaros de uma lista predefinida a cada 10 segundos.
- **Detecção de Sono**: Exibe um aviso se os olhos ficarem fechados por um período prolongado.

## Requisitos

- Python 3.x
- OpenCV
- MediaPipe
- NumPy
- Pygame

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/henriqueserafin/sons-do-cerrado
    cd sons-do-cerrado
    cd aplicativo
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Execute o script com:
```bash
python birdsenai.py
