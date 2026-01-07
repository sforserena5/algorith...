# Two Sum

- **Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## 🕒 Trials

- **Trial 1:** Accepted

## 💡 Approach

num 배열의 정수 2개 조합을 효율적으로 카운트하기 위해서, 2가지 변수를 활용한 이중 for문을 사용해 모든 가능한 조합을 검사함. Leetcode 케이스 3가지 모두 통과함.

## ⏱️ Time Complexity

O(n^2)

이중 for문을 사용하기 때문

## ✍️ Review

- Why did I choose this approach?
같은 인덱스는 중복 사용하지 않기 위해 두 번째 반복문은 첫 번째 인덱스의 다음 위치인 a+1부터 시작함.
주어진 조건을 만족하는 인덱스를 반환하도록 구현함

- Any mistakes or improvements made during the process?
