from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: # prices = [7,1,5,3,6,4]
        min_price = float('inf')  # 매수 / inf=infinite, 지금까지의 최저가 / 실제 가격이 와도 무조건 갱신되도록 의도적으로 말도 안 되게 큰 값으로 시작
        max_profit = 0            # 매도－매수 / 지금까지의 최대 이익

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit