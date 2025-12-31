"""
8-7. Album: 

Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the num-
ber of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
"""

def make_album(album_artist, album_title, album_tracks = ''):
    album = {
        'artist': album_artist, 
        'album': album_title, 
        'tracks': album_tracks
        }
    return album

album1 = make_album('red hot chili peppers', 'stadium arcadium')
print(album1)

album2 = make_album('eminem', 'the marshall mathers lp')
print(album2)

album3 = make_album('queen', 'a night at the opera')
print(album3)

album4 = make_album('fleetwood mac', 'rumours', '11')
print(album4)
