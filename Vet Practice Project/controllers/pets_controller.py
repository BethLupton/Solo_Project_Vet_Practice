from flask import Blueprint, render_template, request, redirect
from repositories import pet_repository, vet_repository
from models.pet import Pet

pets_blueprint = Blueprint("Pets", __name__)

# INDEX
# GET /tasks
@pets_blueprint.route("/pets")
def

# NEW
# GET /books/new
@pets_blueprint.route("/pets/new")
def 

# CREATE
# POST /tasks
@pets_blueprint.route("/pets", methods=['POST'])
def 

# SHOW
# GET /tasks/<id>
@pets_blueprint.route("/pets/<id>")
def

# EDIT
# GET /tasks/<id>/edit
@pets_blueprint.route("/pets/<id>/edit")
def 

# UPDATE 
# PUT (POST) /tasks/<id>
@pets_blueprint.route("/pets/<id>", methods=["POST"])
def 

# DELETE
# DELETE (POST) /tasks/<id>/delete
@pets_blueprint.route("/pets/<id>/delete", methods=["POST"])
def 