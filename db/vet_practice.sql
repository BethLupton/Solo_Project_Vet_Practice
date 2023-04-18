DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  contact_number VARCHAR(11)
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  species VARCHAR(255),
  date_of_birth VARCHAR(255),
  treatment_notes TEXT,
  vet_id INT NOT NULL REFERENCES vets(id),
  owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
  checked_in BOOLEAN
);

