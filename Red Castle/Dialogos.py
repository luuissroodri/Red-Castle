import os
import platform

def limpiar_consola():
    sistema = platform.system()
    if sistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def Mostrar_Dialogo_Prologo():
    print("""
Has aparecido en el interior de un oscuro y frío calabozo. Las paredes de piedra, húmedas y desgastadas por el tiempo, parecen cerrar el espacio en un abrazo claustrofóbico. El aire es denso y está cargado de un aroma a moho y encierro. La única fuente de luz proviene de una antorcha parpadeante que proyecta sombras danzantes en las paredes.

A tu lado, en el suelo de piedra rugosa, descansa un anciano que parece ser el único otro ser en este sombrío lugar. Su rostro está surcado por profundas arrugas, y su piel, pálida y arrugada, muestra signos de haber estado en condiciones extremas. Su ropa, raída y sucia, apenas lo cubre. A pesar de su aspecto deplorable, hay una chispa de sabiduría en sus ojos cansados.

Presiona Enter para acercarte y hablar con él.
""")
    input()  # Espera a que el usuario presione Enter para continuar

    limpiar_consola()  # Borra la consola

    print("Yo: ¿Estás bien?\n")
    input("Presiona Enter para escuchar la respuesta...")

    limpiar_consola()  # Borra la consola

    print("Anciano: La vida es como un río que fluye sin cesar, a veces tranquilo, a veces turbulento. No te preocupes por las piedras en el camino, pues cada obstáculo es una oportunidad para crecer.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()  # Borra la consola

    print("Yo: Déjate de acertijos, anciano, ¿cuánto tiempo llevas aquí?\n")
    input("Presiona Enter para escuchar la respuesta...")

    limpiar_consola()  # Borra la consola

    print("Anciano: He perdido la cuenta. El tiempo aquí se ha vuelto una maraña de recuerdos difusos y añoranzas. Cada día se siente igual, un eco interminable en esta oscuridad.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()  # Borra la consola

    print("Yo: ¿Qué puedo hacer para salir? ¿Tienes alguna idea?\n")
    input("Presiona Enter para escuchar la respuesta...")

    limpiar_consola()  # Borra la consola

    print("Anciano: He encontrado una manera de escapar, pero se necesitan dos personas para hacerlo. Aunque mis fuerzas han decaído, he aprendido un hechizo que me permite convertirme en una llave. Usándome, podrás abrir la puerta que bloquea nuestra salida.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()  # Borra la consola

    print("El anciano murmura unas palabras en un lenguaje antiguo, y un brillo mágico envuelve su cuerpo. Con un destello dorado, se transforma en una antigua llave de aspecto majestuoso que cae suavemente al suelo.\n")
    input("Presiona Enter para recoger la llave...")

    limpiar_consola()  # Borra la consola

    # Agrega la llave al inventario del usuario
    inventario = ["Llave del Destino Eterno"]

    print("Has añadido 'Llave del Destino Eterno' a tu inventario.")
    print("Ahora puedes buscar la salida del calabozo.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()  # Borra la consola

    # Simula la apertura de la puerta y el encuentro con el Caballero Rokuro
    print("Colocas la llave en la cerradura y la puerta se abre con un chirrido. Al salir, te encuentras en otro calabozo iluminado por una débil luz. Agarras una antorcha de la pared y te diriges hacia una escalera que sube a la superficie.\n")
    input("Presiona Enter para subir la escalera...")

    limpiar_consola()  # Borra la consola

    print("Al salir, te encuentras en un pasillo y enfrentas a un caballero con una apariencia imponente. Él te mira con sorpresa.\n")
    input("Presiona Enter para escuchar al caballero...")

    limpiar_consola()  # Borra la consola

    print("Caballero Rokuro: ¿Quién eres y qué haces aquí? Este lugar está desierto. No debería haber nadie más aquí.\n")
    input("Presiona Enter para responder...")

    limpiar_consola()  # Borra la consola

    print("Yo: No recuerdo nada. Aparecí en ese calabozo y no sé cómo llegué allí.\n")
    input("Presiona Enter para escuchar la respuesta del Caballero Rokuro...")

    limpiar_consola()  # Borra la consola

    print("Caballero Rokuro: ¡Imposible! Aquí solo hay un prisionero, y no me logras engañar con tus mentiras. Si no puedes explicar tu presencia, no me dejas otra opción que atacarte.\n")
    print("El Caballero Rokuro desenfunda su espada con una mirada desafiante, preparado para luchar.\n")
    input("Presiona Enter para prepararte para el combate...")

    limpiar_consola()  # Borra la consola

    # Aquí podrías agregar la lógica para el combate o el siguiente paso en el juego.


def Mostrar_Dialogo_Epi1_GanadorDelDuelo():
    # El Caballero Rokuro está moribundo en el suelo
    print("El Caballero Rokuro yace en el suelo, gravemente herido. Su respiración es débil y sus ojos muestran una mezcla de dolor y resignación.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Yo: Lo siento, no me dejaste opción.\n")
    input("Presiona Enter para escuchar la respuesta del Caballero Rokuro...")

    limpiar_consola()

    print("Caballero Rokuro: Eres el portador del mal... No debiste haber escapado...\n")
    print("El Caballero Rokuro cierra los ojos y su cuerpo se queda inmóvil. Con su último aliento, fallece.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Confusión del personaje
    print("Te sientes confuso y atónito por las últimas palabras del Caballero Rokuro. Te preguntas qué quiso decir con 'portador del mal'.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Salida del calabozo y entrada al pasillo
    print("Sales del calabozo y te encuentras en un pasillo sombrío. A lo largo del suelo hay numerosos esqueletos en descomposición, lo que te da una sensación inquietante. Al final del pasillo, ves una puerta que da a un salón.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Encuentro en el salón
    print("Entras al salón, una antigua sala de festines. La mesa está cubierta de polvo y hay una nota sobre ella, escrita en un idioma extraño.\n")
    input("Presiona Enter para agarrar la nota...")

    limpiar_consola()

    print("Has añadido 'nota extraña' a tu inventario.\n")
    input("Presiona Enter para examinar la nota...")

    limpiar_consola()

    # Encuentro con la arquera
    print("De repente, sientes que alguien te apunta con un arco. Una voz firme y desafiante rompe el silencio.\n")
    print("Arquera Kanie: ¡No te muevas! ¿Quién eres?\n")
    input("Presiona Enter para responder...")

    limpiar_consola()

    print("Yo: Soy el caballero que hace guardia.\n")
    input("Presiona Enter para escuchar la respuesta de la arquera...")

    limpiar_consola()

    print("Arquera Kanie: Ah, eres tú. ¿Por qué no estás en tu puesto?\n")
    input("Presiona Enter para responder...")

    limpiar_consola()

    print("Yo: El prisionero es un viejo que no puede escapar.\n")
    input("Presiona Enter para escuchar la respuesta de la arquera...")

    limpiar_consola()

    print("La arquera asiente, parece aceptar tu explicación.\n")
    print("Arquera Kanie: Bueno, ven. Necesito ayuda con unos libros.\n")
    input("Presiona Enter para seguirla...")

    limpiar_consola()

    # Llegada a la biblioteca
    print("La arquera te lleva a una biblioteca antigua y polvorienta. Allí, saca un libro gigante de una estantería. Te preguntas qué es ese libro.\n")
    input("Presiona Enter para preguntar sobre el libro...")

    limpiar_consola()

    print("Yo: ¿Qué es ese libro?\n")
    input("Presiona Enter para escuchar la respuesta de la arquera...")

    limpiar_consola()

    print("Arquera Kanie: Este libro es el Libro Mágico del Castillo. Habla de una profecía sobre cómo el portador del mal mata a todos los guardianes del castillo. Pero es solo una leyenda, una historia de hace más de mil años.\n")
    input("Presiona Enter para preguntar sobre el portador del mal...")

    limpiar_consola()

    print("Yo: ¿El portador del mal?\n")
    input("Presiona Enter para escuchar la respuesta de la arquera...")

    limpiar_consola()

    print("Arquera Kanie: Es alguien, no se sabe si es él o ella, que desatará un camino de sangre hasta lograr salir del castillo. Si sale del castillo, todo estará perdido.\n")
    input("Presiona Enter para reflexionar sobre la información...")

    limpiar_consola()

    # La arquera sospecha que eres el portador del mal
    print("Mientras miras el libro, sientes que la arquera te apunta con su arco nuevamente.\n")
    print("Arquera Kanie: Sé que eres tú, el portador del mal. Si fueras el guardia del calabozo, nunca habrías abandonado tu puesto.\n")
    input("Presiona Enter para intentar convencerla...")

    limpiar_consola()

    print("Tratas de convencerla de que no eres el portador del mal, pero su mirada decidida y desafiante sugiere que no te escuchará. La tensión en el aire aumenta mientras se prepara para el combate.\n")
    print("Arquera Kanie: Si quieres probar tu inocencia, tendrás que hacerlo en combate.\n")
    input("Presiona Enter para comenzar el combate...")

    limpiar_consola()

def Mostrar_Dialogo_Epi1_Desenlace_Kanie():
    # La Arquera Kanie intenta escapar
    print("La Arquera Kanie, gravemente herida, se aleja arrastrándose hacia la puerta, intentando escapar de ti.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Yo: No soy el portador del mal. Tú me atacaste y me pusiste en tu contra.\n")
    input("Presiona Enter para escuchar la respuesta de Kanie...")

    limpiar_consola()

    print("Arquera Kanie: Si no fueras el portador del mal, te habría vencido. Soy la mejor arquera de mi generación, nunca fallo un tiro.\n")
    print("Con un último esfuerzo, Kanie agarra su arco y dispara una flecha explosiva. El ruido particular de la explosión activa una alarma.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Yo: ¡Maldita!\n")
    print("Le clavas tu espada, rematándola. Con su último aliento, Kanie te dice:\n")
    input("Presiona Enter para escuchar las últimas palabras de Kanie...")

    limpiar_consola()

    print("Arquera Kanie: No lograrás salir de aquí con vida. Te hemos esperado todos estos años, y no tienes oportunidad.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Tropas se acercan a la biblioteca
    print("Escuchas cómo muchas tropas se acercan rápidamente a la biblioteca. Cierras la puerta con un estante mientras intentan derribarla.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Personaje se teletransporta
    print("Te acercas al Libro Mágico del Castillo, buscando desesperadamente una salida. De repente, logras entender la letra del libro.\n")
    print("Libro Mágico: 'Si eres el portador del mal, lee la nota que tomaste de la mesa.'\n")
    input("Presiona Enter para leer la nota...")

    limpiar_consola()

    print("Lees la nota y, para tu sorpresa, entiendes perfectamente el conjuro que contiene. Mientras recitas las palabras, empiezas a brillar con destellos mágicos y te teletransportas a otro sitio del castillo.\n")
    print("Yo: ¿Qué es esto? ¿Por qué de repente entiendo todo lo que decía el libro y la nota? ¿Seré yo el portador del mal? No lo creo... tengo que probar mi inocencia.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Personaje llega a un sótano y se encuentra con Ralof y Fantar
    print("Te encuentras en un sótano oscuro y polvoriento, lleno de barriles viejos. Intentas escapar subiendo la escalera, pero ves a dos mercenarios jugando cartas.\n")
    print("Mercenario Ralof: Fantar, ve a avisar al resto que está aquí el portador del mal. Yo lo entretengo mientras pides refuerzos.\n")
    print("Mercenario Fantar se va rápidamente mientras Ralof se prepara para el combate.\n")
    input("Presiona Enter para intentar hablar con Mercenario Ralof...")

    limpiar_consola()

    print("Yo: Por favor, escúchame. No soy el portador del mal.\n")
    print("Mercenario Ralof no parece escucharte, obligándote a prepararte para pelear.\n")
    input("Presiona Enter para comenzar el combate con Mercenario Ralof...")

    limpiar_consola()

def Mostrar_Dialogo_Epi2_RalofDerrotado():
    # Ralof ha sido derrotado inicialmente
    print("Ralof cae al suelo, respirando con dificultad. Su armadura dorada está abollada y cubierta de sangre. Parece que la batalla ha terminado.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Yo: Por favor, escúchame, no soy el portador del mal. No quería pelear contigo.\n")
    input("Presiona Enter para escuchar la respuesta de Ralof...")

    limpiar_consola()

    print("Ralof: No... Si no fueras el portador del mal, no me habrías derrotado... Pero no he terminado contigo aún...\n")
    print("Ralof saca una pequeña botella con un líquido rojo oscuro. Con una sonrisa siniestra, se la bebe de un trago.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Ralof usa la poción "Elixir del Fénix"
    print("Ralof: Este es el Elixir del Fénix, una poción que me otorga la fuerza y velocidad de los dioses. ¡Prepárate para la verdadera batalla!\n")
    print("De repente, las heridas de Ralof se curan parcialmente, y su cuerpo se envuelve en una aura roja. Se pone de pie, listo para luchar de nuevo con más ferocidad que antes.\n")
    input("Presiona Enter para continuar con la segunda fase del combate...\n")

    limpiar_consola()

    # Comienza la segunda fase del combate
    print("Ralof se lanza hacia ti con una velocidad y fuerza sorprendentes. Sabes que este será un combate aún más difícil que el anterior.\n")
    input("Presiona Enter para prepararte para la batalla final...\n")

    limpiar_consola()

def Mostrar_Dialogo_Final_Anciano():
    # Después de derrotar a Ralof
    print("Ralof se desvanece en cenizas ante tus ojos, dejando tras de sí un silencio inquietante.")
    print("Pero no tienes tiempo para procesar lo ocurrido; un estruendo distante anuncia la llegada de tropas.")
    print("Comienzas a correr por un pasillo oscuro, intentando perder a los soldados que se acercan rápidamente.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # La llave del destino habla
    print("Mientras corres, escuchas una voz extraña.")
    print("Yo: ¿Qué?\n")
    print("Es la llave del destino.")
    input("Presiona Enter para escuchar la voz...")

    limpiar_consola()

    print("Llave del Destino: Soy yo, el anciano. Para escapar, debes usarme en una puerta, en una cerradura.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Encuentro con la puerta
    print("Confundido pero sin alternativas, sigues las instrucciones de la llave.")
    print("Al final del pasillo, encuentras una puerta que parece no tener salida.")
    print("Sin embargo, cuando insertas la llave, la puerta se abre, revelando otra parte del castillo.")
    print("Al atravesarla, te encuentras en el salón principal. Ves la puerta principal, la única salida.")
    print("Corres hacia ella e intentas abrirla, pero está cerrada.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    # Transformación del anciano
    print("Usas la llave del destino una vez más. Al insertarla, la puerta emite destellos.")
    print("Ante tus ojos, la llave se transforma en el anciano, pero su apariencia ha cambiado drásticamente.")
    print("Ahora se ve más joven, más fuerte, con una oscuridad palpable en su presencia.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Yo: Gracias... por ayudarme a escapar.\n")
    input("Presiona Enter para escuchar la respuesta del anciano...")

    limpiar_consola()

    print("Intentas apartarlo para abrir la puerta, pero él te detiene con una sonrisa siniestra.\n")
    print("Anciano: ¿No quieres saber cómo llegaste aquí?\n")
    input("Presiona Enter para responder...")

    limpiar_consola()

    print("Yo: Explícate.\n")
    input("Presiona Enter para escuchar la explicación del anciano...")

    limpiar_consola()

    # Revelación del anciano
    print("Anciano: Yo te invoqué. Sabía que eras el mejor guerrero de tu generación, y te necesitaba para poder escapar.")
    print("Anciano: Cada vez que matabas a alguien, absorbía su alma, por eso ahora me ves así, rejuvenecido.")
    print("Anciano: Pero te diré la verdad… no eres el portador del mal. Esa leyenda, ese mito, no te merece.")
    print("Anciano: No, tú eres simplemente un peón en mi juego.\n")
    input("Presiona Enter para responder...")

    limpiar_consola()

    print("Yo: Entonces, no soy malo... No siento esa oscuridad dentro de mí.\n")
    input("Presiona Enter para escuchar la respuesta del anciano...")

    limpiar_consola()

    # El anciano revela su verdadero plan
    print("Anciano: Quizás no ahora, pero... aún no has cumplido tu propósito.")
    print("Anciano: No puedo dejarte ir. Necesito absorber tu alma para abrir la puerta principal... y finalmente, escapar de este maldito lugar.\n")
    input("Presiona Enter para prepararte para la batalla final...")

    limpiar_consola()

    # Preparación para el combate final contra el anciano
    print("El anciano se prepara para absorber tu alma. Sabes que no hay otra salida: debes luchar contra él.\n")
    input("Presiona Enter para comenzar el combate final...")

    limpiar_consola()

def Mostrar_Dialogo_Final_PortadorDelMal():
    # El Portador del Mal ha sido derrotado
    print("El Portador del Mal cae al suelo, derrotado. Su cuerpo, antes imponente, ahora parece frágil y vencido. Un resplandor oscuro emana de su forma, desvaneciéndose lentamente.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Tú te pones de pie, agotado pero triunfante. La batalla ha sido brutal, pero has logrado vencer al ser que amenazaba el castillo.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("De repente, escuchas un estruendoso rugido y el castillo comienza a temblar. La estructura se sacude violentamente, como si los cimientos estuvieran colapsando.\n")
    input("Presiona Enter para correr hacia la salida...")

    limpiar_consola()

    # Salida del castillo y escena de la fogata
    print("Corres por los pasillos oscuros del castillo, mientras los escombros caen a tu alrededor. Finalmente, logras salir al aire libre, el castillo se derrumba tras de ti, en una espectacular lluvia de escombros y fuego.\n")
    input("Presiona Enter para continuar...")

    limpiar_consola()

    print("Te sientas en una roca cercana, exhausto pero aliviado. Prendes una fogata y contemplas el castillo, ahora envuelto en llamas y humo. Cada chispa y cada crepitar de la madera quemada parecen simbolizar el fin de una era oscura.\n")
    input("Presiona Enter para descansar y observar el castillo...")

    limpiar_consola()

    # Dos días después, llegada al pueblo
    print("Después de dos días de descanso, te diriges hacia el pueblo más cercano. El viaje ha sido tranquilo, pero tu mente está llena de pensamientos sobre las pruebas que has enfrentado.\n")
    input("Presiona Enter para entrar al pueblo...")

    limpiar_consola()

    # Reconocimiento en el pueblo
    print("Al llegar al pueblo, los guardias te reconocen inmediatamente. Sus rostros muestran sorpresa y admiración. Se acercan a ti y empiezan a aplaudir, sus voces se elevan en un rugido de celebración.\n")
    input("Presiona Enter para escuchar lo que dicen los guardias...")

    limpiar_consola()

    print("Guardia: ¡Eres tú! Pensábamos que eras el portador del mal, pero has demostrado ser nuestro salvador. Has liberado al castillo y a todos nosotros de una amenaza terrible.\n")
    input("Presiona Enter para escuchar el reconocimiento...")

    limpiar_consola()

    print("Los aldeanos se unen a la celebración, aplaudiendo y vitoreando. Un anciano del pueblo se acerca a ti y, con un gesto solemne, te declara:\n")
    print("Anciano: Has enfrentado oscuridad y destrucción, pero has salido como un héroe. Desde hoy, te llamaremos 'El Redentor del Alba'.\n")
    input("Presiona Enter para la ceremonia de celebración...")

    limpiar_consola()

    print("El pueblo celebra tu victoria con una gran fiesta en tu honor. La gente canta, baila y se regocija en la plaza del pueblo. La oscuridad del pasado ha sido reemplazada por la luz de tu valentía.\n")
    print("Mientras miras el horizonte, te das cuenta de que, aunque la batalla ha terminado, el verdadero triunfo es el futuro que has ayudado a construir. Con una sonrisa en el rostro y el corazón lleno de esperanza, te despides del pueblo y te diriges hacia el horizonte, listo para nuevas aventuras.\n")
    input("Presiona Enter para terminar el juego...")
