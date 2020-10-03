import json
import urllib
from urllib import request, parse


class MyJSON:
    """Класс создает URL и др входные параметры для запроса.
    Умеет собирать строку.
    Умеет передавть запрос.
    Сохраняет и раскодирует ответ."""

    def __init__(self, url='https://regions-test.2gis.com/1.0/regions',
                 q=None,
                 country_code=None,
                 page=1,
                 page_size=15):
        self.url = url
        self.q = q
        self.country_code = country_code
        self.page = page
        self.page_size = page_size

    @property
    def make_url(self):
        url_for_request = self.url + '?'

        if self.q is not None:
            self.q = urllib.parse.quote(self.q)
            str_q = 'q={0}'.format(self.q)
            url_for_request = url_for_request + str_q

        if self.country_code is not None:
            str_country_code = '&country_code={0}'.format(self.country_code)
            url_for_request = url_for_request + str_country_code

        if self.page is not None:
            str_page = '&page={}'.format(self.page)
            url_for_request = url_for_request + str_page

        if self.page_size is not None:
            str_page_size = '&page_size={0}'.format(self.page_size)
            url_for_request = url_for_request + str_page_size

        return url_for_request

    @staticmethod
    def do_request(url_for_request):
        """Метод получает на вход строку с собранным url и делает запрос.
        Возвращает раскодированный json"""
        response = request.urlopen(url_for_request)
        response_for_check = json.loads(response.read().decode('utf-8'))
        return response_for_check

    def get_total(self, response_for_check):
        """Возвращает значение параметра total"""
        return response_for_check['total']

    def get_id(self, response_for_check, index):
        """Возвращает значение параметра id"""
        return response_for_check["items"][index]["id"]

    def get_name(self, response_for_check, index):
        """Возвращает значение параметра name"""
        return response_for_check["items"][index]["name"]

    def get_code(self, response_for_check, index):
        """Возвращает значение параметра code"""
        return response_for_check["items"][index]["code"]

    def get_country_name(self, response_for_check, index):
        """Возвращает значение параметра country : name """
        return response_for_check["items"][index]["country"]["name"]

    def get_country_code(self, response_for_check, index):
        """Возвращает значение параметра country : code """
        return response_for_check["items"][index]["country"]["code"]


