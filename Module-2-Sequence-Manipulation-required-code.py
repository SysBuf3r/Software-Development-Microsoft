animals_list = ['cat', 'Fish', 'Yara', 'Bear']


def list_o_matic():
#    str_inp = input("Please enter an animal name to check it on the list: ")
    if inp == '':
        animals_list.pop()
        print("Popped", animals_list)
        return animals_list
    if inp in animals_list:
        animals_list.remove(inp)
        print("Removed", animals_list)
        return "Removed"
    else:
        animals_list.append(inp)
        print("the list", animals_list)
        return "Appended"


inp = input('Enter the name of an animal or "quit": ')
print("Look at all the animals: ", animals_list)
if len(animals_list) == 0:
    print("List empty")
if inp == "quit":
    print("Quitting! ")
else:
    print("Entering list")
    list_o_matic()
