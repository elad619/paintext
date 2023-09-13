from constants import MISSING_VALUE_STRING
from parser_columns.base_parser import BaseParser

# TODO two typos found קסלטו, אפסירין
BLOOD_THINNERS_KEYWORD_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס', 'קומדין',
                        'קלקסל']
BLOOD_THINNERS_KEYWORD = 'מדללי דם'


class BloodThinners(BaseParser):
    def parse_document(self, document_content: str) -> str:
        for blood_thinner in BLOOD_THINNERS_KEYWORD_TYPES:
            if blood_thinner in document_content:
                return blood_thinner
        if BLOOD_THINNERS_KEYWORD in document_content:
            return BLOOD_THINNERS_KEYWORD
        return MISSING_VALUE_STRING
