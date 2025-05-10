from abc import ABC, abstractmethod
import json
import os
from typing import Dict, List, Union

from src.vacancy import Vacancy
from config import ROOT_DIR

class BaseJson(ABC):



    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(BaseJson):



    def __init__(self, file_name: str = "filtered_vacancies.json") -> None:
        """Метод инициализации класса"""

        self.__file_name = f"{ROOT_DIR}/data/{file_name}.json"
        self.data_file: list = []


    def _load_data(self) :
        """Метод загрузки данных из файла"""
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "a", encoding="UTF-8"):
                pass
        else:
            with open(self.__file_name, "r", encoding="UTF-8") as f:
                self.data_file = json.load(f)

    def _save_data(self, data: List[Dict]) -> None:
        """Метод сохранения данных в файл"""
        with open(self.__file_name, "w", encoding="UTF-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))

    def add_vacancy(self, vacancy: Dict[str, Union[str, int, float]]) -> None:
        """Метод для добавления одной вакансии в JSON-файл"""
        data = self.data_file
        if vacancy not in data:
            data.append(vacancy)
            self._save_data(data)

    def add_vacancies(self, vacancies: List[Dict[str, Union[str, int, float]]]) -> None:
        """Метод для добавления вакансий в JSON-файл"""
        data = self.data_file
        data.extend(vacancies)
        self._save_data(data)

    def get_vacancies(self, **criteria) -> List[Dict[str, Union[str, int, float]]]:
        """Метод для получения вакансий из JSON-файл по указанным критериям"""
        data = self.data_file
        if not criteria:
            return data

        result = []
        for vacancy in data:
            if all(str(vacancy.get(k, "")).lower() == str(v).lower() for k, v in criteria.items()):
                result.append(vacancy)
        return result


    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод удаления вакансий"""
        for index, item in enumerate(self.data_file):
            if item["vacancy_id"] == vacancy.vacancy_id:
                del self.data_file[index]

        self._save_data(self.data_file)



