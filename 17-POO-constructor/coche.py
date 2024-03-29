class Coche:
    
    # Atributos o propiedades (variables)
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Hola soy un atributo publico"
    __soy_privado = "Hola soy un atributo privado"

    def __init__(self, color, marca, modelo, velocida, caballaje, plazas):
        self.color= color 
        self.marca= marca
        self.modelo=modelo
        self.velocidad = velocida
        self.caballaje= caballaje
        self.plazas=plazas
        


    # Metodos, son acciones que hace el objeto (coche) (funciones)
    def acelerar(self):
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -=1

    #getters y setters
    def getPrivado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color=color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo=modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca= marca

    def getMarca(self):
        return self.marca

    def getVelocidad(self):
        return self.velocidad
    
    def getInformacion(self):
        info = "---- Información del coche -----"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocididad: " + str(self.getVelocidad())
        
        return info