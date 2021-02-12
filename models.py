from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = "movies-test"

    title = db.Column(db.String, primary_key=True)
    description = db.Column(db.String, primary_key=False)
    director = db.Column(db.String, primary_key=False)
    starring = db.Column(db.String, primary_key=False)
    genre = db.Column(db.String, primary_key=False)
    subtitles = db.Column(db.String, primary_key=False)
    audio_languages = db.Column(db.String, primary_key=False)
    producer = db.Column(db.String, primary_key=False)
    studio = db.Column(db.String, primary_key=False)
    amazon_maturity_rating = db.Column(db.String, primary_key=False)
    supporting_actors = db.Column(db.String, primary_key=False)

    # title = db.Column(db.String, primary_key=True)
    # description = db.Column(db.String, primary_key=False)
    # director = db.Column(db.String, primary_key=False)
    # starring = db.Column(db.String, primary_key=False)
    # genre = db.Column(db.String, primary_key=False)
    # # imdb_rating = db.Column(db.String, primary_key=False)
    # duration = db.Column(db.String, primary_key=False)
    # year_released = db.Column(db.String, primary_key=False)
    # age_category = db.Column(db.String, primary_key=False)
    # subtitles = db.Column(db.String, primary_key=False)
    # audio_languages = db.Column(db.String, primary_key=False)
    # producer = db.Column(db.String, primary_key=False)
    # studio = db.Column(db.String, primary_key=False)
    # amazon_maturity_rating = db.Column(db.String, primary_key=False)
    # supporting_actors = db.Column(db.String, primary_key=False)
    # def init(self, title, description, director, starring, genre, imdb_rating, duration, age_category, year_released,
    #          subtitles,
    #          audio_languages, producer, studio, amazon_maturity_rating, supporting_actors):
    #     self.title = title
    #     self.description = description
    #     self.director = director
    #     self.starring = starring
    #     self.genre = genre
    #     self.imdb_rating = imdb_rating
    #     self.duration = duration
    #     self.year_released = year_released
    #     self.age_category = age_category
    #     self.subtitles = subtitles
    #     self.audio_languages = audio_languages
    #     self.producer = producer
    #     self.studio = studio
    #     self.amazon_maturity_rating = amazon_maturity_rating
    #     self.supporting_actors = supporting_actors

#
#
# class Flight(db.Model):
#     __tablename__ = "flights"
#     id = db.Column(db.Integer, primary_key=True)
#     origin = db.Column(db.String, primary_key=False)
#     destination = db.Column(db.String, primary_key=False)
#     duration = db.Column(db.Integer, primary_key=False)
#     # def __init__(self, origin, destination, duration):
#     #     self.id = Flight.counter
#     #     Flight.counter += 1
#     #     self.passengers = []
#     #     self.origin = origin
#     #     self.destination = destination
#     #     self.duration = duration
#
#     # def print_info(self):
#     #     print(f"Flight Origin: {self.origin}")
#     #     print(f"Flight Destination: {self.destination}")
#     #     print(f"Flight Duration: {self.duration}")
#     #     print()
#     #     print("Passengers:")
#     #     for passenger in self.passengers:
#     #         print(f"{passenger.name}")
#     #
#     # def delay(self, amount):
#     #     self.duration += amount
#     #
#     # def add_passenger(self,p):
#     #     self.passengers.append(p)
#     #     p.flight_id = self.id
#
#
# class Passenger(db.Model):
#     __tablename__ = "passengers"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#     flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
#     # def __init__(self, name):
#     #     self.name = name
#
#
# # def main():
# #     f = Flight("Mumbai", "Delhi", 120)
# #     alice = Passenger(name="Alice")
# #     vishank = Passenger("Vishank")
# #     f.add_passenger(alice)
# #     f.add_passenger(vishank)
# #     f.print_info()
# #     print()
# #     f1 = Flight("Chennai", "Kolkata", 180)
# #     bob = Passenger("Bob")
# #     f1.add_passenger(bob)
# #     f1.print_info()
# #
# #
# # if __name__ == '__main__':
# #     main()
