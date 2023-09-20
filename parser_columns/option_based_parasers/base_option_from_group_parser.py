from base_parser import BaseParser
from utils.word_searcher import WordSearcher
from typing import List

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

