# from the documentation
# parsing a date
from parsy import string, regex
from datetime import date
ddmmyy = regex(r'[0-9]{2}').map(int).sep_by(string("-"), min=3, max=4).combine(
               lambda d, m, y: date(2000 + y, m, d))

print(str(ddmmyy.parse('06-05-14')))