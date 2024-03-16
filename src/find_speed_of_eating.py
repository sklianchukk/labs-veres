# 2 лаба, 2 рівень, 3 варіант
import math


def sum_hour(arr, middle_speed):
    sum_hour = 0
    for num in arr:
        hour = math.ceil(num / middle_speed)
        sum_hour += hour
    return sum_hour


def find_speed_of_eating(arr, h):
    min_speed = 1
    max_speed = max(arr)
    while min_speed < max_speed:
        middle_speed = (min_speed + max_speed) // 2
        sum = sum_hour(arr, middle_speed)
        if sum == h:
            return f"The monkey will eat all piles at speed of {middle_speed} bananas per hour"
        elif sum < h:
            max_speed = middle_speed - 1
        else:
            min_speed = middle_speed + 1
    return f"The monkey will eat all piles at speed of {min_speed} bananas per hour"
