#Lista de armas disponibles (si no tienes una clase Weapon, define las armas aquí)
armas_disponibles=["Blaster", "Lightsaber", "Thermal Detonator", "Bowcaster"]

missions=[]
#Lista global para almacenar las misiones

def listar_opciones(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")

def seleccionar_opcion(opciones, max_seleccion=1, permitir_repetidos=True):
    seleccionados=[]
    while len(seleccionados)<max_seleccion:
        listar_opciones(opciones)
        seleccion=input(f"Seleccione una opción (1-{len(opciones)}), o presione Enter para terminar: ")
        if seleccion=="":
            break
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(opciones):
            opcion_selecccionada=opciones[int(seleccion) - 1]
            if not permitir_repetidos and opcion_seleccionada in seleccionados:
                print("Esa opción ya ha sido seleccionada. Por favor, elija otra opción.")
            else:
                seleccionados.append(opcion_selecccionada)
        else: 
            print("Opción inválida. Por favor, elija una opción válida.")
    return seleccionados


