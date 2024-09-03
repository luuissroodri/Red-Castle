import os
import platform
import random
from Personaje import Caballero, Mercenario, Arquero, PortadorDelMal

# Método para limpiar la consola
def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

class Combate:
    def __init__(self, personaje_jugador, enemigo):
        self.personaje_jugador = personaje_jugador
        self.enemigo = enemigo
        self.turnos = 0
        self.hp_inicial = personaje_jugador.hp  # Guardamos la vida inicial del personaje

    def mostrar_menu_acciones(self, personaje):
        if isinstance(personaje, Caballero):
            acciones = [
                "1. Golpe de Escudo",
                "2. Embestida",
                "3. Carga Imparable",
                "4. Espadazo"
            ]
        elif isinstance(personaje, Mercenario):
            acciones = [
                "1. Corte Desgarrador",
                "2. Asalto Furioso",
                "3. Ataque Crítico",
                "4. Ruptura"
            ]
        elif isinstance(personaje, Arquero):
            acciones = [
                "1. Flecha Perforante",
                "2. Lluvia de Flechas",
                "3. Disparo de Precisión",
                "4. Flecha Explosiva"
            ]
        elif isinstance(personaje, PortadorDelMal):
            acciones = [
                "1. Sombra Aplastante",
                "2. Llamas del Abismo",
                "3. Grito del Vacío",
                "4. Juicio Final"
            ]
        else:
            acciones = []

        print("Elige una acción:")
        for accion in acciones:
            print(accion)

    def realizar_ataque(self, atacante, ataque):
        if isinstance(atacante, Caballero):
            if ataque == 1:
                return 10 + 0.5 * atacante.atk, "Golpe de Escudo"
            elif ataque == 2:
                return 15 + 0.7 * atacante.atk, "Embestida"
            elif ataque == 3:
                return 22 + 1.0 * atacante.atk, "Carga Imparable"
            elif ataque == 4:
                return 12 + 0.6 * atacante.atk, "Espadazo"
        elif isinstance(atacante, Mercenario):
            if ataque == 1:
                return 12 + 0.5 * atacante.atk, "Corte Desgarrador"
            elif ataque == 2:
                return 18 + 0.7 * atacante.atk, "Asalto Furioso"
            elif ataque == 3:
                return 25 + 0.9 * atacante.atk, "Ataque Crítico"
            elif ataque == 4:
                return 14 + 0.6 * atacante.atk, "Ruptura"
        elif isinstance(atacante, Arquero):
            if ataque == 1:
                return 14 + 0.6 * atacante.atk, "Flecha Perforante"
            elif ataque == 2:
                return 20 + 0.8 * atacante.atk, "Lluvia de Flechas"
            elif ataque == 3:
                return 18 + 0.7 * atacante.atk, "Disparo de Precisión"
            elif ataque == 4:
                return 16 + 0.9 * atacante.atk, "Flecha Explosiva"
        elif isinstance(atacante, PortadorDelMal):
            if ataque == 1:
                return 50 + 1.0 * atacante.atk, "Sombra Aplastante"
            elif ataque == 2:
                return 60 + 1.2 * atacante.atk, "Llamas del Abismo"
            elif ataque == 3:
                return 70 + 1.4 * atacante.atk, "Grito del Vacío"
            elif ataque == 4:
                return 80 + 1.5 * atacante.atk, "Juicio Final"

    def enemigo_ataca(self):
        ataque = random.randint(1, 4)
        danio, nombre_ataque = self.realizar_ataque(self.enemigo, ataque)
        print(f"{self.enemigo.nombre} ha usado {nombre_ataque}.")
        return danio

    def mostrar_estado(self):
        print(f"{self.personaje_jugador.nombre} - HP: {self.personaje_jugador.hp:.2f}")
        print(f"{self.personaje_jugador.nombre} - ATK: {self.personaje_jugador.atk:.2f}")
        print(f"{self.personaje_jugador.nombre} - DEF: {self.personaje_jugador.def_:.2f}")
        print(f"{self.personaje_jugador.nombre} - VEL: {self.personaje_jugador.vel:.2f}")
        print(f"{self.enemigo.nombre} - HP: {self.enemigo.hp:.2f}")

    def iniciar_combate(self):
        # Determinar quién ataca primero según la velocidad
        if self.personaje_jugador.vel >= self.enemigo.vel:
            primero = self.personaje_jugador
            segundo = self.enemigo
            turno_jugador = True
        else:
            primero = self.enemigo
            segundo = self.personaje_jugador
            turno_jugador = False

        while self.personaje_jugador.hp > 0 and self.enemigo.hp > 0:
            self.turnos += 1
            limpiar_consola()
            print(f"Turno {self.turnos}:")
            self.mostrar_estado()

            if turno_jugador:
                print("\nTu turno:")
                self.mostrar_menu_acciones(self.personaje_jugador)

                while True:
                    try:
                        opcion = int(input("Selecciona tu acción (1-4): "))
                        if opcion not in [1, 2, 3, 4]:
                            print("Opción no válida. Por favor, selecciona un número entre 1 y 4.")
                        else:
                            break
                    except ValueError:
                        print("Entrada no válida. Por favor, ingresa un número.")

                dano_jugador, nombre_ataque_jugador = self.realizar_ataque(self.personaje_jugador, opcion)
                self.enemigo.hp -= dano_jugador
                print(f"¡{self.personaje_jugador.nombre} ha usado {nombre_ataque_jugador} e inflige {dano_jugador:.2f} de daño!")

                if self.enemigo.hp <= 0:
                    print(f"{self.enemigo.nombre} ha sido derrotado.")
                    break

            else:
                print("\nTurno del enemigo:")
                dano_enemigo = self.enemigo_ataca()
                self.personaje_jugador.hp -= dano_enemigo
                print(f"¡El enemigo inflige {dano_enemigo:.2f} de daño!")

                if self.personaje_jugador.hp <= 0:
                    print(f"{self.personaje_jugador.nombre} ha sido derrotado.")
                    input("Presiona Enter para volver al menú...")
                    return False  # Retorna False si el jugador pierde

            # Cambiar de turno
            turno_jugador = not turno_jugador

            input("Presiona Enter para continuar al siguiente turno...")
            limpiar_consola()

        # Mensaje final y ajuste de estadísticas
        if self.personaje_jugador.hp > 0:
            # Curar a la vida inicial antes de la subida de nivel
            self.personaje_jugador.hp = self.hp_inicial
            # Aumentar las estadísticas en un 50%
            self.personaje_jugador.hp = self.personaje_jugador.hp + self.personaje_jugador.hp * 0.5 
            self.personaje_jugador.atk = self.personaje_jugador.atk + self.personaje_jugador.atk * 0.5
            self.personaje_jugador.def_ = self.personaje_jugador.def_ + self.personaje_jugador.def_ * 0.5
            self.personaje_jugador.vel = self.personaje_jugador.vel + self.personaje_jugador.vel * 0.5

            print(f"\n¡Felicidades! Has derrotado al enemigo. Has subido de nivel.")
            print(f"Estadísticas actuales de {self.personaje_jugador.nombre}:")
            self.mostrar_estado()

            input("Presiona Enter para salir...")
            return True  # Retorna True si el jugador gana
