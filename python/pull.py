import uuid
from exercise import Exercise

class Pull:
    def __init__(self, db, connection, table,user_id):
        self.BarbellRows = None
        self.Pullups = None
        self.SeatedCableRows = None
        self.FacePulls = None
        self.HammerCurls = None
        self.DumbbellCurls = None
        self.user_id=user_id
        self.id = uuid.uuid4()
        self.db = db
        self.connection = connection
        self.table = table

    def Add_BarbellRows(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table,self.user_id)
        exer.add_to_exercise_table()
        self.connection.commit()
        print("BOMOBMOMBOMBMOB")
        self.BarbellRows = str(exer.id)

    def Add_Pullups(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table,self.user_id)
        exer.add_to_exercise_table()
        self.Pullups = str(exer.id)

    def Add_SeatedCableRows(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table,self.user_id)
        exer.add_to_exercise_table()
        self.SeatedCableRows = str(exer.id)

    def Add_FacePulls(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table,self.user_id)
        exer.add_to_exercise_table()
        self.FacePulls = str(exer.id)

    def Add_HammerCurls(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table,self.user_id)
        exer.add_to_exercise_table()
        self.HammerCurls = str(exer.id)

    def Add_DumbbellCurls(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table,self.user_id)
        exer.add_to_exercise_table()
        self.DumbbellCurls = str(exer.id)

    def Add_pullWorkout(self, pull_table):
        query = self.db.insert(pull_table).values(
            user_id=self.user_id,
            workout_id=str(self.id),
            BarbellRows_id=self.BarbellRows,
            Pullups_id=self.Pullups,
            SeatedCableRows_id=self.SeatedCableRows,
            FacePulls_id=self.FacePulls,
            HammerCurls_id=self.HammerCurls,
            DumbbellCurls_id=self.DumbbellCurls
        )
        self.connection.execute(query)
        self.connection.commit()

