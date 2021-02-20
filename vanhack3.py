# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers or a range of integers denoted by the starting integer separated from the end integer in the
# range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not
# considered a range unless it spans at least 3 numbers. For example "12,13,15-17". Complete the solution so that it
# takes a list of integers in increasing order and returns a correctly formatted string in the range format.
#
# Documentation
# solution(list)
# Parameters
# list: Array (of Integers) - An ordered list of unique integers
#
# Return Value
# String - formatted string with range format
#
# Example:
#
# solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])


def solution(args):
    length_args = len(args)
    zero = 0
    new_list = []

    if args:
        while zero < length_args:
            min_num, new_var = args[zero], zero
            while new_var < length_args - 1 and args[new_var + 1] == args[new_var] + 1:
                new_var += 1
            if new_var - zero > 1:
                min_num = str(args[zero]) + "-" + str(args[new_var])
                zero = new_var + 1
            else:
                zero = (new_var if new_var > zero else zero + 1)
            new_list.append(min_num)

    return ",".join(str(num) for num in new_list)
