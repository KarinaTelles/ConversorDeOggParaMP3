# WhatsApp Audio to MP3 Converter

Converta rapidamente seus áudios do WhatsApp (.ogg) para .mp3 com este script Python simples.

## Como usar

* Clone ou baixe este repositório.

* Abra o terminal na pasta do script.

## Execute:

* python converter.py

* Informe o caminho da pasta com seus áudios do WhatsApp (.ogg).

  
Exemplo:

C:\Usuários\UserName\Downloads\Audios


## Todos os arquivos serão convertidos para .mp3 na mesma pasta.

Funcionalidades:

* Converte todos os .ogg de uma pasta para .mp3

* Mantém o nome original

* Qualidade de áudio ajustada para 128 kbps

* Sobrescreve arquivos existentes com o mesmo nome

## Pré-requisitos

Python 3.x

FFmpeg
 instalado e no PATH

## Instalação rápida do FFmpeg:

Windows:

* choco install ffmpeg


macOS:

* brew install ffmpeg


Linux (Debian/Ubuntu):

* sudo apt update
* sudo apt install ffmpeg

## Observações

* Certifique-se de que a pasta contém arquivos .ogg.

* Arquivos existentes com o mesmo nome serão sobrescritos.

## Modo Gráfico (Recomendado)

Execute a versão com interface gráfica:
python converter_gui.py