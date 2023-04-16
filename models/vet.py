from repositories import vet_repository;
class Vet:
    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def full_name(self):
        return self.first_name +  ' ' + self.last_name
    
    def get_pets(self):
        return vet_repository.pets(self)