import sum_num
import math
import pytest


def main():
    test_1 = sum_num.ListOfNumbers([-5, 2, 6, 1, -7, 10])
    maxdiff_output_1 = test_1.MaxDiff()

    test_2 = sum_num.ListOfNumbers([9, 8, -7, 6, 5, -4])
    maxdiff_output_2 = test_2.MaxDiff()

    test_3 = sum_num.ListOfNumbers([0.5, -0.9, 0.1, -0.2])
    maxdiff_output_3 = test_3.MaxDiff()

    assert maxdiff_output_1 == 17
    assert maxdiff_output_2 == 16
    assert maxdiff_output_3 - 1.4 < 0.0001

    with pytest.raises(ValueError):
        test_4 = sum_num.ListOfNumbers(math.sqrt(2),
                                       math.sqrt(-5),
                                       math.sqrt(8))
        test_4.MaxDiff()
    with pytest.raises(TypeError):
        test_5 = sum_num.ListOfNumbers('9', 5, 9, 5, 9, 5)
        test_5.MaxDiff()

    test_6 = sum_num.ListOfNumbers([0, -1.5, -2, -7, -53])
    findextremes_Output1 = test_6.findextremes()

    test_7 = sum_num.ListOfNumbers([0, 3.2, 2, 10, 6])
    findextremes_Output2 = test_7.findextremes()

    test_8 = sum_num.ListOfNumbers([2, -3, 54, 6, 10])
    findextremes_Output3 = test_8.findextremes()

    assert findextremes_Output1 == [-53.0, 0.0]
    assert findextremes_Output2 == [0, 10]
    assert findextremes_Output3 == [-3.0, 54.0]

    with pytest.raises(ValueError):
        test_9 = sum_num.ListOfNumbers([3+2j, 4])
        test_9.findextremes()

    with pytest.raises(TypeError):
        test_10 = sum_num.ListOfNumbers([])
        test_10.findextremes()

    test_11 = sum_num.ListOfNumbers([1, 5, 8, 3, 6, 3])
    summed_output_1 = test_11.sum_numbers()

    test_12 = sum_num.ListOfNumbers([-4, 5, 7, 5, 3, -5])
    summed_output_2 = sum_numbers()

    test_13 = sum_num.ListOfNumbers([0.5, -0.3, 0.2, -0.5])
    summed_output_3 = sum_numbers()

    assert summed_output_1 == 26
    assert summed_output_2 == 11
    assert summed_output_3 - 0.1 < 0.0001

    with pytest.raises(ValueError):
        test_14 = sum_num.ListOfNumbers(math.sqrt(-2),
                                        math.sqrt(4),
                                        math.sqrt(2))
        test_14.sum_numbers()

    with pytest.raises(TypeError):
        test_15 = sum_num.ListOfNumbers("1", 2, 3)
        test_15.sum_numbers()


if __name__ == '__main__':
    main()
