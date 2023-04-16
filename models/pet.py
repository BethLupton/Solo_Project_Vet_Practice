class Pet:
    def __init__(self, name, species, date_of_birth, owner_id, treatment_notes, id = None):
        self.name = name
        self.species = species
        self.date_of_birth = date_of_birth
        self.owner_id = owner_id
        self.treatment_notes = treatment_notes
        self.id = id