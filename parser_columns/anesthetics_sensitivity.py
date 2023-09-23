from constants import POSITIVE_VALUE, NEGATIVE_VALUE, MISSING_VALUE
from parser_columns.base_parser import BaseParser

NO_ANESTHETICS_SENSITIVITY_IMPLIERS = ["אין רגישות לחומר ניגוד", "אין רגישות לחומרי הרדמה מקומית או לחומר ניגוד", "וכי אין רגישות לחומרי הרדמה מקומית ולחמר ניגוד", "אין רגישות לחמר ניגוד", "אין רגישות לאנטיביוטיקה או לחומר ניגוד"]
ANESTHETICS_SENSITIVITY_IMPLIERS = ["יש רגישות לחומר ניגוד"]


# TODO - consider a list of NO_ANESTHETICS_SENSITIVITY and insead of initiating WordSearcher at init method,
#   create a new one at each item in the list or modify word_searcher to receive multiple words

class AnestheticsSensitivity(BaseParser):
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
                    print(document_content)
                    print('___________________________________________________________________________')
                    return MISSING_VALUE
        except:
            return MISSING_VALUE
