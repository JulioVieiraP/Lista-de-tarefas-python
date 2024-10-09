import customtkinter as ctk


class Header(ctk.CTkLabel):
    def __init__(self, window, **kwargs):
        super().__init__(
            window, text="Meu App de Tarefas", font=("Garamond", 24, "bold"), **kwargs
        )
        self.pack(pady=20)
