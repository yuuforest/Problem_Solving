
""" 골드 5. 강의실 배정 """

import sys
from heapq import heappush, heappop

def solution():
    input = sys.stdin.readline

    N = int(input())

    meeting = []
    for _ in range(N):
        start, end = map(int, input().split())
        meeting.append((start, end))

    meeting.sort()

    room = []
    heappush(room, meeting[0][1])
    for (start, end) in meeting[1:]:
        if start < room[0]:
            heappush(room, end)
        else:
            heappop(room)
            heappush(room, end)

    return len(room)
    
print(solution())