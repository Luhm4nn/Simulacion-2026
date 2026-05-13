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

    fig_indiv, axs_indiv = plt.subplots(2, 2, figsize=(15, 8))
    fig_indiv.suptitle(f'Corridas Individuales\n{cant_corridas} corridas de {cant_tiradas} tiradas (Nº elegido: {numero_elegido})', fontsize=16)

    fig_prom, axs_prom = plt.subplots(2, 2, figsize=(15, 8))
    fig_prom.suptitle(f'Promedio de las {cant_corridas} Corridas\n({cant_tiradas} tiradas, Nº elegido: {numero_elegido})', fontsize=16)

    todas_frecuencias = []
    todos_promedios = []
    todas_varianzas = []
    todos_desvios = []

    for corrida in range(cant_corridas):
        resultados_tiradas = []
        frecuencias_relativas = []
        promedios = []
        varianzas = []
        desvios = []
        
        aciertos = 0
        suma = 0
        suma_cuadrados = 0

        for n in range(1, cant_tiradas + 1):
            tirada = random.randint(0, 36)
            resultados_tiradas.append(tirada)
            
            if tirada == numero_elegido:
                aciertos += 1
            
            frecuencia_relativa = aciertos / n
            frecuencias_relativas.append(frecuencia_relativa)
            
            suma += tirada
            promedio = suma / n
            promedios.append(promedio)
            
            suma_cuadrados += (tirada ** 2)
            
            varianza = (suma_cuadrados / n) - (promedio ** 2)
            varianzas.append(varianza)
            desvios.append(np.sqrt(varianza))

        eje_x = list(range(1, cant_tiradas + 1))
        
        axs_indiv[0, 0].plot(eje_x, frecuencias_relativas, alpha=0.6)
        axs_indiv[0, 1].plot(eje_x, promedios, alpha=0.6)
        axs_indiv[1, 0].plot(eje_x, varianzas, alpha=0.6)
        axs_indiv[1, 1].plot(eje_x, desvios, alpha=0.6)

        todas_frecuencias.append(frecuencias_relativas)
        todos_promedios.append(promedios)
        todas_varianzas.append(varianzas)
        todos_desvios.append(desvios)

    # Gráficos de Promedios en la segunda ventana
    axs_prom[0, 0].plot(eje_x, np.mean(todas_frecuencias, axis=0), color='black', linewidth=2, label='Promedio de corridas')
    axs_prom[0, 1].plot(eje_x, np.mean(todos_promedios, axis=0), color='black', linewidth=2, label='Promedio de corridas')
    axs_prom[1, 0].plot(eje_x, np.mean(todas_varianzas, axis=0), color='black', linewidth=2, label='Promedio de corridas')
    axs_prom[1, 1].plot(eje_x, np.mean(todos_desvios, axis=0), color='black', linewidth=2, label='Promedio de corridas')
    
    # Líneas teóricas, títulos y etiquetas para Figura Individual
    axs_indiv[0, 0].axhline(y=prob_teorica, color='r', linestyle='-', linewidth=2, label=f'Teórico = {prob_teorica:.4f}')
    axs_indiv[0, 0].set_title('Frecuencia Relativa (fr) del Número Elegido')
    axs_indiv[0, 0].set_xlabel('Nº de Tiradas')
    axs_indiv[0, 0].set_ylabel('Frecuencia Relativa')
    
    axs_indiv[0, 1].axhline(y=esperanza_teorica, color='r', linestyle='-', linewidth=2, label=f'Teórico = {esperanza_teorica}')
    axs_indiv[0, 1].set_title('Valor Promedio (vp) de las Tiradas')
    axs_indiv[0, 1].set_xlabel('Nº de Tiradas')
    axs_indiv[0, 1].set_ylabel('Valor Promedio')
    
    axs_indiv[1, 0].axhline(y=varianza_teorica, color='r', linestyle='-', linewidth=2, label=f'Teórico = {varianza_teorica}')
    axs_indiv[1, 0].set_title('Varianza (vv) de las Tiradas')
    axs_indiv[1, 0].set_xlabel('Nº de Tiradas')
    axs_indiv[1, 0].set_ylabel('Varianza')
    
    axs_indiv[1, 1].axhline(y=desvio_teorico, color='r', linestyle='-', linewidth=2, label=f'Teórico = {desvio_teorico:.2f}')
    axs_indiv[1, 1].set_title('Desvío Estándar (vd) de las Tiradas')
    axs_indiv[1, 1].set_xlabel('Nº de Tiradas')
    axs_indiv[1, 1].set_ylabel('Desvío')

    # Líneas teóricas, títulos y etiquetas para Figura de Promedios
    axs_prom[0, 0].axhline(y=prob_teorica, color='r', linestyle='--', linewidth=2, label=f'Teórico = {prob_teorica:.4f}')
    axs_prom[0, 0].set_title('Promedio de Frecuencia Relativa (fr)')
    axs_prom[0, 0].set_xlabel('Nº de Tiradas')
    axs_prom[0, 0].set_ylabel('Frecuencia Relativa (Promediada)')
    
    axs_prom[0, 1].axhline(y=esperanza_teorica, color='r', linestyle='--', linewidth=2, label=f'Teórico = {esperanza_teorica}')
    axs_prom[0, 1].set_title('Promedio del Valor Promedio (vp)')
    axs_prom[0, 1].set_xlabel('Nº de Tiradas')
    axs_prom[0, 1].set_ylabel('Valor Promedio (Promediado)')
    
    axs_prom[1, 0].axhline(y=varianza_teorica, color='r', linestyle='--', linewidth=2, label=f'Teórico = {varianza_teorica}')
    axs_prom[1, 0].set_title('Promedio de la Varianza (vv)')
    axs_prom[1, 0].set_xlabel('Nº de Tiradas')
    axs_prom[1, 0].set_ylabel('Varianza (Promediada)')
    
    axs_prom[1, 1].axhline(y=desvio_teorico, color='r', linestyle='--', linewidth=2, label=f'Teórico = {desvio_teorico:.2f}')
    axs_prom[1, 1].set_title('Promedio del Desvío Estándar (vd)')
    axs_prom[1, 1].set_xlabel('Nº de Tiradas')
    axs_prom[1, 1].set_ylabel('Desvío (Promediado)')

    for ax in axs_indiv.flat:
        ax.legend()
        ax.grid(True)
        
    for ax in axs_prom.flat:
        ax.legend()
        ax.grid(True)

    fig_indiv.tight_layout()
    fig_prom.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
