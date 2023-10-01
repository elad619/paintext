import difflib
import json
from typing import List, Iterable

from const.constants import MISSING_VALUE


class FoundWord:
    def __init__(self, original_word: str, found_word: str, ratio: float):
        self.ratio = ratio
        self.original_word = original_word
        self.found_word = found_word

    @property
    def is_null(self) -> bool:
        return self.ratio == 0

    @property
    def as_dict(self) -> dict:
        return {"ratio": self.ratio, "original_word": self.original_word, "found_word": self.found_word}


class FoundWords:
    def __init__(self, words: List[FoundWord]):
        self.words = words

    def get_max_word(self) -> FoundWord:
        return max(self.words, key=lambda x: x.ratio)

    @property
    def as_json(self) -> str:
        return json.dumps([word.as_dict for word in self.words])

    @property
    def without_null(self) -> "FoundWords":
        return FoundWords([word for word in self.words if not word.is_null])

    @property
    def original_values(self) -> List[str]:
        return [word.original_word for word in self.words]


class TextSearcher:

    def __init__(self, text: str):
        self.text = text

    def _get_found_words(self, word_to_search: str) -> FoundWords:
        words = [
            FoundWord(word_to_search, word, 1 if word == word_to_search else difflib.SequenceMatcher(a=word,
                                                                                                     b=word_to_search).ratio())
            for word in self.text.split()]
        return FoundWords(words=words)

    def is_word_in_documentation(self, word_to_search: str, threshold: float = 0.6) -> bool:
        return self._get_found_words(word_to_search).get_max_word().ratio > threshold

    def get_word_if_found(self, word_to_search: str, threshold: float = 0.6) -> FoundWord:
        closest_word = self._get_found_words(word_to_search).get_max_word()
        return closest_word if closest_word.ratio > threshold else FoundWord(MISSING_VALUE, MISSING_VALUE, 0)

    def get_words_if_found(self, words: List[str], threshold: float = 0.6) -> FoundWords:
        closest_words: List[FoundWord] = [self.get_word_if_found(word, threshold) for word in words]
        return FoundWords([word for word in closest_words if not word.is_null]).without_null

    def is_sentence_in_text(self, sentence: str, musts: Iterable[str] = (), threshold: float = 0.6) -> bool:
        for line in self.text.split('\n'):
            if difflib.SequenceMatcher(None, line, sentence).ratio() > threshold and all(
                    [must in line for must in musts]):
                return True
        return False
