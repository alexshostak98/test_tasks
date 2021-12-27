"""
Написать функцию на вход которой подается список с целыми числами
Результатом работы функции должен являться отсортированный по правилам список
Правила сортировки:
1 - количество объектов в входном списке
2 - значения в возрастающем порядке
например:
[3, 4, 11, 13, 11, 4, 4, 7, 3] >> [4, 4, 4, 3, 3, 11, 11, 7, 13]
[99, 99, 55, 55, 21, 21, 10, 10] >> [10, 10, 21, 21, 55, 55, 99, 99]
"""

from typing import List


def sort_list(data: List[int]) -> List[int]:
    """
    Return a list sorted by the number of occurrences (first) and by values in increasing order (second).
    """
    return sorted(sorted(data), key=data.count, reverse=True)
