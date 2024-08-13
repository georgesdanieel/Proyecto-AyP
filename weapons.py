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
    