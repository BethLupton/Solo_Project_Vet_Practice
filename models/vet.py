from db.run_sql import run_sql

from models.pet import Pet

class Vet:
    def __init__(self, first_name, last_name, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def full_name(self):
        return self.first_name +  ' ' + self.last_name
    
    def get_pets(self):
        pets = []
        sql = "SELECT * FROM pets WHERE vet_id = %s"
        values = [self.id]
        results = run_sql(sql, values)

        for row in results:
            pet = Pet(row['name'], self, row['species'], row['date_of_birth'], row['owner_id'], row['treatment_notes'], row['id'] )
            pets.append(pet)
        return pets