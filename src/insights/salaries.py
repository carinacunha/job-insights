from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    max_salaries = set()
    for elem in data:
        if elem['max_salary'] != '':
            try:
                max_salaries.add(int(elem['max_salary']))
            except ValueError:
                print('Error')
    return max(max_salaries)
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    data = read(path)
    min_salaries = set()
    for elem in data:
        if elem['min_salary'] != '':
            try:
                min_salaries.add(int(elem['min_salary']))
            except ValueError:
                print('Error')
    return min(min_salaries)
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        int_min_salary = int(job['min_salary'])
        int_max_salary = int(job['max_salary'])
        int_salary = int(salary)

    except KeyError:
        raise ValueError("Minimum or maximum salary does not exist")

    except TypeError:
        raise ValueError("Minimum, maximum and salary should be a number")

    if int_min_salary > int_max_salary:
        raise ValueError("Minimum salary is higher than the maximum salary")

    return int_max_salary >= int_salary >= int_min_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    filtered_jobs = []

    for elem in jobs:
        try:
            if matches_salary_range(elem, salary):
                filtered_jobs.append(elem)
        except ValueError:
            print("Error")
    return filtered_jobs
