class Weapon:
    weapon_list=[]
    def __init__(self, weapon_id, name, model, manufacturer, cost_in_credits, length, weapon_type, description, films):
        self.weapon_id = weapon_id
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.weapon_type = weapon_type
        self.description = description
        self.films = films
    def __repr__(self):
        return (f"ID: {self.weapon_id}\n"
                f"Name: {self.name}\n"
                f"Model: {self.model}\n"
                f"Manufacturer: {self.manufacturer}\n"
                f"Cost in Credits: {self.cost_in_credits}\n"
                f"Length: {self.length}\n"
                f"Type: {self.weapon_type}\n"
                f"Description: {self.description}\n"
                f"Films: {self.films}\n")
