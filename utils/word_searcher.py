from typing import List

from fuzzywuzzy import fuzz


class WordSearcher:
    def __init__(self, word: str):
        self.word = word

    def find_similar_words(self, text: str) -> List[str]:
        words_in_text = text.split()
        length_of_word = len(self.word)
        similar_words = []
        minimum_similarity_ratio_threshold = (length_of_word - 1) / length_of_word * 100
        for w in words_in_text:
            if self._compute_similarity_ratio_and_compare_to_threshold(minimum_similarity_ratio_threshold, w,
                                                                       self.word):
                similar_words.append(w)

        return similar_words

    @staticmethod
    def _compute_similarity_ratio_and_compare_to_threshold(threshold: float, s1: str, s2: str) -> bool:
        similarity_ratio_of_strings = fuzz.ratio(s1, s2)
        return similarity_ratio_of_strings >= threshold
