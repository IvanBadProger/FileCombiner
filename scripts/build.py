from PyInstaller.__main__ import run

run(
    [
        "src/main.py",
        "--onefile",
        "--windowed",
        "--icon=assets/icon.ico",
        "--name=FileCombiner",
        "--add-data=src/core;core",
        "--add-data=src/ui;ui",
    ]
)
