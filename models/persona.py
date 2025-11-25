from models.mascotas import Mascota

class Persona:
   
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        print(f"nombre {self.nombre} especie {self.especie} edad {self.edad} adoptado {self.adoptado}")

class Adoptante(Persona):

    def __init__(self,nombre,edad):
        super().__init__(nombre, edad)
        self.mascotas_adoptadas=[]

    def adoptar(self,mascotaAdoptada):
        
        self.mascotas_adoptadas.append(mascotaAdoptada)
        mascotaAdoptada.adoptar()


