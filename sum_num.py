def sum_numbers(num_list):
    sum = 0
    for num in num_list:
        sum = sum + num
    return sum

def MaxDiff(num_list):
    max_diff = abs(num_list[1] - num_list[0])
    for i in range(0, num_list_size):
        for j in range(i + 1, num_list):
            if (abs(num_list[j] - num_list[i]) > max_diff):
                max_diff = abs(num_list[j] - num_list[i])
    return max_diff
