import math
import numpy as np

class Student():
    """
    __id=""
    __name=""
    __DoB=""
    __GPAl=[]
    __GPA=0.0"""
    def __init__(self,id,name,date):
        self.__id = str(id)
        self.__name = str(name)
        self.__DoB = str(date)
        self.__GPAl=[]
        self.__GPA=0.0
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
        return str(f"{self._get_id()} - {self._get_name()} - {self._get_DoB()} - {self._getGPA()}")  
    def addmark(self,mark):
        self.__GPAl.append(mark)
        self.averageGPA()
        
    def averageGPA(self):
        GPAarray=np.array(self.__GPAl)   
        self.__GPA=np.average(GPAarray)
    def _getGPA(self):
        return float(self.__GPA)
    def getgpalist(self):
        return self.__GPAl    


class Course():
    """
    __id=""
    __name=""
    __marklist=[]
    """
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
        self.__marklist=[]
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
        mark=math.floor(float(input("Enter mark: ")))
        a=Mark(id,mark)
        vsd=stulist.studentjustfind
        vsd.addmark(mark)
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

