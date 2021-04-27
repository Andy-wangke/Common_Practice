import re
class Dog:

    #tricks = []

    i=12345
    #contruction
    def __init__(self,name):
        self.name=name


name = ['2017-12-22 14:07 来源：数据宝'][0]
#name=[n.encode('utf-8') for n in name]
matched=re.match(r'\d{4}\-\d{1,2}\-\d{1,2}',name).group(0)
print(matched)

x=Dog('Tom')
print(x.i)


check_date=['20171211','20171212']
date= '20171211'
if date in check_date:
	print('exist...')
else:
	print('not exist...')

print(date,"not in",str(check_date))

# test 'or' phrase
key = None or 1
print("key value is not None",key)

#

source= '2017-12-22 11:05 来源：证券时报·e公司'
matched = re.match(r'(\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}\:\d{1,2})',source)
print('matched...'+matched.group(0))

#search from dict list

ly_legislator={'ad':2,"name":'123'}
origin_npl_dict_list = [{'ad':2,"name":'朱勝號'},{'ad':2,"name":'王顯明'},{'ad':2,"name":'王金平'},{'ad':2,"name":'123'}]
possible = [legislator for legislator in origin_npl_dict_list if legislator['name']==ly_legislator['name'] and legislator['ad']==ly_legislator['ad']]
print(possible)



force = True

print(not force)


