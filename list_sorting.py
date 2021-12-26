from typing import List


def sort_list(data: List[int]) -> List[int]:
    """
    Return a list sorted by the number of occurrences (first) and by values in increasing order (second).
    """
    return sorted(sorted(data), key=data.count, reverse=True)
