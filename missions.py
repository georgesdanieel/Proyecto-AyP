import os
from planet import Planet
from starship import Starship
from character import Character
from weapons import Weapon

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
            eleccion=opciones[int(seleccion) - 1]
            if not permitir_repetidos and eleccion in seleccionados:
                print("Esa opción ya ha sido seleccionada. Por favor, elija otra opción.")
            else:
                seleccionados.append(eleccion)
        else: 
            print("Opción inválida. Por favor, elija una opción válida.")
    return seleccionados

def construir_mision():
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
    armas =[weapon.name for weapon in Weapon.weapon_list]
    mision["armas"]=seleccionar_opcion(armas, max_seleccion=7)

    #Solicitar los integrantes de la misión
    print("Seleccione hasta 7 integrantes:")
    integrantes=[character.name for character in Character.character_list]
    mision["integrantes"]=seleccionar_opcion(integrantes, max_seleccion=7, permitir_repetidos=False)

    #Añadir la misión a la lista de misiones
    missions.append(mision)
    print(f"Misión '{mision['nombre']}' construida exitosamente.")

def modificar_mision():
    if not missions:
        print("No hay misiones definidas para el momento")
        return
    else: 
        print('Misiones definidas: ')
        for mision in missions:
            listar_opciones(mision['nombre'])
    print(len(missions))
    seleccion=input('Seleccione una mision para modificar: ')
    if not seleccion.isdigit() or 1 <= int(seleccion) <= len(missions):
        print("Opción inválida. Por favor, elija una opción válida.")
        return

    mision_escogida=int(seleccion) - 1
    mision=missions[mision_escogida]

    print(f'Modificando mision {mision['nombre']}')

    while True:
        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Planeta destino")
        print("3. Nave")
        print("4. Armas")
        print("5. Integrantes")
        print("6. Salir")

        opcion=input('---->  ')
        if opcion=='1':
            print('Seleccione el nuevo nombre: ')
            nuevo_nombre=input('--> ')
            mision['nombre']=nuevo_nombre
            print(f'El nombre de la mision ha sido actualizado: {mision['nombre']}')
        elif opcion=='2':
            print('Seleccione el nuevo planeta destino: ')
            for planet in Planet.planet_list:
                planetas=planet.name
                nuevo_planeta = seleccionar_opcion(planetas, max_seleccion=1)[0]
                mision['planeta_destino']=nuevo_planeta
                print(f'El planeta destino de la mision ha sido actualizado: {mision['planeta_destino']}')
        elif opcion=='3':
            print('Seleccione la nueva nave a utilizar: ')
            for starship in Starship.starship_list:
                naves=starship.name
                nueva_nave = seleccionar_opcion(naves, max_seleccion=1)[0]
                mision['nave']=nueva_nave
                print(f'La nave de la mision ha sido actualizada: {mision['nave']}')
        elif opcion=='4':
            print('Seleccione las nuevas armas: ')
            for weapons in Weapon.weapon_list: #escoge desde 0 las armas
                armas=weapons.name
                nuevas_armas = seleccionar_opcion(armas)
                mision['armas']=nuevas_armas
                print(f'Armas actualizadas: {mision['armas']}')
        elif opcion=='5':
            print('Seleccione los nuevos integrantes: ')
            for character in Character.character_list:
                integrantes=character.name
                nuevos_integrantes= seleccionar_opcion(integrantes)
                mision['integrantes']=nuevos_integrantes
                print(f'Nuevos integrantes de la mision: {mision['integrantes']}')
        elif opcion == "5":
            break
        else:
            print("Selección no válida. Por favor, intente de nuevo.")
        
    print('Mision modificada exitosamente')

def ver_mision():
    if not missions:
        print("No hay misiones definidas.")
        return
    else: 
        print('Misiones definidas: ')
        for mision in missions:
            listar_opciones(mision['nombre'])

    print(len(missions))
    seleccion=input('Seleccione una mision para visualizar: ')
    if not seleccion.isdigit() or 1 <= int(seleccion) <= len(missions):
        print("Opción inválida. Por favor, elija una opción válida.")
        return

    mision_escogida=int(seleccion) - 1
    mision=missions[mision_escogida]

    print('\nDetalles de la misión')
    print(f"'{mision['nombre']}':")
    print(f"Planeta destino: {mision['planeta_destino']}")
    print(f"Nave a utilizar: {mision['nave']}")
    print(f"Armas: {', '.join(mision['armas'])}")
    print(f"Integrantes: {', '.join(mision['integrantes'])}")

def guardar_mision():
    if not missions:
        print("No hay misiones definidas para guardar.")
        return

    with open("misiones.txt", "w") as file:
        for mision in missions:
            mision["armas"] = ','.join(mision["armas"])
            mision["integrantes"] = ','.join(mision["integrantes"])
            linea = f"{mision['nombre']}|{mision['planeta_destino']}|{mision['nave']}|{mision['armas']}|{mision['integrantes']}"
            file.write(linea)
    
    print("Misiones guardadas exitosamente.")

def cargar_mision():
    if not os.path.exists("misiones.txt"):
        print("No se encontró el archivo misiones.txt")
        return
    
    global missions
    missions = []

    with open("misiones.txt", "r") as file:
        for linea in file:
            nombre, planeta_destino, nave, armas, integrantes = linea.strip().split('/')
            mision = {
                "nombre": nombre,
                "planeta_destino": planeta_destino,
                "nave": nave,
                "armas": armas.split(','),
                "integrantes": integrantes.split(',')
            }
            missions.append(mision)

    print("Misiones cargadas exitosamente.")


            







    
