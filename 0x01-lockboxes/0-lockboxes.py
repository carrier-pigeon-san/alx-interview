#!/usr/bin/python3
"""
Module 0-lockboxes
This module contains a function that determines if all the boxes can be opened.

Functions:
    canUnlockAll(boxes): Determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """Determines if all the boxes can be unlocked."""
    rack = [0]
    for key in rack:
        for box_key in boxes[key]:
            if box_key not in rack and box_key < len(boxes):
                rack.append(box_key)
    return len(rack) == len(boxes)
