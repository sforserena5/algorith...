from typing import List

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

            # 다음 칸이 범위를 벗어나거나, 이미 갔으면 방향 전환
            if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                d = (d + 1) % 4
                nr = r + directions[d][0]
                nc = c + directions[d][1]

            r, c = nr, nc

        return res
