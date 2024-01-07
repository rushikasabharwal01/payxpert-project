import dbconnectionutil
from DBproperty import create_connection
class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, date_of_birth=None, gender=None, email=None, phone_number=None, address=None, position=None, joining_date=None, termination_date=None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.position = position
        self.joining_date = joining_date
        self.termination_date = termination_date

    def GetEmployeeById(self, EmployeeID):
        m=dbconnectionutil.create_connection()
        cur=m.cursor()
        cur.execute("select * from Employee where EmployeeID   =%s", (EmployeeID,))
        var = cur.fetchall()
        for i in var:
            print(i, end="\n")

    def GetAllEmployees(self):
        try:
            cur = create_connection().cursor()
            cur.execute("select * from Employee")
            var = cur.fetchall()
            for i in var:
                print(i, end="\n")
        except Exception as e:
            print(f"Exception details  : {e}")

    def AddEmployee(self, EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position,
                    JoiningDate,
                    TerminationDate):
        cur = create_connection().cursor()
        try:

            query = "insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val = (
                EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position,
                JoiningDate,
                TerminationDate)
            cur.execute(query, val)
            return True
        except Exception as e:
            print(f"Exception details  : {e}")
            cur.close()

    def RemoveEmployee(self, EmployeeID):
        try:
            cur = create_connection().cursor()
            cur.execute("delete from Payroll where EmployeeID = %s", (EmployeeID,))
            cur.execute("delete from Tax where EmployeeID = %s", (EmployeeID,))
            cur.execute("delete from FinancialRecord where EmployeeID = %s", (EmployeeID,))
            cur.execute("delete from Employee where EmployeeID = %s", (EmployeeID,))
            return True
        except Exception as e:
            print(f"Exception details  : {e}")
