import os
import subprocess
from pathlib import Path

def converter_ogg_para_mp3(pasta):
    pasta = Path(pasta)
    arquivos = list(pasta.glob("*.ogg"))

    if not arquivos:
        print("Nenhum arquivo .ogg encontrado na pasta.")
        return

    for arquivo in arquivos:
        mp3_saida = arquivo.with_suffix(".mp3")
        print(f"Convertendo: {arquivo.name} → {mp3_saida.name}")
        comando = [
            "ffmpeg", "-y",
            "-i", str(arquivo),
            "-acodec", "libmp3lame",
            "-ab", "128k",
            str(mp3_saida)
        ]
        subprocess.run(comando, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("✅ Conversão concluída!")

if __name__ == "__main__":
    pasta_entrada = input("Digite o caminho da pasta com os áudios do WhatsApp: ").strip()
    converter_ogg_para_mp3(pasta_entrada)
