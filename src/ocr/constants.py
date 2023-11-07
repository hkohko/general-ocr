from pathlib import Path

PROJ_DIR = Path(__file__).parents[2]
SRC = PROJ_DIR.joinpath("src")
ROOT = Path.home().parents[1]
BIN = ROOT.joinpath("usr", "bin")
IMAGES = PROJ_DIR.joinpath("images")
OCR_RESULT = PROJ_DIR.joinpath("ocr_result")

tesseract_cmd = BIN.joinpath("tesseract")
SAVE_FILE_PREFIX = "OCR_"
