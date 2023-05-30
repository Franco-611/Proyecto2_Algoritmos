from time import perf_counter
import matplotlib.pyplot as plt
from tareas import *

# Encuentre el número máximo de trabajos no conflictivos que se pueden realizar
# por una sola persona
def findNonConflictingJobs(jobs):
 
    # ordena los trabajos según el orden creciente de su hora de inicio
    jobs.sort(key=lambda x: x[0])
 
    # `L[i]` almacena la cantidad máxima de trabajos que no están en conflicto y que terminan en i-ésimo trabajo
    L = [[] for _ in range(len(jobs))]
 
    for i in range(len(jobs)):
        # considera cada `j` menor que `i`
        for j in range(i):
            # L[i] = max(L[j]), donde `jobs[j].finish` es menor que `jobs[i].start`
            start, finish = (jobs[i][0], jobs[j][1])
            if finish < start and len(L[i]) < len(L[j]):
                L[i] = L[j].copy()
 
        # `L[i]` termina en i-ésimo trabajo
        L[i].append(jobs[i])
 
    # encuentra la lista que tiene un tamaño máximo
    max = []
    for pair in L:
        if len(max) < len(pair):
            max = pair
    
    return max
    # # imprime el máximo de trabajos no conflictivos
    # print("Se seleccionaron las siguientes actividades :")
    # print(max)
 
 
 
 
    
tareas = Tareas()
actividades = tareas.task_lists
tamaños = []
tiempos = []

for actividad in actividades:

    n = len(actividad)
    tamaños.append(n)
    
    start_time = perf_counter()
    findNonConflictingJobs(actividades)
    end_time = perf_counter()
    execution_time = end_time - start_time
    tiempos.append(execution_time)

tamaños, tiempos = zip(*sorted(zip(tamaños, tiempos)))

plt.plot(tamaños, tiempos)
plt.xlabel('Tamaño de entrada')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución en función del tamaño de entrada solucion Programación Dinamica')
plt.show()