import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Album, Artist
 
engine = create_engine('sqlite:///mymusic.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
# Create an artist
new_artist = Artist("Classixx")
new_artist.albums = [Album("Hanging Gardens", 
                           "House",
                           "Publisher1", "Digital")]
 
# add more albums
more_albums = [Album("The Bones of What You Believe",
                     "Electropop",
                     "Publisher2", "CD"),
               Album("Settle", 
                     "House",
                     "Publisher3", "CD"),
               Album("Pure Heroine",
                     "Futurepop",
                     "Publisher3", "CD")]
new_artist.albums.extend(more_albums)
 
# Add the record to the session object
session.add(new_artist)
# commit the record the database
session.commit()
 
# Add several artists
session.add_all([
    Artist("CHVRCHES"),
    Artist("Disclosure"),
    Artist("Lorde")
    ])
session.commit()