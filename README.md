# 🎵 Conversor de Áudio WhatsApp - Guia de Instalação

## 📌 O que você precisa fazer no PC do cliente:

---

## PASSO 1: Levar o Executável

1. Pegue o arquivo `ConversorAudioWhatsApp.exe` da pasta:
   ```
   C:\DEV\ConversorDEOggParaMP3\dist\ConversorAudioWhatsApp.exe
   ```

2. Copie para o PC do cliente (use pendrive, nuvem, etc.)

3. Coloque em uma pasta fácil de acessar, exemplo:
   ```
   C:\Programas\ConversorAudio\
   ```

---

## PASSO 2: Instalar o FFmpeg no PC do Cliente

### Método Rápido (5 minutos):

1. **Abra o PowerShell como Administrador**
   - Clique direito no menu Iniciar
   - Selecione "Terminal (Admin)" ou "PowerShell (Admin)"

2. **Cole este comando** e aperte Enter:
   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   ```
   *(Isso instala o Chocolatey - aguarde 1-2 minutos)*

3. **Cole este comando** e aperte Enter:
   ```powershell
   choco install ffmpeg -y
   ```
   *(Isso instala o FFmpeg - aguarde 2-3 minutos)*

4. **REINICIE O COMPUTADOR** (obrigatório!)

---

## PASSO 3: Verificar se Funcionou

1. Abra o Prompt de Comando (Win + R, digite `cmd`, Enter)

2. Digite:
   ```
   ffmpeg -version
   ```

3. **Se aparecer a versão do FFmpeg = Tudo certo! ✅**

4. **Se der erro = FFmpeg não instalou, tente de novo**

---

## PASSO 4: Testar o Programa

1. Clique duas vezes em `ConversorAudioWhatsApp.exe`

2. Se não abrir:
   - Clique direito > "Executar como Administrador"

3. Clique em "Selecionar Pasta"

4. Escolha uma pasta com arquivos .ogg

5. Clique em "Converter para MP3"

6. **Se funcionar = Instalação completa! 🎉**

---

## 🆘 Se Der Problema:

### FFmpeg não instalou?
1. Reinicie o computador
2. Tente instalar de novo
3. Execute os comandos como Administrador

### Programa não abre?
1. Execute como Administrador (clique direito no .exe)
2. Desative temporariamente o antivírus
3. Tente em outro PC para confirmar que o .exe está ok

### Nenhum arquivo .ogg encontrado?
1. Certifique-se que os arquivos são realmente .ogg
2. Verifique se está na pasta correta
3. No Explorador de Arquivos > Exibir > Marcar "Extensões de nomes de arquivos"

---

## 📝 Resumo Ultra-Rápido:

```
1. Leve o .exe para o PC do cliente
2. Instale FFmpeg (PowerShell Admin):
   - Instalar Chocolatey (comando 1)
   - Instalar FFmpeg (comando 2)
   - Reiniciar PC
3. Testar: ffmpeg -version
4. Abrir o programa e testar conversão
```

**Tempo total: 10-15 minutos**

---

## 💾 Onde Encontrar os Áudios do WhatsApp?

Se o cliente perguntar onde estão os áudios:

```
C:\Users\[NOME]\AppData\Roaming\WhatsApp\Media\WhatsApp Voice Notes
```

Ou na pasta Downloads se foram salvos do WhatsApp Web.

---

## ✅ Checklist Final:

Antes de sair:

- [ ] FFmpeg instalado (`ffmpeg -version` funciona)
- [ ] Programa abre
- [ ] Conversão funciona com arquivo teste
- [ ] Cliente sabe usar (selecionar pasta > converter)
- [ ] Cliente sabe onde ficam os arquivos convertidos (mesma pasta)

---

**Pronto! Isso é tudo que você precisa lembrar! 🚀**