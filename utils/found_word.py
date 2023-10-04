class FoundWord:
    """
    A class that represents a found word and its similarity ratio to the original word.
    """

    def __init__(self, original_word: str, found_word: str, ratio: float):
        """
        Initializes a new instance of the FoundWord class.

        Args:
            original_word (str): The original word to compare against.
            found_word (str): The word that was found.
            ratio (float): The similarity ratio between the two words.
        """
        self.ratio = ratio
        self.original_word = original_word
        self.found_word = found_word

    def __bool__(self) -> bool:
        """
        Gets a value indicating whether this instance represents a null value.

        Returns:
            bool: True if this instance represents a null value; otherwise, False.
        """
        return bool(self.ratio)

    @property
    def as_dict(self) -> dict:
        """
        Gets a dictionary representation of this instance.

        Returns:
            dict: A dictionary representation of this instance.
        """
        return dict(ratio=self.ratio, original_word=self.original_word, found_word=self.found_word)
