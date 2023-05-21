class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        
        # DFS paint the first island to 2
        def paint(x: int, y: int) -> None:
            grid[x][y] = 2
            q.append((x, y))
            for dx, dy in directions:
                nx, ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1:
                    paint(nx, ny)
                    
        def init() -> None:
            for i in range(N):
                for j in range(N):
                    if grid[i][j]:
                        paint(i, j)
                        return
                    
        init()
        
        # BFS level order traversal
        level = 0
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 2:
                        q.append((nx, ny))
                        if grid[nx][ny] == 1:
                             return level
                        grid[nx][ny] = 2
            level += 1

        return -1