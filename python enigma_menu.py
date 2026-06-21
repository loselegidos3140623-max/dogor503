import time
import os
import sys

# Colores ANSI para la interfaz
VERDE = '\033[0;32m'
CIAN = '\033[0;36m'
AMARILLO = '\033[1;33m'
BLANCO = '\033[1;37m'
ROJO = '\033[0;31m'
NC = '\033[0m'

def limpiar_pantalla():
    os.system('clear')

def mostrar_banner():
    limpiar_pantalla()
    print(f"{VERDE}┌──────────────────────────────────────────────────┐")
    print("│  _____ _   _ ___ ____ __  __    _                │")
    print("│ | ____| \ | |_ _|  _ \  \/  |  / \               │")
    print("│ |  _| |  \| || || |_) | |\/| | / _ \              │")
    print("│ | |___| |\  || ||  _ <| |  | |/ ___ \             │")
    print("│ |_____|_| \_|___|_| \_\_|  |_/_/   \_\            │")
    print(f"└──────────────────────────────────────────────────┘{NC}")
    print(f"\n==================== {CIAN}⚙️ MENU PRINCIPAL ⚙️{NC} ====================")
    print(f"{CIAN}[1]{NC} 📊 Estructurar Formato de Datos (Nombres)")
    print(f"{CIAN}[2]{NC} 🗑️ Eliminar Duplicados de un Archivo")
    print(f"{CIAN}[3]{NC} 📐 Configurar Filtro de Longitud")
    print(f"{CIAN}[4]{NC} 🔠 Cambiar Formato de Mayúsculas/Minúsculas")
    print(f"{CIAN}[0]{NC} ❌ Salir del Programa")
    print("========================================================\n")

def dibujar_barra_progreso(total):
    print(f"\n{AMARILLO}[*] 🔄 INICIANDO PROCESAMIENTO ANALÍTICO...{NC}\n")
    time.sleep(0.5)
    
    for i in range(1, 101):
        tiempo_espera = 0.03 if i < 80 else 0.06
        time.sleep(tiempo_espera)
        
        bloques = int(i / 4)
        barra = f"[{VERDE}{'█' * bloques}{'░' * (25 - bloques)}{NC}]"
        registros_actuales = int((i / 100) * total)
        
        sys.stdout.write(f"\r{CIAN}[*] Progreso: {barra} {i}% | Procesados: {registros_actuales}/{total}")
        sys.stdout.flush()
    print("\n")

def procesar_archivo(ruta_in, ruta_out, modo, cantidad):
    try:
        if not os.path.exists(ruta_in):
            print(f"{ROJO}[!] El archivo de origen no existe.{NC}")
            return
            
        with open(ruta_in, 'r', encoding='utf-8') as f:
            lineas = [l.strip() for l in f if l.strip()]

        if modo == 1:
            lineas_processed = list(dict.fromkeys(lineas))[:cantidad]
        elif modo == 2:
            lineas_processed = [l.lower() for l in lineas][:cantidad]
            
        dibujar_barra_progreso(min(cantidad, len(lineas_processed) if lineas_processed else cantidad))
            
        with open(ruta_out, 'w', encoding='utf-8') as f_out:
            for elemento in lineas_processed:
                f_out.write(f"{elemento}\n")
                
        print(f"{VERDE}[+] Proceso completado con éxito. ✨{NC}")
        print(f"[*] Registros guardados en: {ruta_out}")
        
    except Exception as e:
        print(f"{ROJO}[!] Error durante el procesamiento: {str(e)}{NC}")

def ejecutar():
    while True:
        mostrar_banner()
        opcion = input(f"{VERDE}[+] Opción ➔ {NC}")
        
        if opcion == "1" or opcion == "2":
            ruta_entrada = input(f"{CIAN}[*] Ruta archivo (.txt) ➔ {NC}")
            ruta_salida = input(f"{CIAN}[*] Nombre archivo salida ➔ {NC}")
            
            try:
                cantidad = int(input(f"{CIAN}[*] Cantidad total ➔ {NC}"))
            except ValueError:
                print(f"{ROJO}[!] Cantidad no válida. Usando 100 por defecto.{NC}")
                cantidad = 100
            
            modo = 1 if opcion == "1" else 2
            procesar_archivo(ruta_entrada, ruta_salida, modo, cantidad)
            input(f"\nPresiona Enter para continuar...")
            
        elif opcion == "3" or opcion == "4":
            print(f"\n{AMARILLO}[*] 🛠️ Función en desarrollo para el entorno simulado.{NC}")
            input(f"\nPresiona Enter para continuar...")
            
        elif opcion == "0":
            print(f"\n{AMARILLO}👋 Saliendo del entorno...{NC}")
            break
        else:
            print(f"\n{ROJO}[!] Opción no válida.{NC}")
            time.sleep(1)

if __name__ == "__main__":
    ejecutar()
