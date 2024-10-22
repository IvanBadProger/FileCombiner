import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from file_manager import FileManager


class FileCombinerApp:
    def __init__(self, root):
        """Инициализирует интерфейс приложения."""
        self.root = root
        self.file_manager = FileManager()
        self.create_gui()


    def add_files(self):
        """Добавляет выбранные файлы в список."""
        file_paths = filedialog.askopenfilenames(
            title="Выберите файлы",
            filetypes=(("Все файлы", "*.*"),)
        )
        existing_files = self.file_listbox.get(0, tk.END)
        for file_path in file_paths:
            if file_path not in existing_files:
                self.file_listbox.insert(tk.END, file_path)
            else:
                messagebox.showinfo("Информация", f"Файл {os.path.basename(file_path)} уже добавлен.")


    def remove_selected_file(self):
        """Удаляет выбранный файл из списка."""
        selected_index = self.file_listbox.curselection()
        if selected_index:
            self.file_listbox.delete(selected_index)


    def clear_files(self):
        """Очищает список файлов."""
        self.file_listbox.delete(0, tk.END)


    def save_combined_file(self):
        """Сохраняет объединённые файлы в один."""
        file_paths = self.file_listbox.get(0, tk.END)
        if file_paths:
            output_file = filedialog.asksaveasfilename(
                title="Сохранить объединенный файл как",
                defaultextension=".txt",
                filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
            )
            if output_file:
                self.file_manager.combine_files(file_paths, output_file)
                self.file_manager.save_operation_history(file_paths, output_file)
        else:
            messagebox.showwarning("Предупреждение", "Пожалуйста, добавьте файлы для объединения.")


    def create_gui(self):
        """Создаёт графический интерфейс пользователя."""
        self.root.title("Объединение файлов")


        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


        self.file_listbox = tk.Listbox(main_frame, width=50, height=10, selectmode=tk.SINGLE)
        self.file_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5, padx=5)


        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.file_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.file_listbox.config(yscrollcommand=scrollbar.set)


        button_frame = ttk.Frame(main_frame, padding="5")
        button_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E))


        add_button = ttk.Button(button_frame, text="Добавить файлы", command=self.add_files)
        add_button.grid(row=0, column=0, padx=5, pady=5)


        remove_button = ttk.Button(button_frame, text="Удалить выбранный файл", command=self.remove_selected_file)
        remove_button.grid(row=0, column=1, padx=5, pady=5)


        clear_button = ttk.Button(button_frame, text="Очистить список", command=self.clear_files)
        clear_button.grid(row=0, column=2, padx=5, pady=5)


        save_button = ttk.Button(button_frame, text="Сохранить объединенный файл", command=self.save_combined_file)
        save_button.grid(row=0, column=3, padx=5, pady=5)


        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(0, weight=1)
        self.root.geometry("800x400")
