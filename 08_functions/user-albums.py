"""
8-8. User Albums: 

Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

def make_album(album_artist, album_title):
    album = {
        'artist': album_artist, 
        'album': album_title, 
        }
    return album

while True:
    print("\nEnter music albums into your collection: ")
    print("(enter 'q' at any time to quit)\n")

    a_artist = input("\tAlbum artist: ")
    if a_artist == 'q':
        break

    a_title = input("\tAlbum name: ")
    if a_title == 'q':
        break

    album_input = make_album(a_artist, a_title)

    print("\n === New album entry ===")
    print(album_input)
