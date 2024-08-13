class Starship:
    starship_list = []

    def __init__(self, name, model, starship_class, manufacturer, cost_in_credits, length, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, pilots, url, created, edited,films) -> None:
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.crew = crew
        self.passengers = passengers 
        self.max_atmosphering_speed = max_atmosphering_speed
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.pilots = pilots
        self.url = url
        self.created = created
        self.edited = edited
        self.films=films

  