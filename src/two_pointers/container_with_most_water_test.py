
def test_container_with_most_water0():
    from container_with_most_water import container_with_most_water0

    assert container_with_most_water0([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert container_with_most_water0([1, 1]) == 1
    assert container_with_most_water0([8, 7, 2, 1]) == 7
    

def test_container_with_most_water():
    from container_with_most_water import container_with_most_water

    assert container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert container_with_most_water([1, 1]) == 1
    assert container_with_most_water([8, 7, 2, 1]) == 7