def solution(maps):
    # 준비
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])

    # bfs 함수 만들기
    def bfs(a, b):
        Q = []
        Q.append([a, b])
        while Q:
            x, y = Q.pop(0)
            if x == n - 1 and y == m - 1:
                return maps[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if maps[nx][ny] == 1:
                        Q.append([nx, ny])
                        maps[nx][ny] = maps[x][y] + 1
        return -1

    answer = bfs(0, 0)
    return answer