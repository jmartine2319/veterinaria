from models.helpers import Utilidades
from models.persona import Adoptante

class Refugio:

    def __init__(self):
        self.__mascotas=[]

    def registrar_mascota(self,mascota):
        self.__mascotas.append(mascota)

    def listar_disponibles(self):
        for mascota in self.__mascotas:
            if not mascota.adoptado:
                print(mascota)

    
    def asignar_adopcion(self,nombre_mascota,adoptante):
        mascota = Utilidades.buscar_mascota(self.__mascotas,nombre_mascota)
        if(mascota is not None and not mascota.adoptado):
            adoptante.adoptar(mascota);
            print("felicidades por tu nueva mascota")
        else:
            print("Mascota adoptada :(")




