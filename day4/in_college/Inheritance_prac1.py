class x:
    def __init__(self, name, phone_number, reg_num, marks):
        self.marks = marks
        self.name = name
        self.phone_number = phone_number
        self.reg_num = reg_num

    def display(self):
        print(self.name)
        print(self.reg_num)
        print(self.marks)


class xii(x):
    def __init__(self,name, phone_number, reg_num, marks, branch_name):
        super().__init__(name, phone_number, reg_num, marks)
        self.branch_name = branch_name

    def display(self):
        super().display()

class bachelor(xii):
    def __init__(self, name, reg_num, marks, passout_year, branch_name, phone_number):
        super().__init__(name, phone_number, reg_num, marks, branch_name)
        self.passout_year = passout_year
        self.branch_name = branch_name

    def display(self):
        super().display()
        print(self.passout_year)

student1 = x("somu", 897897, 'jsh76787', 87.9)
student2 = xii("somu", 786786987, 'iuij89987', 76.98, 'arts')
student2.display()
print('------------------------------------------------------')
coll_student= bachelor('deep', '19079878', '8.9 cgpa', 2027, 'IT', '9878979878')
coll_student.display()
