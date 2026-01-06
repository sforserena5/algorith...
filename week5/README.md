# 📅 Week 5: Tree, Heap, and Trie

다섯 번째 주차의 주제는 계층적 데이터 구조인 **Tree**, 우선순위를 효율적으로 관리하는 **Heap**, 그리고 문자열 검색에 최적화된 **Trie**입니다. 재귀적 사고방식을 강화하고 데이터의 순서와 우선순위를 다루는 능력을 기릅니다.

## 🎯 Learning Goals

* **트리의 재귀적 구조 이해:** 트리의 재귀적 정의를 이해하고, 전위/중위/후위 순회(Traversal)를 자유자재로 구현하여 데이터를 탐색할 수 있다.
* **BST의 효율성 활용:** 이진 탐색 트리(BST)의 정렬된 특성을 이용하여 검색, 삽입, 삭제 연산을 최적화된 시간 복잡도로 수행할 수 있다.
* **힙과 우선순위 큐:** 힙(Heap)의 반정렬 상태(Heap Property)를 이해하고, 우선순위 큐를 활용해 최댓값이나 최솟값을 $O(\log n)$의 성능으로 추출한다.
* **트라이(Trie) 구조 파악:** 문자열의 접두사(Prefix)를 공유하는 트라이 구조를 이해하고, 대량의 문자열 탐색 및 자동완성 로직을 설계한다.

---

## 🔍 Self-Study Keywords

문제를 풀기 전, 다음 키워드들을 충분히 검색하고 공부하세요.

* **Binary Tree Traversal:** DFS 기반의 순회 방식과 BFS(Level-order) 방식의 차이.
* **Binary Search Tree (BST):** 왼쪽 자식 < 부모 < 오른쪽 자식의 속성과 불균형 트리(Skewed Tree).
* **Binary Heap:** 배열을 이용한 완전 이진 트리 구현 및 Heapify 과정.
* **Serialization & Deserialization:** 계층적 트리 구조를 선형적인 데이터(String/Array)로 변환하는 기법.
* **Prefix Tree (Trie):** 각 노드가 문자를 저장하는 트리의 변형과 메모리 효율성.

---

## 📝 Exercises

| 순번 | 문제 제목 (Problem Title) | 난이도 | 리트코드 링크 (LeetCode Link) |
| --- | --- | --- | --- |
| 1 | Maximum Depth of Binary Tree | Easy | [leetcode.com/problems/maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| 2 | Diameter of Binary Tree | Easy | [leetcode.com/problems/diameter-of-binary-tree](https://leetcode.com/problems/diameter-of-binary-tree/) |
| 3 | Longest Univalue Path | Medium | [leetcode.com/problems/longest-univalue-path](https://leetcode.com/problems/longest-univalue-path/) |
| 4 | Invert Binary Tree | Easy | [leetcode.com/problems/invert-binary-tree](https://leetcode.com/problems/invert-binary-tree/) |
| 5 | Merge Two Binary Trees | Easy | [leetcode.com/problems/merge-two-binary-trees](https://leetcode.com/problems/merge-two-binary-trees/) |
| 6 | Balanced Binary Tree | Easy | [leetcode.com/problems/balanced-binary-tree](https://leetcode.com/problems/balanced-binary-tree/) |
| 7 | Convert Sorted Array to BST | Easy | [leetcode.com/problems/convert-sorted-array-to-binary-search-tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) |
| 8 | BST to Greater Sum Tree | Medium | [leetcode.com/problems/binary-search-tree-to-greater-sum-tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/) |
| 9 | Range Sum of BST | Easy | [leetcode.com/problems/range-sum-of-bst](https://leetcode.com/problems/range-sum-of-bst/) |
| 10 | Minimum Distance Between BST Nodes | Easy | [leetcode.com/problems/minimum-distance-between-bst-nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/) |
| 11 | Serialize and Deserialize Binary Tree | Hard | [leetcode.com/problems/serialize-and-deserialize-binary-tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) |
| 12 | Construct Tree from Preorder and Inorder | Medium | [leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |
| 13 | Minimum Height Trees | Medium | [leetcode.com/problems/minimum-height-trees](https://leetcode.com/problems/minimum-height-trees/) |
| 14 | Lowest Common Ancestor of a Binary Tree | Medium | [leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) |
| 15 | Kth Largest Element in an Array | Medium | [leetcode.com/problems/kth-largest-element-in-an-array](https://leetcode.com/problems/kth-largest-element-in-an-array/) |
| 16 | Merge k Sorted Lists | Hard | [leetcode.com/problems/merge-k-sorted-lists](https://leetcode.com/problems/merge-k-sorted-lists/) |
| 17 | Find Median from Data Stream | Hard | [leetcode.com/problems/find-median-from-data-stream](https://leetcode.com/problems/find-median-from-data-stream/) |
| 18 | Implement Trie (Prefix Tree) | Medium | [leetcode.com/problems/implement-trie-prefix-tree](https://leetcode.com/problems/implement-trie-prefix-tree/) |
| 19 | Palindrome Pairs | Hard | [leetcode.com/problems/palindrome-pairs](https://leetcode.com/problems/palindrome-pairs/) |
