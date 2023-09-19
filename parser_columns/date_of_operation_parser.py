from parser_columns.base_parser import BaseParser
from constants import MISSING_VALUE
import pandas as pd
from datetime import datetime
import re

DATE_STRING_REGEX_FORMAT = r'\d+[\./]\d+[\./]\d+'
DATE_FORMATS = ["%d/%m/%y", "%d.%m.%y"]


class OperationDateParser(BaseParser):
    def __init__(self):
        self.date_string_format = DATE_STRING_REGEX_FORMAT
        self.possible_date_formats = DATE_FORMATS

    def _convert_string_to_date(self, date_as_string: str) -> datetime:
        for date_format in self.possible_date_formats:
            try:
                date_obj = datetime.strptime(date_as_string, date_format)
                return date_obj
            except ValueError:
                continue
        raise ValueError(f"Cannot convert {date_as_string} to date!")

    def parse_document(self, document_content: str) -> str:
        all_dates_in_documents = re.findall(self.date_string_format, document_content)
        if len(all_dates_in_documents) != 0:
            try:
                all_dates_in_documents_as_datetime = [self._convert_string_to_date(date_in_document) for
                                                      date_in_document in
                                                      all_dates_in_documents]
                most_recent_date_in_document = max(all_dates_in_documents_as_datetime).date()
                return str(most_recent_date_in_document)
            except:
                return MISSING_VALUE

        return MISSING_VALUE
