from urllib.request import urlopen, Request
from urllib.error import URLError
import json

""" WotBlitz Client
"""

__author__ = "Sergey Postument (sergey.postument@gmail.com)"

MY_ID = 39282989
MY_USERNAME = 's1rc0r'
APP_ID = '6c8058cb8dadba5f30be5439d9d15490'
GAME = 'wotb'
HTTP_API_HOST = 'http://api.wotblitz.ru/'
HTTPS_API_HOST = 'https://api.wotblitz.ru/'
ACCOUNT_LIST_METHOD = '/account/list/?application_id='
ACCOUNT_INFO_METHOD = '/account/info/?application_id='
ACCOUNT_ACHIEVEMENTS_METHOD = '/account/achievements/?application_id='
TANKS_STATS_METHOD = '/tanks/stats/?application_id='
TANKS_ACHIEVEMENTS_METHOD = '/tanks/achievements/?application_id='

# my_id, my_name = 39282989, 's1rc0r'
# scheme, api_host, game, app_id = 'http://', 'api.wotblitz.ru/', 'wotb', '6c8058cb8dadba5f30be5439d9d15490'


class WotBlitz:
    def get_account_id_by_name(self):
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
        request = Request(HTTP_API_HOST + GAME + ACCOUNT_LIST_METHOD + APP_ID + '&search=' + str(self))
        try:
            request = urlopen(request, data=None, context=None)
            response = request.read()
            data = json.loads(response.decode())
            for i in data['data']:
                return i['account_id']
        except URLError as e:
            print(e.code)
            if response is None:
                print("url is not found")

    def get_player_personal_data(self):
        request = Request(HTTP_API_HOST + GAME + ACCOUNT_INFO_METHOD + APP_ID + '&account_id=' + str(self))
        try:
            request = urlopen(request, data=None, context=None)
            response = request.read()
            data = json.loads(response.decode())
            return data
            # for i in data['meta']:
            #    return i['count']
        except URLError as e:
            print(e.code)
            if response is None:
                print("url is not found")


print(WotBlitz.get_account_id_by_name(MY_USERNAME))
print(WotBlitz.get_player_personal_data(MY_ID))

