class Film:
    film_list = []
    def __init__(self, title, episode_id, opening_crawl, director, producer, release_date, species, starships, vehicles, characters, planets, url, created, edited):
        self.title = title
        self.episode_id = episode_id
        self.opening_crawl = opening_crawl
        self.director = director
        self.producer = producer
        self.release_date = release_date
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
        self.characters = characters
        self.planets = planets
        self.url = url
        self.created = created
        self.edited = edited
        self.residents = residents
        self.films = films

    def __repr__(self):
        return (f"Planet(name={self.name}, diameter={self.diameter}, rotation_period={self.rotation_period}, "
                f"orbital_period={self.orbital_period}, gravity={self.gravity}, population={self.population}, "
                f"climate={self.climate}, terrain={self.terrain}, surface_water={self.surface_water}, "
                f"url={self.url}, created={self.created}, edited={self.edited})")

    