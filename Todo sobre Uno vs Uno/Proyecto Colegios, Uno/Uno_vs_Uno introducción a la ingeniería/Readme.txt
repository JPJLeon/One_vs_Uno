"Uno vs 1", se trata de nuestro proyecto para el ramo de Introduccion an la Ingenieria. Nuestro proyecto
se trató de lograr crear una Inteligencia Artificial con la cual se pudiese jugar al juego de cartas
"Uno" a travez de comandos por consola. Para jugar contra la computadora uno simplemente corre 
el archivo "Humano vs Bot", utilizando comandos (en mayusculas) uno puede jugar contra la computadora
con el objetivo de desacerse de todas las cartas de la mano antes que el oponente. Las reglas del juego
son sencillas y estan disponibles en la web, debido a que nosotros programamos el juego solo para jugar
de a dos jugadores es que decidimos adaptar ciertas reglas como creímos combeniente. 

Para lograr que la computadora aprendiera a jugar es que creamos todos los archivos de texto que se
pueden ver en ambas carpetas. Nosotros, luego de cada partida, guardamos en una lista todas las jugadas
que hizo cada jugador, por ejemplo: en el cementerio estaba la carta ('B','1') y se lanzó la carta
('B','9'), entonces en la lista quedaran ambas cartas guardadas. La idea fue que, cuando se terminaba
la partida, a cada jugador se le asignaba un puntaje. Luego con las listas de jugadas se ivan recorriendo
los elementos para a cada jugada asignarle el puntaje obtenido. En el caso anterior se abriría el archivo
de texto denominado ('B','1').txt y se buscaría la carta ('B','9') para modificar su puntaje, sumandole
a su antiguo puntaje el puntaje obtenido por cada jugador. La idea fue que de esta forma la Inteligencia
artificial podria usar estos puntajes en el futuro para tomar decisiones sobre que cartas lanzar. Para 
lograr una base de datos lo suficientemente grande como para poder notar un aprendisaje en la Inteligencia
fue que creamos un segundo "Bot", el cual sabía las reglas básicas del Uno por lo que nunca se equivocaba,
y lo pusimos a jugar con nuestra Inteligencia, luego de 11000 partidas detuvimos el proceso y obtuvimos
lo que nos propusimos, una base de datos que le permitió a la Inteligencia aprender a jugar desde 0,
ya que al inicio no sabía las reglas básicas siempre se equivocaba pero, a medida que fue jugando con el
segundo Bot, la base de datos le permitía copiar cada vez mejor los patrones de juego de su oponente,
llegando al punto en que despues nunca cometía jugadas que rompían las reglas del juego.

Dejamos dos carpetas con archivos, unos estan "en 0" pues los puntajes asignados a cada carta es 0, 
esto es util para realizar la comparacion entre una Inteligencia que recien comienza a jugar con otra
que ya tiene experiencia. Esperemos que les haya gustado nuestro proyecto,

Juan Pablo Leon, Rol: 201473047-0
Jordan Esquivel, Rol: 201473022-5
Yeison Fernandez, Rol: 201473006-3