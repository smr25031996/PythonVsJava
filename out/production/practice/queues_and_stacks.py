#6. Queues and Stacks (Using collections.deque)
#Deque (double-ended queue) provides O(1) operations at both ends.
from collections import deque

# Creating deque
dq = deque([1, 2, 3, 4, 5])
dq = deque(maxlen=5)  # Fixed size, drops oldest when full

# Stack operations (LIFO)
dq.append(1)  # Push to right
dq.append(2)
last = dq.pop()  # Pop from right (2)

# Queue operations (FIFO)
dq.append(1)  # Enqueue to right
dq.append(2)
first = dq.popleft()  # Dequeue from left (1)

# Other operations
dq.appendleft(0)  # Add to left
dq.extend([6, 7])  # Extend right
dq.extendleft([-2, -1])  # Extend left (adds in reverse order)
dq.rotate(2)  # Rotate right by 2
dq.rotate(-1)  # Rotate left by 1


# Example: Sliding window maximum
def sliding_window_max(nums, k):
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        # Remove elements outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements from back
        while dq and nums[dq[-1]] <= num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


print(sliding_window_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]
