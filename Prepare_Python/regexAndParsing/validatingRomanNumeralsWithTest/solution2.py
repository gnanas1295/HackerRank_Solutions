# The pattern is broken down for readability:
# ^                  - Start of the string
# M{0,3}             - Thousands (0 to 3 'M's)
# (CM|CD|D?C{0,3})   - Hundreds (900, 400, 500-800, or 100-300)
# (XC|XL|L?X{0,3})   - Tens (90, 40, 50-80, or 10-30)
# (IX|IV|V?I{0,3})   - Ones (9, 4, 5-8, or 1-3)
# $                  - End of the string
def validate_roman_numeral(numeral):

    import re

    regex_pattern = r"^[M]{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
    return bool(re.fullmatch(regex_pattern, numeral))
