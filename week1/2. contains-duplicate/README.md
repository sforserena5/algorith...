# Contains Duplicate

- **Link:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

## 🕒 Trials

- **Trial 1:** Accepted but.. 길이가 최대 10^5이기 때문에 이중 for문은 시간 초과 날 가능성이 있음

    from typing import List

    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            i = len(nums) 
            for a in range(0,i):
                for b in range (a+1, i):
                    if nums[a] == nums [b]:
                        return True
                return False

- **Trial 2:** Accepted but.. 리스트를 사용한 중복 검사로 인해 최악의 경우 O(n^2)....

    from typing import List

    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            blank = []
            for a in nums:
                if a in blank: # 문제의 부분...
                    return True
                else:
                    blank.append(a)
            return False
    
- **Trial 3:** Accepted

## 💡 Approach

중복 여부를 효율적으로 확인하기 위해 set 자료구조를 사용함. num을 순회하면서 각 원소가 이미 set에 존재하는지 확인함.Leetcode 케이스 3가지 모두 통과함.

## ⏱️ Time Complexity

O(n)

## ✍️ Review

- Why did I choose this approach?
해당 숫자가 리스트 안에 있는지 여부(True/False)만 판단하면 되기 때문에 여러개의 조합을 이중 for문을 활용해 일일이 찾는 것은 비효율적이라는 생각이 들었음

- Any mistakes or improvements made during the process?
리스트와 달리, set는 존재여부 확인이 빠르다는 것을 새롭게 알게 되었음
    리스트 = 순서 O, 중복 O, 검색 느림 (인덱스 문제에 유리)
    세트 = 순서 X, 중복 X, 검색 빠름 (중복 검사 문제에 유리)