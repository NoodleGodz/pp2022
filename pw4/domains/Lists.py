import math
import numpy as np
from pw4.domains.Classes import *

class student_list():
    __list=[]
    def check_id(self,id):
        for i in range(len(self.__list)):
            if id==self.__list[i]._get_id():
                self.studentjustfind=self.__list[i]
                return True
        return False

    def __init__(self) -> None:
        self.__list=[]
        self.__list.append(Student("BI1","Minh","3/4/2003"))
        self.__list.append(Student("BI2","Dat","4/5/2006"))
        self.__list.append(Student("BI3","Tuan","8/12/1992"))
    def add_student(self):
        id=input("Enter ID: ")
        while self.check_id(id) or id=="":
                id=input("Enter new ID: ")
        name=input("Enter Name: ")
        DoB=input("Enter DoB (dd-mm-yyyy) : ")
        a= Student(id,name,DoB)
        self.__list.append(a)
    def print_studentlist(self):
        for i in range(len(self.__list)):
            print(self.__list[i])
    def GPAlist(self):
        a=[]       
        for i in self.__list:
            a.append(i._getGPA())
        a=np.array(a)    
        self.__GPAindex=np.argsort(a)[::-1][:len(a)]
        for i in self.__GPAindex:
            print(self.__list[i])
    def ListGPA(self):
        for i in self.__list:
            print(i.getgpalist())        

class course_list():
    __list=[]
    def get_list(self,index):
        return self.__list[index]
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
        self.__list.append(Course("1","Van"))
        self.__list.append(Course("2","Toan"))
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

