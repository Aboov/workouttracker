from legs import Legs
from pull import Pull
from push import Push
import uuid
from sqlalchemy import and_
import datetime
from sqlalchemy import select
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    def __init__(self,name,password,conn,legs,pull,push):
        self.username=name
        self.userid=str(uuid.uuid4())
        hashed = generate_password_hash(password)

        self.password=hashed
        self.unhashed=password
        self.connection=conn
        self.legs=legs
        self.pull=pull
        self.push=push

    def get_last_workout(self):
        tables=[self.legs,self.pull,self.push]
        min_date= datetime.datetime(1999, 5, 17)
        lastest_workout="no workout recorded"

        for table in tables:
            query=select(table).where(table.columns.user_id==self.userid).order_by(table.columns.DateTime)
            result=self.connection.execute(query)
            try: #in case there isn't any workouts found
                top_date=result.first().DateTime
                if top_date>min_date:
                    low_date=min_date
                    lastest_workout=table.name
            except:
                print(f"no workout in {table.name}")
        return lastest_workout


    def count_workouts(self):
        tables = [self.legs, self.pull, self.push]
        count=0
        for table in tables:
            query = select(table).where(table.columns.user_id == self.userid)
            result = self.connection.execute(query)
            if result:
                for row in result:
                    count+=1
        return count

    def Add_user(self,user_table,db):
        #not working for some reason it still adds users which already exist
        #still not work i have no clue as to why, need to look at it.
        if self.searchforuser(user_table):
            print("user already exists")
        else:
            try:
                query = db.insert(user_table).values(
                    user_id=self.userid,
                    username=self.username,
                    password=str(self.password)

                )
                self.connection.execute(query)
                self.connection.commit()
            except:
                pass
                # print("seems like the user id is the same as another user, lemme change this")
                # self.userid=str(uuid.uuid4())
                # query = db.insert(user_table).values(
                #     user_id=self.userid,
                #     username=self.username,
                #     password=str(self.password)
                #
                # )
                # self.connection.execute(query)

    def searchforuser(self,user_table):

        query = select(user_table).where((user_table.columns.username == self.username))

        result = self.connection.execute(query)

        for row in result:
            if check_password_hash(row.password,self.unhashed):
                return True


        print("could not find user, please create one")
        return False













