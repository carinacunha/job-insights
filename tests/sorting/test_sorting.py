from src.pre_built.sorting import sort_by

jobs = [
    {'date_posted': '2023-02-01', 'max_salary': 4000, 'min_salary': 200},
    {'date_posted': '2023-03-01', 'max_salary': 3000, 'min_salary': 650},
    {'date_posted': '2023-01-01', 'max_salary': 5000, 'min_salary': 2000}
    ]

sorted_by_max = [
    {'date_posted': '2023-01-01', 'max_salary': 5000, 'min_salary': 2000},
    {'date_posted': '2023-02-01', 'max_salary': 4000, 'min_salary': 200},
    {'date_posted': '2023-03-01', 'max_salary': 3000, 'min_salary': 650}
   
]

sorted_by_min = [
    {'date_posted': '2023-02-01', 'max_salary': 4000, 'min_salary': 200},
    {'date_posted': '2023-03-01', 'max_salary': 3000, 'min_salary': 650},
    {'date_posted': '2023-01-01', 'max_salary': 5000, 'min_salary': 2000}
]

sorted_by_date = [
    {'date_posted': '2023-01-01', 'max_salary': 5000, 'min_salary': 2000},
    {'date_posted': '2023-02-01', 'max_salary': 4000, 'min_salary': 200},
    {'date_posted': '2023-01-01', 'max_salary': 5000, 'min_salary': 2000}

]


def test_sort_by_criteria():
    sort_by(jobs, 'max_salary')
    assert jobs == sorted_by_max

    sort_by(jobs, 'min_salary')
    assert jobs == sorted_by_min