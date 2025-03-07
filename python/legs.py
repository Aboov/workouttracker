import uuid

from exercise import Exercise

class Legs:
    def __init__(self, db, connection, table, user_id):
        self.Squat = None
        self.SplitSquat = None
        self.LegPress = None
        self.LegCurls = None
        self.CalfRaises = None
        self.user_id = user_id
        self.id = uuid.uuid4()
        self.db = db
        self.connection = connection
        self.table = table

    def Add_Squat(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.Squat = str(exer.id)

    def Add_SplitSquat(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.SplitSquat = str(exer.id)

    def Add_LegPress(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.LegPress = str(exer.id)

    def Add_LegCurls(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.LegCurls = str(exer.id)

    def Add_CalfRaises(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.CalfRaises = str(exer.id)

    def Add_legWorkout(self, leg_table):
        query = self.db.insert(leg_table).values(
            user_id=self.user_id,
            workout_id=str(self.id),
            Squat_id=self.Squat,
            SplitSquat_id=self.SplitSquat,
            LegPress_id=self.LegPress,
            LegCurls_id=self.LegCurls,
            CalfRaises_id=self.CalfRaises

        )
        self.connection.execute(query)
        self.connection.commit()
