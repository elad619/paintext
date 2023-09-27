from const.constants import MISSING_VALUE

from utils.text_searcher import TextSearcher

NEEDLE_TYPES = ["Spinal", "Tuohy", "SMK", "RFK", "US"]


def parse_document(text_searcher: TextSearcher) -> str:
    found_needle_types = sorted(text_searcher.get_words_if_found(NEEDLE_TYPES))
    return ",".join(found_needle_types) if found_needle_types else MISSING_VALUE
