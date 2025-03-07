import uuid
from exercise import Exercise

class Push:
    def __init__(self, db, connection, table, user_id):
        self.BenchPress = None
        self.OverheadPress = None
        self.InclineDumbbellPress = None
        self.TricepsPushdowns = None
        self.LateralRaises = None
        self.OverheadTricepsExtensions = None
        self.user_id = user_id
        self.id = uuid.uuid4()
        self.db = db
        self.connection = connection
        self.table = table

    def Add_BenchPress(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.BenchPress = str(exer.id)

    def Add_OverheadPress(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.OverheadPress = str(exer.id)

    def Add_InclineDumbbellPress(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.InclineDumbbellPress = str(exer.id)

    def Add_TricepsPushdowns(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.TricepsPushdowns = str(exer.id)

    def Add_LateralRaises(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.LateralRaises = str(exer.id)

    def Add_OverheadTricepsExtensions(self, weight, rep1, rep2, rep3):
        exer = Exercise(weight, rep1, rep2, rep3, self.db, self.connection, self.table, self.user_id)
        exer.add_to_exercise_table()
        self.OverheadTricepsExtensions = str(exer.id)

    def Add_pushWorkout(self, push_table):
        query = self.db.insert(push_table).values(
            user_id=self.user_id,
            workout_id=str(self.id),
            BenchPress_id=self.BenchPress,
            OverheadPress_id=self.OverheadPress,
            InclineDumbbellPress_id=self.InclineDumbbellPress,
            TricepsPushdowns_id=self.TricepsPushdowns,
            LateralRaises_id=self.LateralRaises,
            OverheadTricepsExtensions_id=self.OverheadTricepsExtensions
        )
        self.connection.execute(query)
        self.connection.commit()

