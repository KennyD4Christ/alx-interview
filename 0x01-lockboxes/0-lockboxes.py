#!/usr/bin/python3

"""
Module for determining if all boxes can be unlocked.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Parameters:
    boxes (List[List[int]]): A list of lists where each list
    contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    queue = deque([0])  # Start with the first box

    while queue:
        box_index = queue.popleft()
        if not visited[box_index]:
            visited[box_index] = True
            for key in boxes[box_index]:
                if not visited[key]:
                    queue.append(key)

    return all(visited)
