from typing import List

from utils.word_searcher import WordSearcher

from base_parser import BaseParser
from constants import MISSING_VALUE_STRING


class OptionBasedParser(BaseParser):
    def __init__(self, options: List[str] = None):
        self.word_searchers_list = [WordSearcher(word=option) for option in options]

    def _get_matches_for_all_options(self, document_content: str) -> List[str]:
        options_found_in_text = []
        for word_searcher in self.word_searchers_list:
            if (word_searcher.word in document_content) or (
                    len(word_searcher.find_similar_words(document_content)) > 0):
                options_found_in_text.append(word_searcher.word)
        return sorted(options_found_in_text)


BLOOD_THINNERS_KEYWORD_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס',
                                'קומדין', 'קלקסל']
BLOOD_THINNERS_KEYWORD = 'מדללי דם'
DOESNT_TAKE_BLOOD_THINNERS_MESSAGE = 'ללא'


class BloodThinners(OptionBasedParser):
    def __init__(self):
        super().__init__(options=BLOOD_THINNERS_KEYWORD_TYPES)

    def parse_document(self, document_content: str) -> str:
        options_found_in_document = self._get_matches_for_all_options(document_content)
        if len(options_found_in_document) == 0:
            options_found_in_document.append(MISSING_VALUE_STRING)
        sorted_options_found_in_document = sorted(options_found_in_document)
        return ",".join(sorted_options_found_in_document)
