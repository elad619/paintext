from constants import POSITIVE_VALUE, NEGATIVE_VALUE, MISSING_VALUE
from parser_columns.base_parser import BaseParser
from utils.word_searcher import WordSearcher

from constants import MISSING_VALUE

class AnestheticsSensitivity(BaseParser):
    def __init__(self) -> None:
        super().__init__()
        self.word_searcher = WordSearcher()

    def parse_document(self, document_content: str) -> str:
        try:
            similar_words_in_text = self.word_searcher.find_similar_words(document_content)
            if len(similar_words_in_text) > 0:
                return POSITIVE_VALUE
            else:
                return NEGATIVE_VALUE
        except:
            return MISSING_VALUE
