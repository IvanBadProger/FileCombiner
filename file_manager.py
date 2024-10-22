import os
from tkinter import messagebox
import json


class FileManager:
    def __init__(self):
        """Инициализирует объект FileManager."""
        pass


    def combine_files(self, file_paths, output_file):
        """Объединяет содержимое нескольких файлов и сохраняет в один файл."""
        total_lines = 0
        total_characters = 0
        try:
            with open(output_file, 'w', encoding='utf-8') as outfile:
                for file_path in file_paths:
                    if os.path.isfile(file_path):
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            total_lines += content.count('\n')
                            total_characters += len(content)
                            outfile.write(f"{os.path.basename(file_path)}\n")
                            outfile.write(content)
                            outfile.write("\n\n")
                messagebox.showinfo("Статистика", f"Всего строк: {total_lines}\nВсего символов: {total_characters}")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл не найден.")
        except IOError as e:
            messagebox.showerror("Ошибка", f"Ошибка ввода-вывода: {e}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")


    def save_operation_history(self, file_paths, output_file):
        """Сохраняет историю операции объединения файлов."""
        history = {
            "files_combined": list(file_paths),
            "output_file": output_file
        }
        try:
            with open('history.json', 'a', encoding='utf-8') as history_file:
                history_file.write(json.dumps(history) + "\n")
            messagebox.showinfo("История", "Операция объединения сохранена в историю.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить историю: {e}")
