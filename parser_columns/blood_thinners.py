# from utils.find_similar_words import find_similar_words
#
# from constants import MISSING_VALUE_STRING
# from parser_columns.base_parser import BaseParser
#
# BLOOD_THINNERS_KEYWORD_TYPES = ['אספירין', 'מיקרופירין', 'קרטיה', 'פלביקס', 'קלופידרוגל', 'קסרלטו', 'אליקוויס',
#                                 'קומדין',
#                                 'קלקסל']
# BLOOD_THINNERS_KEYWORD = 'מדללי דם'
# DOESNT_TAKE_BLOOD_THINNERS_MESSAGE = 'ללא'
#
#
# class BloodThinners(BaseParser):
#     def parse_document(self, document_content: str) -> str:
#         for blood_thinner in BLOOD_THINNERS_KEYWORD_TYPES:
#             if (blood_thinner in document_content) or (len(find_similar_words(document_content, blood_thinner)) > 0):
#                 return blood_thinner
#         if (BLOOD_THINNERS_KEYWORD in document_content) or (
#                 len(find_similar_words(document_content, BLOOD_THINNERS_KEYWORD)) > 0):
#             return DOESNT_TAKE_BLOOD_THINNERS_MESSAGE
#         return MISSING_VALUE_STRING
