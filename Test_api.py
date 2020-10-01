import pytest

from MyJSON import MyJSON


@pytest.mark.tryfirst
def test_total_count():
    """Проверям праметр total. Отправляем запрос без параметров
    https://regions-test.2gis.com/1.0/regions
    """
    req = MyJSON()
    response = req.do_request(req.make_url)
    assert req.get_total(response) >= 22


@pytest.mark.tryfirst
def test_find_name():
    """Проверяем поиск по полному имени города : Актау
    https://regions-test.2gis.com/1.0/regions?q=Актау
    """
    req = MyJSON(q='Актау')
    response = req.do_request(req.make_url)
    assert req.get_name(response, 0) == 'Актау'
    assert req.get_id(response, 0) == 196
    assert req.get_code(response, 0) == 'aktau'
    assert req.get_country_name(response, 0) == "Казахстан"
    assert req.get_country_code(response, 0) == 'kz'


@pytest.mark.trylast
def test_find_by_part_of_name():
    """
    Проверяем выдачу всех городов, содержащих в имени "рск"
    https://regions-test.2gis.com/1.0/regions?q=рск
    """
    req = MyJSON(q='рск')
    response = req.do_request(req.make_url)
    cities = ["Красноярск", "Магнитогорск", "Новосибирск", "Орск", "Усть-Каменогорск"]
    for i in range(len(cities)):
        assert req.get_name(response, i) == cities[i]
