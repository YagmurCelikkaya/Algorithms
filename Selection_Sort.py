def get_user_input():
    """Gets a list of numbers from the user."""
    while True:
        try:
            count = int(input("Please enter the length of your list: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    selection_list = [] # Create an empty list

    print(f"Please enter {count} numbers:")
    for i in range(count):
        while True:
            try:
                num = int(input(f"Number {i+1}: "))
                selection_list.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
    print(f"Your current list is: {selection_list}")
    return selection_list

# Initialize the list
Select_List = get_user_input()
while True:
    choice = input("\nEnter 'yes' to sort the list, 'no' to re-enter the list, or 'q' to quit: ").lower()
    if choice == "yes":
        print("\nSorting list using *Selection Sort*...")
        n = len(Select_List)
        # Selection Sort Logic
        for i in range(n - 1):
            min_index = i
            for j in range(i + 1, n):
                # Compare elements
                if Select_List[j] < Select_List[min_index]:
                    min_index = j
            
            # Swap the found minimum element with the first element
            if min_index != i:
                Select_List[i], Select_List[min_index] = Select_List[min_index], Select_List[i]
        
        print(f"Sorted array: {Select_List}")
        break # Exit after sorting

    elif choice == "no":
        print("\nOkay, let's start over.")
        Select_List = get_user_input() # Update the list with new input
        
    elif choice == 'q':
        print("Exiting.")
        break
        
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")