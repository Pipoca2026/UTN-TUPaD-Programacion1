# =========================================================
# TP INTEGRADOR - PROGRAMACIÓN 1 (UTN)
# =========================================================

def ejercicio_1():
    print("\n--- EJERCICIO 1: CAJA DEL KIOSCO ---")
    nombre = input("Cliente: ")
    # Validación: solo letras y no vacío
    while not nombre.isalpha() or nombre == "":
        print("Error: Solo letras.")
        nombre = input("Cliente: ")

    cant_in = input("Cantidad de productos: ")
    # Validación: número positivo > 0
    while not cant_in.isdigit() or int(cant_in) <= 0:
        print("Error: Ingrese un número mayor a 0.")
        cant_in = input("Cantidad de productos: ")

    cantidad = int(cant_in)
    t_sin = 0
    t_con = 0

    for i in range(1, cantidad + 1): # Ciclo for obligatorio
        print(f"Producto {i}")
        p_in = input("Precio: ")
        while not p_in.isdigit():
            p_in = input("Error. Ingrese precio: ")
        
        precio = int(p_in)
        t_sin += precio
        
        desc = input("¿Descuento S/N?: ").lower()
        while desc not in ['s', 'n']:
            desc = input("Error (S/N): ").lower()
        
        if desc == 's':
            t_con += (precio * 0.90) # 10% descuento
        else:
            t_con += precio

    print(f"\nTotal sin descuentos: ${t_sin}")
    print(f"Total con descuentos: ${t_con:.2f}") # Formateo .2f
    print(f"Ahorro: ${t_sin - t_con:.2f}")

def ejercicio_2():
    print("\n--- EJERCICIO 2: ACCESO AL CAMPUS ---")
    intentos = 0
    acceso = False
    while intentos < 3 and not acceso: # Máximo 3 intentos
        intentos += 1
        u = input(f"Intento {intentos}/3 - Usuario: ")
        c = input("Clave: ")
        if u == "alumno" and c == "python123": # Credenciales fijas
            acceso = True
        else:
            print("Error: credenciales inválidas.")

    if acceso:
        op = ""
        while op != "4":
            print("\n1) Estado 2) Clave 3) Mensaje 4) Salir")
            op = input("Opción: ")
            if op == "1": print("Estado: Inscripto")
            elif op == "2":
                nueva = input("Nueva clave (min 6): ")
                while len(nueva) < 6: # Validación longitud
                    nueva = input("Error (min 6): ")
                print("Clave actualizada.")
            elif op == "3": print("¡Sigue adelante!")
    else:
        print("Cuenta bloqueada.")

def ejercicio_3():
    print("\n--- EJERCICIO 3: AGENDA (SIN LISTAS) ---")
    # Variables individuales según restricción
    l1 = l2 = l3 = l4 = m1 = m2 = m3 = ""
    op = ""
    while op != "5":
        print("\n1. Reservar 2. Ver 5. Salir")
        op = input("Opción: ")
        if op == "1":
            dia = input("Día (1=Lun, 2=Mar): ")
            paciente = input("Paciente: ")
            if dia == "1":
                if l1 == "": l1 = paciente; print("Reservado.")
                elif l2 == "": l2 = paciente; print("Reservado.")
                else: print("Sin cupo.")
            # ... se puede extender para el resto de variables ...

def ejercicio_4():
    print("\n--- EJERCICIO 4: LA BÓVEDA ---")
    e, t, c = 100, 12, 0 # Energía, Tiempo, Cerraduras
    alarma = False
    racha = 0
    while e > 0 and t > 0 and c < 3:
        if alarma and t <= 3: # Bloqueo por alarma
            print("SISTEMA BLOQUEADO."); break
        print(f"E:{e} T:{t} C:{c}")
        acc = input("1. Forzar 2. Hackear 3. Descansar: ")
        if acc == "1":
            e -= 20; t -= 2; racha += 1
            if racha == 3: # Regla anti-spam
                alarma = True; print("¡Alarma activa!")
            else: c += 1
        elif acc == "2":
            e -= 10; t -= 3; racha = 0
            for i in range(4): print("Hackeando...") # Ciclo for obligatorio
            c += 1
        elif acc == "3":
            e = min(100, e + 15); t -= 1; racha = 0
    if c >= 3: print("¡VICTORIA!")

def ejercicio_5():
    print("\n--- EJERCICIO 5: LA ARENA DEL GLADIADOR ---")
    nombre = input("Nombre: ")
    while not nombre.isalpha(): # Validación texto
        nombre = input("Error. Solo letras: ")
    
    hp_g, hp_e, pociones = 100, 100, 3 # Estadísticas iniciales

    # --- LÍNEA CORREGIDA AQUÍ ---
    while hp_g > 0 and hp_e > 0: # El ciclo continúa mientras ambos tengan vida
        print(f"\nHP {nombre}: {hp_g} | HP Enemigo: {hp_e} | Pociones: {pociones}")
        op = input("1. Pesado 2. Ráfaga 3. Curar: ")
        
        if op == "1":
            d = 15.0 # Float obligatorio
            if hp_e < 20: d *= 1.5; print("¡CRÍTICO!")
            hp_e -= int(d)
        elif op == "2":
            for i in range(3): # For de 3 repeticiones
                hp_e -= 5
                print("> Golpe de 5 de daño")
        elif op == "3":
            if pociones > 0:
                hp_g += 30; pociones -= 1
            else: print("No hay pociones.")
        
        if hp_e > 0: # Turno enemigo
            hp_g -= 12
            print("El enemigo te quitó 12 HP")

    if hp_g > 0: print("¡VICTORIA!")
    else: print("DERROTA.")

# --- MENÚ DE INICIO ---
while True:
    print("\n--- MENU TP INTEGRADOR ---")
    print("1-5 para ejercicios, 0 para salir")
    sel = input("Seleccione: ")
    if sel == "1": ejercicio_1()
    elif sel == "2": ejercicio_2()
    elif sel == "3": ejercicio_3()
    elif sel == "4": ejercicio_4()
    elif sel == "5": ejercicio_5()
    elif sel == "0": break