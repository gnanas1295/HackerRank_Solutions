regex_pattern = r"^(?!.*(IIII|XXXX|CCCC|MMMM|VV|LL|DD))[IVXLCDM]+$"


import re

print(str(bool(re.match(regex_pattern, input()))))
