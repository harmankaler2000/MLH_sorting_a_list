try:
    length = int(input("Enter the Length of the list: "))
    print("Enter the list numbers: ")
    input_list = []
    for i in range(length):
        value = int(input("> "))
        input_list.append(value)
    print("Entered list is: ", input_list)
    input_list.sort()
    print("The sorted list is: ", input_list)
except ValueError:
    print("Invalid Value")