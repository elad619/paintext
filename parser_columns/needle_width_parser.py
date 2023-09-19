from parser_columns.base_parser import BaseParser
from constants import NEEDLE_WIDTH_SYMBOL, NEEDLE_WIDTH_OPTIONS, MISSING_VALUE_STRING
import pandas as pd
import re

class NeedleWidthParser(BaseParser):
    def __init__(self):
        one_of_possible_lengths_regex = self._create_possible_length_regex()
        self.needle_width_regex_with_G_before_number = rf'{NEEDLE_WIDTH_SYMBOL}.*{one_of_possible_lengths_regex}'
        self.needle_width_regex_with_G_after_nunber = rf'{one_of_possible_lengths_regex}.*{NEEDLE_WIDTH_SYMBOL}'

    def _create_possible_length_regex(self):
        one_of_possible_lengths_regex = "|".join(NEEDLE_WIDTH_OPTIONS)
        one_of_possible_lengths_regex_with_brackets = rf"({one_of_possible_lengths_regex})"
        return one_of_possible_lengths_regex_with_brackets

    def parse_document(self, document_content: str) -> str:
        match_with_G_before_number = re.search(self.needle_width_regex_with_G_before_number, document_content)
        match_with_G_after_number = re.search(self.needle_width_regex_with_G_after_nunber, document_content)
        if match_with_G_before_number:
            match_group: str = match_with_G_before_number.group()
            match_without_spaces = match_group.replace(" ", "")
            needle_width = match_without_spaces[0] + match_without_spaces[-2:]
            return needle_width

        elif match_with_G_after_number:
            match_group: str = match_with_G_after_number.group()
            match_without_spaces = match_group.replace(" ", "")
            needle_width = match_without_spaces[-1] + match_without_spaces[:-1]
            return needle_width
        else:
            print(f"No needle width in document! filling with {MISSING_VALUE_STRING}!")
            return MISSING_VALUE_STRING
