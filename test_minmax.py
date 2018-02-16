def test_minmax():
    from minmax import findextremes
    from minmax import contains_imaginary
    from minmax import check_list
    from minmax import check_input
    import pytest
    findextremes_Output1 = findextremes([0, -1.5, -2, -7, -53])
    findextremes_Output2 = findextremes([0, 3.2, 2, 10, 6])
    findextremes_Output3 = findextremes([2, -3, 54, 6, 10])
    assert findextremes_Output1 == [-53.0, 0.0]
    assert findextremes_Output2 == [0, 10]
    assert findextremes_Output3 == [-3.0, 54.0]

    def test_imaginary_input():
        with pytest.raises(ValueError):
            findextremes([3+2j, 4])

    def test_empty_input():
        with pytest.raises(TypeError):
            findextremes([])

    def test_non_list_in():
        with pytest.raises(TypeError):
            findextremes('Hello World')
