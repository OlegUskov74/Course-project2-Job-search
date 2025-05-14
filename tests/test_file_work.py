import os.path

import pytest

from config import ROOT_DIR
from src.file_work import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def storage():
    file_path = os.path.join(f"{ROOT_DIR}/data/test_data.json")

    if os.path.exists(file_path):
        os.remove(file_path)

    return JSONSaver(file_name="test_data.json")


def test_add_and_get_vacancy(storage):
    vacancy = {
        "vacancy_id": 1,
        "name": "Dev",
        "url": "http://url",
        "salary_from": 0,
        "salary_to": 0,
        "currency": "RUB",
    }
    storage.add_vacancy(vacancy)
    result = storage.get_vacancies()
    assert len(result) == 1
    assert result[0]["name"] == "Dev"


def test_prevent_duplicate_vacancies(storage):
    vacancy = {
        "vacancy_id": 1,
        "name": "Dev",
        "url": "http://url",
        "salary_from": 0,
        "salary_to": 0,
        "currency": "RUB",
    }
    storage.add_vacancy(vacancy)
    storage.add_vacancy(vacancy)
    result = storage.get_vacancies()
    assert len(result) == 1


def test_get_vacancies_with_filter(storage):
    """[Тест]"""
    vacancies = [
        {
            "vacancy_id": 1,
            "name": "Python Dev",
            "url": "http://url1",
            "salary_from": 100000,
            "salary_to": 150000,
            "currency": "RUB",
        },
        {
            "vacancy_id": 2,
            "name": "Java Dev",
            "url": "http://url2",
            "salary_from": 80000,
            "salary_to": 120000,
            "currency": "RUB",
        },
    ]
    for v in vacancies:
        storage.add_vacancy(v)

    filtered = storage.get_vacancies(name="Python Dev")
    assert len(filtered) == 1
    assert filtered[0]["vacancy_id"] == 1


def test_delete_file(hh_api_data: dict) -> None:
    """[Тест] Удаление вакансий"""
    vacancies = Vacancy.new_vacancies_json(hh_api_data["items"])
    data_file = JSONSaver("test_data")
    data_file.delete_vacancy(vacancies[0])
