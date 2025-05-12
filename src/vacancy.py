from typing import Union, Hashable, Dict, List


class Vacancy:
    """
    Класс для описания вакансии

    Атрибуты:
        vacancy_id (int | str): Уникальный идентификатор вакансии.
        name (str): Название вакансии.
        url (str): Ссылка на вакансию.
        salary_from (float): Нижняя граница зарплаты.
        salary_to (float): Верхняя граница зарплаты.
        currency (str): Валюта зарплаты.
        description (str): Краткое описание или требования.
        area (str): Город или регион.
        employment (str): Тип занятости.
        experience (str): Требуемый опыт работы.
    """
    __slots__ = (
        "vacancy_id",
        "name",
        "url",
        "salary_from",
        "salary_to",
        "currency",
        "description",
        "area",
        "employment",
        "experience",
    )
    vacancy_id: int
    name: str
    url: str
    salary: str
    salary_from: float
    salary_to: float
    currency: str
    description: str
    area: str
    employment: str
    experience: str

    def __init__(
            self,
            vacancy_id,
            name,
            url,
            salary_from=0,
            salary_to=0,
            currency="RUB",
            description="",
            area="",
            employment="",
            experience="",
    ):
        """Метод для инициализации экземпляра класса"""
        self.__validate_string(name)
        self.__validate_url(url)
        self.__validate_salary(salary_from, salary_to)

        self.vacancy_id = vacancy_id
        self.name = name
        self.url = url
        self.salary_from = float(salary_from)
        self.salary_to = float(salary_to)
        self.currency = currency
        self.description = description
        self.area = area
        self.employment = employment
        self.experience = experience

    def __str__(self):
        """Магический метод отображения информации об объекте класса Vacancy для пользователей"""
        salary_str = f"{self.salary_to} - {self.salary_from} {self.currency}"
        return (
            f"Вакансия: {self.name} "
            f"- Зарплата: {salary_str} "
            f"- Опыт работы: {self.experience} "
            f"- Описание: {self.description[:200]} "
            f"- Подробнее по ссылке: {self.url}"
        )

    def __eq__(self, other):
        """Магический метод для равенства"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_comparison == other.salary_comparison

    def __lt__(self, other):
        """Магический метод для оператора меньше"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_comparison < other.salary_comparison

    def __gt__(self, other):
        """Магический метод для оператора больше"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_comparison > other.salary_comparison

    @property
    def salary_comparison(self):
        """Метод для сравнения зарплаты"""
        return self.salary_to if self.salary_to else self.salary_from

    @staticmethod
    def __validate_string(name: str):
        """Метод валидации имени"""
        if not isinstance(name, str):
            raise ValueError("Не должно быть пустой строкой.")

    @staticmethod
    def __validate_url(url: str):
        """Метод валидации URL"""
        if not url.startswith("http"):
            raise ValueError("Некорректный URL.")

    @staticmethod
    def __validate_salary(salary_from: float, salary_to: float):
        """Метод валидации верхней и нижний границ зарплаты"""
        if not isinstance(salary_from, (int, float)) or salary_from < 0:
            raise ValueError("Нижняя граница зарплаты должно быть числом >= 0.")
        if not isinstance(salary_to, (int, float)) or salary_to < 0:
            raise ValueError("Верхняя граница зарплаты должно быть числом >= 0.")

    @classmethod
    def new_vacancies_json(cls, vacancies_json: List[Dict[Hashable, Union[str, int, float]]]):
        """Класс-метод для создания списка объектов Vacancy из списка JSON-данных."""
        return [cls.new_vacancy_json(vacancy) for vacancy in vacancies_json]

    @classmethod
    def new_vacancy_json(cls, vacancy_json: Dict[Hashable, Union[str, int, float]]):
        """Класс-метод для создания объекта Vacancy из JSON-данных одной вакансии."""
        salary_data = vacancy_json.get("salary") or {}

        salary_from = salary_data.get("from") or 0
        salary_to = salary_data.get("to") or 0
        currency = salary_data.get("currency") or "RUB"

        return cls(
            vacancy_id=vacancy_json.get("id", ""),
            name=vacancy_json.get("name", ""),
            url=vacancy_json.get("alternate_url", ""),
            salary_from=salary_from,
            salary_to=salary_to,
            currency=currency,
            description=vacancy_json.get("snippet", {}).get("requirement", "") or "Нет данных",
            area=vacancy_json.get("area", {}).get("name", "") or "Нет данных",
            employment=vacancy_json.get("employment", {}).get("name", "") or "Нет данных",
            experience=vacancy_json.get("experience", {}).get("name", "") or "Нет данных",
        )
        return vacancy

    def to_dict(self) -> dict:
        """Метод преобразует объект в словарь (для сохранения в JSON)."""
        return {
            "vacancy_id": self.vacancy_id,
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency,
            "description": self.description,
            "area": self.area,
            "employment": self.employment,
            "experience": self.experience
        }

# if __name__ == "__main__":
#     vacancy1 = Vacancy(
#         "93353083",
#         "Тестировщик комфорта квартир",
#         "https://hh.ru/vacancy/93353083",
#         350000,
#         4500000,
#         "RUB",
#         "Занимать активную жизненную позицию, уметь активно танцевать и громко петь..." ,
#         "Воронеж",
#         "Полная занятость",
#         "Нет опыта"
#     )
#     vacancy2 = Vacancy(
#         "92223756",
#         "Удаленный диспетчер чатов (в Яндекс)",
#         "https://hh.ru/vacancy/92223756",
#         33000,
#         44000,
#         "RUB",
#         "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое.",
#         "Россия",
#         "Полная занятость",
#         "Нет опыта"
#     )
#
#     print(vacancy1 > vacancy2)
#     print(str(vacancy1))
