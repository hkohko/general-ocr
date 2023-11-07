from subprocess import run
from sys import platform

from src.ocr.constants import PROJ_DIR, SRC

python = PROJ_DIR.joinpath(".venv", "bin", "python")
if platform == "win32":
    python = PROJ_DIR.joinpath(".venv", "Scripts", "python.exe")
main = SRC.joinpath("ocr", "main.py")
run([python, main])
