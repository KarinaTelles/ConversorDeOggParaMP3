#!/usr/bin/env python3
"""
Script para criar o executável do Conversor de Áudio WhatsApp
"""

import os
import subprocess
import sys
import platform


def verificar_pyinstaller():
    """Verifica se o PyInstaller está instalado"""
    try:
        import PyInstaller
        print("✓ PyInstaller encontrado")
        return True
    except ImportError:
        print("✗ PyInstaller não encontrado")
        return False


def instalar_pyinstaller():
    """Instala o PyInstaller"""
    print("\n📦 Instalando PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("✓ PyInstaller instalado com sucesso!")
        return True
    except subprocess.CalledProcessError:
        print("✗ Erro ao instalar PyInstaller")
        return False


def criar_executavel():
    """Cria o executável usando PyInstaller"""
    print("\n🔨 Criando executável...")
    
    sistema = platform.system()
    
    # Comando básico do PyInstaller
    comando = [
        "pyinstaller",
        "--onefile",  # Arquivo único
        "--windowed",  # Sem console (só janela gráfica)
        "--name=ConversorAudioWhatsApp",
        "converter_gui.py"
    ]
    
    try:
        subprocess.check_call(comando)
        print("\n✓ Executável criado com sucesso!")
        
        # Localizar o executável
        if sistema == "Windows":
            exe_path = os.path.join("dist", "ConversorAudioWhatsApp.exe")
        else:
            exe_path = os.path.join("dist", "ConversorAudioWhatsApp")
        
        print(f"\n📂 O executável está em: {exe_path}")
        print(f"💾 Tamanho: {os.path.getsize(exe_path) / 1024 / 1024:.2f} MB")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Erro ao criar executável: {e}")
        return False


def limpar_arquivos_temporarios():
    """Remove arquivos temporários da build"""
    print("\n🧹 Limpando arquivos temporários...")
    
    import shutil
    
    diretorios_para_remover = ["build", "__pycache__"]
    arquivos_para_remover = ["*.spec"]
    
    for diretorio in diretorios_para_remover:
        if os.path.exists(diretorio):
            shutil.rmtree(diretorio)
            print(f"  ✓ Removido: {diretorio}/")
    
    for arquivo in arquivos_para_remover:
        import glob
        for f in glob.glob(arquivo):
            os.remove(f)
            print(f"  ✓ Removido: {f}")


def main():
    print("=" * 60)
    print("🎵 GERADOR DE EXECUTÁVEL - CONVERSOR DE ÁUDIO WHATSAPP")
    print("=" * 60)
    
    # Verificar se o arquivo existe
    if not os.path.exists("converter_gui.py"):
        print("\n✗ Erro: converter_gui.py não encontrado!")
        print("  Execute este script na mesma pasta do converter_gui.py")
        sys.exit(1)
    
    # Verificar/instalar PyInstaller
    if not verificar_pyinstaller():
        resposta = input("\nDeseja instalar o PyInstaller? (s/n): ")
        if resposta.lower() == 's':
            if not instalar_pyinstaller():
                sys.exit(1)
        else:
            print("\nPyInstaller é necessário para criar o executável.")
            sys.exit(1)
    
    # Criar executável
    if criar_executavel():
        print("\n" + "=" * 60)
        print("✅ PROCESSO CONCLUÍDO COM SUCESSO!")
        print("=" * 60)
        
        limpar = input("\nDeseja limpar arquivos temporários? (s/n): ")
        if limpar.lower() == 's':
            limpar_arquivos_temporarios()
        
        print("\n📌 PRÓXIMOS PASSOS:")
        print("   1. Vá até a pasta 'dist'")
        print("   2. O executável está lá pronto para usar!")
        print("   3. Você pode distribuir apenas esse arquivo")
        print("\n⚠️  IMPORTANTE: O FFmpeg ainda precisa estar instalado")
        print("   no computador onde o executável for usado!")
        
    else:
        print("\n❌ Falha ao criar executável")
        sys.exit(1)


if __name__ == "__main__":
    main()