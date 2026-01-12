# Move Zeroes

- **Link:** [https://leetcode.com/problems/move-zeroes/]

## 🕒 Trials

- **Trial 1:** Accepted but.. for > while > for, 이렇게 리스트를 3번이나 훑다보니 비효율적이며, while 속에 remove로 인해 시간 복잡도가 O(n2^)

    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            count = 0
            for num in nums:
                if num == 0:
                    count +=1
                else:
                    pass

            while 0 in nums:
                nums.remove(0)
            
            for i in range(count):
                nums.append(0)
                
    // 1. 0의 개수를 센다
    // 2. 리스트에서 0을 하나씩 지운다
    // 3. 0 개수만큼 뒤에 붙인다

- **Trial 2:** Accepted

    class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            idx = 0  # 다음에 non-zero가 들어갈 위치

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[idx] = nums[i]
                    idx += 1

            # 남은 자리를 0으로 채우기
            for i in range(idx, len(nums)):
                nums[i] = 0

    
- **Trial 3:** Accepted

## 💡 Approach
remove 대신 index를 활용해 덮어쓰기를 함.
내부에서 이동(밀기, 찾기 등)할 필요 없이 가능함.  
Leetcode 케이스 2가지 모두 통과함.

## ⏱️ Time Complexity

O(n)

## ✍️ Review

- Why did I choose this approach?
0이 아닌 숫자들 순서는 유지하면서 in-place를 해결하기 위해
읽기/쓰기 포인터를 사용하는 덮어쓰기 방식을 선택했다.
이 방법은 배열을 선형으로 순회하며 효율적으로 값을 재배치할 수 있었다.

- Any mistakes or improvements made during the process?
처음에는 remove를 반복 사용하는 방식으로 시간복잡도가 O(n²) 이었다.
2번째 시도에서는, 0을 제거하는 대신 0이 아닌 값만 앞쪽에 다시 쓰는 방식을 사용했다.