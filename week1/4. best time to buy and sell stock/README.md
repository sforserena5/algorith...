# Best Time To Buy And Sell Stock

- **Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/]

## 🕒 Trials

- **Trial 1:** Accepted 

    from typing import List

    class Solution:
        def maxProfit(self, prices: List[int]) -> int: # prices = [7,1,5,3,6,4]
            min_price = float('inf')  # 매수 / 실제 가격이 와도 무조건 갱신되도록 말도 안 되게 큰 값으로 세팅
            max_profit = 0            # 매도 / 지금까지의 최대 이익

            for price in prices:
                if price < min_price:
                    min_price = price
                else:
                    max_profit = max(max_profit, price - min_price)

            return max_profit



## 💡 Approach
    prices를 한번만 돌기 위해서 max와 min의 세팅을 의도적으로 역으로 세팅함

## ⏱️ Time Complexity

    O(n)    

## ✍️ Review

- Why did I choose this approach?
매수와 매도의 순서를 유지하면서 최대 이익을 구하기 위해, 배열을 한 번만 순회하며 최저가를 갱신하는 풀이를 선택했다.

- Any mistakes or improvements made during the process?