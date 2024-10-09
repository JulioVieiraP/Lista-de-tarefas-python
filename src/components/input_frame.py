import customtkinter as ctk


class InputFrame(ctk.CTkFrame):
    def __init__(self, window, add_task_callback, **kwargs):
        super().__init__(window, fg_color="transparent", **kwargs)
        self.pack(pady=10)

        # Campo de entrada
        self.input = ctk.CTkEntry(
            self,
            font=("Garamond", 14),
            border_width=2,
            border_color="gray",
            corner_radius=0,
            fg_color="#F0F0F0",
            text_color="gray",
            width=300,
        )
        self.input.pack(side="left", padx=10)

        # Botão para adicionar tarefa
        self.add_button = ctk.CTkButton(
            self,
            text="Adicionar Tarefa",
            fg_color="#4CAF50",
            text_color="#FFFFFF",
            corner_radius=0,
            width=115,
            font=("Roboto", 11),
            command=self.add_task,
        )
        self.add_button.pack(side="left", padx=10)

        self.add_task_callback = add_task_callback

    def add_task(self):
        task_title = self.input.get()
        if len(task_title) >= 4:
            self.add_task_callback(task_title)
            self.input.delete(0, "end")
