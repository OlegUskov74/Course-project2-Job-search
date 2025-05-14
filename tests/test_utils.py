from src.utils import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    sort_vacancies,
)
from src.vacancy import Vacancy


def test_filter(hh_api_dates: dict) -> None:
    """[Тест] Тестирование функций"""
    data_filter = Vacancy.new_vacancies_json(hh_api_dates["items"])
    filt_vac = filter_vacancies(data_filter, ["Водитель"])
    assert filt_vac[0].name == "Водитель"
    vac_salary = get_vacancies_by_salary(filt_vac, "0 - 100000000")
    assert vac_salary[0].name == "Водитель"
    sort_vac = sort_vacancies(vac_salary)
    assert sort_vac[0].name == "Водитель"
    top_vac = get_top_vacancies(sort_vac, 3)
    assert top_vac[0].name == "Водитель"
