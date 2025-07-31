from PyInstaller.__main__ import run

run(
    [
        "main.py",
        "--onefile",
        "--windowed",
        "--icon=assets/icon.ico",
        "--name=FileCombiner",
        "--add-data=core;core",
        "--add-data=ui;ui",
    ]
)
