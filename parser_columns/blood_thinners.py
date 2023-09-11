from constants import MISSING_VALUE_STRING
from parser_columns.base_parser import BaseParser

CONTENT = 'Content'
# TODO two typos found קסלטו, אפסירין
BLOOD_THINNERS_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס', 'קומדין',
                        'קלקסל']
BLOOD_THINNERS = 'מדללי דם'


class BloodThinners(BaseParser):
    def parse_document(self, document_content: str) -> str:
        for blood_thinner in BLOOD_THINNERS_TYPES:
            if blood_thinner in document_content:
                return blood_thinner
        if BLOOD_THINNERS in document_content:
            return BLOOD_THINNERS
        return MISSING_VALUE_STRING
