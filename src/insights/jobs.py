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
    specific_job = []
    for elem in jobs:
        if elem['job_type'] == job_type:
            specific_job.append(elem)
    return specific_job

    raise NotImplementedError
