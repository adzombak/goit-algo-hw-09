import timeit
import random

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(sum_):
    coins_count = {}
    for coin in coins:
        count = sum_ // coin
        coins_count[coin] = count

        sum_ -= count * coin

    return coins_count


def find_min_coins(sum_):
    min_coins = [0] + [float('inf')] * (sum_ + 1)
    used_coins = [0] * (sum_ + 1)

    for i in range(1, sum_ + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                used_coins[i] = coin

    count_coins = {}
    current_sum = sum_
    while current_sum > 0:
        coin = used_coins[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum -= coin

    return count_coins


def test_find_coins(data_set, func):
    for data in data_set:
        func(data)


if __name__ == '__main__':
    dataset = [random.randint(1_000, 2_000) for _ in range(1_000)]

    time_for_greedy = timeit.timeit(lambda: test_find_coins(dataset, find_coins_greedy), number=10)
    time_for_min_coins = timeit.timeit(lambda: test_find_coins(dataset, find_min_coins), number=10)

    print(f"{'|Алгоритм': <21} | {'Час на виконання': <20}|")
    print(f"|{'-' * 20} | {'-' * 20}|")
    print(f"|{'Greedy': <20} | {time_for_greedy: <20.5f}|")
    print(f"|{'Min coins': <20} | {time_for_min_coins: <20.5f}|")
