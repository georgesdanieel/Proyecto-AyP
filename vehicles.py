class Vehicle:
    vehicle_list=[] 

    def __init__(self, name, model, vehicle_class, manufacturer,cost_in_credits, lenght, crew, passengers, max_atmosphering_speed, cargo_capacity, consumables, films, pilots, url, created, edited) -> None:
        self.name=name
        self.model=model
        self.vehicle_class=vehicle_class
        self.manufacturer=manufacturer
        self.cost_in_credits=cost_in_credits
        self.lenght=lenght
        self.crew=crew
        self.passengers=passengers
        self.max_atmosphering_speed=max_atmosphering_speed
        self.cargo_capacity=cargo_capacity
        self.consumables=consumables
        self.films=films
        self.pilots=pilots
        self.url=url
        self.created=created
        self.edited=edited

    def __repr__(self):
        return(f"Vehicle(name={self.name}, model={self.model}, vehicle_class={self.vehicle_class}, "
               f"manufacturer={self.manufacturer}, cost_in_credits={cost_in_credits}, lenght={self.lenght}, "


