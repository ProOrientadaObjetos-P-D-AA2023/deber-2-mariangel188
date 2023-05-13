


# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01


class Estudiante:
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def presentar(self):
        print("Soy {}, mi edad es {} y mi altura es {}".format(self.nombre, self.edad, self.altura))
    def __str__(self):
        return "Estudiante: {}, Edad: {}, Altura: {}".format(self.nombre, self.edad, self.altura)





# clase 02
class Hospital:
    def __init__(self, nombre, camas, doctores):
        self.nombre = nombre
        self.camas = camas
        self.doctores = doctores

    def presentar(self):
        print("El hospital {} se llama {} y tiene {} camas y {} doctores".format(self.nombre, self.nombre, self.camas, self.doctores))

    def __str__(self):
        return "Hospital: {}, Camas: {}, Doctores: {}".format(self.nombre, self.camas, self.doctores)


