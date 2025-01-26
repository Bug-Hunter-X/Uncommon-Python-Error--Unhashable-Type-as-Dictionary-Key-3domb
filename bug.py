def function_with_uncommon_bug(data):
    try:
        # Assume 'data' is a dictionary-like object
        result = data['key']
        return result
    except KeyError:
        # Common error handling
        return None
    except TypeError as e:
        # This might be uncommon
        if 'unhashable type' in str(e):
            print("Uncommon error: unhashable type encountered.")
            return None
        else:
            raise e #re-raise other TypeErrors

# Example showing the uncommon error
data = {1: 'value1', 2: 'value2'}
print(function_with_uncommon_bug(data))  #Output: value1

data = { [1,2]: 'value3'}
print(function_with_uncommon_bug(data)) #Output: Uncommon error: unhashable type encountered.
None