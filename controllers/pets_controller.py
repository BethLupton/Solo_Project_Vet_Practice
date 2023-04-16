from flask import Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository
from models.pet import Pet

pets_blueprint = Blueprint("Pets", __name__)

@pets_blueprint.route("/")
def home():
    return render_template('index.html')

@pets_blueprint.route("/pets")
def pets():
    return render_template('/pets/index.html')

@pets_blueprint.route("/vets")
def vets():
    return render_template('/vets/index.html')

@pets_blueprint.route("/add-pet")
def add_pet():
    return render_template('/add-pet/index.html')
