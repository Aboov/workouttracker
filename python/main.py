import os

import sqlalchemy
import uuid
import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy import select

#imports for each class
from exercise import Exercise as Ex
from legs import Legs as leg
from user import User as use
from pull import Pull as pul
from push import Push as pus



app = Flask(__name__)

class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
engine = db.create_engine('sqlite:///datacamp.sqlite')
conn = engine.connect()
metadata = db.MetaData()
run=True



Exercise = db.Table('Exercise', metadata,
              db.Column('exercise_id',db.String(255),primary_key=True),
              db.Column('sets', db.Integer()),
              db.Column('weight', db.String(255)),
              db.Column('rep1', db.Integer()),
              db.Column('rep2', db.Integer()),
              db.Column('rep3', db.Integer()),
              db.Column('user_id',db.String(255)),
              )
Legs=db.Table('Legs',metadata,
              db.Column('workout_id',db.String(255),primary_key=True),
              db.Column('Squat_id', db.Integer()),
              db.Column('SplitSquat_id', db.String(255)),
              db.Column('LegPress_id', db.Integer()),
              db.Column('LegCurls_id', db.Integer()),
              db.Column('CalfRaises_id', db.Integer()),
              db.Column('user_id',db.String(255)),
              db.Column("DateTime", db.DateTime,default=datetime.datetime.now())

              )
Pull = db.Table('Pull', metadata,
                db.Column('workout_id', db.String(255), primary_key=True),
                db.Column('BarbellRows_id', db.Integer()),
                db.Column('Pullups_id', db.Integer()),
                db.Column('SeatedCableRows_id', db.Integer()),
                db.Column('FacePulls_id', db.Integer()),
                db.Column('HammerCurls_id', db.Integer()),
                db.Column('DumbbellCurls_id', db.Integer()),
                db.Column('user_id',db.String(255)),
                db.Column("DateTime", db.DateTime, default=datetime.datetime.now())
                )

Push = db.Table('Push', metadata,
                db.Column('workout_id', db.String(255), primary_key=True),
                db.Column('BenchPress_id', db.Integer()),
                db.Column('OverheadPress_id', db.Integer()),
                db.Column('user_id', db.String(255)),
                db.Column('InclineDumbbellPress_id', db.Integer()),
                db.Column('TricepsPushdowns_id', db.Integer()),
                db.Column('LateralRaises_id', db.Integer()),
                db.Column('OverheadTricepsExtensions_id', db.Integer()),
                db.Column("date", db.String(255)),
                db.Column("DateTime", db.DateTime, default=datetime.datetime.now())
                )

User=db.Table('User',metadata,
              db.Column('username', db.String(255)),
              db.Column('password', db.String(255)), #need to not forget to hash
              db.Column('user_id',db.String(255),unique=True)
              )
#need to learn git commits
#need to create a website
metadata.create_all(engine)

@app.route('/')
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    # Use .scalars() to get the elements rather than entire rows from the database
    return render_template("home.html")
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method=="POST":
        username=request.form["username"]
        password=request.form["password"]
        user=use(username,password,conn,Legs,Pull,Push)
        if user.searchforuser(User):
            print("user was found")
            return render_template("index.html")
        return render_template("login.html")
    else:
        return render_template("login.html")
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        user=use(username,password,conn,Legs,Pull,Push)
        if not user.searchforuser(User):
            user.Add_user(User,db)
        return render_template("index.html")
    return render_template("signup.html")

@app.route('/create', methods=["GET", "POST"])
def create():
    if request.method == "POST":
        workoutname = request.args.get('workout')
        print(workoutname)
        # creating a workout
        if workoutname=="legs":
            new_workout_legs = leg(db, conn, Exercise, "333")
            # Squat
            if request.form.get("weight-squat"):
                weight = request.form["weight-squat"]
                rep1 = request.form["rep1-squat"]
                rep2 = request.form["rep2-squat"]
                rep3 = request.form["rep3-squat"]
                new_workout_legs.Add_Squat(weight, rep1, rep2, rep3)

            # SplitSquat
            if request.form.get("weight-splitsquat"):
                weight = request.form["weight-splitsquat"]
                rep1 = request.form["rep1-splitsquat"]
                rep2 = request.form["rep2-splitsquat"]
                rep3 = request.form["rep3-splitsquat"]
                new_workout_legs.Add_SplitSquat(weight, rep1, rep2, rep3)

            # LegPress
            if request.form.get("weight-legpress"):
                weight = request.form["weight-legpress"]
                rep1 = request.form["rep1-legpress"]
                rep2 = request.form["rep2-legpress"]
                rep3 = request.form["rep3-legpress"]
                new_workout_legs.Add_LegPress(weight, rep1, rep2, rep3)

            # LegCurls
            if request.form.get("weight-legcurls"):
                weight = request.form["weight-legcurls"]
                rep1 = request.form["rep1-legcurls"]
                rep2 = request.form["rep2-legcurls"]
                rep3 = request.form["rep3-legcurls"]
                new_workout_legs.Add_LegCurls(weight, rep1, rep2, rep3)

            # CalfRaises
            if request.form.get("weight-calfraises"):
                weight = request.form["weight-calfraises"]
                rep1 = request.form["rep1-calfraises"]
                rep2 = request.form["rep2-calfraises"]
                rep3 = request.form["rep3-calfraises"]
                new_workout_legs.Add_CalfRaises(weight, rep1, rep2, rep3)

            # Add to the workout table
            new_workout_legs.Add_legWorkout(Legs)
            # Creating a pull workout
        elif  workoutname == "pull":
            new_workout_pull = pul(db, conn, Exercise, "333")

            if request.form.get("weight-barbellrows"):
                weight = request.form["weight-barbellrows"]
                rep1 = request.form["rep1-barbellrows"]
                rep2 = request.form["rep2-barbellrows"]
                rep3 = request.form["rep3-barbellrows"]
                new_workout_pull.Add_BarbellRows(weight, rep1, rep2, rep3)

            if request.form.get("weight-pullups"):
                weight = request.form["weight-pullups"]
                rep1 = request.form["rep1-pullups"]
                rep2 = request.form["rep2-pullups"]
                rep3 = request.form["rep3-pullups"]
                new_workout_pull.Add_Pullups(weight, rep1, rep2, rep3)

            if request.form.get("weight-seatedcablerows"):
                weight = request.form["weight-seatedcablerows"]
                rep1 = request.form["rep1-seatedcablerows"]
                rep2 = request.form["rep2-seatedcablerows"]
                rep3 = request.form["rep3-seatedcablerows"]
                new_workout_pull.Add_SeatedCableRows(weight, rep1, rep2, rep3)

            if request.form.get("weight-facepulls"):
                weight = request.form["weight-facepulls"]
                rep1 = request.form["rep1-facepulls"]
                rep2 = request.form["rep2-facepulls"]
                rep3 = request.form["rep3-facepulls"]
                new_workout_pull.Add_FacePulls(weight, rep1, rep2, rep3)

            if request.form.get("weight-hammercurls"):
                weight = request.form["weight-hammercurls"]
                rep1 = request.form["rep1-hammercurls"]
                rep2 = request.form["rep2-hammercurls"]
                rep3 = request.form["rep3-hammercurls"]
                new_workout_pull.Add_HammerCurls(weight, rep1, rep2, rep3)

            if request.form.get("weight-dumbbellcurls"):
                weight = request.form["weight-dumbbellcurls"]
                rep1 = request.form["rep1-dumbbellcurls"]
                rep2 = request.form["rep2-dumbbellcurls"]
                rep3 = request.form["rep3-dumbbellcurls"]
                new_workout_pull.Add_DumbbellCurls(weight, rep1, rep2, rep3)

            new_workout_pull.Add_pullWorkout(Pull)
        elif workoutname == "push":
            new_workout_push = pus(db, conn, Exercise, "333")

            if request.form.get("weight-benchpress"):
                weight = request.form["weight-benchpress"]
                rep1 = request.form["rep1-benchpress"]
                rep2 = request.form["rep2-benchpress"]
                rep3 = request.form["rep3-benchpress"]
                new_workout_push.Add_BenchPress(weight, rep1, rep2, rep3)

            if request.form.get("weight-overheadpress"):
                weight = request.form["weight-overheadpress"]
                rep1 = request.form["rep1-overheadpress"]
                rep2 = request.form["rep2-overheadpress"]
                rep3 = request.form["rep3-overheadpress"]
                new_workout_push.Add_OverheadPress(weight, rep1, rep2, rep3)

            if request.form.get("weight-inclinedumbbellpress"):
                weight = request.form["weight-inclinedumbbellpress"]
                rep1 = request.form["rep1-inclinedumbbellpress"]
                rep2 = request.form["rep2-inclinedumbbellpress"]
                rep3 = request.form["rep3-inclinedumbbellpress"]
                new_workout_push.Add_InclineDumbbellPress(weight, rep1, rep2, rep3)

            if request.form.get("weight-tricepspushdowns"):
                weight = request.form["weight-tricepspushdowns"]
                rep1 = request.form["rep1-tricepspushdowns"]
                rep2 = request.form["rep2-tricepspushdowns"]
                rep3 = request.form["rep3-tricepspushdowns"]
                new_workout_push.Add_TricepsPushdowns(weight, rep1, rep2, rep3)

            if request.form.get("weight-lateralraises"):
                weight = request.form["weight-lateralraises"]
                rep1 = request.form["rep1-lateralraises"]
                rep2 = request.form["rep2-lateralraises"]
                rep3 = request.form["rep3-lateralraises"]
                new_workout_push.Add_LateralRaises(weight, rep1, rep2, rep3)

            if request.form.get("weight-overheadtricepsextensions"):
                weight = request.form["weight-overheadtricepsextensions"]
                rep1 = request.form["rep1-overheadtricepsextensions"]
                rep2 = request.form["rep2-overheadtricepsextensions"]
                rep3 = request.form["rep3-overheadtricepsextensions"]
                new_workout_push.Add_OverheadTricepsExtensions(weight, rep1, rep2, rep3)

            new_workout_push.Add_pushWorkout(Push)

    workoutname = request.args.get('workoutname')
    return render_template("create.html", workoutname=workoutname)


if __name__ == "__main__":
    banan = use("barka", "123", conn, Legs, Pull, Push)
    print(1)
    banan.Add_user(User, db)
    app.run(debug=False)
conn.close()
# print(banan.count_workouts())
# id = uuid.uuid4() # problem which needs to fixed, while not common there is a chance that there will be two id's which are the same
# # and an error will comeup I need to make it so id's are just added one by one ie 1 2 3
# banan.Add_user(User,db)



#this is how to enter data
# query = db.insert(Exercise).values(exercise_id=str(id), sets=1, weight="English", rep1=1,rep2=3,rep3=4)
# Result = conn.execute(query)

# squat=Ex("46kg",12,12,15,db,conn,Exercise,"333")
# squat.add_to_exercise_table()
#
# legworkout=leg(db,conn,Exercise,"333")
# legworkout.Add_LegCurls("50",12,14,10)
# legworkout.Add_legWorkout(Legs)







