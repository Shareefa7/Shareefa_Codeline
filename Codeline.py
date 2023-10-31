def display_menu():
    print("Welcome to the Menu-Based Program!")
    print("Please select an option:")
    print("1. Print Pattern")
    print("2. Rotate Array")
    print("3. Help")
    print("4. Exit")

def print_pattern():
    print("--- You Have selected Print Pattern ---")
    n = int(input("Enter the number of rows for the pattern: "))
    if n <= 0:
        print("Please enter a vaild number.")
    else:
        for i in range(n, 0, -1):
            print('* ' * i)

def rotate_array():
    print("--- You have selected Rotate Array ---")
    n = int(input("Enter the number of elements (n): "))
    k = int(input("Enter the number of steps (k): "))
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

    if n != len(arr):
        print("Number of elements doesn't match the array length.")
        return

    rotated_arr = arr[-k:] + arr[:-k]
    print("Output:", rotated_arr)

def help_option():
    print("--- Help ---")
    print("Option 1: Print a pattern with 'n' rows of decreasing asterisks.")
    print("Option 2: Rotate an array of 'n' elements to the right by 'k' steps.")
    print("Option 3: Display this help message.")
    print("Option 4: Exit the program.")


def main():
    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == '1':
            print_pattern()
        elif choice == '2':
            rotate_array()
        elif choice == '3':
            help_option()
        elif choice == '4':
            print("Exiting the program. Goodbye! ")
            print("Shareefa Humood Al-Nadabi.. ")

            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")
            
if __name__ == "__main__":
    main()
