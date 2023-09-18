from typing import List

from fuzzywuzzy import fuzz


def find_similar_words(text: str, word: str) -> List[str]:
    words_in_text = text.split()
    length_of_word = len(word)
    similar_words = []
    minimum_similarity_ratio_threshold = (length_of_word - 1) / length_of_word * 100
    for w in words_in_text:
        if _compute_similarity_ratio_and_compare_to_threshold(minimum_similarity_ratio_threshold, w, word):
            similar_words.append(w)

    return similar_words


def _compute_similarity_ratio_and_compare_to_threshold(threshold: float, s1: str, s2: str) -> bool:
    similarity_ratio_of_strings = fuzz.ratio(s1, s2)
    return similarity_ratio_of_strings >= threshold
