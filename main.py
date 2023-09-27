import pandas as pd

from const.constants import PATH


def run_state_machine(document_content: str):
    return None


def save_file_to_db(parsed_document_results: str):
    pass


def main():
    df = pd.read_csv(PATH)

    for _, row in df.iterrows():
        document_content = row['Content']
        result = run_state_machine(document_content)
        save_file_to_db(result)


if __name__ == '__main__':
    main()
