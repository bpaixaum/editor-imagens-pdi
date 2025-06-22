# Editor de Imagens - Projeto de Processamento Digital

Este projeto foi desenvolvido para a disciplina **SIN 392 - Introdução ao Processamento Digital de Imagens**, da Universidade Federal de Viçosa - Campus Rio Paranaíba. O objetivo foi criar um sistema interativo com interface gráfica capaz de realizar operações clássicas de edição e análise de imagens.

## 🎯 Funcionalidades Implementadas

- ✅ **Carregar e salvar imagens** (RGB ou convertidas para tons de cinza)
- ✅ **Visualização de histograma**
- ✅ **Alargamento de contraste**
- ✅ **Equalização de histograma**
- ✅ **Filtros passa-baixa**:
  - Média
  - Mediana
  - Gaussiano
  - Máximo (Dilatação)
  - Mínimo (Erosão)
- ✅ **Filtros passa-alta**:
  - Laplaciano
  - Sobel
  - Prewitt
  - Roberts
- ✅ **Transformada de Fourier**
  - Visualização do espectro de magnitude
- ✅ **Morfologia matemática**
  - Erosão
  - Dilatação
- ✅ **Segmentação**
  - Método de Otsu
- ✅ **Funcionalidade extra (opcional)**:
  - Descritor de cor baseado em histogramas RGB normalizados

## 🖼️ Interface Gráfica (GUI)

A interface foi desenvolvida com a biblioteca [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) por sua leveza e simplicidade. As imagens são exibidas e manipuladas diretamente a partir da interface.

## 🛠️ Tecnologias Utilizadas

- Python 3.13.5
- OpenCV
- NumPy
- Matplotlib
- PySimpleGUI
- Pillow

## ▶️ Como Executar

1. Clone ou baixe este repositório:
```bash
git clone https://github.com/SEU_USUARIO/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

> Ou instale manualmente:
```bash
pip install opencv-python numpy matplotlib PySimpleGUI Pillow
```

3. Execute o sistema:
```bash
python main.py
```

## 🎥 Demonstração

[🔗 Link para o vídeo demonstrativo no YouTube (não listado)](https://youtube.com/seu-link)

## 📁 Estrutura de Pastas

```
📂 images/       → Imagens de entrada (opcional)
📂 output/       → Saídas salvas pelo usuário
📄 main.py       → Código principal com a GUI
📄 README.md     → Este arquivo
```

## 🧠 Observações

- Projeto individual e original
- Testado em ambiente Windows com Python 3.13.5

## 👨‍🏫 Professores

- Profa. Dra. Larissa Ferreira Rodrigues Moreira (T1)
- Prof. Dr. João Fernando Mari (T2)

---

Desenvolvido por Gabriel de Freitas Paixão, 2025.
