import random
from clases.jugador import Jugador
from clases.enemigo import Enemigo


def main():
    nombre_jugador = input(
        "Bienvenidos a la aventura en el espacio!, por favor, ingresa tu nombre: "
    )
    jugador = Jugador(nombre_jugador)
    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 10),
        Enemigo("Monstruo", 70, 15),
    ]

    enemigos_derrotados = []

    print("Comienza la aventura")

    while enemigos:
        enemigo_actual = random.choice(enemigos)
        if enemigo_actual in enemigos_derrotados:
            continue

        print(f"Te encuentras con un {enemigo_actual.nombre} en tu camino")
        while enemigo_actual.salud > 0:
            accion = input("¿Que deseas hacer? (atacar/huir)").lower()

            if accion == "atacar":
                dano_jugador = jugador.atacar()
                print(
                    f"has atacado al {enemigo_actual.nombre} y le has causado {dano_jugador} de daño"
                )
                enemigo_actual.recibir_dano(dano_jugador)

                if enemigo_actual.salud > 0:
                    dano_enemigo = enemigo_actual.atacar()
                    print(
                        f"{enemigo_actual.nombre} te ataco y te causo {dano_enemigo} de daño"
                    )
                    jugador.recibir_dano(dano_enemigo)
            elif accion == "huir":
                print("Has decidido huir del combate")
                break
        if jugador.salud <= 0:
            print("Has perdido la partida")
            break
        if enemigo_actual.salud <= 0:
            enemigos_derrotados.append(enemigo_actual)
            enemigos.remove(enemigo_actual)
        jugador.ganar_experiencia(20)
        continuar = input("¿Quieres seguir explorando? (s/n)").lower()
        if continuar != "s":
            print("Gracias por haber jugado")
            break
    if not enemigos:
        print("Felicidades has derrotado a todos los enemigos")


if __name__ == "__main__":
    main()
