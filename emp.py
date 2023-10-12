"""
InheritancePolymorphism.py.
"""
class Employee:
    """
    Holds the data structure for the Employee class.
    """
    def __init__(self, emp_name, emp_no):
        """
        Contructor for Employee.
        """
        self.emp_name = emp_name
        self.emp_no = emp_no
    def get_emp_name(self):
        """
        Accessor for emp_name.
        """
        return self.emp_name
    def set_emp_name(self, emp_name):
        """
        Mutator for emp_name.
        """
        self.emp_name = emp_name

    def get_emp_no(self):
        """
        Accessor for emp_no.
        """
        return self.emp_no
    def set_emp_no(self, emp_no):
        """
        Mutator for emp_no.
        """
        self.emp_no = emp_no

class ProductionWorker(Employee):
    """
    Subclass of the Employee class, holds data structure for ProductionWorker class.
    """
    def __init__(self, emp_name, emp_no, shift, hourly_pay):
        """
        Contructor for ProductionWorker.
        """
        super().__init__(emp_name, emp_no)
        self.shift = shift
        self.hourly_pay = hourly_pay

    def get_shift(self):
        """
        Accessor for shift.
        """
        return self.shift
    def get_hourly_pay(self):
        """
        Accessor for hourly_pay.
        """
        return self.hourly_pay
    def set_shift(self, shift):
        """
        Mutator for shift.
        """
        self.shift = shift

    def set_hourly_pay(self, hourly_pay):
        """
        Mutator for hourly_pay.
        """
        self.hourly_pay = hourly_pay
    def __str__(self):
        """
        Returns the item.
        """
        worker_result = f'Name: {self.get_emp_name()}' + '\n' + \
        f'ID number: {self.get_emp_no()}' + '\n' + \
        f'Shift: {self.get_shift()}' + '\n' + \
        f'Hourly Pay Rate: ${self.get_hourly_pay():.2f}'
        return worker_result

class ShiftSupervisor(Employee):
    """
    Subclass of the Employee class, holds data structure for ShiftSupervisor class.
    """
    def __init__(self, emp_name, emp_no, annual_sal, prod_bonus):
        """
        Contructor for ShiftSupervisor.
        """
        super().__init__(emp_name, emp_no)
        self.annual_sal = annual_sal
        self.prod_bonus = prod_bonus

    def get_annual_sal(self):
        """
        Accessor for annual_sal.
        """
        return self.annual_sal
    def get_prod_bonus(self):
        """
        Accessor for prod_bonus.
        """
        return self.prod_bonus
    def set_annual_sal(self, annual_sal):
        """
        Mutator for annual_sal.
        """
        self.annual_sal = annual_sal

    def set_prod_bonus(self, prod_bonus):
        """
        Mutator for prod_bonus.
        """
        self.prod_bonus = prod_bonus
    def __str__(self):
        """
        Returns the item.
        """
        supervisor_result = f'Name: {self.get_emp_name()}' + '\n' + \
        f'ID number: {self.get_emp_no()}' + '\n' + \
        f'Annual Salary: ${self.get_annual_sal():,.2f}' + '\n' + \
        f'Annual Production Bonus: ${self.get_prod_bonus():,.2f}'
        return supervisor_result
