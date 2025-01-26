# Uncommon Python Error: Unhashable Type as Dictionary Key

This repository demonstrates an uncommon error in Python that can occur when using unhashable types as keys in dictionaries.  The `bug.py` file contains the erroneous code, while `bugSolution.py` shows how to handle this issue gracefully.

The core issue stems from attempting to use a mutable object (like a list) as a dictionary key.  Dictionaries require hashable keys for efficient lookup. Mutable objects, by nature, cannot be hashed, resulting in a `TypeError` with the message "unhashable type".

This example showcases robust error handling to prevent program crashes and provides informative feedback to the user when the error occurs. This uncommon error is likely to be encountered less frequently than more common exceptions such as `KeyError`.