def get_last_element(lst: list):
    # print(lst[-1])
    print(lst[len(lst) -1])

def get_list():
    list = []
    elem = input("Please Enter an element of the list or press enter to stop.")
    while elem != "":
        list.append(elem)
        elem = input("Please Enter an element of the list or press enter to stop.")
    return list

def main():
    list = get_list()
    get_last_element(list)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()