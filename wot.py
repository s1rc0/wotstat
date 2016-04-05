from WotBlitz import WotBlitz
import json
import sys

MY_ID = 39282989
MY_USERNAME = 's1rc0r'

account_id = '39282989'

WotBlitz.application_id = '6c8058cb8dadba5f30be5439d9d15490'

c = WotBlitz()
c.application_id = '6c8058cb8dadba5f30be5439d9d15490'

x = c.get_account_id('s1r',limit=2)

print(x)

'''
def get_all_key_value_pairs_where_values_are_simple(data):
    class Namespace(object):
        pass
    ns = Namespace()
    ns.results = []

    def inner(data):
        if isinstance(data, dict):
            for k, v in data.items():
                if (isinstance(v, dict) or
                    isinstance(v, list) or
                    isinstance(v, tuple)
                    ):
                    inner(v)
                else:
                    ns.results.append((k, v))
        elif isinstance(data, list) or isinstance(data, tuple):
            for item in data:
                inner(item)

    inner(data)
    return ns.results

from pprint import pprint



#s = c.get_player_personal_data(MY_ID)
s = c.get_account_id_by_name('s1rc0r')
x = get_all_key_value_pairs_where_values_are_simple(s)
for k, v in x:
    print(k, "=", v)
#print(type(k))

#print(c.get_account_id_by_name('s1c0'))
'''