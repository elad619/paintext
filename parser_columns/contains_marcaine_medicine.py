from parser_columns.base_parser import BaseParser
from utils.find_similar_words import find_similar_words
from constants import POSITIVE_VALUE_STRING, NEGATIVE_VALUE_STRING, MISSING_VALUE_STRING

MARCAINE_STRING = "מרקאין"

class DoesContainMarcaineMedicineParser(BaseParser):
    def __init__(self) -> None:
        super().__init__()
        self.marcaine_string = MARCAINE_STRING

    def parse_document(self, document_content: str) -> str:
        try:
            similar_words_in_text = find_similar_words(document_content, self.marcaine_string)
            if len(similar_words_in_text) > 0:
                return POSITIVE_VALUE_STRING
            else:
                return NEGATIVE_VALUE_STRING
        except:
            return MISSING_VALUE_STRING