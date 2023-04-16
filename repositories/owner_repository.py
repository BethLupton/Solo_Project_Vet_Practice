from db.run_sql import run_sql

from models.owner import Owner
from models.pet import Pet
# from models.owner import Owner


def save(owner):
    sql = "INSERT INTO owners (first_name, last_name, contact_number) VALUES (%s, %s, %s) RETURNING *"
    values = [owner.first_name, owner.last_name, owner.contact_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    owner.id = id
    return owner

def select_all_owners():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)

    for row in results:
        owner = Owner(row['first_name'], row['last_name'], row['contact_number'], row['id'] )
        owners.append(owner)
    return owners

def select(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        owner = Owner(result['first_name'], result['last_name'], result['contact_number'], result['id'] )
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(owner):
    sql = "UPDATE owners SET (first_name, last_name, contact_number) = (%s, %s, %s) WHERE id = %s"
    values = [owner.first_name, owner.last_name, owner.contact_number]
    run_sql(sql, values)

def pets(owner):
    pet = []

    sql = "SELECT * FROM pets WHERE owner_id = %s"
    values = [owner.id]
    results = run_sql(sql, values)

    for row in results:
        pets = Pet(row['name'], owner, row['species'], row['date_of_birth'], row['owner_id'], row['treatment_notes'], row['id'] )
        pets.append(pet)
    return pets