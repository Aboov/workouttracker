import uuid

class Exercise:
    def __init__(self,weight,rep1,rep2,rep3,db,connection,table,user_id):
        self.id=uuid.uuid4()
        self.sets=3
        self.weight=weight
        self.rep1 = rep1
        self.rep2 = rep2
        self.user_id=user_id
        self.rep3 = rep3
        self.db = db
        self.connection = connection
        self.table = table
    def add_to_exercise_table(self):
         query = self.db.insert(self.table).values(user_id=self.user_id,exercise_id=str(self.id), sets=self.sets, weight=self.weight, rep1=self.rep1,rep2=self.rep2,rep3=self.rep3)
         self.connection.execute(query)
