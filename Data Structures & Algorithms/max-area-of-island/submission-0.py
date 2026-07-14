class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxarea = 0
        def bfs(r, c):
            area = 0
            q = collections.deque()
            visit.add((r,c))
            q.append((r, c))
            while q:
                row, col = q.popleft()
                area += 1
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and
                    nc in range(cols) and 
                    grid[nr][nc] == 1 and
                    (nr,nc) not in visit):
                        q.append((nr, nc))
                        visit.add((nr, nc))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    maxarea = max(maxarea, bfs(r, c))
        return maxarea