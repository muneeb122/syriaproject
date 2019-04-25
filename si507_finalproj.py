from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
import csv
import wikipedia
import os
from flask import Flask, request, flash, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_nav import Nav
from flask_nav.elements import Navbar, Subgroup, View, Link, Text, Separator

# Application configurations
app = Flask(__name__)
nav = Nav(app)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'hard to guess string for app security adgsd fsadfdflsdfsj'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./syriadatabase.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy



class responses(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   userresponse = db.Column(db.String(999))

class RefugeeData(db.Model):
    __tablename__ = 'refugeedata'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date = db.Column(db.String)
    NumRefugees = db.Column(db.Integer)


class WarDetails(db.Model):
    __tablename__ = 'wardetails'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Date = db.Column(db.String)
    Details = db.Column(db.Integer)

db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that


# # creating an empty CSV file to append data to
# csvempty = []
#
# with open('syriawardetails.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvempty)
#
# csvFile.close()
#
#
# title = "Timeline of the Syrian Civil War "
# # daterange = ["(May–August 2011)","(September–December 2011)","(January–April 2012)","(May–August 2012)","(September–December 2012)","(January–April 2013)","(May–December 2013)","(January–July 2014)","(August–December 2014)","(January–July 2015)","(August–December 2015)","(January–April 2016)","(May–August 2016)","(September–December 2016)","(January–April 2017)","(May–August 2017)","(September–December 2017)","(January–April 2018)","(May–August 2018)","(September–December 2018)","(January–April 2019)"]
# daterange = ["(May–August 2011)","(September–December 2011)"]
#
# listtitles = []
# for range in daterange:
#     listtitles.append(title+range)
#
# for sitetitle in listtitles:
#     try:
#         syriatimeline = wikipedia.page(sitetitle)
#
#         pagecontent = syriatimeline.content.split('\n=== ')
#         newlist = []
#
#         for item in pagecontent:
#             # print(item)
#             each = item.split()
#             newlist.append(each)
#         # print(newlist)
#
#         numlist = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
#         eachline = []
#         for thing in newlist:
#             if len(thing) > 0:
#                 if thing[0] in numlist:
#                     eachline.append(thing)
#
#         # print(eachline)
#         eachlinestr = [[sitetitle]]
#         for thing in eachline:
#             newlist = " ".join(thing)
#             eachlinestr.append([newlist])
#
#
#         csvData = eachlinestr
#
#
#
#
#         with open('syriawardetails.csv', 'w') as csvFile:
#             writer = csv.writer(csvFile)
#             writer.writerows(csvData)
#
#         csvFile.close()
#
#         with open('syriawardetails.csv', 'a') as csvFile:
#             writer = csv.writer(csvFile)
#             writer.writerows(csvData)
#
#         csvFile.close()
#     except:
#         print(sitetitle + "not found!")
#
# print("Done!")


#----- Takes the data from the UN Refugees website and puts it in the database ------

with open("numrefugees.csv", "r") as f:
    # next(f) #skip the first line in the file (if it's the header)
    reader = csv.reader(f)

    data = []

    for row in reader:
        data.append(RefugeeData(Date=row[0],NumRefugees=row[1]))

for x in data:
    session.add(x)
session.commit()


with open("syriawardetails.csv", "r") as f:
    reader = csv.reader(f)

    detaileddata = []

    for row in reader:
        detaileddata.append(WarDetails(Details=row[0]))
        # data.append(ChocolateBars(Company =row[0],SpecificBeanBarName=row[1],ReviewDate=row[3],CocoaPercent=new_percent,CompanyCountry=getid(row[5]),Rating=row[6]))

for x in detaileddata:
    session.add(x)
session.commit()

# def getdate(dateneeded):
#     date = SyrianRefugees.query.filter_by(Date=dateneeded).first()
#     return date
#
# def getnumber(numberneeded):
#     numberrefugees = SyrianRefugees.query.filter_by(NumRefugees=numberneeded).first()
#     return numberrefugees

nav.register_element('my_navbar', Navbar(
    'thenav',
    View('Home', 'index'),
    View('Refugee Data', 'see_alldata'),
    View('Daily Details from the Syrian War', 'see_alldetails')
    ))


@app.route('/')
def index():
    return render_template('index.html')
#
@app.route('/all_lines')
def see_alldata():
    all_lines = [] # Will be be tuple list of title, genre
    refugeedata = RefugeeData.query.all()
    for r in refugeedata:
        date = RefugeeData.query.filter_by(id=r.Date).first() # get just one director instance
        nrefugees = RefugeeData.query.filter_by(id=r.NumRefugees).first()
        all_lines.append((r.Date,r.NumRefugees)) # get list of songs with info to easily access [not the only way to do this]
    return render_template('all_lines.html',all_lines=all_lines) # check out template to see what it's doing with what we're sending!


@app.route('/all_details')
def see_alldetails():
    all_details = []
    allwardetails = WarDetails.query.all()
    for deet in allwardetails:
        date = WarDetails.query.filter_by(id=deet.Date).first() # get just one director instance
        datesdetail = WarDetails.query.filter_by(id=deet.Details).first()
        all_details.append((deet.Date,deet.Details)) # get list of songs with info to easily access [not the only way to do this]
    return render_template('all_details.html',all_details=all_details) # check out template to see what it's doing with what we're sending!

# @app.route('/form', methods = ['POST','GET'])
# def form():
#     if request.method == 'POST':
#         language = request.form.get('language')
#         framework = request.form.get('framework')
#         return '<h1>The language is {}. The framework is {}. </h1>'.format(language, framework)
#
#     return '''<form method ="POST">
#     Language <input type ='text' name = 'language'>
#     Fremework <input type = "text" name ='framework'>
#     <input type ="submit">
#     </form>'''

@app.route('/interactive')
def interactive():
   return render_template('interactive.html', responses = responses.query.all() )


@app.route('/new', methods=['GET', 'POST'])
def new():
   if request.method == 'POST':
       if not request.form['userresponse']:
           flash('Please enter all the fields', 'error')
       else:
           user = responses(request.form['userresponse'])

           session.add(user)
           session.commit()
           flash('Record was successfully added')
           return redirect(url_for('interactive'))
   return render_template('new.html')




if __name__ == '__main__':
    # db.drop_all()
    app.run() # run with this: python main_app.py runserver
