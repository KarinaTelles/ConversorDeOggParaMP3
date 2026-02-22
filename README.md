# 🎵 Conversor de Áudio WhatsApp

Converta rapidamente seus áudios do WhatsApp (.ogg) para .mp3

## 📥 Download Rápido (Para Usuários)

**Versão Executável (Não precisa instalar Python!)**

1. Baixe o executável da seção [Releases](../../releases)
2. Clique duas vezes no arquivo para abrir
3. Selecione a pasta com seus áudios
4. Clique em "Converter para MP3"
5. Pronto! ✓

> ⚠️ **Importante:** Você ainda precisa ter o FFmpeg instalado no seu computador.

### Como instalar o FFmpeg:

**Windows:**
```bash
# Usando Chocolatey
choco install ffmpeg

# Ou baixe em: https://ffmpeg.org/download.html
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

---

## 👨‍💻 Para Desenvolvedores

### Método 1: Executar com Python (Modo Gráfico)

**Requisitos:**
- Python 3.7+
- FFmpeg instalado

**Passo a passo:**

1. Clone o repositório:
```bash
git clone https://github.com/KarinaTelles/ConversorDeOggParaMP3.git
cd ConversorDeOggParaMP3
```

2. Execute a interface gráfica:
```bash
python converter_gui.py
```

### Método 2: Criar seu próprio executável

**Gerar o executável automaticamente:**

1. Execute o script de build:
```bash
python build_exe.py
```

2. O script vai:
   - Verificar se você tem o PyInstaller (se não tiver, ele instala)
   - Criar o executável
   - Colocar na pasta `dist/`
   - Limpar arquivos temporários (opcional)

3. O executável estará em: `dist/ConversorAudioWhatsApp.exe` (Windows) ou `dist/ConversorAudioWhatsApp` (Mac/Linux)

**Criar executável manualmente:**

```bash
# Instalar PyInstaller
pip install pyinstaller

# Gerar executável
pyinstaller --onefile --windowed --name=ConversorAudioWhatsApp converter_gui.py

# O executável estará em dist/
```

### Método 3: Usar via linha de comando (Modo Original)

```bash
python converter_ogg_mp3.py
```

---

## 📋 Funcionalidades

✅ Interface gráfica intuitiva  
✅ Conversão em lote de múltiplos arquivos  
✅ Barra de progresso em tempo real  
✅ Detecção automática de arquivos .ogg  
✅ Qualidade de áudio ajustada para 128 kbps  
✅ Mantém o nome original dos arquivos  
✅ Verifica se FFmpeg está instalado  

---

## 🖼️ Capturas de Tela

*[Adicione screenshots da interface aqui]*

---

## ❓ Problemas Comuns

### "FFmpeg não encontrado"
- Certifique-se de que o FFmpeg está instalado
- No Windows, verifique se está no PATH do sistema
- Reinicie o terminal/computador após instalar

### "Nenhum arquivo .ogg encontrado"
- Verifique se está selecionando a pasta correta
- Os arquivos devem ter extensão `.ogg`
- Verifique se você tem permissão para ler a pasta

### O executável não abre
- Tente executar como administrador (Windows)
- Verifique seu antivírus (pode estar bloqueando)
- Certifique-se de que tem o FFmpeg instalado

---

## 📦 Estrutura do Projeto

```
ConversorDeOggParaMP3/
│
├── converter_gui.py          # Interface gráfica (principal)
├── converter_ogg_mp3.py       # Versão linha de comando
├── build_exe.py               # Script para gerar executável
├── converter.spec             # Configuração PyInstaller
└── README.md                  # Este arquivo
```

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abrir um Pull Request

---

## 📝 Licença

Este projeto é de código aberto e está disponível para uso livre.

---

## Suporte

Se encontrar algum problema ou tiver sugestões:

- Entre em contato através do GitHub


**Desenvolvido por Karina Telles (https://github.com/KarinaTelles)**