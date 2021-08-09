import mysql.connector

con = mysql.connector.connect(user='root', password='root', host='localhost', database='poc-cadastro')
cursor = con.cursor()

with open('data.csv') as file:
  dataFrame = [row.split(',') for row in file.read().split('\n')]

file.close()

header = dataFrame[0]
data = [dict(zip(header, row)) for row in dataFrame[1:]]

create = ("CREATE TABLE IF NOT EXISTS SONG ("
    "id INTEGER AUTO_INCREMENT, "
    "Rank INTEGER NOT NULL, "
    "Track VARCHAR(200) NOT NULL, "
    "Artist VARCHAR(80) NOT NULL, "
    "Streams INTEGER NOT NULL, "
    "Link VARCHAR(150), "
    "Week DATE NOT NULL,"
    "Album_Name VARCHAR(200), "
    "Duration_MS INTEGER NOT NULL, "
    "Explicit BOOLEAN NOT NULL, "
    "Track_Number_on_Album INTEGER, "
    "Artist_Followers INTEGER NOT NULL, "
    "PRIMARY KEY(id)"
")")

cursor.execute(create)
con.commit()

insert = ("INSERT INTO SONG (Rank, Track, Artist, Streams, Link, Week, Album_Name, Duration_MS, Explicit, Track_Number_on_Album, Artist_Followers) "
    "VALUES ("
        "%(Rank)s, "
        "%(Track)s, "
        "%(Artist)s, "
        "%(Streams)s, "
        "%(Link)s, "
        "%(Week)s, "
        "%(Album_Name)s, "
        "%(Duration_MS)s, "
        "%(Explicit)s, "
        "%(Track_Number_on_Album)s, "
        "%(Artist_Followers)s"
    ")"
)

for index, song in enumerate(data):
  cursor.execute(insert, song)

con.commit()

cursor.close()
con.close()