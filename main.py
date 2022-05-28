class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score


    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = int(new_age)

    def add_track(self, add_track):
        self.tracks = add_track

    def get_score(self):
        return self.score

    def show(self):
        print('My name is ', self.name)
        print('My age is ', self.age)
        print('My tracks are ', self.tracks)
        print('My score is ', self.score)



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Joseph")
Bob.change_age(32)
Bob.add_track("frontend web development, python")
Bob.get_score()


Bob.show()
