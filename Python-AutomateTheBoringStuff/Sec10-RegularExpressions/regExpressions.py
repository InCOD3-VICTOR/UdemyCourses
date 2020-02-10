import re

phoneNumRegx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegx.search('Call me at 415-555-1011 tomorrow. or at 710-644-3825 for my office line.')
print(mo.group())
