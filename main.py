import numpy as np

arr = np.random.randint(0, 10, 10)
print(arr)


def min_max(arr_par):
    min_val, max_val = arr_par[0], arr_par[0]
    for i in range(1, len(arr_par)):
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    return max_val, min_val


countArray = [0] * (min_max(arr)[0] + 1)


def store_values():
    for num in arr:
        if num in arr:
            countArray[num] += 1
    print(countArray)


store_values()
