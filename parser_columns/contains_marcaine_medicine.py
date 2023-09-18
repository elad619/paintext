from parser_columns.base_parser import BaseParser
from utils.find_similar_words import find_similar_words
from constants import POSITIVE_VALUE, NEGATIVE_VALUE, MISSING_VALUE

MARCAINE = "מרקאין"

class DoesContainMarcaineMedicineParser(BaseParser):
    def __init__(self) -> None:
        super().__init__()

    def parse_document(self, document_content: str) -> str:
        try:
            similar_words_in_text = find_similar_words(document_content, MARCAINE)
            if len(similar_words_in_text) > 0:
                return POSITIVE_VALUE
            else:
                return NEGATIVE_VALUE
        except:
            return MISSING_VALUE