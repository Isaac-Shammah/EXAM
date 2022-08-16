import csv

from cs50 import SQL

open("songs.db","w").close()

db = SQL("sqlite:///songs.db")

db.execute("CREATE TABLE artist(id INTEGER, name TEXT, PRIMARY KEY(id))")

db.execute("CREATE TABLE song(id INTEGER, title TEXT, length INTEGER, popularity INTEGER, year INTEGER, PRIMARY KEY(id))")

db.execute("CREATE TABLE topgenre(id INTEGER, energy INTEGER, danceability INTEGER, liveness INTEGER, PRIMARY KEY(id))")

db.execute("CREATE TABLE media(media_id INTEGER, art_id INTEGER, song_id INTEGER, tg_id INTEGER, PRIMARY KEY(media_id), FOREIGN KEY(art_id) REFERENCES artist(id), FOREIGN KEY(song_id) REFERENCES song(id), FOREIGN KEY(tg_id) REFERENCES topgenre(id))")

with open("songs.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        name = row["artist"].strip()

        title = row["title"].strip()
        length = row["length"].strip()
        popularity = row["popularity"].strip()
        year = row["year"].strip()
        
        energy = row["energy"].strip()
        danceability = row["danceability"].strip()
        liveness = row["liveness"].strip()

        art_id = db.execute("INSERT INTO artist(name) VALUES(?)",name)
        song_id = db.execute("INSERT INTO song(title,length,popularity,year) VALUES(?,?,?,?)",title,length,popularity,year)
        tg_id = db.execute("INSERT INTO topgenre(energy,danceability,liveness) VALUES(?,?,?)",energy,danceability,liveness)
        media_id = db.execute("INSERT INTO media(art_id,song_id,tg_id) VALUES(?,?,?)",art_id,song_id,tg_id)

