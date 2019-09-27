#   a117_grades.py
#   This code is incomplete.
my_courses = ["spanish", "chemistry", "CS", "english", "choir", "band", "geometry"]

for course in my_courses:
    print()
    print("enter your points for " + course)

    a = int(input("points -> "))
    if (a >= 90):
        print("A")
    elif (a >= 80):
        print("B")
    elif (a >= 70):
        print("C")
    elif (a >= 60):
        print("D")
    else:
        print("F")

check_grades = True
while (check_grades):
    redo = input("do you need to re-do these grades? (y/n)")
    if (redo == "y"):
        check_grades = True
    else:
        check_grades = False 