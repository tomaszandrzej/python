import re

string = 'jibbgerihsdh deco20170808rator shfjskhfd 890 sf8yr4897rdmj9u9cmn98n8 7n897nv 12345678 8 8 n98 7n98798t7'

find = re.findall(r'\w\d{8}',string)

print(find)
