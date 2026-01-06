# 📅 Week 7: Advanced Algorithms

마지막 주차의 주제는 **Advanced Algorithms**입니다. 슬라이딩 윈도우를 통한 효율적인 구간 관리, 그리디의 최적 선택, 분할 정복의 논리적 분해, 그리고 동적 계획법(DP)의 최적화 기법을 학습하며 복잡한 문제를 해결하는 통찰력을 기릅니다.

---

## 🎯 Learning Goals

* **그리디(Greedy)의 정당성 확보:** 매 순간의 최선이 전체의 최적해가 되는 **탐욕적 선택 속성(Greedy Choice Property)**과 **최적 부분 구조(Optimal Substructure)**를 이해하고, 알고리즘의 정당성을 논리적으로 증명할 수 있다.
* **분할 정복(Divide & Conquer)적 사고:** 거대한 문제를 독립적인 하위 문제로 분할하여 해결하고 다시 병합하는 사고방식을 익혀 복잡도를 낮춘다.
* **동적 계획법(DP) 최적화:** 중복되는 하위 문제(Overlapping Subproblems)를 해결하기 위해 **'상태 정의'**와 **'점화식 세우기'**를 수행하고, 메모이제이션(Memoization) 혹은 타뷸레이션(Tabulation)을 통해 계산 효율을 극대화한다.

---

## 🔍 Self-Study Keywords

문제를 풀기 전, 다음 키워드들을 충분히 검색하고 공부하세요.

* **Sliding Window:** 윈도우의 시작과 끝을 조절하며 구간의 상태를 유지하는 법.
* **Greedy vs DP:** 매 단계의 최선(Greedy)과 모든 가능성을 고려한 최적(DP)의 차이.
* **Overlapping Subproblems:** 동일한 작은 문제가 반복해서 계산되는 구조 파악.
* **Memoization:** 하향식(Top-down) 접근과 계산 결과 저장.
* **Tabulation:** 상향식(Bottom-up) 접근과 DP 테이블 채우기.

---

## 📝 Exercises

### Part 1: Sliding Window (3문제)

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 1 | Sliding Window Maximum | Hard | [leetcode.com/problems/sliding-window-maximum](https://leetcode.com/problems/sliding-window-maximum/) |
| 2 | Minimum Window Substring | Hard | [leetcode.com/problems/minimum-window-substring](https://leetcode.com/problems/minimum-window-substring/) |
| 3 | Longest Repeating Character Replacement | Medium | [leetcode.com/problems/longest-repeating-character-replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) |

### Part 2: Greedy Algorithm (5문제)

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 4 | Best Time to Buy and Sell Stock II | Medium | [leetcode.com/problems/best-time-to-buy-and-sell-stock-ii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/) |
| 5 | Assign Cookies | Easy | [leetcode.com/problems/assign-cookies](https://leetcode.com/problems/assign-cookies/) |
| 6 | Queue Reconstruction by Height | Medium | [leetcode.com/problems/queue-reconstruction-by-height](https://leetcode.com/problems/queue-reconstruction-by-height/) |
| 7 | Task Scheduler | Medium | [leetcode.com/problems/task-scheduler](https://leetcode.com/problems/task-scheduler/) |
| 8 | Gas Station | Medium | [leetcode.com/problems/gas-station](https://leetcode.com/problems/gas-station/) |

### Part 3: Divide-and-Conquer (2문제)

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 9 | Majority Element | Easy | [leetcode.com/problems/majority-element](https://leetcode.com/problems/majority-element/) |
| 10 | Different Ways to Add Parentheses | Medium | [leetcode.com/problems/different-ways-to-add-parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/) |

### Part 4: Dynamic Programming (6문제)

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 11 | Fibonacci Number | Easy | [leetcode.com/problems/fibonacci-number](https://leetcode.com/problems/fibonacci-number/) |
| 12 | Climbing Stairs | Easy | [leetcode.com/problems/climbing-stairs](https://leetcode.com/problems/climbing-stairs/) |
| 13 | Maximum Subarray | Medium | [leetcode.com/problems/maximum-subarray](https://leetcode.com/problems/maximum-subarray/) |
| 14 | House Robber | Medium | [leetcode.com/problems/house-robber](https://leetcode.com/problems/house-robber/) |
| 15 | Coin Change | Medium | [leetcode.com/problems/coin-change](https://leetcode.com/problems/coin-change/) |
| 16 | Longest Increasing Subsequence | Medium | [leetcode.com/problems/longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) |
