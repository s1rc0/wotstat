""" WotBlitz Client
"""
__author__ = "Sergey Postument (sergey.postument@gmail.com)"

from urllib.request import urlopen, Request
from urllib.error import URLError
import json

MY_ID = 39282989
MY_USERNAME = 's1rc0r'
APP_ID = '6c8058cb8dadba5f30be5439d9d15490'
GAME = 'wotb'
HTTP_API_HOST = 'http://api.wotblitz.ru/'
HTTPS_API_HOST = 'https://api.wotblitz.ru/'
ACCOUNT_LIST_METHOD = 'account/list'
ACCOUNT_INFO_METHOD = 'account/info'
ACCOUNT_ACHIEVEMENTS_METHOD = 'account/achievements'
TANKS_STATS_METHOD= 'tanks/stats'
TANKS_ACHIEVEMENTS_METHOD = 'tanks/achievements'


class WotBlitz():
    my_id, my_name = 39282989, 's1rc0r'
    scheme, api_host, game, app_id = 'http://', 'api.wotblitz.ru/', 'wotb', '6c8058cb8dadba5f30be5439d9d15490'


    def get_account_id_by_name(name, method='/account/list/?application_id='):
        """
        Searching user-id's by username

        Argumens:
        Parameter           Type            Description
        *application_id     string	        Application ID
        *search             string          Player name search string. Parameter 'type' defines minimum length and
                                            type of search.Maximum length: 24 symbols.
        language            string          en,ru,pl,de,fr,es...
        fields              string,list     Response field. The fields are separated with commas. Embedded fields are
                                            separated with dots. To exclude a field, use "-" in front of its name. In case
                                            the parameter is no defined, the method returns all fields.
        type                string          Search type. Defines minimum length and type of search.
                                            Default value: startswith. Valid values:
                                            "startswith" - Search by initial characters of player name.
                                            Minimum length: 3 characters. Case insensitive. (by default)
                                            "exact" — Search by exact match of player name. Minimum length: 1 character.
                                            Case insensitive.
        limit               numeric         Number of returned entries (fewer can be returned, but not more than 100).
                                            If the limit sent exceeds 100, an limit of 100 is applied (by default).

        Example query string:
        http://api.wotblitz.ru/wotb/account/list/?application_id=6c8058cb8dadba5f30be5439d9d15490&language=en&fields=-&type=exact&search=s1rc0r&limit=100
        """
        request = Request(scheme + api_host + game + method + app_id + '&search=' + name)
        try:
            request = urlopen(request, data=None, context=None)
            response = request.read()
            data = json.loads(response.decode())
            # print(data)
            for i in data['data']:
                return i['account_id']
        except URLError as e:
            print(e.code)
            if response is None:
                print("url is not found")


    def get_player_personal_data(account_id, method='/account/info/?application_id='):
        request = Request(scheme + api_host + game + method + app_id + '&account_id=' + str(account_id))
        try:
            request = urlopen(request, data=None, context=None)
            response = request.read()
            data = json.loads(response.decode())
            print(data)
            #for i in data['data']:
            #    return i['account_id']
        except URLError as e:
            print(e.code)
            if response is None:
                print("url is not found")


    # http://api.wotblitz.ru/wotb/account/info/?application_id=6c8058cb8dadba5f30be5439d9d15490&account_id=39282989


# print(get_account_id_by_name(my_name))
x = 10


#while True:
#    i = list(range(x))
#    print(i, "\n")
#    x += 10



#i = list(range(10))
#print(i)
#while True:
#    print(get_player_personal_data(print(str(i)[1:-1])))



# for i in range(1, 100):
#    print(i)
