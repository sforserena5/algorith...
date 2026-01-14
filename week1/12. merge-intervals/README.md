# Merge Intervals

- **Link:** [https://leetcode.com/problems/merge-intervals/]

## 🕒 Trials

- **Trial 1:** Accepted..

    class Solution:
        def merge(self, intervals: List[List[int]]) -> List[List[int]]:

            # 1. 정렬하고 시작
            intervals.sort(key=lambda x: x[0]) # "리스트 각요소의 첫번째 값"을 기준으로 sort
            # intervals = [[4,7],[1,4]] -> [[1,4], [4,7]]
            merged = [intervals[0]] # [[4,7]] 하나를 넣고 시작해야함

            # 2. 하나씩 보면서 합치기
            for start, end in intervals[1:]: # (첫번째반복) start = 1, end = 4
                last_start, last_end = merged[-1] # merged는 [[4,7]]이므로, last_start = 4,      last_end = 7    

                # overlapping case
                if last_end >= start:
                    merged[-1][1] = max(last_end, end)
                else:
                    merged.append([start, end])

            return merged

## 💡 Approach  
    먼저 정렬한 후, 앞에서부터 하나씩 보면서 이전 구간과 겹치는지 확인했다.
## ⏱️ Time Complexity
    O(n log n)

## ✍️ Review
- Why did I choose this approach?
    한 번의 순회로 모든 구간을 처리할 수 있어 효율적임