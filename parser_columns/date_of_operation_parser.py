from typing import List
import datetime as dt
from parser_columns.base_parser import BaseParser
from constants import MISSING_VALUE
import re
from dateutil.parser import parse as date_parser, ParserError

DATE_STRING_REGEX_FORMAT = r'\d+[\./]\d+[\./]\d+'


class OperationDateParser(BaseParser):
    def __init__(self):
        self.date_string_format = DATE_STRING_REGEX_FORMAT
        self.dates: List[dt.date] = []

    def parse_document(self, document_content: str) -> str:
        dates_in_documents: List[str] = re.findall(self.date_string_format, document_content)
        for date in dates_in_documents:
            try:
                self.dates.append(date_parser(date.replace(".", "/")).date())
            except ParserError as e:
                print(e)
        return str(max(dates_in_documents)) if dates_in_documents else MISSING_VALUE
