"""
Heaps in Python
A heap is a specialized tree-based data structure that satisfies the heap property:
- In a max heap, for any given node N, the value of N is greater than or equal to the values of its children
- In a min heap, for any given node N, the value of N is less than or equal to the values of its children

Python's heapq module implements a min heap by default
"""

import heapq

# under the hood are arrays
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])

while len(minHeap):
    print(heapq.heappop(minHeap))

# No max heaps by deafult, work around is
# to use min heap and multiply by 01 when
# push & pop.
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

# Max is always at index 0
print(-1 * maxHeap[0])

# Build heap from inital values in linear time
arr = [2, 1, 8, 4 ,5]
heapq.heapify(arr)
while arr:
    print(heapq.heappop(arr))