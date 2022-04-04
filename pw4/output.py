def get_case():
        print("\n---------------------------")
        print("\n1) Add students")
        print("2) Add courses")
        print("3) Add marks for a course")
        print("4) Show all students")
        print("5) Show all courses")
        print("6) Show all marks in a course")
        print("7)  Sort student list by GPA descending")
        print("-1) ESC")
        num = input("Choose ones : ")
        try :
            num=int(num)
        except:
            num=-404   
        print("---------------------------\n")
        return num
