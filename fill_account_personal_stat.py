from WotBlitz import WotBlitz
#from stats.models import BlitzUsers
import math

MY_ID = 39282989
EN_ID = 6154905
IDs = [39282989, 6154905]

wot = WotBlitz()
wot.application_id = '6c8058cb8dadba5f30be5439d9d15490'


def fill_user_stat(ids):
    for account in ids:
        stats = wot.get_player_personal_data(account)
        for item in stats['data'].items():
            print(item)


fill_user_stat(IDs)
'''
def filling_gamer_ids(start_id, end_id, ids_per_request):
    if start_id > end_id:
        return print('End ID cant be more then Start ID')
    a = (end_id - start_id) / ids_per_request
    number_of_iter = math.ceil(a)
    for iteration in range(number_of_iter):
        if ids_per_request < (end_id - start_id):
            ids_list = str(list(range(start_id, start_id+ids_per_request)))[1:-1]
        else:
            ids_list = str(list(range(start_id, end_id)))[1:-1]
        stats = wot.get_player_personal_data(ids_list, fields="nickname,account_id")
        for item in stats['data'].items():
            if item[1] is not None:
                b = BlitzUsers(account_id=item[1]['account_id'], nickname=item[1]['nickname'])
                b.save()
        start_id += ids_per_request
    return print("Filled")
filling_gamer_ids(1137916, 2000000, 100)
'''




