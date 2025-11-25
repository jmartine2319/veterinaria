class Utilidades:

    @staticmethod
    def buscar_mascota(mascotas,nombre):
        for i in range(len(mascotas)):
            if(mascotas[i].nombre==nombre):
                return mascotas[i]
        return None


