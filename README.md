# What's Happening in Syria?

Muneeb Hameed

https://github.com/muneeb122/syriaproject

---

## Project Description

"What's Happening in Syria?" is a project I've taken up in order to raise awareness about the ongoing war in Syria. In my project, I've gotten data from the United Nations High Commissioner for Refugees (UNHCR) as well as from several Wikipedia pages titled "Timeline of the Syrian Civil War", stored all said data in a database, and displayed it on a Flask application for a user's easy reading. This project is also an effort to gain insight from the public as to how they think we can make the world better. This input is taken through a submission form and displayed directly on the Flask application upon submission.

## How to run

1. Install all requirements with `pip install -r requirements.txt`
2. Run `python si507_finalproj.py` in terminal/command prompt
3. In your internet browser, visit http://localhost:5000/

## How to use

1. Explore the application by clicking the links in the Navigation at the top of the page. Each page displays some type of data (Number of refugees by date, Daily details from the war)
2. On the "Comments?" page, enter your thoughts about the prompt by typing in the submission box and clicking submit.

## Routes in this application
- `/` -> this is the home page
- `/all_lines` -> this route displays the number of refugees in Syria by date.
- `/all_details` -> this shows the user very specific details about each day in the Syrian War since 2011
- `/form` -> this provides space for users to input their response to a prompt on the page, and see all responses

## How to run tests
1. Run `python tests_si507_finalproj.py` in terminal/command prompt

## In this repository:
- si507_finalproj.py
- tests_si507_finalproj.py
- templates
  - index.html
  - all_details.html
  - all_lines.html
  - my-form.html
- Screenshots
  - Home.png
  - Daily Details from the Syrian War.png
  - Refugee Data.png
  - Form.png
- DB.png
- requirements.txt
- README.md
- numrefugees.csv
- syriawardetails.csv
- syriadatabase.db
- SI507_Final_Project_by_Muneeb.pdf

---
## Code Requirements for Grading
Please check the requirements you have accomplished in your code as demonstrated.
- [x] This is a completed requirement.
- [ ] This is an incomplete requirement.

Below is a list of the requirements listed in the rubric for you to copy and paste.  See rubric on Canvas for more details.

### General
- [x] Project is submitted as a Github repository
- [x] Project includes a working Flask application that runs locally on a computer
- [x] Project includes at least 1 test suite file with reasonable tests in it.
- [x] Includes a `requirements.txt` file containing all required modules to run program
- [x] Includes a clear and readable README.md that follows this template
- [x] Includes a sample .sqlite/.db file
- [x] Includes a diagram of your database schema
- [x] Includes EVERY file needed in order to run the project
- [x] Includes screenshots and/or clear descriptions of what your project should look like when it is working

### Flask Application
- [x] Includes at least 3 different routes
- [x] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [x] Interactions with a database that has at least 2 tables
- [x] At least 1 relationship between 2 tables in database
- [x] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)
- [x] Use of a new module
- [x] Use of a second new module
- [ ] Object definitions using inheritance
- [ ] A many-to-many relationship in your database structure
- [x] At least one form in your Flask application
- [x] Templating in your Flask application
- [ ] Inclusion of JavaScript files in the application
- [x] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [ ] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [x] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [ ] Caching of data you continually retrieve from the internet in some way

### Submission
- [x] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [x] I included a summary of my project and how I thought it went **in my Canvas submission**!
