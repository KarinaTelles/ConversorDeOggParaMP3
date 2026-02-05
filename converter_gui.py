import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import subprocess
from pathlib import Path
import threading


class ConverterGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Áudio WhatsApp")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # Variáveis
        self.pasta_selecionada = tk.StringVar()
        self.arquivos_ogg = []
        
        # Configurar estilo
        self.configurar_estilo()
        
        # Criar interface
        self.criar_widgets()
        
    def configurar_estilo(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Cores modernas
        self.cor_primaria = "#25D366"  # Verde WhatsApp
        self.cor_secundaria = "#128C7E"
        self.cor_fundo = "#f0f0f0"
        self.cor_texto = "#333333"
        
        self.root.configure(bg=self.cor_fundo)
        
    def criar_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="🎵 Conversor de Áudio WhatsApp",
            font=("Arial", 18, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_secundaria
        )
        titulo.pack(pady=(0, 20))
        
        # Subtítulo
        subtitulo = tk.Label(
            main_frame,
            text="Converta seus áudios .ogg para .mp3",
            font=("Arial", 10),
            bg=self.cor_fundo,
            fg=self.cor_texto
        )
        subtitulo.pack(pady=(0, 30))
        
        # Frame de seleção de pasta
        pasta_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        pasta_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Botão selecionar pasta
        btn_selecionar = tk.Button(
            pasta_frame,
            text="📁 Selecionar Pasta",
            command=self.selecionar_pasta,
            bg=self.cor_primaria,
            fg="white",
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=10
        )
        btn_selecionar.pack(side=tk.LEFT)
        
        # Label com caminho da pasta
        self.label_pasta = tk.Label(
            pasta_frame,
            textvariable=self.pasta_selecionada,
            font=("Arial", 9),
            bg=self.cor_fundo,
            fg=self.cor_texto,
            anchor="w"
        )
        self.label_pasta.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
        
        # Frame da lista de arquivos
        lista_frame = tk.LabelFrame(
            main_frame,
            text="Arquivos encontrados",
            font=("Arial", 10, "bold"),
            bg=self.cor_fundo,
            fg=self.cor_secundaria
        )
        lista_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(lista_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox
        self.listbox = tk.Listbox(
            lista_frame,
            yscrollcommand=scrollbar.set,
            font=("Arial", 9),
            bg="white",
            relief=tk.FLAT,
            selectmode=tk.SINGLE
        )
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.listbox.yview)
        
        # Frame de progresso
        self.progress_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        self.progress_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Label de status
        self.label_status = tk.Label(
            self.progress_frame,
            text="",
            font=("Arial", 9),
            bg=self.cor_fundo,
            fg=self.cor_texto
        )
        self.label_status.pack(anchor="w")
        
        # Barra de progresso
        self.progressbar = ttk.Progressbar(
            self.progress_frame,
            mode='determinate',
            length=300
        )
        self.progressbar.pack(fill=tk.X, pady=(5, 0))
        
        # Botão converter
        self.btn_converter = tk.Button(
            main_frame,
            text="▶ Converter para MP3",
            command=self.iniciar_conversao,
            bg=self.cor_secundaria,
            fg="white",
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=12,
            state=tk.DISABLED
        )
        self.btn_converter.pack(fill=tk.X)
        
    def selecionar_pasta(self):
        pasta = filedialog.askdirectory(title="Selecione a pasta com os áudios")
        if pasta:
            self.pasta_selecionada.set(pasta)
            self.buscar_arquivos_ogg(pasta)
            
    def buscar_arquivos_ogg(self, pasta):
        self.listbox.delete(0, tk.END)
        self.arquivos_ogg = []
        
        try:
            for arquivo in os.listdir(pasta):
                if arquivo.lower().endswith('.ogg'):
                    self.arquivos_ogg.append(arquivo)
                    self.listbox.insert(tk.END, f"🎵 {arquivo}")
            
            if self.arquivos_ogg:
                self.label_status.config(
                    text=f"✓ {len(self.arquivos_ogg)} arquivo(s) .ogg encontrado(s)",
                    fg="green"
                )
                self.btn_converter.config(state=tk.NORMAL)
            else:
                self.label_status.config(
                    text="⚠ Nenhum arquivo .ogg encontrado nesta pasta",
                    fg="orange"
                )
                self.btn_converter.config(state=tk.DISABLED)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao ler a pasta: {str(e)}")
            
    def verificar_ffmpeg(self):
        """Verifica se o FFmpeg está instalado"""
        try:
            subprocess.run(['ffmpeg', '-version'], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE,
                         check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
            
    def iniciar_conversao(self):
        if not self.verificar_ffmpeg():
            messagebox.showerror(
                "FFmpeg não encontrado",
                "O FFmpeg não está instalado ou não está no PATH.\n\n"
                "Por favor, instale o FFmpeg:\n"
                "• Windows: choco install ffmpeg\n"
                "• macOS: brew install ffmpeg\n"
                "• Linux: sudo apt install ffmpeg"
            )
            return
        
        # Desabilitar botões durante conversão
        self.btn_converter.config(state=tk.DISABLED)
        
        # Iniciar conversão em thread separada
        thread = threading.Thread(target=self.converter_arquivos)
        thread.daemon = True
        thread.start()
        
    def converter_arquivos(self):
        pasta = self.pasta_selecionada.get()
        total = len(self.arquivos_ogg)
        
        self.progressbar['maximum'] = total
        self.progressbar['value'] = 0
        
        sucesso = 0
        erro = 0
        
        for i, arquivo_ogg in enumerate(self.arquivos_ogg, 1):
            try:
                # Atualizar status na thread principal
                self.root.after(0, self.atualizar_status, 
                              f"Convertendo {i}/{total}: {arquivo_ogg}")
                
                # Caminhos dos arquivos
                caminho_ogg = os.path.join(pasta, arquivo_ogg)
                nome_base = os.path.splitext(arquivo_ogg)[0]
                caminho_mp3 = os.path.join(pasta, f"{nome_base}.mp3")
                
                # Comando FFmpeg
                comando = [
                    'ffmpeg',
                    '-i', caminho_ogg,
                    '-codec:a', 'libmp3lame',
                    '-b:a', '128k',
                    '-y',  # Sobrescrever sem perguntar
                    caminho_mp3
                ]
                
                # Executar conversão
                resultado = subprocess.run(
                    comando,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=True
                )
                
                sucesso += 1
                
            except subprocess.CalledProcessError as e:
                erro += 1
                print(f"Erro ao converter {arquivo_ogg}: {e}")
            except Exception as e:
                erro += 1
                print(f"Erro inesperado com {arquivo_ogg}: {e}")
            
            # Atualizar barra de progresso
            self.root.after(0, self.progressbar.config, {'value': i})
        
        # Finalizar
        self.root.after(0, self.finalizar_conversao, sucesso, erro, total)
        
    def atualizar_status(self, mensagem):
        self.label_status.config(text=mensagem, fg=self.cor_texto)
        
    def finalizar_conversao(self, sucesso, erro, total):
        if erro == 0:
            self.label_status.config(
                text=f"✓ Conversão concluída! {sucesso}/{total} arquivos convertidos com sucesso",
                fg="green"
            )
            messagebox.showinfo(
                "Sucesso!",
                f"Todos os {sucesso} arquivos foram convertidos para MP3!\n\n"
                f"Os arquivos estão na mesma pasta dos originais."
            )
        else:
            self.label_status.config(
                text=f"⚠ Conversão finalizada: {sucesso} sucesso, {erro} erro(s)",
                fg="orange"
            )
            messagebox.showwarning(
                "Conversão finalizada com erros",
                f"Sucesso: {sucesso}\nErros: {erro}\n\n"
                f"Verifique se os arquivos com erro estão corrompidos."
            )
        
        # Reabilitar botão
        self.btn_converter.config(state=tk.NORMAL)
        
        # Resetar barra de progresso
        self.progressbar['value'] = 0


def main():
    root = tk.Tk()
    app = ConverterGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()