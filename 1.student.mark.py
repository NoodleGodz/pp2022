
studentlist = []
courselist = []
marklist=[]

def Studentpinput():
    na=int(input("\nEnter number of students: "))
    for i in range(na):
        print(f"\nStudent {i+1}:")
        id=input("Enter ID: ")
        name=input("Enter Name: ")
        DoB=input("Enter DoB: ")
        a=[id,name,DoB]
        studentlist.append(a)

def Coursepinput():
    na=int(input("\nEnter number of Courses: "))
    for i in range(na):
        print(f"\nCourse {i+1}:")
        id=input("Enter ID: ")
        name=input("Enter Name: ")
        a=[id,name]
        courselist.append(a)
        
     




def Markpinput(a):
    for i in courselist:
        print(a, " vs ",i[0])
        if i[0]==a:
            d=[]
            na=int(input(f"Enter number of Student in Courses {a} : "))
            for i in range(na):   
                id=input("Enter ID of Student: ")
                mark=float(input("Enter Mark: "))
                v=[id,mark]
                d.append(v)  
            marklist.append([a,d])    
        break    
 


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
            print(f"\nList of Marks in Course {a} : ")
            for j in i[1]:
                print(j[0],"-",j[1])



Studentpinput() 
Coursepinput()

Markpinput(courselist[0][0])

listStudents()
listCourses()
listMarks(courselist[0][0])



