import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    parser = argparse.ArgumentParser(description="Simulación de Ruleta (Probabilidad y Estadística)")
    parser.add_argument("-c", "--tiradas", type=int, required=True, help="Cantidad de tiradas por corrida")
    parser.add_argument("-n", "--corridas", type=int, required=True, help="Cantidad de corridas")
    parser.add_argument("-e", "--elegido", type=int, required=True, help="Número elegido (0 al 36)")

    args = parser.parse_args()

    cant_tiradas = args.tiradas
    cant_corridas = args.corridas
    numero_elegido = args.elegido

    if not (0 <= numero_elegido <= 36):
        print("Error: El número elegido debe estar entre 0 y 36.")
        return

    esperanza_teorica = 18.0
    prob_teorica = 1.0 / 37.0
    varianza_teorica = 114.0
    desvio_teorico = np.sqrt(varianza_teorica)

    todas_frecuencias = []
    todos_promedios = []
    todas_varianzas = []
    todos_desvios = []

    for corrida in range(cant_corridas):

        frecuencias_relativas = []
        promedios = []
        varianzas = []
        desvios = []

        aciertos = 0
        suma = 0
        suma_cuadrados = 0

        for n in range(1, cant_tiradas + 1):

            tirada = random.randint(0, 36)

            if tirada == numero_elegido:
                aciertos += 1

            frecuencia_relativa = aciertos / n
            frecuencias_relativas.append(frecuencia_relativa)

            suma += tirada
            promedio = suma / n
            promedios.append(promedio)

            suma_cuadrados += tirada ** 2

            varianza = (suma_cuadrados / n) - (promedio ** 2)
            varianzas.append(varianza)

            desvios.append(np.sqrt(varianza))

        todas_frecuencias.append(frecuencias_relativas)
        todos_promedios.append(promedios)
        todas_varianzas.append(varianzas)
        todos_desvios.append(desvios)

    eje_x = list(range(1, cant_tiradas + 1))

    plt.figure(figsize=(10, 5))

    for fr in todas_frecuencias:
        plt.plot(eje_x, fr, alpha=0.6)

    plt.axhline(
        y=prob_teorica,
        color='r',
        linestyle='-',
        linewidth=2,
        label=f'Teórico = {prob_teorica:.4f}'
    )

    plt.title(f'Frecuencia Relativa (fr)\n{cant_corridas} corridas')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))

    for prom in todos_promedios:
        plt.plot(eje_x, prom, alpha=0.6)

    plt.axhline(
        y=esperanza_teorica,
        color='r',
        linestyle='-',
        linewidth=2,
        label=f'Teórico = {esperanza_teorica}'
    )

    plt.title(f'Valor Promedio (vp)\n{cant_corridas} corridas')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Valor Promedio')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))

    for var in todas_varianzas:
        plt.plot(eje_x, var, alpha=0.6)

    plt.axhline(
        y=varianza_teorica,
        color='r',
        linestyle='-',
        linewidth=2,
        label=f'Teórico = {varianza_teorica}'
    )

    plt.title(f'Varianza (vv)\n{cant_corridas} corridas')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Varianza')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))

    for desv in todos_desvios:
        plt.plot(eje_x, desv, alpha=0.6)

    plt.axhline(
        y=desvio_teorico,
        color='r',
        linestyle='-',
        linewidth=2,
        label=f'Teórico = {desvio_teorico:.2f}'
    )

    plt.title(f'Desvío Estándar (vd)\n{cant_corridas} corridas')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Desvío')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))

    plt.plot(
        eje_x,
        np.mean(todas_frecuencias, axis=0),
        color='black',
        linewidth=2,
        label='Promedio de corridas'
    )

    plt.axhline(
        y=prob_teorica,
        color='r',
        linestyle='--',
        linewidth=2,
        label=f'Teórico = {prob_teorica:.4f}'
    )

    plt.title('Promedio de Frecuencia Relativa')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Frecuencia Relativa')
    plt.legend()
    plt.grid(True)
    plt.show()

    # =========================================================
    # PROMEDIO DE PROMEDIOS
    # =========================================================
    plt.figure(figsize=(10, 5))

    plt.plot(
        eje_x,
        np.mean(todos_promedios, axis=0),
        color='black',
        linewidth=2,
        label='Promedio de corridas'
    )

    plt.axhline(
        y=esperanza_teorica,
        color='r',
        linestyle='--',
        linewidth=2,
        label=f'Teórico = {esperanza_teorica}'
    )

    plt.title('Promedio del Valor Promedio')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Valor Promedio')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))

    plt.plot(
        eje_x,
        np.mean(todas_varianzas, axis=0),
        color='black',
        linewidth=2,
        label='Promedio de corridas'
    )

    plt.axhline(
        y=varianza_teorica,
        color='r',
        linestyle='--',
        linewidth=2,
        label=f'Teórico = {varianza_teorica}'
    )

    plt.title('Promedio de la Varianza')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Varianza')
    plt.legend()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 5))

    plt.plot(
        eje_x,
        np.mean(todos_desvios, axis=0),
        color='black',
        linewidth=2,
        label='Promedio de corridas'
    )

    plt.axhline(
        y=desvio_teorico,
        color='r',
        linestyle='--',
        linewidth=2,
        label=f'Teórico = {desvio_teorico:.2f}'
    )

    plt.title('Promedio del Desvío Estándar')
    plt.xlabel('Nº de Tiradas')
    plt.ylabel('Desvío')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
