# Spiral-Matrix

- **Link:** [https://leetcode.com/problems/spiral-matrix/description/]

## 🕒 Trials

- **Trial 1:** Accepted..gpt 도움 받음!
    class Solution:
        def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

            m, n = len(matrix), len(matrix[0])
            visited = [[False] * n for _ in range(m)]

            # 오른쪽, 아래, 왼쪽, 위
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            d = 0  # 방향 인덱스

            r = c = 0
            res = []

            for _ in range(m * n):
                res.append(matrix[r][c])
                visited[r][c] = True

                nr = r + directions[d][0]
                nc = c + directions[d][1]

                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    d = (d + 1) % 4
                    nr = r + directions[d][0]
                    nc = c + directions[d][1]

                r, c = nr, nc

            return res


## 💡 Approach
    행렬을 오른쪽, 아래, 왼쪽, 위 방향으로 이동하면서 가지 않은 칸을 순서대로 탐색했다.

## ⏱️ Time Complexity
    O(n)

## ✍️ Review
- Why did I choose this approach?
    이동방향만 숫자로 생각하면 되므로 로직이 간단함   