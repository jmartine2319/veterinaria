from models.mascotas import Mascota 
from models.refugio import Refugio 
from models.persona import Persona
from models.persona import Adoptante
from models.helpers import Utilidades
import sys

def main()->int:
    refugio = Refugio()

    mascota1 = Mascota("Alf","Ovni",1000)
    mascota2 = Mascota("firu","perro",1)
    mascotas = [mascota1,mascota2]
    
    #persona = Persona("Pedro",22)

    adoptante = Adoptante("Pedro",22)

    refugio.registrar_mascota(mascota1)
    refugio.registrar_mascota(mascota2)

    while(True):
        print("""************* Menu del refugio *************
               1. Ver mascotas disponibles
               2. Adoptar mascota por nombre
               3. Ver mascotas
               """)
        opcion = input("Seleccione la opcion: ")

        if opcion == "1":
            refugio.listar_disponibles()
        elif opcion == "2":
            nombre_mascota=input("Digite el nombre: ")
            refugio.asignar_adopcion(nombre_mascota,adoptante)

    return 0
if __name__ == "__main__":
    main()
