class Starship:
    starship_list = []

    def __init__(self, name, model, starship_class, manufacturer, cost_in_credits, lenght, crew, passengers, max_atmosphering_speed, hyperdrive_rating, MGLT, cargo_capacity, consumables, pilots, url, created, edited) -> None:
        self.name = name
        self.model = model
        self.starship_class = starship_class
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.lenght = lenght
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

    def __repr__(self):
        return(f"Starship(name={self.name}, name={self.name}, model={self.model}, 
               starship_class={self.starship_class}, manufacturer={self.manufacturer}, 
               cost_in_credits={self.cost_in_credits}, lenght={self.lenght}, crew={self.crew}, 
               passengers={self.passengers}, max_atmosphering_speed={self.max_atmosphering_speed}, 
               hyperdrive_rating={self.hyperdrive_rating}, MGLT={self.MGLT}, cargo_capacity={self.cargo_capacity}, 
               consumables={self.consumables}, pilots={self.pilots}, url={self.url}, created={self.created}, 
               edited={self.edited})")
