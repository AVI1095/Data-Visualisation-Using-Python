# Take input Name roll Addr and Print it. For multiple studententry, use lists, use dictionaries. Add Update Delete student records.


def studententry():
    students = []
    while True:
        name = input("Name: ")
        roll = input("Roll no: ")

        student = {
            "name": name,
            "roll": roll
        }

        students.append(student)

        add = input("add more:").casefold()
        if add != "y" and add != "yes":
            break

    print("student list:\n")
    for student in  students:
        print(student)

    while True:
        remove_stu = input("roll no of student to be deleted:")
        for student in students:
            if student["roll"] == remove_stu:
                students.remove(student)
                break
        else:
            print("student not found")
        choice = input("continue deleting? (y/n): ").casefold()
        if choice != "y" and choice != "yes":
            break
    for student in students:
        print(student)

    while True:
        update_stu = input("roll no of student whose details to be updated:")
        for student in students:
            if student["roll"] == update_stu:
                new_name = input("new name: ")
                now_roll = input("new roll no: ")
                student["name"] = new_name
                student["roll"] = now_roll
                break
        else:
            print("student not found")
        choice_upd = input("continue updating? (y/n): ").casefold()
        if choice_upd != "y" and choice_upd != "yes":
            break
    for student in students:
        print(student)

studententry()