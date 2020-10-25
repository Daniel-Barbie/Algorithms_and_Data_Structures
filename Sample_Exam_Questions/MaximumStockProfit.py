def maximum_stock_profit(prices, k):
    if k == 0:
        return 0
    maximum_profit = 0
    # last entry of range(0,len(prices)) is actually len(prices)-1 ! -> because of python slicing! (list_[1:5] only slices objects with index 1-4 !)
    for i in range(0, len(prices)-1):
        for j in range(i+1, len(prices)):
            combined_profit = 0
            current_profit = prices[j] - prices[i]
            if current_profit > 0:
                combined_profit = current_profit + maximum_stock_profit(prices[j+1:], k-1)
                if combined_profit > maximum_profit:
                    maximum_profit = combined_profit
    return maximum_profit


stock_prices_1 = [3, 2, 6, 5, 0, 3]
print(maximum_stock_profit(stock_prices_1, 2))
