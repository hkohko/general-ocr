from pathlib import Path

from constants import IMAGES, OCR_RESULT


def check_folder(func):
    def wrapper(*args, **kwargs):
        check = True
        dirs = (IMAGES, OCR_RESULT)
        for folder in dirs:
            if not Path(folder).exists():
                check = False
                Path(folder).mkdir()
        if check:
            func(*args, **kwargs)
            return
        print("Image and OCR result folders not found. Creating dirs...")
        print(IMAGES)
        print(OCR_RESULT)
        print("\nRun the program again")
        return

    return wrapper
