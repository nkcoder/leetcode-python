

def test_product_of_array_except_self2():
    from product_of_array_except_self import product_of_array_except_self2

    assert product_of_array_except_self2([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_of_array_except_self2([1, 2, 3, 4, 5]) == [
        120, 60, 40, 30, 24]
    assert product_of_array_except_self2([1, 2, 3, 4, 5, 6]) == [
        720, 360, 240, 180, 144, 120]

    assert product_of_array_except_self2([0, 2, 3, 4]) == [24, 0, 0, 0]
    assert product_of_array_except_self2([1, 2, 3, 4, 5, 0]) == [
        0, 0, 0, 0, 0, 120]
    assert product_of_array_except_self2([0, 0, 3, 4, 5, 6]) == [
        0, 0, 0, 0, 0, 0]


def test_product_of_array_except_self():
    from product_of_array_except_self import product_of_array_except_self2

    assert product_of_array_except_self2([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_of_array_except_self2([1, 2, 3, 4, 5]) == [
        120, 60, 40, 30, 24]
    assert product_of_array_except_self2([1, 2, 3, 4, 5, 6]) == [
        720, 360, 240, 180, 144, 120]

    assert product_of_array_except_self2([0, 2, 3, 4]) == [24, 0, 0, 0]
    assert product_of_array_except_self2([1, 2, 3, 4, 5, 0]) == [
        0, 0, 0, 0, 0, 120]
    assert product_of_array_except_self2([0, 0, 3, 4, 5, 6]) == [
        0, 0, 0, 0, 0, 0]
