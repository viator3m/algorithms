# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order: list[int], max_e: int) -> list[int]:
    for ph in range(len(order) - 1, 0, -1):
        if order[:ph + 1].count(order[ph]) > max_e:
            order.pop(ph)
    return order


def test():
    assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
    assert delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3) == [1, 1, 3, 3, 7, 2, 2, 2]


if __name__ == '__main__':
    test()
