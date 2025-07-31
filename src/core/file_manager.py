import os
import json
from datetime import datetime
from typing import List, Dict


class FileManager:
    def combine_files(self, file_paths: List[str], output_file: str) -> Dict[str, int]:
        """Объединяет файлы и возвращает статистику."""
        total_lines = 0
        total_chars = 0

        try:
            with open(output_file, "w", encoding="utf-8") as outfile:
                for file_path in file_paths:
                    if os.path.isfile(file_path):
                        with open(file_path, "r", encoding="utf-8") as infile:
                            content = infile.read()
                            total_lines += content.count("\n") + 1
                            total_chars += len(content)
                            outfile.write(f"=== {os.path.basename(file_path)} ===\n")
                            outfile.write(content + "\n\n")

            return {"lines": total_lines, "chars": total_chars}
        except Exception as e:
            raise RuntimeError(f"Ошибка объединения: {e}")

    def save_history(self, file_paths: List[str], output_file: str) -> None:
        """Сохраняет историю операций в JSON."""
        history = {
            "files": file_paths,
            "output": output_file,
            "timestamp": datetime.now().isoformat(),
        }
        with open("history.json", "a", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False)
            f.write("\n")
