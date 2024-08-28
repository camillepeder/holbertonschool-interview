#!/usr/bin/python3
"""
Task for interview preparation: lockboxes algorithm
"""


def canUnlockAll(boxes):

    # if the first box is empty
    if len(boxes[0]) < 1:
        return False
    flag = True
    # Dictionary to track open boxes
    toBeOpened = {}
    for x in range(len(boxes)):
        toBeOpened[x] = False
    toBeOpened[0] = True

    # Store keys on an array and a copy
    keys = boxes[0]

    # Iterate the keys
    for key in keys:
        # If the key can open a box
        if key in toBeOpened:

            # If the box is not already open
            if not toBeOpened[key]:
                toBeOpened[key] = True

                # Add the keys from the newly open box to the keys array
                for newKey in boxes[key]:
                    if 0 < newKey <= len(boxes) and newKey not in keys:
                        keys.append(newKey)

    # Check if all the boxes have been opened
    for key in toBeOpened:

        # In case a box is not open, the return flag will be false
        if not toBeOpened[key]:
            flag = False
    return flag
