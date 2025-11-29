# Ask user to input his name and print its initials
def initials():
    name = input("enter name: ")
    name_split = name.split()
    print("enter choice: 1. all initials 2.first initials 3.second initials" )
    choice = int(input())
    initials = "".join(n[0] for n in name_split)
    firstname = name_split[0]
    surname = name_split[1]
    if choice == 1:
        print("enter all initials: " + initials)
    if choice == 2:
        print("enter first initials: " + name_split[0][0] +" "+ surname)
    if choice == 3:
        print("enter second initials: " + firstname +" "+ surname[0])
    if choice > 4:
        print("invalid input")
initials()