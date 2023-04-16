from flask import Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository
from models.pet import Pet

pets_blueprint = Blueprint("Pets", __name__)

@pets_blueprint.route("/")
def home():
    return render_template('index.html')

@pets_blueprint.route("/pets")
def pets():
    all_pets = pet_repository.select_all_pets()
    return render_template('/pets/index.html', all_pets = all_pets)

@pets_blueprint.route("/vets")
def vets():
    all_vets = vet_repository.select_all_vets()
    return render_template('/vets/index.html', all_vets = all_vets)

@pets_blueprint.route("/add-pet")
def add_pet():
    return render_template('/add-pet/index.html')
