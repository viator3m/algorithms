from typing import List


def search_day(price: int, days: List, left: int, right: int):
    mid = (left + right) // 2
    if price > days[-1]:
        return -1
    elif price <= days[mid] and (price > days[mid - 1] or mid == 0):
        return mid + 1
    elif price <= days[mid]:
        return search_day(price, days, left, mid)
    elif price > days[mid]:
        return search_day(price, days, mid + 1, right)


def main() -> None:
    length = int(input())
    days = list(map(int, input().split()))
    price = int(input())
    one_bicycle = search_day(price, days, 0, length)
    two_bicycle = search_day(2 * price, days, 0, length)
    print(one_bicycle, two_bicycle)


if __name__ == '__main__':
    main()
