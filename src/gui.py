import customtkinter as ctk
from src.tasks import TaskManager
from tkinter import PhotoImage


class TaskManagerApp:
    def __init__(self):
        # Inicializando a janela principal
        self.root = ctk.CTk()
        self.root.title("Meu app de Tarefas")
        self.root.geometry("500x600")

        ctk.set_appearance_mode("Dark")

        # Inicializando o gerenciador de tarefas
        self.task_manager = TaskManager()

        # Componentes da interface
        self.create_widgets()

        self.frame_em_edição = None

    def create_widgets(self):
        # Cabeçalho
        self.fonte_cabecalho = ("Garamond", 24, "bold")
        self.cabecalho = ctk.CTkLabel(
            self.root,
            font=self.fonte_cabecalho,
            text="Meu App de Tarefas",
        )
        self.cabecalho.pack(pady=20)

        # Frame para segurar os inputs
        self.frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.frame.pack(fill="x", expand=True, pady=10)

        # Campo de entrada
        self.input = ctk.CTkEntry(
            self.frame,
            font=("Garamond", 14),
            border_width=2,
            border_color="gray",
            fg_color="#F0F0F0",
            text_color="gray",
            width=300,
        )
        self.input.pack(side="left", padx=10)

        # botao para adicionar tarefa
        self.add_button = ctk.CTkButton(
            self.frame,
            text="Adicionar Tarefa",
            fg_color="#4CAF50",
            text_color="#FFFFFF",
            corner_radius=0,
            width=115,
            font=("Roboto", 11),
            command=self.add_task,
        )
        self.add_button.pack(side="left", padx=10)

        # Frame para a lista de tarefas
        self.task_frame = ctk.CTkFrame(self.root, fg_color="transparent")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_manager.add_task(task)
            self.update_task_listbox()
            self.task_entry.delete(0, "end")

    def remove_task(self):
        # Remover a última tarefa da lista
        self.task_manager.remove_last_task()
        self.update_task_listbox()

    def update_task_listbox(self):
        # Atualiza o conteúdo do CTkTextbox com a lista de tarefas
        self.task_textbox.configure(state="normal")
        self.task_textbox.delete("1.0", "end")  # Limpa o conteúdo anterior
        for task in self.task_manager.get_tasks():
            self.task_textbox.insert("end", f"- {task}\n")
        self.task_textbox.configure(state="disabled")

    def run(self):
        self.root.mainloop()
