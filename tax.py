from DBproperty import create_connection
import dbconnectionutil
class Tax:
    def __init__(self, tax_id=None, employee_id=None, tax_year=None, taxable_income=None, tax_amount=None):
        self.tax_id = tax_id
        self.employee_id = employee_id
        self.tax_year = tax_year
        self.taxable_income = taxable_income
        self.tax_amount = tax_amount

    def CalculateTax(self, employeeId, taxYear):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select BasicSalary from Employee where EmployeeID  = %s,TaxYear = %s", (employeeId, taxYear))
            var = cur.fetchone()
            taxAmount = var[0] % 10
            print(f"tax amount   :  {taxAmount}")
            return taxAmount
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetTaxById(self, TaxID):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select * from Tax where TaxID  = %s", (TaxID,))
            var = cur.fetchone()
            taxAmount = var[0] % 10
            print(f"tax amount   :  {taxAmount}")
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetTaxesForEmployee(self, employeeId):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select * from Tax where EmployeeID  = %s", (employeeId,))
            var = cur.fetchone()
            print(var)
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetTaxesForYear(self, taxYear):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            cur.execute("select * from Tax where TaxYear  = %s", (taxYear,))
            var = cur.fetchone()
            print(var)
        except Exception as e:
            print(f"Exception details  : {e}")