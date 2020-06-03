import pyodbc

class CPersona:
    
    def __init__(self):
        conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server={DESKTOP-F8E9PCG\SQLEXPRESS};'
                      'Database={ConexionBD_Python};'
                      'UID={sa};'
                      'PWD={170397};')

        self.cursor = conn.cursor()


    #metodo para mostrar datos
    def obtener(self):
        
        self.cursor.execute('select * from persona')

        for row in self.cursor:
            print(row)

    #Metodo para insertar 
    def Add(self, nombre, pais):
        
        query=('insert into persona (nombre, pais)'
                        'values(?,?)')
        self.cursor.execute(query,[nombre, pais])
        self.cursor.commit()


    #Metodo para editar 
    def Edit(self, nombre, pais, id):

        query=('update persona set nombre=?, pais=? where id=?')
        self.cursor.execute(query,[nombre, pais, id])
        self.cursor.commit()

    
    #Metodo para eliminar
    def Delete(self, id):
        query=('delete from persona where id=?')
        self.cursor.execute(query,[id])
        self.cursor.commit()
     