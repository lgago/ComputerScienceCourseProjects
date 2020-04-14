from abc import ABC, abstractmethod
import os, os.path

#Module Definitions
employees = []
EMPLOYEE_FILE = "employees.csv"
TIMECARD_FILE = "timecards.csv"
SALES_FILE = "receipts.csv"
PAY_LOGFILE = "paylog.txt"

def load_employees():
    with open(EMPLOYEE_FILE) as empFile:
        firstLine = empFile.readline()

        for emp in empFile.readlines():
            employeeFields = emp.rstrip().split(',')
            empId = employeeFields[0]
            firstName = employeeFields[1]
            lastName = employeeFields[2]
            address = employeeFields[3]
            city = employeeFields[4]	
            state = employeeFields[5]	
            empZip = employeeFields[6]
            classification = employeeFields[7]
            salary = employeeFields[8]	
            commission = employeeFields[9]	
            hourly = employeeFields[10]

            #Figure out what Classification the Employee is and Create that object
            #3 is hourly, 1 salary, and 2 is commision
            if classification == 3: #hourly
                empClassification = Hourly(float(hourly))
            elif classification == 1: #salary
                empClassification = Salaried(float(salary))
            else: #classiffication
                empClassification = Commissioned(float(salary), float(commission))

            employees.append(Employee(empId, firstName, lastName, address, city, state, empZip, empClassification))

def process_timecards():
    #51-4678119,7.6,3.1,1.4,4.1,6.4,7.7,6.6
    with open(TIMECARD_FILE) as timecards:
        for line in timecards.readlines():
            empId, *hoursWorked = line.rstrip().split(',')
            emp = find_employee_by_id(empId)
            classification = emp.classification
            if isinstance(emp.classification, Hourly):
                for hours in hoursWorked:
                    classification.add_timecard(float(hours))
            else:
                print("Invalid Employee Type.")

def process_receipts():
    with open(SALES_FILE) as receipts:
        for line in receipts.readlines():
            empId, *allReceipts = line.rstrip().split(',')
            emp = find_employee_by_id(empId)
            classification = emp.classification
            if isinstance(emp.classification, Commissioned):
                for r in allReceipts:
                    classification.add_receipt(float(r))
            else:
                print("Invalid Employee Type.")

def run_payroll():
    if os.path.exists(PAY_LOGFILE): # pay_log_file is a global variable holding ‘payroll.txt’
        os.remove(PAY_LOGFILE)
    for emp in employees:   # employees is the global list of Employee objects
        emp.issue_payment() # issue_payment calls a method in the classification # object to compute the pay, which in turn invokes
                            # the pay method.


def find_employee_by_id(empId):
    for emp in employees:
        if emp.emp_id == empId:
            return emp
    raise Exception("Employee not found")
    

###Class Employee###
class Employee:
    def __init__(self,emp_id,first_name,last_name,address,city,state,emp_zip,classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.emp_zip = emp_zip
        self.classification = classification

    def make_hourly(self, hourly_rate):
        self.classification = Hourly(float(hourly_rate))

    def make_salaried(self, salary):
        self.classification = Salaried(float(salary))

    def make_commissioned(self, salary, commission_rate):
        self.classification = Commissioned(float(salary), float(commission_rate))

    def issue_payment(self):
        pay = self.classification.compute_pay()

        if pay > 0:
            with open(PAY_LOGFILE, 'a') as pay_f:
                first_name = self.first_name
                last_name = self.last_name
                addr = self.address
                city = self.city
                state = self.state
                zipCode = self.emp_zip
                amount = f'{pay:.2f}'
                print("Mailing", amount, "to", first_name, last_name, "at", addr, city, state, zipCode, file=pay_f)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        pass

class Hourly(Classification):
    def __init__(self, hourly_rate):
        self.hourlyRate = hourly_rate
        self.timecard = [] #list to hold hours worked.
    
    def add_timecard(self, hours):
        self.timecard.append(hours)

    def compute_pay(self):
        pay = round(sum(self.timecard)*self.hourlyRate, 2)
        self.timecard.clear()
        return pay

class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self): #check this in the video again.
        pay = round(self.salary/24, 2)
        return pay
        

class Commissioned(Salaried):
    def __init__(self, salary, commission_rate):
        super().__init__(salary)
        self.commission_rate = commission_rate
        self.receipts = []

    def add_receipt(self, amount):
        self.receipts.append(amount)

    def compute_pay(self):
        #1/24 salary + commission rate * sum(receipts)
        pay = round(self.salary/24 + sum(self.receipts)*(self.commission_rate/100), 2)
        self.receipts.clear()
        return pay




    