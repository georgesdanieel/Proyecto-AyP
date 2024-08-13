class Character:
    character_list = []  # Lista para almacenar instancias de Character
    
    def __init__(self, name, birth_year, eye_color, gender, hair_color, height, mass, skin_color, homeworld, url, weight):
        self.name = name
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.gender = gender
        self.hair_color = hair_color
        self.height = height
        self.mass= mass
        self.skin_color = skin_color
        self.homeworld = homeworld  # URL del homeworld
        self.url = url  # URL del detalle de la API
        self.weight = weight

  