from flask import Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository, owner_repository
from models.pet import Pet

pets_blueprint = Blueprint("Pets", __name__)

@pets_blueprint.route("/")
def home():
    return render_template('index.html')

@pets_blueprint.route("/pets")
def pets():
    all_pets = pet_repository.select_all_pets()
    return render_template('/pets/index.html', all_pets = all_pets)

@pets_blueprint.route("/pets/<id>/edit", methods=['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all_vets()
    owners = owner_repository.select_all_owners()
    return render_template('pets/edit.html', pet = pet, all_vets = vets, all_owners = owners)

@pets_blueprint.route("/pets/<id>", methods=['POST'])
def update_pet(id):
    pet = pet_repository.select(id);
    pet.name = request.form['name']
    pet.species = request.form['species']
    pet.date_of_birth = request.form['date_of_birth']
    pet.owner = owner_repository.select(request.form['owner_id'])
    pet.vet = vet_repository.select(request.form['vet_id'])
    pet.treatment_notes = request.form['treatment_notes']
    pet_repository.update(pet)
    return redirect('/pets')

@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')

@pets_blueprint.route("/vets")
def vets():
    all_vets = vet_repository.select_all_vets()
    return render_template('/vets/index.html', all_vets = all_vets)

@pets_blueprint.route("/add-pet")
def add_pet():
    all_owners = owner_repository.select_all_owners()
    all_vets = vet_repository.select_all_vets()

    return render_template('/add-pet/index.html', all_owners = all_owners, all_vets = all_vets)

@pets_blueprint.route("/add-pet", methods=['POST'])
def create_pet():
    name = request.form['name']
    species = request.form['species']
    date_of_birth = request.form['date_of_birth']
    owner = owner_repository.select(request.form['owner_id'])
    vet = vet_repository.select(request.form['vet_id'])
    treatment_notes = request.form['treatment_notes']
    pet = Pet(name, species, date_of_birth, owner, vet, treatment_notes)
    pet_repository.save(pet)
    return redirect('/pets')

