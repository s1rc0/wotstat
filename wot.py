from WotBlitz import WotBlitz

MY_ID = 39282989
MY_USERNAME = 's1rc0r'

account_id = '39282989'
my_list = str(list(range(1, 100)))[1:-1]


WotBlitz.application_id = '6c8058cb8dadba5f30be5439d9d15490'

c = WotBlitz()
c.application_id = '6c8058cb8dadba5f30be5439d9d15490'

y = c.get_player_personal_data(my_list, fields='nickname')

print(y)
