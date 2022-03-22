


class Student():
    __id=""
    __name=""
    __DoB=""
    def __init__(self,id,name,date):
        self.__id = str(id)
        self.__name = str(name)
        self.__DoB = str(date)
    def _get_id(self):
        return self.__id    
    def set_id(self,id): 
        self.__id=id
    def _get_name(self):
        return self.__name    
    def set_name(self,name): 
        self.__name=name    
    def _get_DoB(self) -> str:
        return self.__DoB   
    def set_DoB(self,DoB): 
        self.__DoB=DoB   
    def __str__(self) -> str:
        return str(f"{self._get_id()} - {self._get_name()} - {self._get_DoB()}")          

class Course():
    __id=""
    __name=""
    __marklist=[]
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
    def _get_id(self):
        return self.__id    
    def set_id(self,id): 
        self.__id=id
    def _get_name(self):
        return self.__name    
    def set_name(self,name): 
        self.__name=name
    def markappend(self,a):
        self.__marklist.append(a)
    def _get_mark(self):
        return self.__marklist    
    def add_mark(self,stulist):
        id=input("Enter Student ID: ")
        
        while stulist.check_id(id)==False or id=="":
                id=input("Enter new Student ID: ")
        mark=input("Enter mark: ")
        a=Mark(id,float(mark))
        self.__marklist.append(a)    
    def print_mark(self):
        n=len(self.__marklist)
        for i in range(n):
            print(self.__marklist[i])                
    def __str__(self) -> str:
        return str(f"{self._get_id()} - {self._get_name()}")          

class Mark():
    __student_id=""
    __mark=0.0
    def __init__(self,id,mark):
        self.__student_id=id
        self.__mark=mark
    def _get_id(self):
        return self.__student_id    
    def set_id(self,id): 
        self.__student_id=id
    def _get_mark(self):
        return self.__mark    
    def set_mark(self,mark): 
        self.__mark=mark     
        
    def __str__(self) -> str:
        return str(f"{self._get_id()} - {self._get_mark()}")               

class student_list():
    __list=[]
    def check_id(self,id):
        for i in range(len(self.__list)):
            if id==self.__list[i]._get_id():
                return True
        return False
    def __init__(self) -> None:
        self.__list=[]
    def add_student(self):
        id=input("Enter ID: ")
        while self.check_id(id) or id=="":
                id=input("Enter new ID: ")
        name=input("Enter Name: ")
        DoB=input("Enter DoB (dd-mm-yyyy) : ")
        a=Student(id,name,DoB)
        self.__list.append(a)
    def print_studentlist(self):
        for i in range(len(self.__list)):
            print(self.__list[i])


class course_list():
    __list=[]
    def get_list(self):
        return self.__list
    def check_id(self,id):
        for i in range(len(self.__list)):
            if id==self.__list[i]._get_id():
                return True
        return False
    def find_index(self,id):
        for i in range(len(self.__list)):
            if id==self.__list[i]._get_id():
                return i
        return -1    
    def __init__(self) -> None:
        self.__list=[]
    def add_course(self):
        id=input("Enter ID: ")
        while self.check_id(id) or id=="":
                id=input("Enter new ID: ")
        name=input("Enter Name: ")
        a=Course(id,name)
        self.__list.append(a)
    def print_courselist(self):
        for i in range(len(self.__list)):
            print(self.__list[i])     


class Menu():
    a=student_list()
    b=course_list()
    
    def get_case(self):
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


    def Switch(self,d):
        if d == 1:
            n=input("Enter number of students : ")
            for i in range(int(n)):
                print("\n Student ",i+1)
                self.a.add_student()
        elif d == 2:
            n=input("Enter number of courses : ")
            for i in range(int(n)):
                print("\n Course ",i+1)
                self.b.add_course()
        elif d == 3:
            n=input("Enter Course ID : ")
            v=self.b.find_index(n)
            if v!=-1:
                self.b.get_list()[v].add_mark(self.a)
            else:
                print("Course not exist")    
        elif d == 4:
            self.a.print_studentlist()
        elif d == 5:
            self.b.print_courselist()
        elif d == 6:
            n=input("Enter Course ID : ")
            v=self.b.find_index(n)
            if v!=-1:
                self.b.get_list()[v].print_mark()
            else:
                print("Course not exist")    
        elif d == 7:
            exit()   
        else:
            print("Error")  


bc=Menu()                  
while True:
    bc.Switch(bc.get_case())      