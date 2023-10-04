import json
from typing import List

from utils.found_word import FoundWord


class FoundWords:
    """
    A class that represents a list of FoundWord objects.

    :param words: A list of FoundWord objects.
    """

    def __init__(self, words: List[FoundWord]):
        self.words = words

    def get_max_word(self) -> FoundWord:
        """
        Returns the FoundWord object with the highest ratio.

        :return: The FoundWord object with the highest ratio.
        """
        return max(self.words, key=lambda x: x.ratio)

    @property
    def as_json(self) -> str:
        """
        Returns a JSON string representation of the list of FoundWord objects.

        :return: A JSON string representation of the list of FoundWord objects.
        """
        return json.dumps([word.as_dict for word in self.words])

    @property
    def without_null(self) -> "FoundWords":
        """
        Returns a new instance of FoundWords with all null values removed.

        :return: A new instance of FoundWords with all null values removed.
        """
        return FoundWords([word for word in self.words if word])

    @property
    def original_values(self) -> List[str]:
        """
        Returns a list of original words from the list of FoundWord objects.

        :return: A list of original words from the list of FoundWord objects.
        """
        return [word.original_word for word in self.words]
