import pyodbc
class Cconexion:
    
    def obtener(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server={DESKTOP-F8E9PCG\SQLEXPRESS};'
                      'Database={ConexionBD_Python};'
                      'UID={sa};'
                      'PWD={170397};')

        cursor = conn.cursor()
        cursor.execute('select * from persona')

        for row in cursor:
            print(row)
    