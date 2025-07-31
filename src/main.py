from core.controller import FileCombinerController
from ui.tkinter_ui import FileCombinerView
from core.file_manager import FileManager

if __name__ == "__main__":
    model = FileManager()
    view = FileCombinerView()
    controller = FileCombinerController(view, model)
    view.run()
