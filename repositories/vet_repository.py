from db.run_sql import run_sql

from models.vet import Vet
from models.pet import Pet


def save(vet):
    sql = "INSERT INTO vets (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [vet.first_name, vet.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet

def select_all_vets():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['first_name'], row['last_name'], row['id'] )
        vets.append(vet)
    return vets

def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vet = Vet(result['first_name'], result['last_name'], result['id'] )
    return vet

def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(vet):
    sql = "UPDATE vets SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [vet.first_name, vet.last_name, vet.id]
    run_sql(sql, values)

def pets(vet):
    pet = []

    sql = "SELECT * FROM pets WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        pets = Pet(row['name'], vet, row['species'], row['date_of_birth'], row['owner_id'], row['treatment_notes'], row['id'] )
        pets.append(pet)
    return pets