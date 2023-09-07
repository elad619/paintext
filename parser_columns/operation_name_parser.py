from parser_columns.base_parser import BaseParser
from constants import MISSING_VALUE_STRING
import pandas as pd
import re

class OperationNameParser(BaseParser):
    def __init__(self):
        self.title_regex = r'[A-Z][A-Z -/&0-9 ּa-z\.]+[A-Za-z]'

    def parse_document(self, document_content: str) -> str:
        extracted_titles = re.findall(self.title_regex, document_content)
        if len(extracted_titles) == 0:
            print(f"No title in document! filling with {MISSING_VALUE_STRING}!")
            return MISSING_VALUE_STRING
        main_title = extracted_titles[0]
        if self.validate_title(document_content, main_title):
            operation_name = self.extract_procedure_from_title(main_title)
            return operation_name
        print(f"No title in document! filling with {MISSING_VALUE_STRING}!")
        return MISSING_VALUE_STRING
    
    def validate_title(self, document_content: str, extracted_title: str) -> bool:
        # todo: Add logic to validate that the extracted text is the title
        return True
    
    def extract_opeation_name_from_title(self, title: str) -> str:
        # todo: Check logic to extract operation name from title
        return title
