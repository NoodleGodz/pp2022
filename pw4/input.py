def Switch(a,b,d):
        if d == 1:
            n=input("Enter number of students : ")
            for i in range(int(n)):
                print("\n Student ",i+1)
                a.add_student()
        elif d == 2:
            n=input("Enter number of courses : ")
            for i in range(int(n)):
                print("\n Course ",i+1)
                b.add_course()
        elif d == 3:
            n=input("Enter Course ID : ")
            v=b.find_index(n)
            if v!=-1:
                x=input("Enter number of students : ")
                for i in range(int(x)):
                    b.get_list(v).add_mark(a)
            else:
                print("Course not exist")    

        elif d == 4:
            a.print_studentlist()
        elif d == 5:
            b.print_courselist()
        elif d == 6:
            n=input("Enter Course ID : ")
            v=b.find_index(n)
            if v!=-1:
                b.get_list(v).print_mark()
            else:
                print("Course not exist")    
            a.ListGPA()    
        elif d==7:
            a.GPAlist()   
        elif d==8:
            print(b.get_list(int(input("Nhap ")))  )       
        elif d == -1:
            exit()   
        else:
            print("Error")  
