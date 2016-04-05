from WotBlitz import WotBlitz
import json
import sys

MY_ID = 39282989
MY_USERNAME = 's1rc0r'

account_id = '39282989'

WotBlitz.application_id = '6c8058cb8dadba5f30be5439d9d15490'

c = WotBlitz()
c.application_id = '6c8058cb8dadba5f30be5439d9d15490'

x = c.get_account_id('s1rc0r')
y = c.get_player_personal_data("35305683,2701576")
z = c.get_player_achievements(MY_ID)
print(z)
# getting account id's
#for item in x['data']:
#    print(item.get('account_id'))
#for k in y['data'].values():
#    print(k)
