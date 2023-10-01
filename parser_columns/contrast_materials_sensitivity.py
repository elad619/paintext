from const.constants import MISSING_VALUE
from utils.text_searcher import TextSearcher

CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS = ["וכי יש רגישות לחומר ניגוד וחומרי הרדמה"]
NO_CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS = ["אין רגישות לחומרי הרדמה", "אין רגישות לחומר ניגוד",
                                              "אין רגישות לחומר ניגוד או לחומרי הרדמה", "לא רגישה ליוד או חמרי הרדמה",
                                              "אין רגישות לחומר ניגוד או לחומרי הרדמה",
                                              "אין רגישות לחומר ניגוד ואין רגישות חומרי הרדמה",
                                              "אין רגישות לחמר ניגוד וחומרי הרדמה", "ואין רגישות חומרי הרדמה",
                                              "אין רגישות ליוד ולחומרי הרדמה"]  # worth checking if it can be shorter


def does_have_materials_sensitivity(text_searcher: TextSearcher):
    if any([text_searcher.is_sentence_in_text(sentence, ["אין"]) for sentence in
            NO_CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS]):
        return False
    if any([text_searcher.is_sentence_in_text(sentence, ["יש"]) for sentence in
            CONTRAST_MATERIALS_SENSITIVITY_IMPLIERS]):
        return True
    return MISSING_VALUE
