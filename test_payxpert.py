from DBproperty import create_connection
import dbconnectionutil
import unittest
from employee import *
from payroll import *
from tax import *
from financialrecord import *
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def setUp(self):
        self.t = Tax()

    def test_CalculateNetSalaryAfterDeductions(self):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        PayrollID = 0
        cur.execute("select BasicSalary,OvertimePay,Deductions,NetSalary from  Payroll  where PayrollID = %s",
                    (PayrollID,))
        var = cur.fetchone()
        NetSalary = (var[0] + var[1]) - var[2]
        self.assertEqual(NetSalary, var[3])

    def test_VerifyTaxCalculationForHighIncomeEmployee(self):
        tax_amount =  self.t.CalculateTax(1, 1990)
        self.assertEqual(tax_amount, "enter tax_amount")


if __name__ == '__main__':
    unittest.main()
