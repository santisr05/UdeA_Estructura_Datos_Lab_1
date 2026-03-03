import sys
import time
import random

def crear_matriz_final_con_preview():
    FILAS = 100000
    COLUMNAS = 100000
    NOMBRE_ARCHIVO = "matriz.txt"
    CANTIDAD_FILA = 1000
    
    tiempo_inicio = time.time()
    
    print(f"--- INICIO ---")
    print(f"Generando {CANTIDAD_FILA} moldes aleatorios en RAM...")
    
    # CREACIÓN DE FILAS ALEATORIAS EN MEMORIA
    pool_de_filas = []
    for i in range(CANTIDAD_FILA):
        datos = ''.join(random.choices(['0', '1'], k=COLUMNAS))
        pool_de_filas.append(datos + "\n")
        sys.stdout.write(f"\rPreparando aleatoriedad: {((i+1)/CANTIDAD_FILA)*100:.1f}%")
    
    print("\n\nComenzando escritura veloz en disco...")
    
    try:
        # ESCRITURA
        with open(NOMBRE_ARCHIVO, "w") as archivo:
            for i in range(FILAS):
                fila_random = random.choice(pool_de_filas)
                archivo.write(fila_random)
                
                if i % 5000 == 0:
                    progreso = (i / FILAS) * 100
                    tiempo_actual = time.time() - tiempo_inicio
                    sys.stdout.write(f"\rProgreso: {progreso:.1f}% | Tiempo: {tiempo_actual:.1f}s")
                    sys.stdout.flush()
        
        tiempo_fin = time.time()
        duracion = tiempo_fin - tiempo_inicio
        
        # REPORTE TÉCNICO
        bytes_totales = len(pool_de_filas[0]) * FILAS
        gb_totales = bytes_totales / (1024**3)
        
        print(f"\n\n--- REPORTE DE EJECUCIÓN ---")
        print(f"Archivo generado: {NOMBRE_ARCHIVO}")
        print(f"Dimensiones: {FILAS}x{COLUMNAS}")
        print(f"Tiempo total: {duracion:.2f} segundos")
        print(f"Tamaño final: ~{gb_totales:.2f} GB")
        
        # PREVIEW 
        print(f"\n--- PREVIEW DEL ARCHIVO (Primeras 5 filas) ---")
        print("(Leyendo directamente del disco para verificación...)")
        print("-" * 50)
        
        with open(NOMBRE_ARCHIVO, "r") as f_lectura:
            for i in range(5):
                linea = f_lectura.readline().strip()
                # los primeros 50 caracteres de la fila
                print(f"Fila {i+1}: {linea[:50]}... [continúa]")
        
        print("-" * 50)
        print("Verificación completada. El archivo tiene la estructura correcta.")
        
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    crear_matriz_final_con_preview()