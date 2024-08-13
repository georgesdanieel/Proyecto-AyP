class Species:
    species_list=[]

    def __init__(self, name, classification, designation, average_height, average_lifespan, hair_colors, skin_colors, eye_colors, homeworld, language, people, url, created, edited) -> None:
        self.name=name
        self.classification=classification
        self.designation=designation
        self.average_height=average_height
        self.average_lifespan=average_lifespan
        self.hair_colors=hair_colors
        self.skin_colors=skin_colors
        self.eye_colors=eye_colors
        self.homeworld=homeworld
        self.language=language
        self.people=people
        self.url=url
        self.created=created
        self.edited=edited

    def __repr__(self):
        return(f"Species(name={self.name}, classification={self.classification}, designation={self.designation}, "
               f"average_height={self.average_height}, average_lifespan={self.average_lifespan}, hair_colors={self.hair_colors}, " 
               f"skin_colors={self.skin_colors}, eye_colors={self.eye_colors}, homeworld={self.homeworld}, "
               f"language={self.language}, people={self.people}, url={self.url}, "
               f"created={self.created}, edited={self.edited})")
    

