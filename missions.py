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

def contruir_mision():
    if len(missions)>=5:
        print("No se pueden definir más de 5 misiones")
        return
    
    mision={}
    
    #Solicitar el nombre de la misión
    mision["nombre"]= input("Nombre de la misión: ")

    #Solicitar el planeta destino 
    print("Seleccione el planeta destino:")
    planetas=[planet.name for planet in Planet.planet_list]
    mision["planeta_destino"]=seleccionar_opcion(planetas, max_seleccion=1)[0]

    #Solicitar la nave a utilizar
    print("Seleccione la nave a utilizar:")
    naves=[starship.name for starship in Starship.starship_list]
    mision["nave"]=seleccionar_opcion(naves, max_seleccion=1)[0]

    #Solicitar las armas a utilizar 
    print("Seleccione hasta 7 armas:")
    mision["armas"]=seleccionar_opcion(armas_disponibles, max_seleccion=7)

    #Solicitar los integrantes de la misión
    print("Seleccione hasta 7 integrantes:")
    integrantes=[character.name for character in Character.character_list]
    mision["integrantes"]=seleccionar_opcion(integrantes, max_seleccion=7, permitir_repetido=False)

    #Añadir la misión a la lista de misiones
    missions.append(mision)
    print(f"Misión '{mision['nombre']}' construida exitosamente.")