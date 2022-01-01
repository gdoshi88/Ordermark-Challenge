# The Ordermark LA office has a gate (only one) that can be used either as an exit or an entrance. As can be expected for a single gate, at times, and often at the same time, many people want to exit or enter through the gate. The [i]th person comes to the gate at time[i] and wants to either:

# exit the office if direction[i] = 1; or
# enter the office if direciton[i] = 0.
# People line up in one of two queues, one to exit and another to enter. They are ordered by the time when they came to the gate and, if the times are equal, by their indices (eg, a person might have the same arrival time as another, but their index position cannot be the same as the other person).

# If a person wants to enter and another person wants to leave at the same time, there are three possible outcomes, all dependent on what happened in the previous second. If, in the previous second, the gate was:

# not used at all (maybe it was used before, but not at the previous second), then the person who wants to leave goes first.
# used to exit, then the person who wants to exit goes first
# used to enter, then the person who wants to enter goes first
# Passing through the gate takes 1 second.

# Task:

# Your task is to write a function that determines when each person will pass through the gate.

# The function must return an array of n integers where the value at index[i] is the time when the [i]th person will pass through the turnstile (IMPORTANT see answers to examples below if this isn’t clear).

# The function has the following params:

# • times: an array of n integers where the value at index [i] is the time when the [i]th person will came to the turnstile • directions: an array of n integers where the value at index [i] is the direction of the [i]th person

# Constraints:

# • 1 <= n <= 10^5 • 0 <= times[i] <= 10^9 for 0 <= i <= n – 1 • times[i] <= times[i+1] for 0 <= i <= n - 2 • 0 <= directions[i] <= 1 for 0 <= i <= n – 1

# Assessment:

# Your solution will be assessed for:

# number of tests passed
# readability of your code (make it easy for us to understand your solution please)
# optimizations (run time/time complexity, space complexity)
# Sample function

# def get_times(times, directions): # your code pass

# Example 1

# n = 4

# times = [0,0,1,5] directions = [0,1,1,0] get_times(times, directions) # returns [2,0,1,5]

# Example 2

# n = 5

# times = [0,1,1,3,3] directions = [0,1,0,0,1] output = [0,2,1,4,3]

# Example 3

# n = 5

# times = [0,1,1,3,3] directions = [0,1,0,0,1] output = [0,2,1,4,3]

x = [0, 1, 1, 3, 3]
y = [0, 1, 0, 0, 1]


def solution(times, directions):
    enter = []
    exit = []
    counter_reset = [0] * len(times)

    for index, value in enumerate(times):
        if directions[index] == 0:
            enter.append([times[index], index])
        elif directions[index] == 1:
            exit.append([times[index], index])
        else:
            print(
                "directions can only have values 0, 1. a value other than 0 or 1 exists.")
    # print(enter)
    # print(exit)

    time_count = 0
    last_value = -1
    # not used at all (maybe it was used before, but not at the previous second), then the person who wants to leave goes first.
    # used to exit, then the person who wants to exit goes first
    # used to enter, then the person who wants to enter goes first
    # Passing through the gate takes 1 second.
    while enter or exit:
        if exit and exit[0][0] <= time_count and (last_value == -1 or last_value == 1 or not enter or (last_value == 0 and enter[0][0] > time_count)):
            counter_reset[exit[0][1]] = time_count
            last_value = 1
            exit.pop(0)
            print(f"{exit} exit")
            print(f"exit{last_value}")
        elif enter and enter[0][0] <= time_count:
            counter_reset[enter[0][1]] = time_count
            last_value = 0
            enter.pop(0)
            print(f"{enter} enter")
            print(f"enter{last_value}")
        else:
            last_value = -1
            print(f"{last_value} else")

        time_count += 1

    return counter_reset


solution(x, y)
