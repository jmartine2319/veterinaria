class Mascota:
    
    
    def __init__(self,nombre,especie,edad,adoptado=False):
        self.nombre=nombre
        self.especie=especie
        self.edad=edad
        self.adoptado=adoptado
    
    def __str__(self):
        return f"nombre {self.nombre} especie {self.especie} edad {self.edad} disponible {self.adoptado}"

    def adoptar(self):
        self.adoptado = True
    
    def retornar(self):
        self.adoptado = False
        