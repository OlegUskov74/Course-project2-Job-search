import pytest
from src.vacancy import Vacancy


def test_vacancy_creation(fake_vacancy_data):
    """[Тест] Инициализация класса"""
    vacancy = Vacancy.new_vacancy_json(fake_vacancy_data)
    assert vacancy.name == "Python Developer"
    assert vacancy.url == "http://example.com/vacancy"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.currency == "RUB"


def test_invalid_vacancy_name():
    """[Тест] Валидации имени"""
    with pytest.raises(ValueError):
        Vacancy(1, "", "http://example.com")


def test_invalid_vacancy_url():
    """[Тест] Валидации URL"""
    with pytest.raises(ValueError):
        Vacancy(1, "Name", "invalid_url")


def test_vacancy_str(fake_vacancy_data):
    """[Тест] Магический метод отображения информации об объекте класса"""
    vacancy = Vacancy.new_vacancy_json(fake_vacancy_data)
    result = str(vacancy)
    assert "Python Developer" in result
    assert "Опыт работы: От 1 года до 3 лет" in result


def test_vacancy_comparison():
    """[Тест]"""
    v1 = Vacancy(1, "Dev", "http://url", salary_from=100000)
    v2 = Vacancy(2, "Lead", "http://url", salary_from=150000)
    assert v2 > v1


def test_to_dict(fake_vacancy_data):
    """[Тест] Преобразование объект в словарь """
    vacancy = Vacancy.new_vacancy_json(fake_vacancy_data)
    data = vacancy.to_dict()
    assert isinstance(data, dict)
    assert data["name"] == "Python Developer"
