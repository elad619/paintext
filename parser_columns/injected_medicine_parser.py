from base_parser import BaseParser
from constants import MISSING_VALUE
from utils.word_searcher import WordSearcher

MEDICINE_TYPES = ["דפומדרול", "צלסטון", "דיפרוספן", "דקסמטזון", "דקסאקורט"]


class InjectedMedicineParser(BaseParser):
    def __init__(self):
        self.word_searchers_list = [WordSearcher(word=medicine_type) for medicine_type in MEDICINE_TYPES]

    def parse_document(self, document_content: str) -> str:
        medicines_found_in_text = []
        for word_searcher in self.word_searchers_list:
            if (word_searcher.word in document_content) or (
                    len(word_searcher.find_similar_words(document_content)) > 0):
                medicines_found_in_text.append(word_searcher.word)
        if len(medicines_found_in_text) == 0:
            medicines_found_in_text.append(MISSING_VALUE)

        sorted_medicines_found_in_text = sorted(medicines_found_in_text)
        return ",".join(sorted_medicines_found_in_text)