class Planet:
    planet_list = []  # Lista para almacenar instancias de Planet
    
    def __init__(self, name, diameter, rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, url, created, edited, residents, films):
        self.name = name
        self.diameter = diameter
        self.rotation_period = rotation_period
        self.orbital_period = orbital_period
        self.gravity = gravity
        self.population = population
        self.climate = climate
        self.terrain = terrain
        self.surface_water = surface_water
        self.url = url  # URL del detalle de la API
        self.created = created
        self.edited = edited
        self.residents = residents
        self.films = films

    def __repr__(self):
        return (f"Planet(name={self.name}, diameter={self.diameter}, rotation_period={self.rotation_period}, "
                f"orbital_period={self.orbital_period}, gravity={self.gravity}, population={self.population}, "
                f"climate={self.climate}, terrain={self.terrain}, surface_water={self.surface_water}, "
                f"url={self.url}, created={self.created}, edited={self.edited})")

    