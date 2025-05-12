from typing import List

from src.vacancy import Vacancy


def filter_vacancies(vacancies_list: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """Метод фильтрации вакансий"""
    return [vacancies for vacancies in vacancies_list for word in filter_words if word in vacancies.description]


def get_vacancies_by_salary(filtered_vacancies: List[Vacancy], salary_range: str) -> List[Vacancy]:
    """Метод получения вакансий по зарплате"""
    salary_from, salary_to = salary_range.split("-")

    return [
        vacancy
        for vacancy in filtered_vacancies
        if vacancy.salary_from >= int(salary_from) and vacancy.salary_to <= int(salary_to)
    ]


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> List[Vacancy]:
    """Метод сортировки вакансий"""
    return sorted(ranged_vacancies, key=lambda x: x.salary_to, reverse=True)


def get_top_vacancies(sorted_vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Метод получения запрашиваемых вакансий"""
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies: List[Vacancy]) -> None:
    """Метод вывода в консоль"""
    for vacancy in top_vacancies:
        print(vacancy.__str__())
