from const.constants import MISSING_VALUE
from utils.text_searcher import TextSearcher

BLOOD_THINNERS_KEYWORD_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס',
                                'קומדין',
                                'קלקסל']
BLOOD_THINNERS_KEYWORD = 'מדללי דם'
DOESNT_TAKE_BLOOD_THINNERS_MESSAGE = 'ללא'


def find_blood_thinners(text_searcher: TextSearcher):
    blood_thinners = text_searcher.get_words_if_found(BLOOD_THINNERS_KEYWORD_TYPES)[0]
    answer = ", ".join(blood_thinners) if blood_thinners else text_searcher.get_word_if_found(BLOOD_THINNERS_KEYWORD)
    return answer if answer else MISSING_VALUE
