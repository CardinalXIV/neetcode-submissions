class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create 2 pointers to show a sliding window, one max one min
        maxPrice = 0
        minPrice = prices[0] # don't set to 0 else will never update

        profit = maxPrice - minPrice

        # for each stock price in the list if there is a price higher/lower 
        # than the current max or min price pointers, update it
        # need to know how to update the prices based on the day whether before or after
        for stockprice in range(len(prices)):
            if prices[stockprice] < minPrice:
                minPrice = prices[stockprice]
            # if the current day profit > previous day, then update max price & profit
            if (prices[stockprice] - minPrice) > profit:
                maxPrice = prices[stockprice]
                profit = maxPrice - minPrice

        # return the profit if exists:
        if profit > 0:
            return profit
        else:
            return 0