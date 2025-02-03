#create the class
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
#prints all the info for the students
    def display_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")
#if they have a grade 60 or over then they are passing
    def is_passing(self):
        return self.grade >= 60


student1 = Student("Billy", 25)
student2 = Student("Amy", 65)

#displays the students info
student1.display_info()
student2.display_info()



print(f"{student1.name} is passing: {student1.is_passing()}")
print(f"{student2.name} is passing: {student2.is_passing()}")

    
            
        