import difflib
from typing import List, Iterable

from const.constants import MISSING_VALUE
from utils.found_word import FoundWord
from utils.found_words import FoundWords


class TextSearcher:
    """
    A class that searches for words and sentences in a given text.
    """

    def __init__(self, text: str):
        """
        Initializes a new instance of the TextSearcher class.

        Args:
            text (str): The text to search.
        """
        self._text = text

    def _get_found_words(self, word_to_search: str) -> FoundWords:
        """
        Gets a list of words that match the specified word.

        Args:
            word_to_search (str): The word to search for.

        Returns:
            FoundWords: A list of words that match the specified word.
        """
        words = [
            FoundWord(word_to_search, word, 1 if word == word_to_search else difflib.SequenceMatcher(a=word,
                                                                                                     b=word_to_search).ratio())
            for word in self._text.split()]
        return FoundWords(words=words)

    def get_word_if_found(self, word_to_search: str, threshold: float = 0.6) -> FoundWord:
        """
        Gets the closest matching word if found; otherwise, returns a null value.

        Args:
            word_to_search (str): The word to search for.
            threshold (float): The minimum similarity ratio required to consider a match. Defaults to 0.6.

        Returns:
            FoundWord: The closest matching word if found; otherwise, a null value.
        """
        closest_word = self._get_found_words(word_to_search).get_max_word()
        return closest_word if closest_word.ratio > threshold else FoundWord(word_to_search, MISSING_VALUE, 0)

    def get_words_if_found(self, words: List[str], threshold: float = 0.6) -> FoundWords:
        """
        Gets a list of words that match any of the specified words.

        Args:
            words (List[str]): The words to search for.
            threshold (float): The minimum similarity ratio required to consider a match. Defaults to 0.6.

        Returns:
            FoundWords: A list of words that match any of the specified words.
        """
        closest_words = [self.get_word_if_found(word, threshold) for word in words]
        return FoundWords([word for word in closest_words if word]).without_null

    def is_sentence_in_text(self, sentence: str, musts: Iterable[str] = (), threshold: float = 0.6) -> bool:
        """
        Determines whether the specified sentence is present in the text.

        Args:
            sentence (str): The sentence to search for.
            musts (Iterable[str]): A collection of strings that must be present in the same line as the sentence. Defaults to an empty collection.
            threshold (float): The minimum similarity ratio required to consider a match. Defaults to 0.6.

        Returns:
            bool: True if the specified sentence is present in the text; otherwise, False.
        """
        return any(difflib.SequenceMatcher(None, line.strip(), sentence.strip()).ratio() > threshold and all(
            must in line for must in musts) for line in self._text.split('\n'))
