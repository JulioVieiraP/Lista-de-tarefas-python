import customtkinter as ctk


class Header:
    def __init__(self, window):
        self.fonte_cabecalho = ctk.CTkFont("Garamond", 24, "bold")
        self.cabecalho = ctk.CTkLabel(
            window,
            font=self.fonte_cabecalho,
            text="Meu App de Tarefas",
        )
        self.cabecalho.pack(pady=20)
