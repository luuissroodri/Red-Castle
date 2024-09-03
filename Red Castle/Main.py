import os
import platform

from Mensajes import mostrar_mensaje_bienvenida  # Importa el método desde Mensajes.py
from Dialogos import Mostrar_Dialogo_Prologo, Mostrar_Dialogo_Epi1_GanadorDelDuelo, Mostrar_Dialogo_Epi1_Desenlace_Kanie, Mostrar_Dialogo_Epi2_RalofDerrotado, Mostrar_Dialogo_Final_Anciano,Mostrar_Dialogo_Final_PortadorDelMal
from Personaje import crear_personaje, Caballero, Mercenario, Arquero, PortadorDelMal  # Importamos el método `crear_personaje` desde Personaje.py
from Combate import Combate  # Importa la clase `Combate` desde Combate.py

# Método para limpiar la consola
def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

# Método para mostrar el menú principal
def mostrar_menu():
    print("|==== RED CASTLE ====|")
    print("|====================|")
    print("|        Menú        |")
    print("|====================|")
    print("|1. Comenzar partida |")
    print("|0. Salir            |")
    print("|====================|")

# Método para mostrar el menú de selección de personaje
def mostrar_menu_eleccion_personaje():
    print("Elige un personaje y ve sus estadísticas:")
    print("1. Caballero")
    print("2. Mercenario")
    print("3. Arquero")
    print("4. Salir")  # Opción para salir del menú

# Método usado para iniciar el juego
def iniciar_juego():
    while True:
        limpiar_consola()  # Limpiar la consola antes de mostrar el menú
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        match opcion:
            case "1":
                while True:
                    limpiar_consola()  # Limpiar la consola antes de mostrar el menú de selección de personaje
                    mostrar_mensaje_bienvenida()
                    limpiar_consola()
                    mostrar_menu_eleccion_personaje()

                    while True:
                        try:
                            opcion_personaje = int(input("Introduce el número de tu elección (1-4): "))
                            if opcion_personaje not in [1, 2, 3, 4]:
                                print("Opción no válida. Por favor, selecciona un número entre 1 y 4.")
                            else:
                                break  # Salir del bucle si la opción es válida
                        except ValueError:
                            print("Entrada no válida. Por favor, ingresa un número.")

                    if opcion_personaje == 4:
                        print("Regresando al menú principal...")
                        break
                    
                    # Mensaje de selección de personaje
                    personajes = {
                        1: "Caballero",
                        2: "Mercenario",
                        3: "Arquero"
                    }
                                        
                    limpiar_consola()
                    print(f"Has seleccionado el personaje: {personajes.get(opcion_personaje)}")
                    nombre_personalizado = input("Introduce el nombre de tu personaje: ")

                    # Crear el personaje usando el método `crear_personaje`
                    personaje = crear_personaje(opcion_personaje, nombre_personalizado)

                    if personaje:
                        print(f"Estadísticas de {personaje.nombre}:")
                        print(personaje)  # Mostrar estadísticas del personaje
                        confirmacion = input(f"¿Quieres seleccionar a {personaje.nombre}? (s/n): ").lower()
                        if confirmacion == 's':
                            limpiar_consola()
                            print(f"Has creado el personaje: {personaje.nombre}")
                            print("Aquí están todos los datos de tu personaje:")
                            print(personaje)  # Mostrar todos los datos del personaje
                            input("Presiona Enter para continuar...")
                            limpiar_consola()
                            Mostrar_Dialogo_Prologo()
                            
                            # Crear el Caballero Rokuro con las nuevas estadísticas
                            caballero_rokuro = Caballero("Caballero Rokuro")
                            caballero_rokuro.hp = 125.0
                            caballero_rokuro.atk = 15.0
                            caballero_rokuro.vel = 10.0

                            # Iniciar el combate con Rokuro
                            combate = Combate(personaje, caballero_rokuro)
                            if not combate.iniciar_combate():  # Si pierde contra Rokuro, regresa al menú principal
                                break

                            limpiar_consola()
                            Mostrar_Dialogo_Epi1_GanadorDelDuelo()
                            
                            # Ahora enfrentar a la Arquera Kanie
                            limpiar_consola()
                            # Crear la Arquera Kanie con estadísticas específicas
                            arquera_kanie = Arquero("Arquera Kanie")
                            arquera_kanie.hp = 350.0
                            arquera_kanie.atk = 25.0
                            arquera_kanie.vel = 200.0

                            # Iniciar el combate con Kanie
                            combate_kanie = Combate(personaje, arquera_kanie)
                            if not combate_kanie.iniciar_combate():  # Si pierde contra Kanie, regresa al menú principal
                                break
                            
                            limpiar_consola()
                            Mostrar_Dialogo_Epi1_Desenlace_Kanie()
                            
                            # Enfrentar a Ralof
                            mercenario_ralof = Mercenario("Mercenario Ralof")
                            mercenario_ralof.hp = 500.0
                            mercenario_ralof.atk = 65.0
                            mercenario_ralof.vel = 200.0   
                            limpiar_consola()

                            combate_ralof = Combate(personaje, mercenario_ralof)
                            if not combate_ralof.iniciar_combate():  # Si pierde contra Ralof, regresa al menú principal
                                break

                            limpiar_consola()
                            Mostrar_Dialogo_Epi2_RalofDerrotado()
                            
                            # Segunda fase de Ralof
                            mercenario_ralof2 = Mercenario("Mercenario Ralof")
                            mercenario_ralof2.hp = 200.0  # Estadísticas cambiadas para la segunda fase
                            mercenario_ralof2.atk = 500.0
                            mercenario_ralof2.vel = 300.0 
                            limpiar_consola()

                            combate_ralof2 = Combate(personaje, mercenario_ralof2)
                            if not combate_ralof2.iniciar_combate():  # Si pierde contra Ralof en la segunda fase, regresa al menú principal
                                break
                            limpiar_consola()
                            Mostrar_Dialogo_Final_Anciano()

                            # Combate contra el Portador del Mal
                            portador_del_mal = PortadorDelMal("Portador del Mal")
                            limpiar_consola()

                            combate_portador = Combate(personaje, portador_del_mal)
                            if not combate_portador.iniciar_combate():  # Si pierde contra el Portador del Mal, regresa al menú principal
                                break
                            limpiar_consola()
                            Mostrar_Dialogo_Final_PortadorDelMal()
                            

                        else:
                            print("Volviendo al menú para seleccionar otro personaje...\n")
                    else:
                        print("Opción no válida. Por favor, intenta nuevamente.")

            case "0":
                limpiar_consola()
                print("Saliendo del juego. ¡Hasta luego!")
                break

            case _:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    iniciar_juego()
