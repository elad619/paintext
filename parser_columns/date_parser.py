from parser_columns.base_parser import BaseParser
from constants import DATE_STRING_FORMAT, MISSING_VALUE_STRING
import pandas as pd
import re

class DateParser(BaseParser):
    def __init__(self):
        self.date_string_format = DATE_STRING_FORMAT

    def parse_document(self, document_content: str) -> str:
        match = re.search(self.date_string_format, document_content)
        try:
            return match.group()
        except:
            print(f"No date in document! filling with {MISSING_VALUE_STRING}!")
            return MISSING_VALUE_STRING


if __name__ == "__main__":
    parser = DateParser()
    df = pd.read_csv('../pain_data.csv')
    df['date_of_operation'] = df['Content'].apply(parser.parse_document)
    print(df)