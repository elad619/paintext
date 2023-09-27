from typing import List
import datetime as dt
from const.constants import MISSING_VALUE
import re
from dateutil.parser import parse as date_parser, ParserError

DATE_STRING_REGEX_FORMAT = r'\d+[\./]\d+[\./]\d+'


def parse_document(document_content: str) -> str:
    dates: List[dt.date] = []
    dates_in_documents: List[str] = re.findall(DATE_STRING_REGEX_FORMAT, document_content)
    for date in dates_in_documents:
        try:
            dates.append(date_parser(date.replace(".", "/")).date())
        except ParserError:
            pass
    return str(max(dates_in_documents)) if dates_in_documents else MISSING_VALUE
