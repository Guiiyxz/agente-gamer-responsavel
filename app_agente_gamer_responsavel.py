import customtkinter as ctk
from tkinter import messagebox
from pathlib import Path
from datetime import datetime

# ============================================================
# ENTREGA 4 - AGENTE GAMER RESPONSÁVEL
# Projeto desenvolvido em Python + CustomTkinter
#
# Objetivo:
# Criar um agente inteligente simples baseado em:
# - palavras-chave
# - regras éticas
# - respostas automáticas
#
# O agente responde perguntas relacionadas a:
# - jogos
# - segurança online
# - hardware
# - esports
# - comportamento gamer
#
# ============================================================

# Caminho da pasta do projeto
APP_DIR = Path(__file__).parent

# ============================================================
# CONFIGURAÇÃO VISUAL
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# ============================================================
# BASE DE CONHECIMENTO
#
# Funciona como um "mini cérebro" do agente.
# Cada palavra-chave possui uma resposta associada.
# ============================================================

BASE_CONHECIMENTO = {

    "fps": (
        "Jogos FPS exigem reflexo, estratégia "
        "e comunicação entre jogadores."
    ),

    "valorant": (
        "Valorant é um jogo competitivo que mistura "
        "tiro tático e habilidades especiais."
    ),

    "minecraft": (
        "Minecraft estimula criatividade, construção "
        "e lógica através da exploração do mundo."
    ),

    "steam": (
        "Ative a autenticação em duas etapas na Steam "
        "para aumentar a segurança da sua conta."
    ),

    "golpe": (
        "Nunca clique em links suspeitos ou compartilhe "
        "informações pessoais em jogos online."
    ),

    "senha": (
        "Jamais compartilhe sua senha com outras pessoas."
    ),

    "pc gamer": (
        "Um bom PC Gamer deve possuir processador, "
        "memória RAM e placa de vídeo equilibrados."
    ),

    "esports": (
        "O cenário competitivo exige treino, disciplina "
        "e trabalho em equipe."
    ),

    "toxicidade": (
        "Evite comportamento tóxico e respeite os outros jogadores."
    ),

    "ranked": (
        "Organize seu tempo e evite excesso de partidas seguidas."
    ),

    "mods": (
        "Baixe mods apenas de sites confiáveis para evitar vírus."
    ),

    "hack": (
        "O uso de hacks e cheats prejudica a experiência "
        "dos jogadores e pode causar banimento."
    )
}

# ============================================================
# TERMOS SENSÍVEIS
#
# O agente verifica se o usuário digitou
# informações pessoais ou privadas.
# ============================================================

TERMOS_SENSIVEIS = [
    "cpf",
    "cartão",
    "pix",
    "rg",
    "token",
    "endereço",
    "dados bancários"
]

# ============================================================
# FUNÇÃO PRINCIPAL DE RESPOSTA
#
# Responsável por:
# 1. Ler a pergunta
# 2. Verificar termos sensíveis
# 3. Procurar palavras-chave
# 4. Retornar resposta
# ============================================================

def gerar_resposta(pergunta):

    # Remove espaços e converte para minúsculo
    pergunta_limpa = pergunta.lower().strip()

    # ========================================================
    # VERIFICAÇÃO DE PRIVACIDADE
    # ========================================================

    for termo in TERMOS_SENSIVEIS:

        if termo in pergunta_limpa:

            return (
                "⚠️ Por segurança, não compartilhe "
                "dados pessoais ou financeiros."
            )

    # ========================================================
    # BUSCA POR PALAVRAS-CHAVE
    # ========================================================

    for palavra, resposta in BASE_CONHECIMENTO.items():

        if palavra in pergunta_limpa:

            return resposta

    # ========================================================
    # RESPOSTA FORA DO ESCOPO
    # ========================================================

    return (
        "🎮 Ainda não tenho uma resposta para isso.\n"
        "Tente reformular sua pergunta."
    )

# ============================================================
# CLASSE PRINCIPAL DO APP
# ============================================================

class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ====================================================
        # CONFIGURAÇÃO DA JANELA
        # ====================================================

        self.title("Agente Gamer Responsável")
        self.geometry("1150x720")
        self.minsize(980, 640)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Criação das áreas
        self.criar_sidebar()
        self.criar_conteudo()

    # ========================================================
    # MENU LATERAL
    # ========================================================

    def criar_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="#0B1120"
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_rowconfigure(8, weight=1)

        # Logo simples
        ctk.CTkLabel(
            self.sidebar,
            text="🎮",
            font=ctk.CTkFont(size=50)
        ).grid(row=0, column=0, padx=30, pady=(30, 10))

        # Título
        ctk.CTkLabel(
            self.sidebar,
            text="Agente Gamer",
            font=ctk.CTkFont(size=26, weight="bold")
        ).grid(row=1, column=0)

        # Descrição
        ctk.CTkLabel(
            self.sidebar,
            text=(
                "Assistente gamer com\n"
                "regras éticas e segurança online"
            ),
            justify="center"
        ).grid(row=2, column=0, pady=(0, 25))

        # Informações
        self.card_info(
            "🎮 Jogos",
            "Informações sobre jogos e gameplay.",
            3
        )

        self.card_info(
            "🔒 Segurança",
            "Proteção de contas e privacidade.",
            4
        )

        self.card_info(
            "💻 Hardware",
            "Dicas sobre PC Gamer e desempenho.",
            5
        )

        self.card_info(
            "🏆 Esports",
            "Competitivo, treino e organização.",
            6
        )

        # Botão política ética
        ctk.CTkButton(
            self.sidebar,
            text="Política ética",
            command=self.mostrar_politica
        ).grid(
            row=9,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

        # Botão limpar conversa
        ctk.CTkButton(
            self.sidebar,
            text="Limpar conversa",
            fg_color="#1E3A8A",
            hover_color="#2563EB",
            command=self.limpar_conversa
        ).grid(
            row=10,
            column=0,
            padx=20,
            pady=(0, 25),
            sticky="ew"
        )

    # ========================================================
    # CARDS INFORMATIVOS
    # ========================================================

    def card_info(self, titulo, texto, row):

        frame = ctk.CTkFrame(
            self.sidebar,
            corner_radius=15
        )

        frame.grid(
            row=row,
            column=0,
            padx=18,
            pady=7,
            sticky="ew"
        )

        ctk.CTkLabel(
            frame,
            text=titulo,
            font=ctk.CTkFont(size=15, weight="bold")
        ).pack(anchor="w", padx=15, pady=(10, 0))

        ctk.CTkLabel(
            frame,
            text=texto,
            wraplength=180,
            justify="left"
        ).pack(anchor="w", padx=15, pady=(2, 10))

    # ========================================================
    # CONTEÚDO PRINCIPAL
    # ========================================================

    def criar_conteudo(self):

        self.main = ctk.CTkFrame(
            self,
            fg_color="#111827"
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.main.grid_columnconfigure(0, weight=1)
        self.main.grid_rowconfigure(1, weight=1)

        # Título principal
        ctk.CTkLabel(
            self.main,
            text="Agente Gamer Responsável",
            font=ctk.CTkFont(size=30, weight="bold")
        ).grid(
            row=0,
            column=0,
            padx=25,
            pady=(25, 10),
            sticky="w"
        )

        # Caixa de conversa
        self.conversa = ctk.CTkTextbox(
            self.main,
            font=ctk.CTkFont(size=14),
            corner_radius=20
        )

        self.conversa.grid(
            row=1,
            column=0,
            padx=25,
            pady=10,
            sticky="nsew"
        )

        self.conversa.insert(
            "end",
            (
                "Agente: Olá gamer! 🎮\n"
                "Como posso ajudar você hoje?\n\n"
            )
        )

        # Área de entrada
        entrada_frame = ctk.CTkFrame(
            self.main,
            corner_radius=18
        )

        entrada_frame.grid(
            row=2,
            column=0,
            padx=25,
            pady=(0, 25),
            sticky="ew"
        )

        entrada_frame.grid_columnconfigure(0, weight=1)

        # Campo de pergunta
        self.entrada = ctk.CTkEntry(
            entrada_frame,
            placeholder_text="Digite sua pergunta...",
            height=45
        )

        self.entrada.grid(
            row=0,
            column=0,
            padx=(15, 10),
            pady=15,
            sticky="ew"
        )

        # Enter envia pergunta
        self.entrada.bind(
            "<Return>",
            lambda event: self.perguntar()
        )

        # Botão perguntar
        ctk.CTkButton(
            entrada_frame,
            text="Perguntar",
            width=140,
            height=45,
            command=self.perguntar
        ).grid(
            row=0,
            column=1,
            padx=(0, 15),
            pady=15
        )

    # ========================================================
    # ENVIO DE PERGUNTA
    # ========================================================

    def perguntar(self):

        pergunta = self.entrada.get().strip()

        # Verificação de campo vazio
        if not pergunta:

            messagebox.showwarning(
                "Atenção",
                "Digite uma pergunta antes de enviar."
            )

            return

        # Gera resposta
        resposta = gerar_resposta(pergunta)

        # Exibe conversa
        self.conversa.insert(
            "end",
            f"Usuário: {pergunta}\n"
        )

        self.conversa.insert(
            "end",
            f"Agente: {resposta}\n\n"
        )

        self.conversa.see("end")

        # Salva log
        self.registrar_log(pergunta, resposta)

        # Limpa entrada
        self.entrada.delete(0, "end")

    # ========================================================
    # REGISTRO DE LOG
    # ========================================================

    def registrar_log(self, pergunta, resposta):

        arquivo = APP_DIR / "log_gamer.txt"

        with arquivo.open("a", encoding="utf-8") as f:

            f.write(
                f"[{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}]\n"
            )

            f.write(f"Pergunta: {pergunta}\n")
            f.write(f"Resposta: {resposta}\n")

            f.write("-" * 50 + "\n")

    # ========================================================
    # LIMPAR CONVERSA
    # ========================================================

    def limpar_conversa(self):

        self.conversa.delete("1.0", "end")

        self.conversa.insert(
            "end",
            (
                "Agente: Conversa reiniciada.\n"
                "Como posso ajudar?\n\n"
            )
        )

    # ========================================================
    # POLÍTICA ÉTICA
    # ========================================================

    def mostrar_politica(self):

        texto = (

            "POLÍTICA ÉTICA DO AGENTE GAMER\n\n"

            "1. Não compartilhar senhas ou contas.\n"
            "2. Não incentivar hacks ou cheats.\n"
            "3. Respeitar outros jogadores.\n"
            "4. Não divulgar dados pessoais.\n"
            "5. Utilizar o agente apenas como apoio informativo."
        )

        messagebox.showinfo(
            "Política ética",
            texto
        )

# ============================================================
# INICIALIZAÇÃO DO APP
# ============================================================

if __name__ == "__main__":

    app = App()

    app.mainloop()