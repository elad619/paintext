import re

width_pattern = "\d\d\s*G|G\s*\d\d"
number_pattern = "\d\d"


def get_needle_width(text: str) -> str:
    full_width = [width.group() for width in re.finditer(width_pattern, text)]
    widths = [(re.search(number_pattern, word)).string for word in full_width]
    return ",".join(widths)
