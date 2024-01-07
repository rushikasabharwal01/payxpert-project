
from employee import *
from payroll import *
from tax import *
from financialrecord import *


def taxpayer_menu():
    print("1  .  Get Employee By Id")
    print("2  .  Get All Employees")
    print("3  .  Add Employees")
    print("4  .  Remove Employee")
    print("5  .  Generate Payroll")
    print("6  .  Get Payroll By Id")
    print("7  .  Get Payrolls For Employee")
    print("8  .  Get Payrolls For Period")
    print("9  .  Calculate Tax")
    print("10 .  Get Taxes For Employee")
    print("11  .  Add Financial Record")
    print("12  .  Get Financial Record By Id")
    print("13  .  Get Financial Records For Date")

    ch = int(input("\nenter your choice here  "))

    e = Employee()
    p = Payroll()
    t = Tax()
    f = FinancialRecord()
    if ch == 1:
        employeeID = int(input("\nenter employeeID  "))
        e.GetEmployeeById(employeeID)
    if ch == 2:
        e.GetEmployeeById()
    elif ch == 3:
        EmployeeID = int(input("\nenter employeeID  "))
        FirstName = input("\nenter First name  ")
        LastName = input("\nenter last name  ")
        DateOfBirth = input("\nenter  Date Of Birth ")
        Gender = input("\nenter  Gender ")
        Email = input("\nenter  Email ")
        PhoneNumber = int(input("\nenter Phone Number"))
        Address = input("\nenter  Address ")
        Position = input("\nenter Position")
        JoiningDate = input("\nenterJoining Date ")
        TerminationDate = input("\nenter Termination Date ")
        e.AddEmployee(EmployeeID, FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position,
                      JoiningDate, TerminationDate)

    elif ch == 4:
        employeeID = int(input("\nenter employeeID  "))
        e.RemoveEmployee(employeeID)

    elif ch == 5:
        PayrollId = int(input("\nenter PayrollId  "))
        employeeId = int(input("\nenter employeeId  "))
        startDate = input("\nenter startDate Date ")
        endDate = input("\nenter endDate Date ")
        BasicSalary = int(input("\nenter BasicSalary  "))
        OvertimePay = int(input("\nenter OvertimePay  "))
        Deduction = int(input("\nenter  Deduction  "))
        p.GeneratePayroll(PayrollId, employeeId, startDate, endDate, BasicSalary, OvertimePay, Deduction)

    elif ch == 6:
        PayrollId = int(input("\nenter PayrollId  "))
        p.GetPayrollById(PayrollId)
    elif ch == 7:
        employeeId = int(input("\nenter employeeId  "))
        p.GetPayrollsForEmployee(employeeId)
    elif ch == 8:
        startDate = input("\nenter startDate Date ")
        endDate = input("\nenter endDate Date ")
        p.GetPayrollsForPeriod(startDate, endDate)

    elif ch == 9:
        employeeId = int(input("\nenter employeeId  "))
        taxYear = int(input("\nenter taxYear  "))
        t.CalculateTax(employeeId, taxYear)
    elif ch == 10:
        taxID = int(input("\nenter  taxID"))
        t.GetTaxById(taxID)
    elif ch == 11:
        employeeId = int(input("\nenter employeeId  "))
        RecordID = int(input("\nenter RecordID  "))
        RecordDate = input("\nenter RecordDate  ")
        Description = input("\nenter Description  ")
        Amount = int(input("\nenter Amount  "))
        RecordType = input("\nenter RecordType ")
        f.AddFinancialRecord(RecordID, employeeId, RecordDate, Description, Amount, RecordType)
    elif ch == 12:
        recordId = int(input("\nenter RecordID  "))
        f.GetFinancialRecordById(recordId)
    elif ch == 13:
        RecordDate = input("\nenter RecordDate  ")
        f.GetFinancialRecordsForDate(RecordDate)

taxpayer_menu()
