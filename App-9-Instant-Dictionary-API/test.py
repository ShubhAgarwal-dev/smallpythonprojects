from csvtodb import *

ddgd = DatabaseDevelopment.get_defination('data.db', 'acid')
print(ddgd)

a1 = ddgd[1]
print(str(a1))
