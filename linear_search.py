def linear_search(list_to_search, target):
    """
    Performs a linear search through a list to find target value
    Returns the index if found, -1 if not found
    """
    for i in range(len(list_to_search)):
        if list_to_search[i] == target:
            return i
    return -1

# Example usage
my_list = [5, 2, 8, 1, 9, 3]
search_value = 8

result = linear_search(my_list, search_value)

if result != -1:
    print(f"Value {search_value} found at index {result}")
else:
    print(f"Value {search_value} not found in list")