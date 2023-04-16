from db.run_sql import run_sql

from models.pet import Pet
from models.vet import Vet
import repositories.vet_repository as vet_repository


def save(pet):
    sql = "INSERT INTO pets (name, species, date_of_birth, owner_id, treatment_notes) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.species, pet.date_of_birth, pet.owner.id, pet.treatment_notes]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], vet, row['species'], row['date_of_birth'], row['owner_id'], row['treatment_notes'], row['id'] )
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['name'], vet, result['species'], result['date_of_birth'], result['owner_id'], result['treatment_notes'], result['id'] )
    return pet


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = "UPDATE pet SET (name, species, date_of_birth, owner_id, treatment_notes) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.species, pet.date_of_birth, pet.owner.id, pet.treatment_notes]
    run_sql(sql, values)