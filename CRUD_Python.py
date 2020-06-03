import pyodbc
import Persona
import Conexion

#oPersona = Conexion.Cconexion()
#oPersona.obtener()

print("1.Obtener")
print("2.Crear")
print("3.Editar")
print("4.Eliminar")
op = input("Selecciona una opcion:")

if op == "1":
    oPersona = Persona.CPersona()
    oPersona.obtener()

elif op == "2":
    oPersona = Persona.CPersona()
    nombre = input("escribe el nombre:")
    pais = input("escribe el pais:")
    oPersona.Add(nombre,pais)

elif op == "3":
    oPersona = Persona.CPersona()
    oPersona.obtener()
    id = input("cual persona deceas editar:")
    nombre = input("escribe el nombre:")
    pais = input("escribe el pais:")
    oPersona.Edit(nombre,pais, id)

elif op == "4":
    oPersona = Persona.CPersona()
    oPersona.obtener()
    id = input("cual persona deceas eliminar:")
    oPersona.Delete(id)
    

else:
    print("opcion ivalida")
