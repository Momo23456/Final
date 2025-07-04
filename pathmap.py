import numpy as np
import heapq

N = 30  # grid size
hazards = np.zeros((N, N))
crowd = np.zeros((N, N))

def get_cost(pos):
    x, y = pos
    return 1 + hazards[x, y] + crowd[x, y]

def pathmap(start):
    dist = np.full((N, N), np.inf)
    visited = np.zeros((N, N), dtype=bool)
    prev = np.full((N, N, 2), -1)
    
    hq = [(0, start)]
    dist[start] = 0
    
    while hq:
        d, (x, y) = heapq.heappop(hq)
        if visited[x, y]: continue
        visited[x, y] = True
        
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N:
                cost = get_cost((nx, ny))
                if dist[nx, ny] > dist[x, y] + cost:
                    dist[nx, ny] = dist[x, y] + cost
                    prev[nx, ny] = [x, y]
                    heapq.heappush(hq, (dist[nx, ny], (nx, ny)))
    
    return dist, prev
