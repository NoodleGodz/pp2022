
studentlist = []
courselist = []
marklist=[]

def Studentpinput():
    na=int(input("\nEnter number of students: "))
    for i in range(na):
        print(f"\nStudent {i+1}:")
        id=input("Enter ID: ")
        if i!=0:
            while id in list(list(zip(*studentlist))[0]) or id=="":
                id=input("Enter new ID: ")
        name=input("Enter Name: ")
        DoB=input("Enter DoB (dd-mm-yyyy) : ")
        a=[id,name,DoB]
        studentlist.append(a)

def Coursepinput():
    na=int(input("\nEnter number of Courses: "))
    for i in range(na):

        print(f"\nCourse {i+1}:")
        id=input("Enter ID: ")
        if i!=0:
            while id in list(list(zip(*courselist))[0]) or id=="":
                id=input("Enter new ID: ")
        name=input("Enter Name: ")
        a=[id,name]
        courselist.append(a)
        
     




def Markpinput(a):
    for i in courselist:
        ##print(i[0]," = ",a)
        if i[0]==a:
            d=[]
            na=int(input(f"Enter number of Student in Courses {a} : "))
            for i in range(na):   
                id=input("Enter ID of Student: ")
                while id not in list(list(zip(*studentlist))[0]):
                    id=input("Enter new ID: ")
                mark=float(input("Enter Mark: "))
                v=[id,mark]
                d.append(v)  
            marklist.append([a,d])    
            return  
    
    print("Course ",a," marksheet not exist")

 


def listStudents():
    print("\nList of students : ")
    for i in studentlist:
        print(i[0],"-",i[1],"-",i[2])    

def listCourses():
    print("\nList of Courses : ")
    for i in courselist:
        print(i[0],"-",i[1])

def listMarks(a):
    for i in marklist:
        if i[0]==a:
            print(f"\nCourse {a} Marksheet : ")
            for j in i[1]:
                print(j[0],"-",j[1])
            return
    print(a,"not exist")
            





def get_case():
    print("\n---------------------------")
    print("\n1) Add students")
    print("2) Add courses")
    print("3) Add marks for a course")
    print("4) Show all students")
    print("5) Show all courses")
    print("6) Show all marks in a course")
    print("7) ESC")
    num = int(input("Choose (1-7) : "))
    print("---------------------------\n")
    return num


def Switch(d):
    if d == 1:
        Studentpinput()
    elif d == 2:
        Coursepinput()
    elif d == 3:
        Markpinput(input("Enter Course ID : "))
    elif d == 4:
        listStudents()
    elif d == 5:
        listCourses()
    elif d == 6:
        listMarks(input("Enter Course ID : "))
    elif d == 7:
        exit()   
    else:
        print("Error")     

while True:
    Switch(get_case())
    

