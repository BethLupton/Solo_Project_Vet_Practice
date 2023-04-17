# Solo_Project_Vet_Practice

Project description:

A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.

What does the application do?

This is my first CodeClan project. The web application had to meet the following criteria:

The practice wants to be able to register / track animals. Important information for the vets to know is -

- Name
- Date Of Birth (use a VARCHAR initially)
- Type of animal
- Contact details for the owner
- Treatment notes
- Be able to assign animals to vets

CRUD actions for vets / animals - remember the user - what would they want to see on each View? What Views should there be?

All thing's mentioned above have been done.

Extra functionality/features:

- The homepage shows how many pets are registered at the vets and this is updated whenever a pet is added or deleted.
- The homepage also shows how many pets are checked into the practice.
- I have added the functionality to add, edit and delete an owner. The owner also has it's own page similar to the pets and vets pages.

Technologies used and why?

For the past 4 weeks i've been learning Python, HTML, CSS, Flask framework, Jinja and psql to build a full stack web application. The aim of this project was to consolidate everything that i've learned using the aforementioned languages and framework.

Challenges faced and features I hope to implement in the future:

- I spent longer than necessary on creating wireframes and trying to navigate figma, I should have put a set time on doing this.
- Time management in general was a problem, more breaks should have been taken to get a clearer head.
- Not always understanding what the errors are referring too and taking time to figure these out.
- I would like to have been able to add additional pictures but these would have been for aesthetic purposes.
- I would have also liked to have been able to add a proper appointment function with dates and times.

How to install and run the project:
1. Open files in your preferred editor e.g. Visual Studio Code
2. Create database: 'vet_practice.sql' - From `dropdb vet_practice` then run `createdb vet_practice`
3. Run psql in the terminal to initiate the database `psql -d -f travel_bucket_list.sql`
4. Run console.py file using command `python3 console.py`
5. Run Flask using command `flask run`
6. Access webpage using url: http://localhost:4999
7. To exit Flask, use CTRL + C in the terminal 











