# A bubble sort algorithm based on user input
length = (int)(input("Please enter the length of your list : "))
BubbleList = []
print("Please enter the number you want it")
for i in range(length):
    num = (int)(input(f"Number {i+1} : "))
    BubbleList.append(num)
print(f"Your list is {BubbleList}")
choice = (input("Please enter 'yes' or 'no' if you want your list to be sorted : ")).lower()
if choice == "yes":
    print("\nYour list is going to be sorted by using *Bubble Sort* method")
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if BubbleList[j] > BubbleList[j + 1]:
                BubbleList[j], BubbleList[j + 1] = BubbleList[j + 1], BubbleList[j]
    print(f"Sorted list is : {BubbleList}")
else:
    print("Thanks")
