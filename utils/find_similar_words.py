from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from typing import List

def find_similar_words(text: str, word: str) -> List[str]:
    words = text.split()
    n = len(words)
    similar_words = []

    for w in words:
        similarity = fuzz.ratio(w, word)
        if similarity >= (n - 1) / n * 100:
            similar_words.append(w)

    return similar_words
