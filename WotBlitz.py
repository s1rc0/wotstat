from urllib.request import urlopen, Request
from urllib.error import URLError
from urllib.parse import urlencode
import json



""" WotBlitz Client
"""

__author__ = "Sergey Postument (sergey.postument@gmail.com)"

APP_ID = '6c8058cb8dadba5f30be5439d9d15490'
GAME = 'wotb'
HTTP_API_HOST = 'http://api.wotblitz.ru/'
HTTPS_API_HOST = 'https://api.wotblitz.ru/'
ACCOUNT_LIST_METHOD = '/account/list/'
ACCOUNT_INFO_METHOD = '/account/info/'
ACCOUNT_ACHIEVEMENTS_METHOD = '/account/achievements/'
TANKS_STATS_METHOD = '/tanks/stats/'
TANKS_ACHIEVEMENTS_METHOD = '/tanks/achievements/'

'''
def finditem(obj, key):
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            return finditem(v, key)
'''


class WotBlitz:
    application_id = ''

    def __init__(self):
        self.application_id = ''

    def get_application_id(self):
        return self.application_id

    def get_account_id(self, nickname, language="ru", fields="", type="", limit=100):
        post_data = {"application_id": self.application_id, "language": language, "limit": limit, "type": type, "fields": fields, "search": nickname}
        encoded_post_data = urlencode(post_data)
        p = encoded_post_data.encode("utf-8")
        request = urlopen(Request(HTTP_API_HOST + GAME + ACCOUNT_LIST_METHOD), data=p, context=None)
        response = request.read()
        data = json.loads(response.decode())
        return data

    def get_account_id_by_name(self, nickname, language="en", fields="", type="exact", limit=100):
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
        request = Request(HTTP_API_HOST + GAME + ACCOUNT_LIST_METHOD + self.application_id + '&search=' + str(nickname))
        try:
            request = urlopen(request, data=None, context=None)
            response = request.read()
            data = json.loads(response.decode())
            return data
        except URLError as e:
            print(e.code)
            if response is None:
                print("url is not found")

    def get_player_personal_data(self, player_id):
        request = Request(HTTP_API_HOST + GAME + ACCOUNT_INFO_METHOD + self.application_id + '&account_id=' + str(player_id))
        try:
            request = urlopen(request, data=None, context=None)
            response = request.read()
            data = json.loads(response.decode())
            return data
        except URLError as e:
            print(e.code)
            if response is None:
                print("url is not found")



