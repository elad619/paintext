from option_based_parasers.base_option_from_group_parser import OptionBasedParser

from constants import MISSING_VALUE

BLOOD_THINNERS_KEYWORD_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס',
                                'קומדין', 'קלקסל']


class BloodThinners(OptionBasedParser):
    def __init__(self):
        super().__init__(options=BLOOD_THINNERS_KEYWORD_TYPES)

    def parse_document(self, document_content: str) -> str:
        options_found_in_document = self._get_matches_for_all_options(document_content)
        if len(options_found_in_document) == 0:
            options_found_in_document.append(MISSING_VALUE)
        sorted_options_found_in_document = sorted(options_found_in_document)
        return ",".join(sorted_options_found_in_document)
