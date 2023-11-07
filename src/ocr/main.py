from collections.abc import Iterator
from pathlib import Path
from time import sleep

import pytesseract
from constants import IMAGES, OCR_RESULT, SAVE_FILE_PREFIX, tesseract_cmd
from decor import check_folder
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = tesseract_cmd


def find_file(filename: str, show: bool = False) -> Iterator[Path]:
    for img_path in Path(IMAGES).iterdir():
        if not show:
            if filename in Path(img_path).stem:
                yield img_path
        if show:
            yield img_path


def ocr_image(img_path: Path) -> str:
    return pytesseract.image_to_string(Image.open(img_path))


@check_folder
def main(filename: str, ext: str = ".md"):
    path = next(find_file(filename))
    if path is None:
        print(f"image {filename} is not found.")
    ocr_result = ocr_image(path)
    save_file_name = SAVE_FILE_PREFIX + path.stem + ext
    with open(OCR_RESULT.joinpath(save_file_name), "w") as file:
        file.write(ocr_result)
    print(f"New file: {save_file_name}")


def run_program():
    while True:
        try:
            file_list = "\n".join([str(path) for path in find_file("", show=True)])
            print(file_list)
            file_name = input("Type filename: ")
            main(file_name)
        except KeyboardInterrupt:
            print("Exiting...")
            sleep(0.5)
            exit(0)


if __name__ == "__main__":
    run_program()
