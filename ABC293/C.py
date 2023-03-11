h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]


def dfs(x, y, used):
    if x == h-1 and y == w-1:
        return 1
    cnt = 0
    for dx, dy in ((1, 0), (0, 1)):
        nx, ny = x+dx, y+dy
        if nx < h and ny < w and a[nx][ny] not in used:
            used.add(a[nx][ny])
            cnt += dfs(nx, ny, used)
            used.remove(a[nx][ny])
    return cnt


print(dfs(0, 0, set([a[0][0]])))
