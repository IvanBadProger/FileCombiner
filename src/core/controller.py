from typing import List
from core.file_manager import FileManager
from ui.tkinter_ui import FileCombinerView


class FileCombinerController:
    def __init__(self, view: FileCombinerView, model: FileManager):
        self.view = view
        self.model = model
        self._bind_events()

    def _bind_events(self):
        """Привязка стандартных обработчиков событий."""
        self.view.bind_buttons(
            add_handler=self.on_add_files,
            remove_handler=self.on_remove_files,
            combine_handler=self.on_combine_files,
        )

    def on_add_files(self):
        """Обработчик добавления файлов через диалог."""
        file_paths = self.view.ask_open_files()
        if file_paths:
            self.view.add_files_to_list(file_paths)

    def on_remove_files(self):
        """Обработчик удаления выбранных файлов."""
        self.view.remove_selected()

    def on_combine_files(self):
        """Обработчик объединения файлов."""
        file_paths = self.view.get_selected_files()
        if not file_paths:
            self.view.show_error("Нет файлов для объединения!")
            return

        output_file = self.view.ask_save_path()
        if not output_file:
            return

        try:
            stats = self.model.combine_files(file_paths, output_file)
            self.model.save_history(file_paths, output_file)
            self.view.show_info(
                f"Файлы объединены!\n"
                f"Строк: {stats['lines']}\n"
                f"Символов: {stats['chars']}"
            )
        except Exception as e:
            self.view.show_error(str(e))
