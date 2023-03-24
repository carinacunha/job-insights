from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    unique_industries = set()
    for elem in data:
        if elem['industry'] != '':
            unique_industries.add(elem['industry'])
    return unique_industries

    raise NotImplementedError


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    specifics_jobs_of_industry = []
    for elem in jobs:
        if elem['industry'] == industry:
            specifics_jobs_of_industry.append(elem)
    return specifics_jobs_of_industry

    raise NotImplementedError
