from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, hp, atk, def_, vel):
        self.nombre = nombre
        self.hp = float(hp)
        self.hp_max = float(hp)  # Atributo para restaurar vida
        self.atk = float(atk)
        self.def_ = float(def_)
        self.vel = float(vel)

    def __str__(self):
        return f"Nombre: {self.nombre}, HP: {self.hp:.2f}, ATK: {self.atk:.2f}, DEF: {self.def_:.2f}, VEL: {self.vel:.2f}"

    @abstractmethod
    def atacar(self, enemigo):
        pass

class Caballero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, hp=150.0, atk=65.0, def_=80.0, vel=30.0)

    def atacar(self, enemigo):
        # Ataque básico de espada
        danio = self.atk - enemigo.def_
        danio = max(danio, 0)  # El daño no puede ser negativo
        enemigo.hp -= danio
        return danio

class Mercenario(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, hp=100.0, atk=100.0, def_=50.0, vel=40.0)

    def atacar(self, enemigo):
        # Ataque básico con espadón
        danio = self.atk - enemigo.def_
        danio = max(danio, 0)  # El daño no puede ser negativo
        enemigo.hp -= danio
        return danio

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, hp=120.0, atk=70.0, def_=40.0, vel=100.0)

    def atacar(self, enemigo):
        # Ataque con flechazo
        danio = self.atk - enemigo.def_
        danio = max(danio, 0)  # El daño no puede ser negativo
        enemigo.hp -= danio
        return danio

class PortadorDelMal(Personaje):
    def __init__(self, nombre="Portador del Mal"):
        super().__init__(nombre, hp=500.0, atk=150.0, def_=500.0, vel=1000.0)

    def atacar(self, enemigo):
        # Ataque devastador
        danio = self.atk - enemigo.def_
        danio = max(danio, 0)  # El daño no puede ser negativo
        enemigo.hp -= danio
        return danio

def crear_personaje(opcion, nombre):
    if opcion == 1:
        return Caballero(nombre)
    elif opcion == 2:
        return Mercenario(nombre)
    elif opcion == 3:
        return Arquero(nombre)
    else:
        return None

def mostrar_estadisticas_personaje(opcion, nombre):
    personaje = crear_personaje(opcion, nombre)
    return personaje
