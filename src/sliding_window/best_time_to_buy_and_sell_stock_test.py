from best_time_to_buy_and_sell_stock import best_time_to_buy_and_sell_stock, best_time_to_buy_and_sell_stock_exceed_time


def test_best_time_to_buy_and_sell_stock_exceed_tim():
    assert best_time_to_buy_and_sell_stock_exceed_time([7, 1, 5, 3, 6, 4]) == 5
    assert best_time_to_buy_and_sell_stock_exceed_time([7, 6, 4, 3, 1]) == 0
    assert best_time_to_buy_and_sell_stock_exceed_time(
        [7, 2, 5, 3, 1, 6, 8, 4]) == 7


def test_best_time_to_buy_and_sell_stock():
    assert best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4]) == 5
    assert best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1]) == 0
    assert best_time_to_buy_and_sell_stock([7, 2, 5, 3, 1, 6, 8, 4]) == 7
