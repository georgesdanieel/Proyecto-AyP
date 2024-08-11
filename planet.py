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

    def __repr__(self):
        return f"Film(title={self.title}, episode_id={self.episode_id}, opening_crawl={self.opening_crawl}, director={self.director}, producer={self.producer}, release_date={self.release_date}, species={self.species}, starships={self.starships}, vehicles={self.vehicles}, characters={self.characters}, planets={self.planets}, url={self.url}, created={self.created}, edited={self.edited})"
    
   