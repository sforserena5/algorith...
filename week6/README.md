# 📅 Week 6: Sorting Algorithm & Binary Search Algorithm

여섯 번째 주차의 주제는 데이터를 체계적으로 나열하는 **Sorting(정렬)**과 정렬된 데이터의 이점을 극대화하여 검색 속도를 혁신적으로 줄이는 **Binary Search(이진 탐색)**입니다. 다양한 상황에 맞는 최적의 정렬 방식을 선택하고, 로그 시간 복잡도()의 효율성을 실전 문제에 적용합니다.

## 🎯 Learning Goals

* **정렬 알고리즘의 분석:** 다양한 정렬 알고리즘(Merge, Quick, Heap, Bubble 등)의 시간/공간 복잡도를 비교하고, 동일한 값의 상대적 순서를 보존하는 **안정성(Stability)**의 개념과 트레이드오프를 설명할 수 있다.
* **이진 탐색의 응용 및 경계 탐색:** 단순한 값 찾기를 넘어, 중복 데이터가 존재하는 배열에서 특정 값의 시작 지점과 끝 지점을 찾는 **Lower Bound** 및 **Upper Bound** 로직을 설계하고 구현할 수 있다.
* **정렬 상태와 효율성 분석:** 데이터가 "정렬된 상태"일 때 검색 및 가공 효율이 어떻게 변화하는지 파악하고, 문제 해결을 위해 데이터를 미리 정렬해야 하는 상황을 판단할 수 있다.

---

## 🔍 Self-Study Keywords

문제를 풀기 전, 다음 키워드들을 충분히 검색하고 공부하세요.

* **Stable vs Unstable Sort:** 정렬 후 동일한 키 값을 가진 요소들의 순서 유지 여부.
* **Timsort:** 파이썬의 기본 정렬 알고리즘()이자 실무에서 널리 쓰이는 하이브리드 정렬 방식.
* **Binary Search Range:** `left`, `right` 포인터 이동 조건과 무한 루프 방지를 위한 중간값() 계산법.
* **Search in Rotated Array:** 정렬된 배열이 회전되었을 때(특정 지점에서 꺾일 때) 이진 탐색을 적용하는 논리.
* **Two Pointers on Sorted Array:** 정렬된 상태를 활용해 두 수의 합이나 접점을 찾는 기법.

---

## 📝 Exercises

### Part 1: Sorting Algorithms (7문제)

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 1 | Sort List | Medium | [leetcode.com/problems/sort-list](https://leetcode.com/problems/sort-list/) |
| 2 | Insertion Sort List | Medium | [leetcode.com/problems/insertion-sort-list](https://leetcode.com/problems/insertion-sort-list/) |
| 3 | Largest Number | Medium | [leetcode.com/problems/largest-number](https://leetcode.com/problems/largest-number/) |
| 4 | Valid Anagram | Easy | [leetcode.com/problems/valid-anagram](https://leetcode.com/problems/valid-anagram/) |
| 5 | Merge Intervals | Medium | [leetcode.com/problems/merge-intervals](https://leetcode.com/problems/merge-intervals/) |
| 6 | Sort Colors | Medium | [leetcode.com/problems/sort-colors](https://leetcode.com/problems/sort-colors/) |
| 7 | K Closest Points to Origin | Medium | [leetcode.com/problems/k-closest-points-to-origin](https://leetcode.com/problems/k-closest-points-to-origin/) |

### Part 2: Binary Search (7문제)

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 8 | Binary Search | Easy | [leetcode.com/problems/binary-search](https://leetcode.com/problems/binary-search/) |
| 9 | Find First and Last Position of Element in Sorted Array | Medium | [leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |
| 10 | Search in Rotated Sorted Array | Medium | [leetcode.com/problems/search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |
| 11 | Find Minimum in Rotated Sorted Array | Medium | [leetcode.com/problems/find-minimum-in-rotated-sorted-array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) |
| 12 | Intersection of Two Arrays | Easy | [leetcode.com/problems/intersection-of-two-arrays](https://leetcode.com/problems/intersection-of-two-arrays/) |
| 13 | Two Sum II - Input Array Is Sorted | Medium | [leetcode.com/problems/two-sum-ii-input-array-is-sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| 14 | Search a 2D Matrix II | Medium | [leetcode.com/problems/search-a-2d-matrix-ii](https://leetcode.com/problems/search-a-2d-matrix-ii/) |
