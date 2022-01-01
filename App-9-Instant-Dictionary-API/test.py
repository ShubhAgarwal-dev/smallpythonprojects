from csvtodb import *

ddgd = DatabaseDevelopment.get_defination('data.db', 'acid')
print(ddgd)

print(DatabaseDevelopment.get_defination('data.db', 'newj'))
