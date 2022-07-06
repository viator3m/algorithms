from typing import List
from howlong import how_long


@how_long
def moving_average_naive(timeseries: List[int], K: int) -> List[int or float]:
    result = []
    for begin in range(0, len(timeseries) - (K - 1)):
        end = begin + K
        time_summ = 0
        time_list = timeseries[begin:end]
        for var in time_list:
            time_summ += var
        time_avg = round(time_summ / K, 2)
        result.append(time_avg)
    return result


@how_long
def moving_average_optimized(timeseries: List[int], K: int)\
        -> List[int or float]:
    result = []
    current_summ = sum(timeseries[0:K])
    current_avg = current_summ / K
    result.append(current_avg)
    for i in range(len(timeseries) - K):
        current_summ -= timeseries[i]
        current_summ += timeseries[i + K]
        current_avg = round(current_summ / K, 2)
        result.append(current_avg)
    return result


K = 3
timeseries = [4,3,8,1,5,6,3]
print(moving_average_naive(timeseries, K))

# moving_average_optimized(timeseries * 100000, K)
