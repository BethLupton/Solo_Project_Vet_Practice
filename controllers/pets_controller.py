from flask import Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository, owner_repository
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

pets_blueprint = Blueprint("Pets", __name__)

# pets

@pets_blueprint.route("/")
def home():
    return render_template('index.html')

@pets_blueprint.route("/pets")
def pets():
    all_pets = pet_repository.select_all_pets()
    return render_template('/pets/index.html', all_pets = all_pets)


@pets_blueprint.route("/pets/add")
def add_pet():
    all_owners = owner_repository.select_all_owners()
    all_vets = vet_repository.select_all_vets()

    return render_template('/pets/add_pet.html', all_owners = all_owners, all_vets = all_vets)

@pets_blueprint.route("/pets/add", methods=['POST'])
def create_pet():
    name = request.form['name']
    species = request.form['species']
    date_of_birth = request.form['date_of_birth']
    owner = owner_repository.select(request.form['owner_id'])
    vet = vet_repository.select(request.form['vet_id'])
    treatment_notes = request.form['treatment_notes']
    checked_in = request.form['checked_in']
    pet = Pet(name, species, date_of_birth, owner, vet, treatment_notes, checked_in)
    pet_repository.save(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>/edit", methods=['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all_vets()
    owners = owner_repository.select_all_owners()
    return render_template('pets/edit.html', pet = pet, all_vets = vets, all_owners = owners)

@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>", methods=['POST'])
def update_pet(id):
    pet = pet_repository.select(id);
    name = request.form['name']
    species = request.form['species']
    date_of_birth = request.form['date_of_birth']
    owner = owner_repository.select(request.form['owner_id'])
    treatment_notes = request.form['treatment_notes']
    checked_in = False
    if request.form['checked_in'] in request.form:
        checked_in = True
    vet = vet_repository.select(request.form['vet_id'])
    pet = Pet(name, species, date_of_birth, owner, vet, treatment_notes, checked_in, id)
    pet_repository.update(pet)

    return redirect('/pets')
# vets

@pets_blueprint.route("/vets")
def vets():
    all_vets = vet_repository.select_all_vets()
    return render_template('/vets/index.html', all_vets = all_vets)

@pets_blueprint.route("/vets/add")
def add_vet():
    all_pets = pet_repository.select_all_pets()
    return render_template('/vets/add_vet.html', all_pets = all_pets)

@pets_blueprint.route("/vets/add", methods=['POST'])
def create_vet():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    vet = Vet(first_name, last_name)
    vet_repository.save(vet)
    return redirect('/vets')

@pets_blueprint.route("/vets/<id>/edit", methods=['GET'])
def edit_vet(id):
    vet = vet_repository.select(id)
    return render_template('vets/edit.html', vet = vet)

@pets_blueprint.route("/vets/<id>", methods=['POST'])
def update_vet(id):
    vet = vet_repository.select(id);
    vet.first_name = request.form['first_name']
    vet.last_name = request.form['last_name']
    vet_repository.update(vet)
    return redirect('/vets')

@pets_blueprint.route("/vets/<id>/delete", methods=['POST'])
def delete_vet(id):
    vet_repository.delete(id)
    return redirect('/vets')

# owners

@pets_blueprint.route("/owners")
def owners():
    all_owners = owner_repository.select_all_owners()
    return render_template('/owners/index.html', all_owners = all_owners)

@pets_blueprint.route("/owners/add")
def add_owner():
    all_pets = pet_repository.select_all_pets()
    return render_template('/owners/add_owner.html', all_pets = all_pets)

@pets_blueprint.route("/owners/add", methods=['POST'])
def create_owner():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    contact_number = request.form['contact_number']
    owner = Owner(first_name, last_name, contact_number)
    owner_repository.save(owner)
    return redirect('/owners')

@pets_blueprint.route("/owners/<id>/edit", methods=['GET'])
def edit_owner(id):
    owner = owner_repository.select(id)
    return render_template('owners/edit.html', owner = owner)

@pets_blueprint.route("/owners/<id>", methods=['POST'])
def update_owner(id):
    owner = owner_repository.select(id);
    owner.first_name = request.form['first_name']
    owner.last_name = request.form['last_name']
    owner.contact_number = request.form['contact_number']
    owner_repository.update(owner)
    return redirect('/owners')

@pets_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')