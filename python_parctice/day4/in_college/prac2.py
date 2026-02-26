class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

  # %%
class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


# %%
class Teacher(Person):
    def __init_(self, name, age):
        super().__init__(name, age)


# %%
class Academic:
    def __init__(self, subject, marks):
        self.subject = subject
        if 100 >= marks >= 0:
            self.marks = marks
        else:
            print('Academic marks could not exceed 100')


# %%
class Sports:
    def __init__(self, sport_name, level):
        self.sport_name = sport_name
        if level < 10:
            self.level = level
        else:
            print("level should not exceed 10")
            return

# %%
class AllRounderStudent(Academic, Sports):
    def __init__(self, name, age, subject, marks, sport_name, level):
        Academic.__init__(self, subject, marks)
        Sports.__init__(self, sport_name, level)
  # %%

   # %%