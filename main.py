from pathlib import Path
from multiprocessing import Pool

from const.constants import PATH
from utils.text_searcher import TextSearcher


def get_date_from_file(f):
    with open(f, "r") as file:
        file_content = file.read()
    searcher = TextSearcher(file_content)


def save_file_to_db(data):
    pass


def handle_file(f):
    data = get_date_from_file(f)
    save_file_to_db(data)


def main():
    files = Path(PATH).iterdir()
    with Pool(processes=10) as pool:
        pool.map(handle_file, files)


if __name__ == '__main__':
    main()
