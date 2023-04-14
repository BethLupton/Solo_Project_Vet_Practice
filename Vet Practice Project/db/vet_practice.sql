DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  species VARCHAR(255),
  date_of_birth VARCHAR(255),
  owner_details VARCHAR(255),
  treatment_notes TEXT,
  vets_id INT NOT NULL REFERENCES vets(id)
);