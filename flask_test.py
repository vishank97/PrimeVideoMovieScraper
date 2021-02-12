from flask import Flask, render_template, request
from models import *
from SCRAPER import *
import csv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:5433/postgres'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:admin@localhost:8569/'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Postgres!PascalAPI@pascal-api.cbxxebeeiz6k.ap-south-1.rds.amazonaws.com:5432/postgres'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def add_data(data):
    if Movie.query.filter_by(title=data.title).first() is None:
        db.session.add(data)
        db.session.commit()
    else:
        print("Already present")


def test_add():
    if Movie.query.filter_by(title="Tss").first() == None:
        movie = Movie(title="Tss", description="desacription", director="dirdector",
                      starring="starrinaasg", genre="genrases", subtitles="subtitlesds",
                      audio_languages="audiods_languages",
                      producer="producdsers", studio="studio", amazon_maturity_rating="aasmr",
                      supporting_actors="supportinasdg_actors")
        db.session.add(movie)
        db.session.commit()
    else:
        print("Already Present")



def main():
    db.create_all()


if __name__ == '__main__':
    with app.app_context():
        main()
        start()
