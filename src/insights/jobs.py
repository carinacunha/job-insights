from functools import lru_cache
from typing import List, Dict
from csv import DictReader


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, mode='r') as filecsv:
        all_data = DictReader(filecsv)
        data = []
        for elem in all_data:
            data.append(elem)
    return data

    raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    type_jobs = set()
    for elem in data:
        if elem['job_type'] != '':
            type_jobs.add(elem['job_type'])
    return type_jobs

    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
