from typing import Iterable

def sqrS(list_items: Iterable[int]):
    iteration_count = 0
    result = []
    for i in list_items:
        result.append(i**2)
        iteration_count += 1
    print(f'Len {len(list_items)} to {iteration_count} iteration')
    return result


sqrS([1,2,3,4,5])
sqrS(range(10))
sqrS(range(100))