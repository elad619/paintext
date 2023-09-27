import difflib
import re
from typing import List


class TextSearcher:

    def __init__(self, text: str):
        self.text = text

    def is_subtext_in_documentation(self, threshold: int, word_to_search: str) -> bool:
        return max(
            [difflib.SequenceMatcher(a=word, b=word_to_search).ratio() for word in self.text.split()]) < threshold

    def get_word_if_found(self, sub_text: str, threshold: float = 0.7) -> str:
        closest_words = [[word] if word in self.text else difflib.get_close_matches(word, [sub_text], cutoff=threshold)
                         for word in self.text.split()]
        closest_words = [word[0] for word in closest_words if word]
        return closest_words[0] if closest_words else ""

    def get_words_if_found(self, words: List[str], threshold: float = 0.7) -> list[str]:
        closest_words: List[List[str]] = [
            [word] if word in self.text else difflib.get_close_matches(word, words, cutoff=threshold) for word in
            self.text.split()]
        none_less_words = [word[0] for word in closest_words if word]
        return none_less_words if none_less_words else [""]
