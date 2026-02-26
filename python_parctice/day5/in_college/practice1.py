class Person:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    # %%
class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no

# %%
class Academic:
    def __init__(self, course = None, cgpa = None):
        self.course= course
        self.cgpa = cgpa

# %%
class Sports:
    def __init__(self, sport_name, level):
        self.sport_name = sport_name
        self.level = level

# %%
class AllRounderStudents(Student, Academic, Sports):
    def __init__(self, name, age,roll_no, is_sport = False, cgpa = None, sport_name = None, is_academic = False, course = None, level = None):
        super().__init__(name, age, roll_no)
        self.is_academic = is_academic
        self.is_sport = is_sport
        if self.is_academic:
            Academic.__init__(self, course, cgpa)
        if self.is_sport :
            Sports.__init__(self, sport_name, level)

    def display(self):
        print(f"name :{self.name}")
        print(f"Age : {self.age}")
        print(f"roll no : {self.roll_no}")
        if self.is_academic:
            print(f"course : {self.course}")
            print(f"cgpa : {self.cgpa}")
        if self.is_sport:
            print(f"sport name : {self.sport_name}")
            print(f"sport level : {self.level}")

# %%
s1 = AllRounderStudents('Sonu', 23, 246, is_academic=True, course='IT', cgpa = 7.87)
s1.display()
