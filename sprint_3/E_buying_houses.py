def read_input():
    n, k = map(int, input().split())
    houses = [int(i) for i in input().split()]
    return k, houses


def how_houses(houses, k):
    houses.sort()
    summary = 0
    quantity = 0
    for price in houses:
        if summary + price <= k:
            summary += price
            quantity += 1
    return quantity


def main():
    k, houses = read_input()
    print(how_houses(houses, k))


if __name__ == '__main__':
    main()
