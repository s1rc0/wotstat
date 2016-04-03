from WotBlitz import WotBlitz

MY_ID = 39282989
MY_USERNAME = 's1rc0r'

account_id = '39282989'

WotBlitz.application_id = '6c8058cb8dadba5f30be5439d9d15490'

c = WotBlitz()
c.application_id = '6c8058cb8dadba5f30be5439d9d15490'
# print(c.get_application_id())
print(c.get_account_id_by_name('s1rc0r'))
print(c.get_player_personal_data(1))

