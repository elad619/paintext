from constants import POSITIVE_VALUE, NEGATIVE_VALUE, MISSING_VALUE
from parser_columns.base_parser import BaseParser
from utils.word_searcher import WordSearcher

NO_CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS = ["אין רגישות לחומרי הרדמה", "אין רגישות לחומר ניגוד וחומרי הרדמה", "אין רגישות לחומר ניגוד או לחומרי הרדמה", "לא רגישה ליוד או חמרי הרדמה", "אין רגישות לחומר ניגוד או לחומרי הרדמה", "אין רגישות לחומר ניגוד ואין רגישות חומרי הרדמה", "אין רגישות לחמר ניגוד וחומרי הרדמה", "ואין רגישות חומרי הרדמה", "אין רגישות ליוד ולחומרי הרדמה"]
CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS = ["וכי יש רגישות לחומר ניגוד וחומרי הרדמה"]


class ContrastMaterialsSensitivity(BaseParser):
    def __init__(self) -> None:
        super().__init__()

    def parse_document(self, document_content: str) -> str:
        try:
            for no_implying_sentence in NO_CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS:
                if no_implying_sentence in document_content:
                    return NEGATIVE_VALUE  # meaning there is no contrast materials sensitivity
            for implying_sentence in CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS:
                if implying_sentence in document_content:
                    return POSITIVE_VALUE
            return MISSING_VALUE
        except:
            return MISSING_VALUE
