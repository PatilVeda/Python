#basic class and object

#class is a blueprint of the object
#creating class

# class Student:
#     name = "karan"


# #creating object (instance)


# s1 =Student()
# print(s1.name)

# class Car:
#     color = "blue"
#     model = "benz"

# car1 = Car()  #constructer
# print(car1.color)  
# print(car1.model)  



#constructor

# _init__function


# All classes have a function called  _init_(),which is always executed when the object is being initialized.



# class Student:

#    #default constructors created by python itself
#     def __init__(self,fullname,marks):
       
#        pass
  

#   #parameterized constrcter
#     def __init__(self,fullname,marks):
#         self.name=fullname
#         self.marks=marks
        
#         print("creating new student")
 
# s1 = Student("karan",67)
# print(s1.name,s1.marks)


# s2 =Student("arjun",87)
# print(s2.name,s2.marks)


#class & instance attribute


# class Student:

#     college_name = "ABC COLLEGE"
#     name ="anonymous"   #class attribute

#     def __init__(self,name,marks):
#         self.name=name  #obj attr > class attr
#         self.marks=marks
        
#         print("creating new student")
 
# s1 = Student("karan",67)
# print(s1.name,s1.marks)


# s2 =Student("arjun",87)
# print(s2.name,s2.marks)
# print(Student.college_name)




#Method 
#class contain two thing data(attribute) and methods
#method are function are belong to objects


class Student:

    college_name = "ABC COLLEGE"


    def __init__(self,name,marks):
        self.name=name  #obj attr > class attr
        self.marks=marks
        
    def welcome(self):
        print("welcome student",self.college_name)

    def get_marks(self):
        return self.marks
 
s1 = Student("karan",67)
s1.welcome()
print(s1.get_marks())

