def merge_sorted_lists(given_list): # Create a function
    if len(given_list) <= 1:  # In best case the list has 0 or 1 element.
        return given_list
    
    middle = len(given_list)// 2  # Split the list into two parts.
 
    # Recursively sort both halves. 
    left = merge_sorted_lists(given_list[:middle])
    right = merge_sorted_lists(given_list[middle:])
    sorted_list = []  # Store the final merge and sorted result.
    i = j = 0  # Indexes of left and right halves.

    while i < len(left) and j < len(right):
        if left[i] < right[j]:  # Compare the elements from both lists.
            sorted_list.append(left[i])  # Add the smaller ones to the sorted_list.
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # These steps for the left over elements, halves might have different number of elements.
    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1
    return sorted_list  # Return the sorted list
    
mylist = [1, 56, 23, -45, 7, 13, 74, 85, 34, 12, -3]  # Create a list
print(f"sorted array is: {merge_sorted_lists(mylist)}")  # Print your list
