from DBproperty import create_connection
import dbconnectionutil
class FinancialRecord:
    def __init__(self, record_id=None, employee_id=None, record_date=None, description=None, amount=None, record_type=None):
        self.record_id = record_id
        self.employee_id = employee_id
        self.record_date = record_date
        self.description = description
        self.amount = amount
        self.record_type = record_type

    def AddFinancialRecord(self, RecordID, EmployeeID, RecordDate, Description, Amount, RecordType):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            query = "insert into FinancialRecord values(%s,%s,%s,%s,%s,%s)"
            val = (RecordID, EmployeeID, RecordDate, Description, Amount, RecordType)
            cur.execute(query, val)
            return True
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetFinancialRecordById(self, recordId):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            query = "select * from FinancialRecord where RecordID   = %s"
            val = (recordId,)
            cur.execute(query, val)
            value = cur.fetchone()
            print(value)
        except Exception as e:
            print(f"Exception details  : {e}")

    def GetFinancialRecordsForDate(self, recordDate):
        m = dbconnectionutil.create_connection()
        cur = m.cursor()
        try:
            query = "select * from FinancialRecord where RecordDate   = %s"
            val = (recordDate,)
            cur.execute(query, val)
            value = cur.fetchone()
            print(value)
        except Exception as e:
            print(f"Exception details  : {e}")