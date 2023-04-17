from db.run_sql import run_sql

from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository


def save(pet):
    sql = "INSERT INTO pets (name, species, date_of_birth, vet_id, owner_id, treatment_notes, checked_in) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.name, pet.species, pet.date_of_birth, pet.vet.id, pet.owner.id, pet.treatment_notes, pet.checked_in]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet

def select_all_pets():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['name'], row['species'], row['date_of_birth'], owner, vet, row['treatment_notes'], row['checked_in'], row['id'] )
        pets.append(pet)
    return pets

def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['name'], result['species'], result['date_of_birth'], result['owner_id'], vet, result['treatment_notes'], result['checked_in'], result['id'] )
    return pet

def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(pet):
    sql = "UPDATE pets SET (name, species, date_of_birth, vet_id, owner_id, treatment_notes, checked_in) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.species, pet.date_of_birth, pet.vet.id, pet.owner.id, pet.treatment_notes, pet.checked_in, pet.id]
    print(values)
    run_sql(sql, values)