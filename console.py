import pdb
from models.pet import Pet
from models.vet import Vet
from models.owner import Owner

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pet_repository.delete_all()
vet_repository.delete_all()
owner_repository.delete_all()

vet1 = Vet("Steve", "Irwin")
vet_repository.save(vet1)

vet2 = Vet("David", "Attenborough")
vet_repository.save(vet2)

owner1 = Owner("Robert", "Smith", '07456789571')
owner_repository.save(owner1)

owner2 = Owner("Simon", "Gallup", '07458589571')
owner_repository.save(owner2)

owner3 = Owner("Roger", "O'Donnell", '07458588579')
owner_repository.save(owner3)

pet1 = Pet("King Grumpy Paws", "Cat", "21-04-2020", owner1, vet1, "Extremely Grumpy", True)
pet_repository.save(pet1)

pet2 = Pet("Cutie Pie", "Dog", "05-05-2004", owner2, vet2, "Has a strange odour", False)
pet_repository.save(pet2)

pet3 = Pet("The Lizard of Oz", "Reptile", "01-01-2023", owner1, vet1, "Good natured", False)
pet_repository.save(pet3)

pet4 = Pet("Squawkers", "Bird", "31-10-2-13", owner3, vet1, "Is a bit feisty", True)
pet_repository.save(pet4)

