from enum import Enum

class CONSTANTS(Enum):
    DAYS = 3
    WEEKS = 7
    MONTHS = 2
    YEARS = 10
 

for constant in CONSTANTS:
    print(f"{constant} : {constant.value}")