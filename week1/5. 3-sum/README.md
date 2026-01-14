# 3sum

- **Link:** [https://leetcode.com/problems/3sum/]

## 🕒 Trials

- **Trial 1:** Accepted.. but time complexity is O(n^3)

    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            seen = set()
            blank = []
            for i in range (0, len(nums)):
                for j in range (i+1, len(nums)):
                    for k in range(j+1, len(nums)):
                        if nums[i] + nums[j]+ nums[k] ==0:
                            to_tuple = tuple(sorted([nums[i], nums[j], nums[k]]))
                            if to_tuple not in seen: # 여기서 seen으로 중복 거름 
                                seen.add(to_tuple) # 이 add로도 거름!
                                blank.append(list(to_tuple))
            return blank

- **Trial 2:** Accepted..gpt 도움 받음

    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []
            n = len(nums)

            for i in range(n):
                # i 중복 제거
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                # nums[i]가 0보다 크면 뒤도 전부 0보다 크거나 같으므로 합이 0 불가
                if nums[i] > 0:
                    break

                left, right = i + 1, n - 1
                while left < right:
                    s = nums[i] + nums[left] + nums[right]

                    if s == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # left 중복 제거
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # right 중복 제거
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif s < 0:
                        left += 1
                    else:
                        right -= 1

            return res



## 💡 Approach
    nums를 우선 정렬하고, 인덱스 i를 0부터 고정하면서(첫 번째 수) 나머지 두 수는 left=i+1, right=n-1로 두고 합이 0이 되도록 왼쪽과 오른쪽을 좁혀가며 탐색
    중복 값은 스킵해서 결과 중복을 방지
    정렬되어 있으니, 합이 작으면(left++ ) 더 큰 값을 만들고, 합이 크면(right-- ) 더 작은 값을 만든다.
    [결과] 테스트 2개 통과함!

## ⏱️ Time Complexity

    O(n^2)    

## ✍️ Review

- Any mistakes or improvements made during the process?
첫번째 시도법은 문제 입력 범위가 의도하는 알고리즘(O(n²))과 맞지 않음...