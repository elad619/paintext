from const.constants import POSITIVE_VALUE, NEGATIVE_VALUE, MISSING_VALUE
from parser_columns.base_parser import BaseParser
from utils.text_searcher import TextSearcher

NO_ANESTHETICS_SENSITIVITY_IMPLIERS = ["אין רגישות לחומר ניגוד", "אין רגישות לחומרי הרדמה מקומית או לחומר ניגוד",
                                       "אין רגישות לחומרי הרדמה מקומית ולחמר ניגוד", "אין רגישות לחמר ניגוד",
                                       "אין רגישות לאנטיביוטיקה או לחומר ניגוד"]
ANESTHETICS_SENSITIVITY_IMPLIERS = ["יש רגישות לחומר ניגוד"]
# ^ is this correct? won't it conflict with the contrast_materials_sensitivity CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS?


class AnestheticsSensitivity(BaseParser):
    """
        to change after searching sentences will be added to text_searcher
    """
    def __init__(self) -> None:
        super().__init__()

    def parse_document(self, document_content: str) -> str:
        try:
            for no_anesthetics_implying_sentence in NO_ANESTHETICS_SENSITIVITY_IMPLIERS:
                if no_anesthetics_implying_sentence in document_content:
                    return NEGATIVE_VALUE  # meaning there is no anesthetics materials sensitivity
            for anesthetics_implying_sentence in ANESTHETICS_SENSITIVITY_IMPLIERS:
                if anesthetics_implying_sentence in document_content:
                    return POSITIVE_VALUE
                else:
                    return MISSING_VALUE
        except:
            return MISSING_VALUE


def does_have_materials_sensitivity(text_searcher: TextSearcher):
    if any([text_searcher.is_sentence_in_text(sentence, ["אין"]) for sentence in
            NO_ANESTHETICS_SENSITIVITY_IMPLIERS]):
        return False
    if any([text_searcher.is_sentence_in_text(sentence, ["יש"]) for sentence in
            ANESTHETICS_SENSITIVITY_IMPLIERS]):
        return True
    return MISSING_VALUE
