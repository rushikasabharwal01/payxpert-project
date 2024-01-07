from DBproperty import create_connection
import dbconnectionutil
class Payroll:
    def __init__(self, payroll_id=None, employee_id=None, pay_period_start_date=None, pay_period_end_date=None, basic_salary=None, overtime_pay=None, deductions=None, net_salary=None):
        self.payroll_id = payroll_id
        self.employee_id = employee_id
        self.pay_period_start_date = pay_period_start_date
        self.pay_period_end_date = pay_period_end_date
        self.basic_salary = basic_salary
        self.overtime_pay = overtime_pay
        self.deductions = deductions
        self.net_salary = net_salary

    def GeneratePayroll(self, PayrollId, employeeId, startDate, endDate, BasicSalary, OvertimePay, Deduction):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            NetSalary = (BasicSalary + OvertimePay) - Deduction
            query = "insert into payroll values(%s,%s,%s,%s,%s,%s,%s)"
            val = (PayrollId, employeeId, startDate, endDate, BasicSalary, OvertimePay, Deduction, NetSalary)
            return True
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetPayrollById(self, payrollId):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select  * from Payroll where PayrollID = %s", (payrollId,))
            var = cur.fetchone()
            print(var)
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetPayrollsForEmployee(self, employeeId):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select  * from payroll where EmployeeID = %s", (employeeId,))
            var = cur.fetchone()
            print(var)
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetPayrollsForPeriod(self, startDate, endDate):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select  * from payroll where PayPeriodStartDate =  %s and PayPeriodEndDate = %s",
                        (startDate, endDate))
            var = cur.fetchone()
            print(var)
        except Exception as e:
            print(f"Exception details  : {e}")