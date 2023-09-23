from constants import POSITIVE_VALUE, NEGATIVE_VALUE, MISSING_VALUE
from parser_columns.base_parser import BaseParser
from utils.word_searcher import WordSearcher

NO_CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS = ["אין רגישות לחומרי הרדמה"]


# TODO - consider a list of NO_CONTRAST_MATERIALS_SENSITIVITY and insead of initiating WordSearcher at init method,
#   create a new one at each item in the list or modify word_searcher to receive multiple words

class ContrastMaterialsSensitivity(BaseParser):
    def __init__(self) -> None:
        super().__init__()

    def parse_document(self, document_content: str) -> str:
        try:
            for implying_sentence in NO_CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS:
                if implying_sentence in document_content:
                    return NEGATIVE_VALUE  # meaning there is no contrast materials sensitivity
                else:
                    return POSITIVE_VALUE
        except:
            return MISSING_VALUE
