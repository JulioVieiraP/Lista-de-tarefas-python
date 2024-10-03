import customtkinter as ctk


class InputFrame:
    def __init__(self, window, add_task_callback):
        self.frame = ctk.CTkFrame(window, fg_color="transparent")
        self.frame.pack(pady=10)

        # Campo de entrada
        self.input = ctk.CTkEntry(
            self.frame,
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
            self.frame,
            text="Adicionar Tarefa",
            fg_color="#4CAF50",
            text_color="#FFFFFF",
            corner_radius=0,
            width=115,
            font=("Roboto", 11),
            command=add_task_callback,
        )
        self.add_button.pack(side="left", padx=10)

    def get_task(self):
        return self.input.get()

    def clear_input(self):
        self.input.delete(0, "end")
