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


def validate_inputs(job: Dict, salary: Union[int, str]) -> bool:
    list = ['min_salary', 'max_salary']
    for elem in list:
        if (type(job[elem]) not in [int, str] or
            type(job[elem]) == str and
                job[elem].isnumeric() is False):
            raise ValueError('Value is invalid')
    if (type(salary) not in [int, str] or
        type(salary) == str and
            salary.isnumeric() is False):
        raise ValueError('Salary is invalid')


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ('min_salary' not in job or 'max_salary' not in job):
        raise ValueError('Minimum or maximum salary does not exist')
    validate_inputs(job, salary)
    if (job['min_salary'] > job['max_salary']):
        raise ValueError("Minimum salary is higher than the maximum salary")
    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
