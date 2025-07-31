import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from typing import Callable, List
import platform


class FileCombinerView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Combiner")
        self.setup_ui()

    def setup_ui(self):
        # Список файлов
        self.listbox = tk.Listbox(self.root, width=60, height=15)
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Scrollbar
        scrollbar = ttk.Scrollbar(
            self.root, orient="vertical", command=self.listbox.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Кнопки
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)

        self.btn_add = ttk.Button(button_frame, text="Добавить файлы")
        self.btn_add.pack(side=tk.LEFT, padx=5)

        self.btn_remove = ttk.Button(button_frame, text="Удалить выбранное")
        self.btn_remove.pack(side=tk.LEFT, padx=5)

        self.btn_combine = ttk.Button(button_frame, text="Объединить")
        self.btn_combine.pack(side=tk.LEFT, padx=5)

    def bind_buttons(
        self, add_handler: Callable, remove_handler: Callable, combine_handler: Callable
    ):
        """Привязка обработчиков к кнопкам."""
        self.btn_add.config(command=add_handler)
        self.btn_remove.config(command=remove_handler)
        self.btn_combine.config(command=combine_handler)

    def get_selected_files(self) -> List[str]:
        """Возвращает список выбранных файлов."""
        return list(self.listbox.get(0, tk.END))

    def add_files_to_list(self, file_paths: List[str]):
        """Добавляет файлы в ListBox."""
        for path in file_paths:
            if path not in self.listbox.get(0, tk.END):
                self.listbox.insert(tk.END, path)

    def remove_selected(self):
        """Удаляет выбранный файл из ListBox."""
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)

    def show_error(self, message: str):
        messagebox.showerror("Ошибка", message)

    def show_info(self, message: str):
        messagebox.showinfo("Готово", message)

    def ask_save_path(self) -> str:
        return filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Текстовые файлы", "*.txt"), ("Все файлы", "*.*")],
        )

    def ask_open_files(self) -> List[str]:
        return filedialog.askopenfilenames()

    def run(self):
        self.root.mainloop()
