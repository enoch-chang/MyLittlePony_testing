def test_sum_numbers():
    from sum_num import sum_numbers
    summed_output_1 = sum_numbers([1, 5, 8, 3, 6, 3])
    summed_output_2 = sum_numbers([-4, 5, 7, 5, 3, -5])
    summed_output_3 = sum_numbers([0.5, -0.3, 0.2, -0.5])
    assert summed_output_1 == 26
    assert summed_output_2 == 11
    assert summed_output_3 - 0.1 < 0.0001