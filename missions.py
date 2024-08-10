#Lista de armas disponibles (si no tienes una clase Weapon, define las armas aquí)
armas_disponibles=["Blaster", "Lightsaber", "Thermal Detonator", "Bowcaster"]

missions=[]
#Lista global para almacenar las misiones

def listar_opciones(opciones):
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
        