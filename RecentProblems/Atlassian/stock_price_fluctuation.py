"""
2034. Stock Price Fluctuation 

You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. 
Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.
 

Example 1:

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
 

Constraints:

1 <= timestamp, price <= 109
At most 105 calls will be made in total to update, current, maximum, and minimum.
current, maximum, and minimum will be called only after update has been called at least once.
"""

# class Node: 
    
#     def __init__

import heapq
class StockPrice(object):

    def __init__(self):
        self.max_timestamp = 0
        self.time_prices = {} # time -> (price, orig_insert_order)
        self.prices = []
        self.prices_heap = []

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp > self.max_timestamp: 
            self.max_timestamp = timestamp

        if timestamp in self.time_prices:
            _, ord = self.time_prices[timestamp]
            self.prices[ord] = price 
            self.time_prices[timestamp] = (price, ord)

        else:
            self.prices.append(price)
            self.time_prices[timestamp] = (price, len(self.prices) -1)

        self.prices_heap = self.prices.copy()
        heapq.heapify(self.prices_heap)


    def current(self):
        """
        :rtype: int
        """
        return self.time_prices[self.max_timestamp][0]
        

    def maximum(self):
        """
        :rtype: int
        """
        return heapq.nlargest(1, self.prices_heap)[0]
        

    def minimum(self):
        """
        :rtype: int
        """
        return heapq.nsmallest(1, self.prices_heap)[0]
    
elf.time_prices[timestamp] = (price, ord)
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


def test_stock_price():
    print("Testing code")

    sol = StockPrice()
    sol.update(1, 20)

    assert sol.current() == 20, f"{sol.current()} is not 20"

    assert sol.maximum() == 20, f"{sol.maximum()} is not 20"

    assert sol.minimum ()== 20

    sol.update(2,5)

    sol.update(1, 30)

    assert sol.minimum() == 5, f"{sol.minimum()} is not 5"

    assert sol.current() == 5

    sol.update(2, 20)

    assert sol.maximum() == 30, f"{sol.maximum()} is not 30"

    assert sol.minimum() == 20, f"{sol.minimum()} is not 5"

    sol.update(5,100)

    sol.update(4, 10)

    assert sol.maximum() == 100 

    assert sol.current() == 100

test_stock_price()